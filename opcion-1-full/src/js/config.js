/**
 * CONFIGURACIÓN CENTRAL — Amari Living Suites
 * --------------------------------------------------------------
 * Todos los datos comerciales y de contacto viven aquí.
 * Ningún componente debe tener teléfonos, precios ni URLs escritos a mano.
 *
 * Convención de estado:
 *   ✅ CONFIRMADO  → dato tomado de una fuente oficial (se indica cuál).
 *   ⏳ PENDIENTE   → dato no encontrado. Mientras sea `null`, la web muestra
 *                    un texto neutro y NO genera enlaces ni precios ficticios.
 */

export const config = {
  brand: {
    name: 'Amari Living Suites',
    city: 'Barranquilla',
    country: 'Colombia',
  },

  /* ✅ CONFIRMADO — URL oficial del motor de reservas (Cloudbeds). No modificar. */
  bookingUrl: 'https://hotels.cloudbeds.com/en/reservation/FuhJUM?currency=cop',

  contact: {
    /* ✅ CONFIRMADO — WhatsApp oficial publicado en las políticas de
       amarilivingsuite.com ("comuníquese vía whatsapp al número +573023307939"). */
    amariWhatsApp: '573023307939',
    /* ✅ CONFIRMADO — Teléfonos publicados en amarilivingsuite.com */
    phoneMobile: { label: '302 330 7939', tel: '+573023307939' },
    phoneLandline: { label: '605 313 3460', tel: '+576053133460' },
    /* ✅ CONFIRMADO */
    email: 'atencionalcliente@amarilivingsuite.com',
    address: 'Carrera 42F #76-41',
    addressCity: 'Barranquilla, Atlántico, Colombia',
    /* ✅ CONFIRMADO — Mapa embebido en la web actual (ficha "Amari Living Suites"). */
    mapsEmbedUrl:
      'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3943.8405507254724!2d-74.81665141380465!3d10.993649180160833!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x8ef42d2cc1030333%3A0x39323d0327e22376!2sAmari%20Living%20Suites!5e0!3m2!1ses-419!2sbr!4v1764865773029!5m2!1ses-419!2sbr',
    mapsDirectionsUrl:
      'https://www.google.com/maps/search/?api=1&query=Amari%20Living%20Suites%2C%20Carrera%2042F%20%2376-41%2C%20Barranquilla',
  },

  /* Espacios por horas. ⏳ PENDIENTE: tarifas no publicadas en ninguna fuente.
     Escribir el número entero en COP, p. ej. 45000 → se mostrará "$45.000 COP / hora". */
  rates: {
    coworkHourlyRate: null,
    meetingRoomHourlyRate: null,
    currency: 'COP',
    pendingLabel: { es: 'Consulta la tarifa por hora', en: 'Ask for the hourly rate' },
  },

  /* Contacto específico para cowork / sala de juntas.
     null → se usa el WhatsApp oficial de Amari (indicado en el brief). */
  workspacesWhatsApp: null,

  /* Negocios aliados — beneficio ✅ CONFIRMADO por el cliente: 10 % para huéspedes. */
  allies: {
    discountPercent: 10,
    restaurant: {
      /* ⏳ PENDIENTE: nombre comercial real. */
      name: null,
      fallbackName: { es: 'Restaurante-café aliado', en: 'Partner restaurant-café' },
      /* ⏳ PENDIENTE: WhatsApp oficial del restaurante-café (formato 57XXXXXXXXXX).
         NO usar el número de Amari aquí. */
      whatsapp: null,
    },
    laundry: {
      /* ⏳ PENDIENTE: nombre comercial real. */
      name: null,
      fallbackName: { es: 'Lavandería aliada', en: 'Partner laundry' },
      /* ⏳ PENDIENTE: WhatsApp oficial de la lavandería. */
      whatsapp: null,
    },
  },

  /* Mensajes precargados de WhatsApp (se codifican automáticamente), por idioma. */
  messages: {
    es: {
      amari:
        'Hola, me gustaría hospedarme en Amari Living Suites. ¿Me ayudan a consultar disponibilidad y opciones de reserva?',
      cowork:
        'Hola, quisiera consultar la disponibilidad y la tarifa por hora del cowork de Amari Living Suites.',
      meeting:
        'Hola, quisiera consultar la disponibilidad y la tarifa por hora de la sala de juntas de Amari Living Suites.',
      restaurant:
        'Hola, soy huésped de Amari Living Suites y quisiera consultar sobre el beneficio del 10 % de descuento y los servicios del restaurante-café.',
      laundry:
        'Hola, soy huésped de Amari Living Suites y quisiera consultar sobre el servicio de lavandería y el beneficio del 10 % de descuento.',
    },
    en: {
      amari:
        'Hello, I would like to stay at Amari Living Suites. Could you help me check availability and booking options?',
      cowork:
        'Hello, I would like to check the availability and hourly rate of the Amari Living Suites coworking space.',
      meeting:
        'Hello, I would like to check the availability and hourly rate of the Amari Living Suites meeting room.',
      restaurant:
        'Hello, I am a guest at Amari Living Suites and I would like to ask about the 10% discount and the restaurant-café services.',
      laundry:
        'Hello, I am a guest at Amari Living Suites and I would like to ask about the laundry service and the 10% discount.',
    },
  },

  /* Políticas: páginas propias del sitio (texto tomado de la web actual). */
  policies: [
    { id: 'cancelacion', es: 'Política de cancelación', en: 'Cancellation policy' },
    { id: 'pagos', es: 'Política de pagos', en: 'Payment policy' },
    { id: 'servicios', es: 'Política de servicios', en: 'Service policy' },
    { id: 'terminos', es: 'Términos y condiciones', en: 'Terms and conditions' },
    { id: 'privacidad', es: 'Política de privacidad', en: 'Privacy policy' },
  ],

  /* IvyMode ya se carga desde public/fonts (archivo de la web actual del cliente).
     Opcional: si el cliente prefiere su kit de Adobe Fonts, poner aquí su ID. */
  adobeFontsKitId: null,

  /* Diferencia funcional entre versiones (Full = true, Sencilla = false). */
  features: {
    allyWhatsAppButtons: true,
  },
};
