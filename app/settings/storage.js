// The ONLY use of browser storage on this page: the opt-in "Keep my answers in this browser"
// toggle. It defaults to off. While it is off nothing is written, and turning it off erases what
// was kept. The access key is never written here.

const KEY = 'goettschepreppy.settings.kept-answers.v1';

export function readKept() {
  try {
    const s = localStorage.getItem(KEY);
    if (!s) return null;
    const v = JSON.parse(s);
    return v && typeof v === 'object' && v.profile ? v : null;
  } catch { return null; }
}
export function writeKept(profile, step) {
  try {
    const p = structuredClone(profile);
    if (p.access) delete p.access.access_key;
    localStorage.setItem(KEY, JSON.stringify({ kept_at: new Date().toISOString(), step, profile: p }));
    return true;
  } catch { return false; }
}
export function eraseKept() {
  try { localStorage.removeItem(KEY); } catch { /* storage blocked: nothing kept anyway */ }
}
