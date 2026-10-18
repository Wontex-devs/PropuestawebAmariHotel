/**
 * CONSENTIMIENTO — contenido de terceros y preferencias de cookies
 * --------------------------------------------------------------
 * - Por defecto NO se carga nada opcional: el mapa de Google solo se
 *   inserta si la persona pulsa «Cargar mapa» o lo acepta en preferencias.
 * - La elección se guarda en localStorage (`amari.consent`), solo como
 *   preferencia del navegador, máximo 12 meses. No es un registro oficial.
 * - Para añadir otra categoría (p. ej. analítica), sumarla a CATEGORIES
 *   y cargar su script únicamente cuando `getConsent()[id] === true`.
 */

const KEY = 'amari.consent';
const MAX_AGE_MS = 365 * 24 * 60 * 60 * 1000;
const LANG = (document.documentElement.lang || 'es').toLowerCase().startsWith('en') ? 'en' : 'es';

const T = {
  es: {
    title: 'Preferencias de cookies',
    intro:
      'Este sitio no usa cookies de analítica ni de publicidad. Puedes elegir si cargar contenido de terceros que puede instalar sus propias cookies.',
    necessary: 'Necesarias',
    necessaryText: 'Guardan esta elección en tu navegador. Siempre activas.',
    maps: 'Mapas (Google Maps)',
    mapsText: 'Muestra el mapa de ubicación. Google recibe tu dirección IP y puede instalar cookies.',
    reject: 'Rechazar opcionales',
    save: 'Guardar preferencias',
    accept: 'Aceptar todas',
    close: 'Cerrar',
    policy: 'Política de cookies',
    saved: 'Preferencias guardadas.',
  },
  en: {
    title: 'Cookie preferences',
    intro:
      'This website does not use analytics or advertising cookies. You can choose whether to load third-party content that may set its own cookies.',
    necessary: 'Necessary',
    necessaryText: 'Store this choice in your browser. Always on.',
    maps: 'Maps (Google Maps)',
    mapsText: 'Shows the location map. Google receives your IP address and may set cookies.',
    reject: 'Reject optional',
    save: 'Save preferences',
    accept: 'Accept all',
    close: 'Close',
    policy: 'Cookie policy',
    saved: 'Preferences saved.',
  },
}[LANG];

const CATEGORIES = [{ id: 'maps', label: T.maps, text: T.mapsText }];

export function getConsent() {
  try {
    const c = JSON.parse(localStorage.getItem(KEY));
    if (!c || c.v !== 1 || Date.now() - Date.parse(c.date) > MAX_AGE_MS) return null;
    return c;
  } catch {
    return null;
  }
}

function setConsent(choices) {
  const c = { ...choices, v: 1, date: new Date().toISOString() };
  try {
    localStorage.setItem(KEY, JSON.stringify(c));
  } catch {
    /* Navegación privada o almacenamiento bloqueado: la elección vale solo para esta visita */
  }
  apply(c);
  return c;
}

/* ---------- Mapa de Google: se inserta solo con consentimiento ---------- */
let mapUrl = null;

function loadMap() {
  document.querySelectorAll('[data-map-consent]').forEach((ph) => {
    if (!mapUrl) return;
    const iframe = document.createElement('iframe');
    iframe.src = mapUrl;
    iframe.title = ph.dataset.mapTitle || 'Google Maps';
    iframe.loading = 'lazy';
    iframe.referrerPolicy = 'strict-origin-when-cross-origin';
    iframe.allowFullscreen = true;
    iframe.dataset.mapFrame = '';
    ph.hidden = true;
    ph.after(iframe);
  });
}

function unloadMap() {
  document.querySelectorAll('[data-map-frame]').forEach((f) => f.remove());
  document.querySelectorAll('[data-map-consent]').forEach((ph) => (ph.hidden = false));
}

function apply(c) {
  if (c && c.maps) {
    if (!document.querySelector('[data-map-frame]')) loadMap();
  } else {
    unloadMap();
  }
}

/* ---------- Diálogo de preferencias ---------- */
let dialog = null;

function buildDialog(policyHref) {
  const d = document.createElement('dialog');
  d.className = 'cookie-prefs';
  d.setAttribute('aria-labelledby', 'cookie-prefs-title');
  const items = CATEGORIES.map(
    (c) => `
      <li class="cookie-prefs__item">
        <input type="checkbox" id="consent-${c.id}" name="${c.id}" />
        <label for="consent-${c.id}"><strong>${c.label}</strong><span>${c.text}</span></label>
      </li>`
  ).join('');
  d.innerHTML = `
    <form method="dialog">
      <button class="icon-btn cookie-prefs__close" type="button" data-prefs-close aria-label="${T.close}">
        <svg class="icon" aria-hidden="true"><use href="#i-close" /></svg>
      </button>
      <h2 id="cookie-prefs-title">${T.title}</h2>
      <p>${T.intro} <a href="${policyHref}">${T.policy}</a>.</p>
      <ul class="cookie-prefs__list" role="list">
        <li class="cookie-prefs__item">
          <input type="checkbox" id="consent-necessary" checked disabled />
          <label for="consent-necessary"><strong>${T.necessary}</strong><span>${T.necessaryText}</span></label>
        </li>${items}
      </ul>
      <div class="cookie-prefs__actions">
        <button class="btn btn--sm btn--outline" type="button" data-prefs="reject">${T.reject}</button>
        <button class="btn btn--sm btn--outline" type="button" data-prefs="save">${T.save}</button>
        <button class="btn btn--sm btn--outline" type="button" data-prefs="accept">${T.accept}</button>
      </div>
      <p class="sr-only" role="status" aria-live="polite" data-prefs-status></p>
    </form>`;
  d.addEventListener('click', (e) => {
    const action = e.target.closest('[data-prefs]')?.dataset.prefs;
    if (e.target === d || e.target.closest('[data-prefs-close]')) d.close();
    if (!action) return;
    const choices = {};
    CATEGORIES.forEach((c) => {
      const box = d.querySelector(`[name="${c.id}"]`);
      choices[c.id] = action === 'accept' ? true : action === 'reject' ? false : box.checked;
    });
    setConsent(choices);
    d.querySelector('[data-prefs-status]').textContent = T.saved;
    d.close();
  });
  document.body.append(d);
  return d;
}

function openPrefs(policyHref, opener) {
  if (!dialog) dialog = buildDialog(policyHref);
  const c = getConsent() || {};
  CATEGORIES.forEach((cat) => {
    dialog.querySelector(`[name="${cat.id}"]`).checked = Boolean(c[cat.id]);
  });
  dialog.addEventListener('close', () => opener && opener.focus(), { once: true });
  if (typeof dialog.showModal === 'function') dialog.showModal();
  else dialog.setAttribute('open', '');
}

/**
 * @param {{ mapsEmbedUrl: string }} opts
 *   El enlace a la política sale del atributo data-policy del botón «Preferencias de cookies».
 */
export function setupConsent({ mapsEmbedUrl }) {
  mapUrl = mapsEmbedUrl;

  // Botón «Cargar mapa» (con opción de recordar la elección)
  document.querySelectorAll('[data-map-consent]').forEach((ph) => {
    const btn = ph.querySelector('[data-map-load]');
    const remember = ph.querySelector('[data-map-remember]');
    btn?.addEventListener('click', () => {
      if (remember?.checked) setConsent({ ...(getConsent() || {}), maps: true });
      else loadMap();
    });
  });

  document.querySelectorAll('[data-cookie-prefs]').forEach((b) =>
    b.addEventListener('click', () => openPrefs(b.dataset.policy || '#', b))
  );

  apply(getConsent());
}
