// styles.js — the binder's one stylesheet (inlined into the generated file).
// Dark by default (OLED, battery), light on request, print CSS for the PDF export.
// Adapted from the household binder's app (SHTF scripts/build-app.mjs).

export const BINDER_CSS = String.raw`
:root{--bg:#11151a;--card:#1a2027;--ink:#e8e6e0;--dim:#9aa4ae;--rule:#2c343d;--acc:#e0b64f;--crit:#e05d5d;--caut:#e0a33f;--ok:#69b06b;--mark:#5a4a12;--blank:#e0b64f}
html[data-t="light"]{--bg:#f5f2ea;--card:#fffdf7;--ink:#22262b;--dim:#5c6670;--rule:#d8d2c4;--acc:#8a6d1f;--crit:#b02a2a;--caut:#9a6a12;--ok:#2e6b31;--mark:#f3e3a0;--blank:#8a6d1f}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);font:16px/1.55 -apple-system,system-ui,"Segoe UI",Roboto,sans-serif;-webkit-text-size-adjust:100%}
header.top{position:sticky;top:0;z-index:5;background:var(--bg);border-bottom:1px solid var(--rule);padding:env(safe-area-inset-top) 0 0}
.bar{display:flex;gap:6px;align-items:center;padding:8px 10px}
.bar button,.bar .hbtn{background:var(--card);color:var(--ink);border:1px solid var(--rule);border-radius:9px;padding:9px 11px;font-size:15px;text-decoration:none;line-height:1.2;min-width:44px;min-height:44px}
#q{flex:1;min-width:0;background:var(--card);color:var(--ink);border:1px solid var(--rule);border-radius:9px;padding:10px 12px;font-size:16px;min-height:44px}
#q::placeholder{color:var(--dim)}
main{padding:12px;max-width:780px;margin:0 auto;padding-bottom:56px}
#err{display:none;background:var(--crit);color:#fff;padding:10px 14px;font-size:14px;white-space:pre-wrap}
#modebar{background:var(--caut);color:#1a1408;padding:7px 12px;font-size:13px;line-height:1.4}
#modebar a{color:inherit;font-weight:700}
body.app #modebar{display:none}
.jsonly{display:none}body.app .jsonly{display:inline-block}
.card{display:block;background:var(--card);border:1px solid var(--rule);border-radius:11px;padding:12px 14px;margin:8px 0;color:var(--ink);text-decoration:none}
.pid{color:var(--dim);font-size:.82em;font-family:ui-monospace,Menlo,monospace}
.badge{font-size:11px;font-weight:700;letter-spacing:.5px;border-radius:5px;padding:2px 6px;vertical-align:2px}
.b-crit,.b-deadly{background:var(--crit);color:#fff}.b-caut,.b-caution,.b-lookalike{background:var(--caut);color:#fff}.b-ok,.b-edible,.b-firewood{background:var(--ok);color:#fff}.b-star{background:var(--acc);color:#111}
.snip{color:var(--dim);font-size:14px;margin-top:4px}
mark{background:var(--mark);color:var(--ink);border-radius:3px;padding:0 2px}
h1{font-size:24px;line-height:1.25;margin:14px 0 6px}
.ph h1{display:inline}
article h2{font-size:19px;border-bottom:1px solid var(--rule);padding-bottom:4px;margin-top:26px}
article h3{font-size:17px;margin-top:20px}
a.xref{font-family:ui-monospace,Menlo,monospace;background:var(--card);border:1px solid var(--rule);border-radius:6px;padding:1px 6px;text-decoration:none;color:var(--acc);white-space:nowrap}
a.xref .xt{font-family:-apple-system,system-ui,sans-serif;font-size:.85em;font-style:italic;opacity:.85;margin-left:.35em;white-space:normal}
span.xref.missing{font-family:ui-monospace,Menlo,monospace;color:var(--dim)}
.qrow{display:grid;grid-template-columns:1fr 1fr;gap:8px;margin:8px 0}
.qrow .card{margin:0;padding:10px 12px;font-size:14.5px}
h2.hrow{font-size:15px;color:var(--dim);letter-spacing:.6px;text-transform:uppercase;margin:20px 0 6px}
article blockquote{margin:14px 0;padding:10px 14px;border-left:4px solid var(--crit);background:var(--card);border-radius:0 9px 9px 0}
article pre{background:var(--card);border:1px solid var(--rule);border-radius:9px;padding:10px;overflow-x:auto;font:13px/1.45 ui-monospace,Menlo,monospace;white-space:pre-wrap}
article code{font-family:ui-monospace,Menlo,monospace;font-size:.92em}
article :not(pre)>code{background:var(--card);border:1px solid var(--rule);border-radius:5px;padding:0 4px}
article table{border-collapse:collapse;font-size:14px;display:block;overflow-x:auto;max-width:100%}
article th,article td{border:1px solid var(--rule);padding:6px 9px;text-align:left;vertical-align:top}
article th{background:var(--card)}
article img{max-width:100%;height:auto;border-radius:8px}
.blank{color:var(--blank);letter-spacing:1px;white-space:nowrap}.blank small{letter-spacing:0;font-size:.72em;opacity:.8}
.choice{border:1px dashed var(--acc);border-radius:7px;padding:1px 7px}
.cardbox{border:2px solid var(--acc);border-radius:11px;padding:10px 14px;margin:14px 0;background:var(--card)}
.cardbox .opt{margin:6px 0}.cardbox .opt.sel{font-weight:700}
.aiblock{border-left:3px solid var(--acc);padding-left:10px}
.aiblock .ailabel{font-size:11.5px;color:var(--dim);display:block}
figure.fig,figure.photo{margin:14px 0;background:var(--card);border:1px solid var(--rule);border-radius:11px;padding:10px}
figure.fig svg{max-width:100%;height:auto;display:block;margin:0 auto;background:#fff;border-radius:6px}
figure figcaption{font-size:13px;color:var(--dim);margin-top:6px}
figure.photo .frame{min-height:150px;border:2px dashed var(--rule);border-radius:9px;display:flex;align-items:center;justify-content:center;color:var(--dim);font-size:14px;padding:12px;text-align:center}
.phimg{display:none;width:100%;aspect-ratio:4/3;background-size:contain;background-repeat:no-repeat;background-position:center;border-radius:8px;-webkit-print-color-adjust:exact;print-color-adjust:exact}
figure.photo .pbtns{margin-top:8px;gap:6px}
figure.photo .pbtns button{background:var(--bg);color:var(--ink);border:1px solid var(--rule);border-radius:8px;padding:8px 12px;font-size:14px;min-height:40px}
.plimg{background-size:cover;background-position:center;border-radius:8px;width:100%;aspect-ratio:3/2;-webkit-print-color-adjust:exact;print-color-adjust:exact}
.platesec .plant{background:var(--card);border:1px solid var(--rule);border-radius:11px;padding:12px;margin:12px 0}
.platesec .figs{display:grid;grid-template-columns:repeat(auto-fill,minmax(150px,1fr));gap:8px}
.platesec figure{margin:0}.platesec figcaption{font-size:12.5px;color:var(--dim)}
.credit{display:block;font-size:11px;color:var(--dim)}
.dim{color:var(--dim);font-size:13.5px}
.note{border:1px solid var(--rule);border-radius:11px;padding:12px 14px;margin:10px 0;background:var(--card);font-size:14px}
details.sec{background:var(--card);border:1px solid var(--rule);border-radius:11px;margin:8px 0;padding:2px 12px}
details.sec summary{padding:10px 2px;cursor:pointer;font-size:16px}
details.sec ul{list-style:none;margin:0 0 10px;padding:0}
details.sec li{padding:7px 2px;border-top:1px solid var(--rule)}
details.sec a{color:var(--ink);text-decoration:none}
article.page{border-top:2px solid var(--rule);margin-top:26px;padding-top:8px}
aside.cites{border-top:1px solid var(--rule);margin-top:22px;font-size:13.5px}
aside.cites h2{font-size:14px;border:none;color:var(--dim);margin:10px 0 4px}
aside.cites ul{margin:0;padding-left:18px}
aside.cites a{color:var(--acc)}
.stamp{border-top:1px solid var(--rule);padding-top:8px;margin-top:16px;color:var(--dim);font-size:12.5px}
.stamp strong{color:var(--caut)}
.stamp a{color:var(--dim)}
section.srcdoc{border:1px solid var(--rule);border-radius:11px;margin:26px 0;padding:10px 14px;background:var(--card);font-size:14.5px}
section.srcdoc .srchead{font-size:13px;color:var(--dim)}
section.srcdoc .srcbody{max-height:none}
footer{color:var(--dim);font-size:12.5px;text-align:center;padding:18px}
.sel{background:var(--card);color:var(--ink);border:1px solid var(--rule);border-radius:9px;padding:10px;font-size:16px;width:100%;min-height:44px}
#savebar{display:none;position:sticky;bottom:0;background:var(--acc);color:#111;padding:10px 12px;text-align:center;font-size:14.5px;z-index:6}
#savebar button{margin-left:8px;background:#111;color:#fff;border:0;border-radius:8px;padding:9px 14px;font-size:15px}
body.dirty #savebar{display:block}
/* app mode: one page at a time */
body.app article.page,body.app section.srcdoc{display:none}
body.app article.page.active,body.app section.srcdoc.active{display:block;border-top:none;margin-top:0}
body.app #tocwrap,body.app #staticnote{display:none}
body.app.athome article.page,body.app.athome section.srcdoc{display:none}
@media print{
  :root,html[data-t="light"]{--bg:#fff;--card:#fff;--ink:#000;--dim:#444;--rule:#999;--acc:#000;--mark:#ddd;--blank:#000}
  body{font-size:11pt;line-height:1.4}
  header.top,#view,#staticnote,#savebar,footer,.noprint,.pbtns,#tocwrap details:not([open]) ul{display:none!important}
  body.app article.page,body.app section.srcdoc,article.page,section.srcdoc{display:block!important;border:none;margin:0}
  article.page{break-before:page}
  article.page.tab{break-before:page;padding-top:30vh}
  article.page.tab .ph h1{font-size:30pt}
  section.srcdoc{break-before:page;border:1px solid #999}
  a.xref{border:none;background:none;padding:0}
  details.sec{break-inside:avoid}
  figure,table,blockquote{break-inside:avoid}
  .stamp{font-size:9pt}
}
`;
