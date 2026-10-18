import { config } from './config.js';

/* ============================================================
   Utilidades
   ============================================================ */
const $ = (sel, root = document) => root.querySelector(sel);
const $$ = (sel, root = document) => [...root.querySelectorAll(sel)];

/* Idioma de la página (<html lang>): 'es' o 'en' */
const LANG = (document.documentElement.lang || 'es').toLowerCase().startsWith('en') ? 'en' : 'es';
const LOCALE = LANG === 'en' ? 'en-US' : 'es-CO';

/* Textos de interfaz generados por JavaScript, por idioma */
const T = {
  es: {
    newTab: 'abre el motor de reservas en una pestaña nueva',
    waPending: 'WhatsApp por confirmar',
    perHour: 'hora',
    and: 'y',
    pleaseFill: 'Por favor indica',
    fName: 'tu nombre',
    fCheckin: 'la fecha de llegada',
    fCheckout: 'la fecha de salida',
    fCheckoutAfter: 'una fecha de salida posterior a la llegada',
    fGuests: 'la cantidad de personas',
    person: 'persona',
    people: 'personas',
    waIntro: (n) => `Hola, soy ${n}. Estoy interesado/a en hospedarme en Amari Living Suites.`,
    waAsk: 'Quisiera consultar disponibilidad y opciones de reserva:',
    waIn: 'Llegada',
    waOut: 'Salida',
    waGuests: 'Huéspedes',
    waOpened:
      'Abrimos WhatsApp con tu mensaje. Nuestro equipo te responderá para confirmar disponibilidad; la reserva aún no está confirmada.',
    menuOpen: 'Abrir menú',
    menuClose: 'Cerrar menú',
    fEmail: 'un correo electrónico válido',
    fMessage: 'tu mensaje',
    fConsent: 'aceptar el tratamiento de datos',
    mailSubject: (n) => `Mensaje desde la web — ${n}`,
    mailBody: (n, e, m) => `Nombre: ${n}\nCorreo: ${e}\n\n${m}`,
    mailOpened: (mail) =>
      `Abrimos tu aplicación de correo con el mensaje listo para enviar. Si no se abrió, escríbenos a ${mail}.`,
    photo: 'Fotografía',
    of: 'de',
    videoTitle: 'Video de Amari Living Suites',
  },
  en: {
    newTab: 'opens the booking engine in a new tab',
    waPending: 'WhatsApp to be confirmed',
    perHour: 'hour',
    and: 'and',
    pleaseFill: 'Please enter',
    fName: 'your name',
    fCheckin: 'the check-in date',
    fCheckout: 'the check-out date',
    fCheckoutAfter: 'a check-out date after check-in',
    fGuests: 'the number of guests',
    person: '',
    people: '',
    waIntro: (n) => `Hello, my name is ${n}. I’m interested in staying at Amari Living Suites.`,
    waAsk: 'Could you help me check availability and booking options?',
    waIn: 'Check-in',
    waOut: 'Check-out',
    waGuests: 'Number of guests',
    waOpened:
      'We opened WhatsApp with your message. Our team will reply to confirm availability; your booking is not confirmed yet.',
    menuOpen: 'Open menu',
    menuClose: 'Close menu',
    fEmail: 'a valid email address',
    fMessage: 'your message',
    fConsent: 'accept the data processing terms',
    mailSubject: (n) => `Message from the website — ${n}`,
    mailBody: (n, e, m) => `Name: ${n}\nEmail: ${e}\n\n${m}`,
    mailOpened: (mail) => `We opened your email app with the message ready to send. If it did not open, write to us at ${mail}.`,
    photo: 'Photo',
    of: 'of',
    videoTitle: 'Amari Living Suites video',
  },
}[LANG];

const pick = (v) => (v && typeof v === 'object' && !Array.isArray(v) ? v[LANG] ?? v.es : v);
const listJoin = (parts) =>
  parts.length > 1 ? `${parts.slice(0, -1).join(', ')} ${T.and} ${parts[parts.length - 1]}` : parts[0];

/** Construye un enlace wa.me con el número internacional y el mensaje codificado. */
export function buildWhatsAppUrl(number, message) {
  const digits = String(number || '').replace(/\D/g, '');
  if (!digits) return null;
  return `https://wa.me/${digits}?text=${encodeURIComponent(message)}`;
}

function formatHourlyRate(value) {
  if (typeof value !== 'number' || !Number.isFinite(value) || value <= 0) {
    return pick(config.rates.pendingLabel);
  }
  return `$${value.toLocaleString('es-CO')} ${config.rates.currency} / ${T.perHour}`;
}

/* ============================================================
   1. Hidratar datos desde la configuración central
   ============================================================ */
function hydrateLinks() {
  // Reserva en línea (Cloudbeds)
  $$('[data-booking]').forEach((el) => {
    el.href = config.bookingUrl;
    if (!el.getAttribute('aria-label')) {
      el.setAttribute('aria-label', `${el.textContent.trim()} (${T.newTab})`);
    }
  });

  // WhatsApp
  const workspaceNumber = config.workspacesWhatsApp || config.contact.amariWhatsApp;
  const msg = config.messages[LANG] || config.messages.es;
  const targets = {
    amari: { number: config.contact.amariWhatsApp, message: msg.amari },
    cowork: { number: workspaceNumber, message: msg.cowork },
    meeting: { number: workspaceNumber, message: msg.meeting },
    restaurant: { number: config.allies.restaurant.whatsapp, message: msg.restaurant },
    laundry: { number: config.allies.laundry.whatsapp, message: msg.laundry },
  };

  $$('[data-wa]').forEach((el) => {
    const key = el.dataset.wa;
    const target = targets[key];

    if ((key === 'restaurant' || key === 'laundry') && !config.features.allyWhatsAppButtons) {
      el.remove();
      return;
    }

    const url = target ? buildWhatsAppUrl(target.number, target.message) : null;
    if (url) {
      el.href = url;
      return;
    }

    // Número no confirmado: no se publica un enlace ficticio.
    el.removeAttribute('href');
    el.removeAttribute('target');
    el.classList.add('is-pending');
    el.setAttribute('role', 'link');
    el.setAttribute('aria-disabled', 'true');
    const label = el.dataset.pendingLabel || T.waPending;
    const icon = el.querySelector('svg');
    el.textContent = '';
    if (icon) el.append(icon);
    el.append(document.createTextNode(label));
    console.warn(`[Amari] WhatsApp "${key}" pendiente: configure el número en src/js/config.js`);
  });

  // Tarifas por hora
  const rates = { cowork: config.rates.coworkHourlyRate, meeting: config.rates.meetingRoomHourlyRate };
  $$('[data-rate]').forEach((el) => {
    el.textContent = formatHourlyRate(rates[el.dataset.rate]);
  });

  // Nombres de aliados
  $$('[data-ally-name]').forEach((el) => {
    const ally = config.allies[el.dataset.allyName];
    if (ally) el.textContent = ally.name || pick(ally.fallbackName);
  });

  // Contacto
  const c = config.contact;
  $$('[data-contact]').forEach((el) => {
    switch (el.dataset.contact) {
      case 'address':
        el.textContent = `${c.address}, ${config.brand.city}`;
        break;
      case 'phoneMobile':
        el.href = `tel:${c.phoneMobile.tel}`;
        el.textContent = c.phoneMobile.label;
        break;
      case 'phoneLandline':
        el.href = `tel:${c.phoneLandline.tel}`;
        el.textContent = c.phoneLandline.label;
        break;
      case 'email':
        el.href = `mailto:${c.email}`;
        el.textContent = c.email;
        break;
      case 'directions':
        el.href = c.mapsDirectionsUrl;
        break;
      case 'map':
        el.src = c.mapsEmbedUrl;
        break;
      default:
        break;
    }
  });

  // Políticas
  const policies = $('[data-policies]');
  if (policies) {
    policies.innerHTML = '';
    config.policies.forEach((p) => {
      const li = document.createElement('li');
      const a = document.createElement('a');
      a.href = `politicas.html#${p.id}`;
      a.textContent = pick(p);
      li.append(a);
      policies.append(li);
    });
  }

  const year = $('[data-year]');
  if (year) year.textContent = String(new Date().getFullYear());
}

/* ============================================================
   2. Formularios de consulta → WhatsApp (no confirma reservas)
   ============================================================ */
function toISODate(d) {
  const tz = d.getTimezoneOffset() * 60000;
  return new Date(d - tz).toISOString().slice(0, 10);
}

function readableDate(iso) {
  const d = new Date(`${iso}T12:00:00`);
  return d.toLocaleDateString(LOCALE, { weekday: 'long', day: 'numeric', month: 'long', year: 'numeric' });
}

function setupBookingForms() {
  const today = toISODate(new Date());

  $$('[data-booking-form]').forEach((form) => {
    const name = form.elements.name;
    const checkin = form.elements.checkin;
    const checkout = form.elements.checkout;
    const guests = form.elements.guests;
    const status = $('[data-form-status]', form);

    checkin.min = today;
    checkout.min = today;

    checkin.addEventListener('change', () => {
      if (!checkin.value) return;
      const next = new Date(`${checkin.value}T12:00:00`);
      next.setDate(next.getDate() + 1);
      checkout.min = toISODate(next);
      if (checkout.value && checkout.value <= checkin.value) checkout.value = '';
    });

    form.addEventListener('input', (e) => e.target.removeAttribute('aria-invalid'));

    form.addEventListener('submit', (e) => {
      e.preventDefault();
      status.classList.remove('is-error');

      const errors = [];
      [name, checkin, checkout, guests].forEach((f) => f.removeAttribute('aria-invalid'));
      if (!name.value.trim()) errors.push([name, T.fName]);
      if (!checkin.value) errors.push([checkin, T.fCheckin]);
      if (!checkout.value) errors.push([checkout, T.fCheckout]);
      if (checkin.value && checkout.value && checkout.value <= checkin.value) {
        errors.push([checkout, T.fCheckoutAfter]);
      }
      if (!guests.value) errors.push([guests, T.fGuests]);

      if (errors.length) {
        errors.forEach(([f]) => f.setAttribute('aria-invalid', 'true'));
        status.classList.add('is-error');
        status.textContent = `${T.pleaseFill} ${listJoin(errors.map(([, t]) => t))}.`;
        errors[0][0].focus();
        return;
      }

      const g = guests.value;
      const people = (g === '1' ? `1 ${T.person}` : /^\d+$/.test(g) ? `${g} ${T.people}` : guests.selectedOptions[0].text).trim();
      const message = [
        T.waIntro(name.value.trim()),
        T.waAsk,
        `• ${T.waIn}: ${readableDate(checkin.value)}`,
        `• ${T.waOut}: ${readableDate(checkout.value)}`,
        `• ${T.waGuests}: ${people}`,
      ].join('\n');

      const url = buildWhatsAppUrl(config.contact.amariWhatsApp, message);
      // Con 'noopener' window.open devuelve null; se anula opener manualmente.
      const win = window.open(url, '_blank');
      if (win) win.opener = null;
      else window.location.href = url;
      status.textContent = T.waOpened;
    });
  });
}

/* ============================================================
   3. Encabezado y navegación
   ============================================================ */
function setupHeader() {
  const header = $('[data-header]');
  if (!header) return;
  const alwaysSolid = header.hasAttribute('data-header-solid');
  const update = () => header.classList.toggle('is-solid', alwaysSolid || window.scrollY > 40);
  update();
  window.addEventListener('scroll', update, { passive: true });
}

function setupScrollSpy() {
  const links = $$('[data-nav-link]');
  const indicator = $('[data-nav-indicator]');
  const sections = links.map((l) => $(l.getAttribute('href'))).filter(Boolean);
  if (!sections.length) return;

  const moveIndicator = (link) => {
    if (!indicator) return;
    if (!link) {
      indicator.classList.remove('is-visible');
      return;
    }
    const navBox = indicator.parentElement.getBoundingClientRect();
    const box = link.getBoundingClientRect();
    indicator.style.width = `${box.width}px`;
    indicator.style.transform = `translateX(${box.left - navBox.left}px)`;
    indicator.classList.add('is-visible');
  };

  let current = null;
  const setActive = (id) => {
    if (id === current) return;
    current = id;
    let activeLink = null;
    links.forEach((l) => {
      const on = l.getAttribute('href') === `#${id}`;
      if (on) {
        l.setAttribute('aria-current', 'true');
        activeLink = l;
      } else l.removeAttribute('aria-current');
    });
    moveIndicator(activeLink);
  };

  const io = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) setActive(entry.target.id);
      });
    },
    { rootMargin: '-45% 0px -50% 0px' }
  );
  sections.forEach((s) => io.observe(s));

  window.addEventListener('resize', () => {
    const active = links.find((l) => l.hasAttribute('aria-current'));
    moveIndicator(active || null);
  });
}

function setupMobileMenu() {
  const toggle = $('[data-menu-toggle]');
  const menu = $('[data-mobile-menu]');
  if (!toggle || !menu) return;
  const label = $('[data-menu-label]', toggle);
  const outside = $$('main, footer, .wa-float, .mobile-bar, .skip-link');
  const animated = () => document.documentElement.classList.contains('motion');
  let closeTimer;

  const open = () => {
    clearTimeout(closeTimer);
    menu.hidden = false;
    // Forzar reflujo para que la transición de entrada se ejecute
    void menu.offsetHeight;
    menu.classList.add('is-open');
    toggle.setAttribute('aria-expanded', 'true');
    label.textContent = T.menuClose;
    document.body.classList.add('is-locked', 'menu-open');
    outside.forEach((el) => (el.inert = true));
    const first = $('a', menu);
    if (first) first.focus({ preventScroll: true });
  };

  const close = ({ returnFocus = true } = {}) => {
    menu.classList.remove('is-open');
    toggle.setAttribute('aria-expanded', 'false');
    label.textContent = T.menuOpen;
    document.body.classList.remove('is-locked', 'menu-open');
    outside.forEach((el) => (el.inert = false));
    closeTimer = setTimeout(() => (menu.hidden = true), animated() ? 700 : 0);
    if (returnFocus) toggle.focus({ preventScroll: true });
  };

  toggle.addEventListener('click', () => (toggle.getAttribute('aria-expanded') === 'true' ? close() : open()));

  $$('a', menu).forEach((a) =>
    a.addEventListener('click', () => {
      close({ returnFocus: false });
    })
  );

  document.addEventListener('keydown', (e) => {
    if (toggle.getAttribute('aria-expanded') !== 'true') return;
    if (e.key === 'Escape') close();
    if (e.key === 'Tab') {
      const focusables = [toggle, ...$$('a', menu)];
      const idx = focusables.indexOf(document.activeElement);
      if (e.shiftKey && idx <= 0) {
        e.preventDefault();
        focusables[focusables.length - 1].focus();
      } else if (!e.shiftKey && idx === focusables.length - 1) {
        e.preventDefault();
        focusables[0].focus();
      }
    }
  });

  window.matchMedia('(min-width: 1081px)').addEventListener('change', (mq) => {
    if (mq.matches && toggle.getAttribute('aria-expanded') === 'true') close({ returnFocus: false });
  });
}

/* ============================================================
   4. Galería desplazable
   ============================================================ */
function setupGallery() {
  $$('[data-gallery]').forEach((gallery) => {
    const track = $('[data-gallery-track]', gallery);
    const prev = $('[data-gallery-prev]', gallery);
    const next = $('[data-gallery-next]', gallery);
    if (!track || !prev || !next) return;

    const step = () => Math.max(track.clientWidth * 0.75, 280);
    const update = () => {
      prev.disabled = track.scrollLeft <= 4;
      next.disabled = track.scrollLeft + track.clientWidth >= track.scrollWidth - 4;
    };
    prev.addEventListener('click', () => track.scrollBy({ left: -step(), behavior: 'smooth' }));
    next.addEventListener('click', () => track.scrollBy({ left: step(), behavior: 'smooth' }));
    track.addEventListener('scroll', update, { passive: true });
    window.addEventListener('resize', update);
    update();
  });
}

/* ============================================================
   5. Hero "reel": las escenas 2…6 se cargan después de la primera,
      para no retrasar la carga inicial. La animación es solo CSS.
   ============================================================ */
function setupHeroReel() {
  const pending = $$('.hero-reel img[data-src]');
  if (!pending.length) return;
  const load = () =>
    pending.forEach((img) => {
      if (img.dataset.srcset) img.srcset = img.dataset.srcset;
      img.src = img.dataset.src;
      img.removeAttribute('data-src');
      img.removeAttribute('data-srcset');
    });
  if (document.readyState === 'complete') setTimeout(load, 150);
  else window.addEventListener('load', () => setTimeout(load, 150), { once: true });

  // Sin menú contextual ni arrastre sobre el reel (no es un video manipulable)
  $$('.hero-reel').forEach((reel) => reel.addEventListener('contextmenu', (e) => e.preventDefault()));
}

/* ============================================================
   Galería completa con visor (todas las fotos de la web actual)
   ============================================================ */
function setupLightbox() {
  const box = $('[data-lightbox]');
  const dataEl = $('[data-gallery-data]');
  if (!box || !dataEl) return;
  let items = [];
  try {
    items = JSON.parse(dataEl.textContent);
  } catch {
    return;
  }
  const img = $('[data-lightbox-img]', box);
  const caption = $('[data-lightbox-caption]', box);
  const counter = $('[data-lightbox-counter]', box);
  const closeBtn = $('[data-lightbox-close]', box);
  const outside = $$('main, footer, header, .mobile-bar');
  let index = 0;
  let opener = null;

  const show = (i) => {
    index = (i + items.length) % items.length;
    const it = items[index];
    img.src = it.src;
    img.alt = it.alt;
    caption.textContent = it.alt;
    counter.textContent = `${index + 1} ${T.of} ${items.length}`;
    // Precarga de la siguiente
    const nxt = new Image();
    nxt.src = items[(index + 1) % items.length].src;
  };

  const open = (i, trigger) => {
    opener = trigger || null;
    box.hidden = false;
    document.body.classList.add('is-locked');
    outside.forEach((el) => (el.inert = true));
    show(i);
    closeBtn.focus();
  };

  const close = () => {
    box.hidden = true;
    document.body.classList.remove('is-locked');
    outside.forEach((el) => (el.inert = false));
    img.removeAttribute('src');
    if (opener) opener.focus();
  };

  $$('[data-gallery-open]').forEach((btn) =>
    btn.addEventListener('click', () => open(Number(btn.dataset.galleryOpen) || 0, btn))
  );
  closeBtn.addEventListener('click', close);
  $('[data-lightbox-prev]', box).addEventListener('click', () => show(index - 1));
  $('[data-lightbox-next]', box).addEventListener('click', () => show(index + 1));
  box.addEventListener('click', (e) => {
    if (e.target === box) close();
  });
  document.addEventListener('keydown', (e) => {
    if (box.hidden) return;
    if (e.key === 'Escape') close();
    if (e.key === 'ArrowRight') show(index + 1);
    if (e.key === 'ArrowLeft') show(index - 1);
    if (e.key === 'Tab') {
      const f = $$('button', box);
      const i = f.indexOf(document.activeElement);
      if (e.shiftKey && i <= 0) {
        e.preventDefault();
        f[f.length - 1].focus();
      } else if (!e.shiftKey && i === f.length - 1) {
        e.preventDefault();
        f[0].focus();
      }
    }
  });
  // Deslizar en pantallas táctiles
  let x0 = null;
  box.addEventListener('touchstart', (e) => (x0 = e.touches[0].clientX), { passive: true });
  box.addEventListener('touchend', (e) => {
    if (x0 === null) return;
    const dx = e.changedTouches[0].clientX - x0;
    if (Math.abs(dx) > 50) show(index + (dx < 0 ? 1 : -1));
    x0 = null;
  });
}

/* ============================================================
   Formulario de contacto (como en la web actual) → correo
   ============================================================ */
function setupContactForm() {
  const form = $('[data-contact-form]');
  if (!form) return;
  const status = $('[data-form-status]', form);
  const { name, email, message, consent } = form.elements;
  form.addEventListener('input', (e) => e.target.removeAttribute('aria-invalid'));
  form.addEventListener('change', (e) => e.target.removeAttribute('aria-invalid'));
  form.addEventListener('submit', (e) => {
    e.preventDefault();
    status.classList.remove('is-error');
    const errors = [];
    if (!name.value.trim()) errors.push([name, T.fName]);
    if (!email.value.trim() || !email.checkValidity()) errors.push([email, T.fEmail]);
    if (!message.value.trim()) errors.push([message, T.fMessage]);
    if (!consent.checked) errors.push([consent, T.fConsent]);
    if (errors.length) {
      errors.forEach(([f]) => f.setAttribute('aria-invalid', 'true'));
      status.classList.add('is-error');
      status.textContent = `${T.pleaseFill} ${listJoin(errors.map(([, t]) => t))}.`;
      errors[0][0].focus();
      return;
    }
    const n = name.value.trim();
    const subject = encodeURIComponent(T.mailSubject(n));
    const body = encodeURIComponent(T.mailBody(n, email.value.trim(), message.value.trim()));
    window.location.href = `mailto:${config.contact.email}?subject=${subject}&body=${body}`;
    status.textContent = T.mailOpened(config.contact.email);
  });
}

/* ============================================================
   6. Tipografía oficial (Adobe Fonts) si existe kit
   ============================================================ */
function loadBrandFonts() {
  if (!config.adobeFontsKitId) return;
  const link = document.createElement('link');
  link.rel = 'stylesheet';
  link.href = `https://use.typekit.net/${encodeURIComponent(config.adobeFontsKitId)}.css`;
  document.head.append(link);
}

loadBrandFonts();
hydrateLinks();
setupBookingForms();
setupHeader();
setupScrollSpy();
setupMobileMenu();
setupGallery();
setupHeroReel();
setupLightbox();
setupContactForm();
