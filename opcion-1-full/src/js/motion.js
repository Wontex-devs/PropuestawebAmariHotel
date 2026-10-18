/* =============================================================
   MOTION — versión Full (sin dependencias)
   - Respeta prefers-reduced-motion: si está activo, no se ejecuta nada
     y todo el contenido queda visible.
   - IntersectionObserver para revelados (sin cálculos por scroll).
   - Parallax solo en elementos visibles, con requestAnimationFrame
     y la propiedad `translate` (no interfiere con otras transformaciones).
   - Sin scroll hijacking.
   ============================================================= */

const root = document.documentElement;
const reduce = window.matchMedia('(prefers-reduced-motion: reduce)');

if (!reduce.matches && 'IntersectionObserver' in window) {
  root.classList.add('motion');
  initIntro();
  initReveals();
  initParallax();
  initCounters();
  initPersistentActions();
}

/* Si el usuario activa "reducir movimiento" con la página abierta, se muestra todo. */
reduce.addEventListener?.('change', (e) => {
  if (e.matches) {
    root.classList.remove('motion');
    document.querySelectorAll('[data-parallax]').forEach((el) => (el.style.translate = ''));
  }
});

/* ---------- Entrada cinematográfica ---------- */
function initIntro() {
  // Si hay animación de logo, la entrada del hero empieza cuando sube la cortina
  if (document.querySelector('[data-splash]') && !root.classList.contains('splash-done')) {
    document.addEventListener('amari:splash-done', initIntro, { once: true });
    return;
  }
  const heroImg = document.querySelector('.hero__img');
  let started = false;
  const start = () => {
    if (started) return;
    started = true;
    const go = () => root.classList.add('is-ready');
    requestAnimationFrame(() => requestAnimationFrame(go));
    setTimeout(go, 120); // respaldo si rAF está en pausa (pestaña en segundo plano)
  };
  if (heroImg && !heroImg.complete) {
    heroImg.decode?.().then(start, start);
    heroImg.addEventListener('load', start, { once: true });
    // Nunca retrasar el contenido esencial más de ~0,6 s
    setTimeout(start, 600);
  } else {
    start();
  }
}

/* ---------- Revelado al desplazarse ---------- */
function initReveals() {
  const items = [...document.querySelectorAll('[data-reveal], [data-stagger], .workspace, .ally')];

  // Retardo escalonado entre hermanos con data-reveal
  document.querySelectorAll('[data-reveal]').forEach((el) => {
    const siblings = [...el.parentElement.children].filter((c) => c.hasAttribute('data-reveal'));
    const idx = siblings.indexOf(el);
    el.style.setProperty('--d', String(Math.min(idx, 5) * 90));
  });

  document.querySelectorAll('[data-stagger]').forEach((group) => {
    [...group.children].forEach((child, i) => child.style.setProperty('--i', String(i)));
  });

  const io = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        entry.target.classList.add('is-in');
        io.unobserve(entry.target);
      });
    },
    { rootMargin: '0px 0px -10% 0px', threshold: 0.12 }
  );
  items.forEach((el) => io.observe(el));
}

/* ---------- Parallax sutil ---------- */
function initParallax() {
  const els = [...document.querySelectorAll('[data-parallax]')];
  if (!els.length) return;
  const visible = new Set();
  let ticking = false;

  const io = new IntersectionObserver(
    (entries) => {
      entries.forEach((e) => (e.isIntersecting ? visible.add(e.target) : visible.delete(e.target)));
      requestTick();
    },
    { rootMargin: '10% 0px' }
  );
  els.forEach((el) => io.observe(el));

  function update() {
    ticking = false;
    const vh = window.innerHeight;
    const factor = window.innerWidth < 760 ? 0.5 : 1;
    visible.forEach((el) => {
      const speed = parseFloat(el.dataset.parallax) || 0.08;
      const rect = el.getBoundingClientRect();
      const offset = rect.top + rect.height / 2 - vh / 2;
      el.style.translate = `0 ${(-offset * speed * factor).toFixed(1)}px`;
    });
  }

  function requestTick() {
    if (!ticking) {
      ticking = true;
      requestAnimationFrame(update);
    }
  }

  window.addEventListener('scroll', requestTick, { passive: true });
  window.addEventListener('resize', requestTick);
}

/* ---------- Contador del descuento ---------- */
function initCounters() {
  const io = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        io.unobserve(entry.target);
        const el = entry.target;
        const to = Number(el.dataset.countTo) || 0;
        const duration = 1300;
        const t0 = performance.now();
        const step = (t) => {
          const p = Math.min((t - t0) / duration, 1);
          const eased = 1 - Math.pow(1 - p, 4);
          el.textContent = String(Math.round(to * eased));
          if (p < 1) requestAnimationFrame(step);
        };
        el.textContent = '0';
        requestAnimationFrame(step);
      });
    },
    { threshold: 0.6 }
  );
  document.querySelectorAll('[data-count-to]').forEach((el) => io.observe(el));
}

/* ---------- Botón flotante y barra móvil tras el hero ---------- */
function initPersistentActions() {
  const hero = document.querySelector('.hero');
  // La barra móvil queda siempre visible (es el acceso a reservar en el primer pantallazo)
  const targets = document.querySelectorAll('.wa-float');
  if (!hero) {
    targets.forEach((t) => t.classList.add('is-visible'));
    return;
  }
  const io = new IntersectionObserver(
    ([entry]) => targets.forEach((t) => t.classList.toggle('is-visible', !entry.isIntersecting)),
    { threshold: 0, rootMargin: '-40% 0px 0px 0px' }
  );
  io.observe(hero);
}
