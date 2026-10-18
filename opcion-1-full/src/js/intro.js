/* =============================================================
   ANIMACIÓN DE INICIO (splash) — controla la salida de la cortina.
   La coreografía del logo es 100 % CSS (src/styles/intro.css),
   así empieza desde el primer pintado sin esperar a JavaScript.

   - Se omite con prefers-reduced-motion (clase .no-splash en <head>).
   - Un clic, Enter, Espacio o Escape la saltan.
   - Al terminar emite "amari:splash-done" y añade .splash-done a <html>.
   ============================================================= */

window.__amariSplash = true;

const root = document.documentElement;
const splash = document.querySelector('[data-splash]');
// La cortina sube cuando termina la última pieza del logo ("Living Suites"),
// sincronizada con el CSS. El temporizador es solo un respaldo.
const FALLBACK = 3200; // ms

function finish() {
  root.classList.add('splash-done');
  document.dispatchEvent(new CustomEvent('amari:splash-done'));
}

if (!splash || root.classList.contains('no-splash') || !root.classList.contains('js')) {
  splash?.remove();
  finish();
} else {
  if ('scrollRestoration' in history) history.scrollRestoration = 'manual';
  window.scrollTo(0, 0);
  document.body.classList.add('is-locked');

  let done = false;
  const out = () => {
    if (done) return;
    done = true;
    clearTimeout(timer);
    splash.classList.add('is-out');
    document.body.classList.remove('is-locked');
    window.removeEventListener('keydown', onKey);
    // La página empieza su propia entrada mientras la cortina sube
    setTimeout(finish, 280);
    setTimeout(() => splash.remove(), 1000);
  };

  const onKey = (e) => {
    if (['Escape', 'Enter', ' '].includes(e.key)) out();
  };

  const timer = setTimeout(out, FALLBACK);
  const last = splash.querySelector('.splash__tag');
  last?.addEventListener('animationend', out, { once: true });
  splash.addEventListener('click', out);
  window.addEventListener('keydown', onKey);
}
