// runtime.js — the binder's in-file script. generate.js inlines `(${binderRuntime})()`.
//
// The binder is complete without this script (static HTML body: contents, every page, sources).
// Where the script runs, it upgrades the file into an app: one page at a time, search, an
// emergency row, the Section 32 region picker, the Section 02 condition picker, photo slots with
// "Save a new copy", a print/PDF button. Every DOM change it makes is reversible so that "Save a
// new copy" can write the file back out clean (see cleanClone).
//
// Constraints: no network, no storage that matters (localStorage only for theme and pins), no
// history API (throws on file:// in WebKit), no animation, no polling.

export function binderRuntime() {
  var errEl = document.getElementById('err');
  function showErr(msg) { if (errEl) { errEl.style.display = 'block'; errEl.textContent = msg; } }
  window.addEventListener('error', function (e) { showErr('App error (the static book below still works): ' + (e.message || e.type)); });
  try {
    var META = JSON.parse(document.getElementById('gp-meta').textContent);
    var P = META.pages, byId = {};
    P.forEach(function (m) { byId[m.id] = m; });
    var view = document.getElementById('view'), q = document.getElementById('q');
    var esc = function (s) { return String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/"/g, '&quot;'); };
    var badge = function (d) { return d === 'critical' ? ' <span class="badge b-crit">CRITICAL</span>' : d === 'caution' ? ' <span class="badge b-caut">CAUTION</span>' : ''; };
    var star = function (m) { return m.pr ? ' <span class="badge b-star">FOR YOU</span>' : ''; };
    var TXT = {};
    function txt(id) {
      if (TXT[id] === undefined) { var el = document.getElementById(id); TXT[id] = el ? el.textContent.replace(/\s+/g, ' ').toLowerCase() : ''; }
      return TXT[id];
    }
    try { if (localStorage.getItem('gp-t') === 'light') document.documentElement.setAttribute('data-t', 'light'); } catch (e) {}
    document.getElementById('theme').onclick = function () {
      var h = document.documentElement, v = h.getAttribute('data-t') === 'light' ? '' : 'light';
      if (v) h.setAttribute('data-t', v); else h.removeAttribute('data-t');
      try { localStorage.setItem('gp-t', v); } catch (e) {}
    };

    // ---- navigation: a self-managed back stack over location.hash ------------------------------
    var stack = [], cur = { h: location.hash || '#home' }, backNav = null;
    var backBtn = document.getElementById('back');
    backBtn.addEventListener('click', function (e) {
      e.preventDefault();
      var st = stack.length ? stack.pop() : { h: '#home' };
      if (location.hash !== st.h) { backNav = st; location.hash = st.h; } else { cur = st; apply(st); }
    });
    addEventListener('hashchange', function () {
      var h = location.hash || '#home';
      if (backNav) { cur = backNav; backNav = null; apply(cur); return; }
      cur.y = scrollY; stack.push(cur); if (stack.length > 100) stack.shift();
      cur = { h: h }; apply(cur);
    });

    var PINS = [];
    try { PINS = JSON.parse(localStorage.getItem('gp-pins') || '[]').filter(function (id) { return byId[id]; }); } catch (e) {}
    function qcard(id) { var m = byId[id]; return m ? '<a class="card" href="#' + id + '"><span class="pid">' + id.slice(0, 5) + '</span> <strong>' + esc(m.t) + '</strong></a>' : ''; }
    function clearActive() { var a = document.querySelectorAll('.active'); for (var i = 0; i < a.length; i++) a[i].classList.remove('active'); }
    function atHome(html) { clearActive(); document.body.classList.add('athome'); view.innerHTML = html; }
    function row(m) { return '<a class="card" href="#' + m.id + '"><span class="pid">' + m.id.slice(0, 5) + '</span> <strong>' + esc(m.t) + '</strong>' + badge(m.d) + star(m) + '</a>'; }

    function home() {
      atHome('<h1>' + esc(META.title) + '</h1>'
        + '<h2 class="hrow">Emergency</h2><div class="qrow">' + META.emergency.map(qcard).join('') + '</div>'
        + (PINS.length ? '<h2 class="hrow">Pinned on this device</h2><div class="qrow">' + PINS.map(qcard).join('') + '</div>' : '')
        + (META.promoted.length ? '<h2 class="hrow">Start here for your household</h2>' + META.promoted.slice(0, 12).map(function (id) { return byId[id] ? row(byId[id]) : ''; }).join('') : '')
        + '<h2 class="hrow">Sections</h2>' + META.sections.map(function (s) {
          var n = P.filter(function (m) { return m.s === s.n; }).length;
          return '<a class="card" href="#s/' + s.n + '"><span class="pid">' + s.n + '</span> <strong>' + esc(s.t) + '</strong> <span class="dim">' + n + ' pages</span></a>';
        }).join('')
        + '<div class="note dim">Works with no network. Built ' + esc(META.built) + '. ' + esc(META.stamp) + '</div>');
    }

    function regionPicker() {
      var states = {}, list = [];
      P.forEach(function (m) { if (m.s === '32' && m.st && !states[m.st]) { states[m.st] = m.stn || m.st; list.push(m.st); } });
      list.sort(function (a, b) { return states[a] < states[b] ? -1 : 1; });
      var pick = cur.state || META.home_state || list[0];
      var opts = list.map(function (s) { return '<option value="' + s + '"' + (s === pick ? ' selected' : '') + '>' + esc(states[s]) + (s === META.home_state ? ' (home)' : META.dest_states.indexOf(s) >= 0 ? ' (destination)' : '') + '</option>'; }).join('');
      var rows = P.filter(function (m) { return m.s === '32' && (m.st === pick || !m.st); });
      return (list.length ? '<label class="dim" for="statepick">Show region pages for</label><select id="statepick" class="sel">' + opts + '</select>' : '<p class="dim">No state region pages in this binder.</p>')
        + rows.map(row).join('');
    }
    function conditionPicker() {
      var mine = P.filter(function (m) { return m.s === '02' && m.c && META.conditions.indexOf(m.c) >= 0; });
      var all = P.filter(function (m) { return m.s === '02'; });
      var opts = all.map(function (m) { return '<option value="' + m.id + '">' + esc((m.c ? m.c + ' ' : '') + m.t) + '</option>'; }).join('');
      return (mine.length ? '<h2 class="hrow">Your household</h2>' + mine.map(row).join('') : '<p class="dim">No conditions were selected in settings. The whole library is here.</p>')
        + '<label class="dim" for="condpick">Look up any condition</label><select id="condpick" class="sel"><option value="">Choose a condition…</option>' + opts + '</select>'
        + '<h2 class="hrow">All pages</h2>' + all.map(row).join('');
    }
    function section(n) {
      var s = META.sections.filter(function (x) { return x.n === n; })[0];
      var head = '<h1><span class="pid">' + n + '</span> ' + esc(s ? s.t : '') + '</h1>';
      if (n === '32') return atHome(head + regionPicker());
      if (n === '02') return atHome(head + conditionPicker());
      var rows = P.filter(function (m) { return m.s === n; });
      atHome(head + rows.map(row).join(''));
    }
    view.addEventListener('change', function (e) {
      if (e.target.id === 'statepick') { cur.state = e.target.value; section('32'); }
      if (e.target.id === 'condpick' && e.target.value) location.hash = '#' + e.target.value;
    });

    var pinBtn = document.getElementById('pin'), curPage = null;
    function pinGlyph() { pinBtn.textContent = PINS.indexOf(curPage) < 0 ? '☆' : '★'; }
    pinBtn.onclick = function () {
      if (!curPage) return;
      var i = PINS.indexOf(curPage); if (i < 0) PINS.push(curPage); else PINS.splice(i, 1);
      try { localStorage.setItem('gp-pins', JSON.stringify(PINS)); } catch (e) {}
      pinGlyph();
    };
    function pageView(id) {
      var el = document.getElementById(id);
      if (!el) return home();
      document.body.classList.remove('athome'); view.innerHTML = ''; clearActive();
      el.classList.add('active');
      curPage = byId[id] ? id : null; pinBtn.hidden = !curPage; if (curPage) pinGlyph();
    }

    function search(query) {
      var terms = query.toLowerCase().split(/\s+/).filter(function (t) { return t.length > 1; });
      if (!terms.length) return home();
      var stems = terms.map(function (t) { var m = t.match(/^(.{4,}?)(?:ing|ed|es|s)$/); return m ? [t, m[1]] : [t]; });
      var out = [];
      P.forEach(function (p) {
        var score = 0, matched = 0, tl = p.t.toLowerCase(), body = txt(p.id);
        stems.forEach(function (vars) {
          var s = 0;
          for (var i = 0; i < vars.length && !s; i++) {
            var t = vars[i];
            if (p.id.indexOf(t) >= 0) s += 30;
            if (tl.indexOf(t) >= 0) s += 50;
            if (p.g.indexOf(t) >= 0) s += 20;
            s += Math.min(body.split(t).length - 1, 10) * 3;
          }
          if (s) { matched++; score += s; }
        });
        if (matched) out.push([score * matched * matched + (p.pr ? 5 : 0), p]);
      });
      out.sort(function (a, b) { return b[0] - a[0]; });
      atHome('<p class="dim">' + out.length + ' page(s) match</p>' + out.slice(0, 40).map(function (r) {
        var p = r[1], body = txt(p.id), snip = '', i = body.indexOf(stems[0][stems[0].length - 1]);
        if (i >= 0) {
          snip = esc(body.slice(Math.max(0, i - 70), i + 90));
          terms.forEach(function (t) { snip = snip.replace(new RegExp('(' + t.replace(/[.*+?^$()[\]{}|\\]/g, '\\$&') + ')', 'gi'), '<mark>$1</mark>'); });
          snip = '<div class="snip">…' + snip + '…</div>';
        }
        return '<a class="card" href="#' + p.id + '"><span class="pid">' + p.id.slice(0, 5) + '</span> <strong>' + esc(p.t) + '</strong>' + badge(p.d) + snip + '</a>';
      }).join('') || '<p class="dim">No pages match. Fewer or shorter words often work better.</p>');
    }
    var deb;
    q.addEventListener('input', function () { clearTimeout(deb); deb = setTimeout(function () { var v = q.value.trim(); cur.q = v || null; v ? search(v) : apply({ h: cur.h }); }, 150); });

    function apply(st) {
      if (st.q) { q.value = st.q; search(st.q); }
      else {
        q.value = '';
        var h = decodeURIComponent((st.h || '#home').replace(/^#/, ''));
        pinBtn.hidden = true; curPage = null;
        if (h.indexOf('s/') === 0) section(h.slice(2));
        else if (h === 'home' || h === 'toc' || !h) home();
        else pageView(h);
      }
      scrollTo(0, st.y || 0);
    }

    // ---- photo slots: attach in the browser, never uploaded --------------------------------------
    var dirty = false;
    function markDirty() { dirty = true; document.body.classList.add('dirty'); }
    function downscale(file, cb) {
      var r = new FileReader();
      r.onload = function () {
        var img = new Image();
        img.onload = function () {
          var max = 1280, w = img.naturalWidth, h = img.naturalHeight, k = Math.min(1, max / Math.max(w, h));
          var c = document.createElement('canvas'); c.width = Math.round(w * k); c.height = Math.round(h * k);
          c.getContext('2d').drawImage(img, 0, 0, c.width, c.height);
          var ar = (w / h).toFixed(3);
          try { cb(c.toDataURL('image/jpeg', 0.78), ar); } catch (e) { cb(r.result, ar); }
        };
        img.onerror = function () { showErr('That file could not be read as a picture.'); };
        img.src = r.result;
      };
      r.readAsDataURL(file);
    }
    // photos: one per slot id, kept as CSS rules in <style id="gp-photos"> (one copy in the file,
    // shown on every page that has the slot, and readable without JavaScript)
    var photoStyle = document.getElementById('gp-photos'), PHOTOS = {};
    (photoStyle.textContent || '').replace(/\.ph-([a-z0-9-]+)\{display:block;aspect-ratio:([0-9.]+);background-image:url\(([^)]*)\)\}/g, function (m, id, ar, u) { PHOTOS[id] = { u: u, ar: ar }; return m; });
    function writePhotos() {
      photoStyle.textContent = Object.keys(PHOTOS).map(function (id) {
        return '.ph-' + id + '{display:block;aspect-ratio:' + PHOTOS[id].ar + ';background-image:url(' + PHOTOS[id].u + ')}\n.phf-' + id + ' .frame{display:none}';
      }).join('\n');
    }
    function setPhoto(id, src, ar) {
      if (src) PHOTOS[id] = { u: src, ar: ar || '1.333' }; else delete PHOTOS[id];
      writePhotos(); markDirty();
    }
    var figs = document.querySelectorAll('figure.photo');
    for (var i = 0; i < figs.length; i++) (function (fig) {
      var id = fig.getAttribute('data-slot');
      var box = document.createElement('div'); box.className = 'pbtns jsonly gp-ui';
      var add = document.createElement('button'); add.type = 'button'; add.textContent = 'Add or replace photo';
      var del = document.createElement('button'); del.type = 'button'; del.textContent = 'Remove';
      var inp = document.createElement('input'); inp.type = 'file'; inp.accept = 'image/*'; inp.hidden = true;
      add.onclick = function () { inp.click(); };
      del.onclick = function () { setPhoto(id, null); };
      inp.onchange = function () { if (inp.files && inp.files[0]) downscale(inp.files[0], function (u, ar) { setPhoto(id, u, ar); }); inp.value = ''; };
      box.appendChild(add); box.appendChild(del); box.appendChild(inp); fig.appendChild(box);
    })(figs[i]);

    // ---- save a new copy: the file as it was opened, plus the photos -----------------------------
    function cleanClone() {
      var root = document.documentElement.cloneNode(true);
      var body = root.querySelector('body');
      body.className = ''; root.removeAttribute('data-t');
      var v = root.querySelector('#view'); if (v) v.innerHTML = '';
      var e = root.querySelector('#err'); if (e) { e.textContent = ''; e.removeAttribute('style'); }
      var ui = root.querySelectorAll('.gp-ui'); for (var i = 0; i < ui.length; i++) ui[i].parentNode.removeChild(ui[i]);
      var act = root.querySelectorAll('.active'); for (i = 0; i < act.length; i++) act[i].classList.remove('active');
      var qq = root.querySelector('#q'); if (qq) qq.removeAttribute('value');
      var pb = root.querySelector('#pin'); if (pb) pb.hidden = true;
      return '<!doctype html>\n' + root.outerHTML;
    }
    document.getElementById('savecopy').onclick = function () {
      var html = cleanClone();
      var blob = new Blob([html], { type: 'text/html' });
      var a = document.createElement('a');
      a.href = URL.createObjectURL(blob);
      a.download = (META.file_base || 'binder') + '-' + new Date().toISOString().slice(0, 10) + '.html';
      document.body.appendChild(a); a.click();
      setTimeout(function () { URL.revokeObjectURL(a.href); a.parentNode.removeChild(a); }, 4000);
      dirty = false; document.body.classList.remove('dirty');
    };
    addEventListener('beforeunload', function (e) { if (dirty) { e.preventDefault(); e.returnValue = ''; } });

    // ---- bound PDF sources: open from the embedded bytes ------------------------------------------
    document.addEventListener('click', function (e) {
      var t = e.target.closest ? e.target.closest('[data-open-pdf]') : null;
      if (!t) return;
      e.preventDefault();
      var el = document.getElementById(t.getAttribute('data-open-pdf'));
      if (!el) return;
      var b64 = el.textContent.replace(/\s+/g, ''), bin = atob(b64), u8 = new Uint8Array(bin.length);
      for (var i = 0; i < bin.length; i++) u8[i] = bin.charCodeAt(i);
      var url = URL.createObjectURL(new Blob([u8], { type: 'application/pdf' }));
      var a = document.createElement('a'); a.href = url; a.target = '_blank'; a.download = t.getAttribute('data-name') || 'document.pdf';
      document.body.appendChild(a); a.click(); a.parentNode.removeChild(a);
    });

    // ---- print / PDF export: every page, sources behind each section ------------------------------
    var openedDetails = [];
    addEventListener('beforeprint', function () {
      var d = document.querySelectorAll('details'); openedDetails = [];
      for (var i = 0; i < d.length; i++) if (!d[i].open) { d[i].open = true; openedDetails.push(d[i]); }
    });
    addEventListener('afterprint', function () { openedDetails.forEach(function (d) { d.open = false; }); });
    document.getElementById('print').onclick = function () { window.print(); };

    document.body.classList.add('app');
    backBtn.textContent = '←';
    apply(cur);
  } catch (e) {
    showErr('App failed to start (' + e.message + '). The full static book below still works.');
    document.body.classList.remove('app');
  }
}
