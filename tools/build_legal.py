"""Genera los documentos legales (borradores) en rutas estables, ES y EN:
  /terminos-y-condiciones/  /politica-de-privacidad/  /politica-de-cookies/
  /en/terms-and-conditions/ /en/privacy-policy/       /en/cookie-policy/
Uso: python3 build_legal.py <carpeta-proyecto>
Ningún dato empresarial se inventa: lo que falta queda marcado como pendiente.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_policies import page
from site_common import ROUTES
from urllib.parse import quote

P = sys.argv[1]
VERSION = 'Borrador v0.1 · 18 de octubre de 2026'
VERSION_EN = 'Draft v0.1 · October 18, 2026'
MAIL = 'atencionalcliente@amarilivingsuite.com'
MAILTO = f'<a href="mailto:{MAIL}">{MAIL}</a>'

def pend(t, en=False):
    return f'<mark class="pending">[{"Pending" if en else "Pendiente"}: {t}]</mark>'

WA = {
    'es': 'https://wa.me/573023307939?text=' + quote('Hola, me gustaría hospedarme en Amari Living Suites. ¿Me ayudan a consultar disponibilidad y opciones de reserva?', safe="-_.!~*'()"),
    'en': 'https://wa.me/573023307939?text=' + quote('Hello, I would like to stay at Amari Living Suites. Could you help me check availability and booking options?', safe="-_.!~*'()"),
}

COMMON_ES = {
    'lang': 'es-CO', 'eyebrow': 'Información legal', 'toc': 'Contenido', 'back': 'Volver al inicio',
    'book': 'Reservar ahora', 'wa': 'Escríbenos por WhatsApp', 'langLabel': 'English version',
    'langCode': ('ES', 'EN'), 'copy': 'Amari Living Suites · Barranquilla, Colombia', 'robots': 'noindex, follow',
    'notice': '<strong>Borrador para revisión.</strong> Este documento aún no ha sido aprobado por Amari Living Suites ni revisado por un asesor jurídico. Los datos marcados como pendientes deben completarse antes de publicarlo de forma definitiva.',
}
COMMON_EN = {
    'lang': 'en', 'eyebrow': 'Legal information', 'toc': 'Contents', 'back': 'Back to home',
    'book': 'Book now', 'wa': 'Message us on WhatsApp', 'langLabel': 'Versión en español',
    'langCode': ('EN', 'ES'), 'copy': 'Amari Living Suites · Barranquilla, Colombia', 'robots': 'noindex, follow',
    'notice': '<strong>Draft for review.</strong> This document has not yet been approved by Amari Living Suites or reviewed by a legal advisor. Items marked as pending must be completed before final publication.',
    'note': 'This is a translation for reference. In case of any discrepancy, the Spanish version shall prevail.',
}

def identity(en=False):
    if en:
        return [
            ('ul', [
                'Trade name: Amari Living Suites',
                'Legal name: ' + pend('legal name of the company or individual', True),
                'Tax ID (NIT): ' + pend('NIT', True),
                'National Tourism Registry (RNT): ' + pend('RNT number', True),
                'Address: Carrera 42F #76-41, Barranquilla, Atlántico, Colombia',
                'Address for legal notices: ' + pend('address for judicial notifications', True),
                'Phone: +57 302 330 7939 · +57 605 313 3460',
                'Email: ' + MAILTO,
            ]),
        ]
    return [
        ('ul', [
            'Nombre comercial: Amari Living Suites',
            'Razón social: ' + pend('razón social de la empresa o persona natural'),
            'NIT: ' + pend('NIT'),
            'Registro Nacional de Turismo (RNT): ' + pend('número de RNT'),
            'Dirección: Carrera 42F #76-41, Barranquilla, Atlántico, Colombia',
            'Dirección de notificación judicial: ' + pend('dirección de notificación judicial'),
            'Teléfonos: +57 302 330 7939 · +57 605 313 3460',
            'Correo electrónico: ' + MAILTO,
        ]),
    ]

# ---------------------------------------------------------------- TÉRMINOS
TERMS_ES = dict(COMMON_ES, **{
    'title': 'Términos y condiciones | Amari Living Suites',
    'crumb': 'Términos y condiciones',
    'desc': 'Términos y condiciones de la prestación del servicio de alojamiento y del uso del sitio web de Amari Living Suites en Barranquilla.',
    'h1': 'Términos y <em>condiciones</em>',
    'intro': 'El Hotel Amari Living Suites, en su estructura de servicio a todos sus clientes y huéspedes, presenta sus términos y condiciones para la prestación del servicio.',
    'sections': [
        ('prestador', 'Identificación del prestador', identity()),
        ('objetivo', 'Objetivo y alcance', [
            ('h', 'Objetivo'),
            ('p', 'Proveer las políticas, condiciones y términos de la reserva de habitación adquirida en Amari Living Suites, en desarrollo del cumplimiento de los lineamientos internos y las disposiciones legales aplicables.'),
            ('h', 'Alcance'),
            ('p', 'Aplica para el cliente que ha adquirido una reserva individual de alojamiento (suites) en Amari Living Suites.'),
        ]),
        ('reservas', 'Reservas a través de este sitio', [
            ('p', 'Este sitio web es informativo. Las reservas en línea se realizan en el motor de reservas de Cloudbeds, un servicio de un tercero que se abre en una pestaña nueva y tiene sus propias condiciones y política de privacidad.'),
            ('p', 'Los formularios de consulta de este sitio abren WhatsApp o tu aplicación de correo con un mensaje listo para enviar. Una consulta no constituye una reserva: la reserva solo queda confirmada cuando el hotel la confirma expresamente.'),
            ('p', 'El débito y el pago de la estadía y de los servicios se realizan en pesos colombianos. Si las tarifas publicadas incluyen o no impuestos: ' + pend('indicar') + '.'),
        ]),
        ('condiciones', 'Condiciones de la estadía', [
            ('p', 'Las condiciones de tarifa, impuestos, check-in y check-out, estancias con niños, registro de menores, salida anticipada, custodia de valores, no show, grupos, visitas, parqueadero, gimnasio, Wi‑Fi, advertencias, ley antitabaco, mascotas, política anticorrupción y declaración de origen de fondos son las descritas en la <a href="../politicas.html#servicios">Política de servicios</a>, junto con la <a href="../politicas.html#cancelacion">Política de cancelación</a> y la <a href="../politicas.html#pagos">Política de pagos</a>.'),
        ]),
        ('retracto', 'Derecho de retracto y reversión del pago', [
            ('p', 'Condiciones de retracto y de reversión del pago para reservas hechas a distancia: ' + pend('definir con asesoría jurídica, teniendo en cuenta los artículos 47 y 51 de la Ley 1480 de 2011 (Estatuto del Consumidor)') + '.'),
        ]),
        ('pqr', 'Peticiones, quejas y reclamos', [
            ('p', f'Puedes presentar peticiones, quejas o reclamos por correo a {MAILTO}, por WhatsApp al +57 302 330 7939 o por teléfono al +57 605 313 3460. Plazo de respuesta: ' + pend('plazo de respuesta') + '.'),
        ]),
        ('menores', 'Protección de niños, niñas y adolescentes', [
            ('p', 'En Colombia, la explotación y el abuso sexual de niños, niñas y adolescentes son delitos. La Ley 679 de 2001 y la Ley 1336 de 2009 establecen medidas para prevenirlos en el sector turístico. ' + pend('texto del código de conducta adoptado por el hotel (Resolución 3840 de 2009 del MinCIT)') + '.'),
        ]),
        ('propiedad', 'Propiedad intelectual', [
            ('p', 'La marca, el logotipo, los textos y las fotografías del hotel pertenecen a sus titulares. ' + pend('confirmar titularidad o licencia de las fotografías y del contenido') + '. Las fotografías de lugares de Barranquilla provienen de Wikimedia Commons y se usan bajo la licencia indicada junto a cada imagen, con el crédito de su autor.'),
        ]),
        ('datos', 'Datos personales y cookies', [
            ('p', 'El tratamiento de datos personales se rige por la <a href="../politica-de-privacidad/">Política de privacidad</a> y el uso de cookies por la <a href="../politica-de-cookies/">Política de cookies</a>.'),
        ]),
        ('ley', 'Ley aplicable', [
            ('p', 'Estos términos se rigen por las leyes de la República de Colombia. ' + pend('confirmar cláusula de jurisdicción y solución de controversias con asesoría jurídica') + '.'),
        ]),
        ('version', 'Versión y vigencia', [
            ('ul', ['Versión: ' + VERSION, 'Fecha de entrada en vigencia: ' + pend('fecha')]),
        ]),
    ],
})

TERMS_EN = dict(COMMON_EN, **{
    'title': 'Terms and conditions | Amari Living Suites',
    'crumb': 'Terms and conditions',
    'desc': 'Terms and conditions for the accommodation service and the use of the Amari Living Suites website in Barranquilla, Colombia.',
    'h1': 'Terms and <em>conditions</em>',
    'intro': 'Hotel Amari Living Suites, as part of its service to all its clients and guests, presents its terms and conditions for the provision of its services.',
    'sections': [
        ('prestador', 'Provider identification', identity(True)),
        ('objetivo', 'Purpose and scope', [
            ('h', 'Purpose'),
            ('p', 'To set out the policies, conditions and terms of the room reservation purchased at Amari Living Suites, in compliance with internal guidelines and applicable legal provisions.'),
            ('h', 'Scope'),
            ('p', 'Applies to clients who have purchased an individual accommodation reservation (suites) at Amari Living Suites.'),
        ]),
        ('reservas', 'Bookings through this website', [
            ('p', 'This website is for information purposes. Online bookings are made on the Cloudbeds booking engine, a third-party service that opens in a new tab and has its own terms and privacy policy.'),
            ('p', 'The enquiry forms on this website open WhatsApp or your email app with a message ready to send. An enquiry is not a booking: a booking is only confirmed when the hotel expressly confirms it.'),
            ('p', 'Stays and services are charged and paid in Colombian pesos. Whether published rates include taxes: ' + pend('to be stated', True) + '.'),
        ]),
        ('condiciones', 'Conditions of stay', [
            ('p', 'The conditions regarding rates, taxes, check-in and check-out, stays with children, registration of minors, early departure, safekeeping of valuables, no-shows, groups, visitors, parking, gym, Wi‑Fi, warnings, anti-smoking law, pets, anti-corruption policy and declaration of origin of funds are those described in the <a href="../politicas.html#servicios">Service policy</a>, together with the <a href="../politicas.html#cancelacion">Cancellation policy</a> and the <a href="../politicas.html#pagos">Payment policy</a>.'),
        ]),
        ('retracto', 'Right of withdrawal and payment reversal', [
            ('p', 'Withdrawal and payment-reversal conditions for bookings made remotely: ' + pend('to be defined with legal advice, considering articles 47 and 51 of Law 1480 of 2011 (Colombian Consumer Statute)', True) + '.'),
        ]),
        ('pqr', 'Requests, complaints and claims', [
            ('p', f'You can submit requests, complaints or claims by email to {MAILTO}, on WhatsApp at +57 302 330 7939 or by phone at +57 605 313 3460. Response time: ' + pend('response time', True) + '.'),
        ]),
        ('menores', 'Protection of children and adolescents', [
            ('p', 'In Colombia, the sexual exploitation and abuse of children and adolescents are crimes. Law 679 of 2001 and Law 1336 of 2009 set out measures to prevent them in the tourism sector. ' + pend('text of the code of conduct adopted by the hotel (MinCIT Resolution 3840 of 2009)', True) + '.'),
        ]),
        ('propiedad', 'Intellectual property', [
            ('p', 'The brand, logo, texts and photographs of the hotel belong to their respective owners. ' + pend('confirm ownership or licence of the photographs and content', True) + '. Photographs of places in Barranquilla come from Wikimedia Commons and are used under the licence shown next to each image, crediting their author.'),
        ]),
        ('datos', 'Personal data and cookies', [
            ('p', 'The processing of personal data is governed by the <a href="../privacy-policy/">Privacy policy</a> and the use of cookies by the <a href="../cookie-policy/">Cookie policy</a>.'),
        ]),
        ('ley', 'Governing law', [
            ('p', 'These terms are governed by the laws of the Republic of Colombia. ' + pend('confirm jurisdiction and dispute-resolution clause with legal advice', True) + '.'),
        ]),
        ('version', 'Version and effective date', [
            ('ul', ['Version: ' + VERSION_EN, 'Effective date: ' + pend('date', True)]),
        ]),
    ],
})

# ---------------------------------------------------------------- PRIVACIDAD
PRIV_ES = dict(COMMON_ES, **{
    'title': 'Política de privacidad | Amari Living Suites',
    'crumb': 'Política de privacidad',
    'desc': 'Cómo trata Amari Living Suites tus datos personales, conforme a la Ley 1581 de 2012: finalidades, derechos y procedimiento para consultas y reclamos.',
    'h1': 'Política de <em>privacidad</em>',
    'intro': 'Política de tratamiento de datos personales de Amari Living Suites, conforme a la Ley 1581 de 2012 y su reglamentación (Decreto 1377 de 2013, compilado en el Decreto 1074 de 2015).',
    'sections': [
        ('responsable', 'Responsable del tratamiento', identity()),
        ('datos', 'Qué datos tratamos y para qué', [
            ('h', 'Formulario de contacto'),
            ('p', 'Nombre, correo electrónico y mensaje, para responder tu solicitud. El formulario abre tu aplicación de correo con el mensaje listo: este sitio web no guarda esos datos.'),
            ('h', 'Consultas por WhatsApp'),
            ('p', 'Nombre, fechas de llegada y salida, número de huéspedes y el número de WhatsApp desde el que escribes, para responder sobre disponibilidad y reservas. WhatsApp es un servicio de Meta, con sus propias condiciones.'),
            ('h', 'Reservas en línea'),
            ('p', 'Las reservas se hacen en el motor de Cloudbeds, que trata los datos según su propia política. Datos que recibe el hotel y finalidades: ' + pend('completar') + '.'),
            ('h', 'Registro de huéspedes'),
            ('p', 'Datos del registro de huéspedes al llegar al hotel y su finalidad: ' + pend('completar según los procesos del hotel') + '.'),
            ('h', 'Navegación'),
            ('p', 'Este sitio no usa herramientas de analítica ni de publicidad. Lo relativo a cookies y almacenamiento local está en la <a href="../politica-de-cookies/">Política de cookies</a>.'),
        ]),
        ('sensibles', 'Datos sensibles y de menores', [
            ('p', 'A través de este sitio no solicitamos datos sensibles. Si en algún trámite se te pregunta por datos sensibles o de niños, niñas y adolescentes, responder es facultativo. El tratamiento de datos de menores respetará su interés superior y sus derechos fundamentales, conforme al artículo 7 de la Ley 1581 de 2012.'),
        ]),
        ('derechos', 'Tus derechos', [
            ('p', 'Como titular de los datos, conforme al artículo 8 de la Ley 1581 de 2012, tienes derecho a:'),
            ('ul', [
                'Conocer, actualizar y rectificar tus datos personales.',
                'Solicitar prueba de la autorización otorgada.',
                'Ser informado, previa solicitud, sobre el uso que se ha dado a tus datos.',
                'Presentar quejas ante la Superintendencia de Industria y Comercio, después de agotar el trámite de consulta o reclamo ante el responsable.',
                'Revocar la autorización o solicitar la supresión de tus datos, en los términos de la ley.',
                'Acceder en forma gratuita a tus datos personales objeto de tratamiento.',
            ]),
        ]),
        ('atencion', 'Área responsable y procedimiento', [
            ('p', f'Área o persona encargada de atender consultas y reclamos: {pend("cargo o área")}. Canal: {MAILTO}.'),
            ('h', 'Consultas'),
            ('p', 'Se atienden en un máximo de diez (10) días hábiles desde su recibo. Si no es posible en ese plazo, te informaremos el motivo y la nueva fecha, que no superará cinco (5) días hábiles adicionales (artículo 14 de la Ley 1581 de 2012).'),
            ('h', 'Reclamos'),
            ('p', 'Para corregir, actualizar o suprimir datos, o si consideras que se incumplió la ley, puedes presentar un reclamo con tu identificación, la descripción de los hechos, tu dirección y los documentos que quieras hacer valer. Si está incompleto, te pediremos completarlo dentro de los cinco (5) días siguientes; si pasan dos (2) meses sin respuesta, se entenderá que desististe. El plazo máximo de respuesta es de quince (15) días hábiles, prorrogable hasta ocho (8) días hábiles más, informándote el motivo (artículo 15 de la Ley 1581 de 2012).'),
        ]),
        ('terceros', 'Encargados y terceros', [
            ('p', 'Proveedores que pueden tratar datos por cuenta del hotel o con los que se comparten datos: ' + pend('listar (por ejemplo, alojamiento web, motor de reservas, correo) e indicar si hay transferencia o transmisión internacional') + '.'),
        ]),
        ('seguridad', 'Seguridad', [
            ('p', 'Medidas de seguridad aplicadas a las bases de datos del hotel: ' + pend('describir') + '.'),
        ]),
        ('vigencia', 'Vigencia', [
            ('ul', ['Versión: ' + VERSION, 'Fecha de entrada en vigencia: ' + pend('fecha'), 'Período de vigencia de las bases de datos: ' + pend('definir')]),
        ]),
    ],
})

PRIV_EN = dict(COMMON_EN, **{
    'title': 'Privacy policy | Amari Living Suites',
    'crumb': 'Privacy policy',
    'desc': 'How Amari Living Suites processes your personal data under Colombian Law 1581 of 2012: purposes, rights and procedure for requests and claims.',
    'h1': 'Privacy <em>policy</em>',
    'intro': 'Personal data processing policy of Amari Living Suites, under Colombian Law 1581 of 2012 and its regulations (Decree 1377 of 2013, compiled in Decree 1074 of 2015).',
    'sections': [
        ('responsable', 'Data controller', identity(True)),
        ('datos', 'What data we process and why', [
            ('h', 'Contact form'),
            ('p', 'Name, email address and message, to reply to your request. The form opens your email app with the message ready: this website does not store that data.'),
            ('h', 'WhatsApp enquiries'),
            ('p', 'Name, check-in and check-out dates, number of guests and the WhatsApp number you write from, to reply about availability and bookings. WhatsApp is a Meta service with its own terms.'),
            ('h', 'Online bookings'),
            ('p', 'Bookings are made on the Cloudbeds engine, which processes data under its own policy. Data received by the hotel and purposes: ' + pend('to be completed', True) + '.'),
            ('h', 'Guest registration'),
            ('p', 'Guest registration data collected on arrival and its purpose: ' + pend('to be completed according to the hotel’s processes', True) + '.'),
            ('h', 'Browsing'),
            ('p', 'This website does not use analytics or advertising tools. Cookies and local storage are covered in the <a href="../cookie-policy/">Cookie policy</a>.'),
        ]),
        ('sensibles', 'Sensitive data and data of minors', [
            ('p', 'We do not request sensitive data through this website. If you are asked for sensitive data or data about children and adolescents, answering is optional. Any processing of minors’ data will respect their best interests and fundamental rights, under article 7 of Law 1581 of 2012.'),
        ]),
        ('derechos', 'Your rights', [
            ('p', 'As the data subject, under article 8 of Law 1581 of 2012, you have the right to:'),
            ('ul', [
                'Know, update and rectify your personal data.',
                'Request proof of the authorization granted.',
                'Be informed, upon request, about how your data has been used.',
                'File complaints with the Superintendence of Industry and Commerce (SIC), after first submitting a request or claim to the controller.',
                'Revoke the authorization or request the deletion of your data, under the terms of the law.',
                'Access your personal data free of charge.',
            ]),
        ]),
        ('atencion', 'Responsible area and procedure', [
            ('p', f'Area or person in charge of requests and claims: {pend("position or area", True)}. Channel: {MAILTO}.'),
            ('h', 'Requests'),
            ('p', 'Answered within a maximum of ten (10) business days of receipt. If that is not possible, we will tell you why and give a new date, no more than five (5) additional business days (article 14 of Law 1581 of 2012).'),
            ('h', 'Claims'),
            ('p', 'To correct, update or delete data, or if you believe the law has been breached, you can submit a claim with your identification, a description of the facts, your address and any supporting documents. If it is incomplete, we will ask you to complete it within five (5) days; if two (2) months pass without a reply, the claim will be deemed withdrawn. The maximum response time is fifteen (15) business days, extendable by up to eight (8) more business days, with the reason given (article 15 of Law 1581 of 2012).'),
        ]),
        ('terceros', 'Processors and third parties', [
            ('p', 'Providers that may process data on behalf of the hotel or with whom data is shared: ' + pend('list them (e.g. web hosting, booking engine, email) and state whether there is any international transfer or transmission', True) + '.'),
        ]),
        ('seguridad', 'Security', [
            ('p', 'Security measures applied to the hotel’s databases: ' + pend('to be described', True) + '.'),
        ]),
        ('vigencia', 'Effective date', [
            ('ul', ['Version: ' + VERSION_EN, 'Effective date: ' + pend('date', True), 'Database retention period: ' + pend('to be defined', True)]),
        ]),
    ],
})

# ---------------------------------------------------------------- COOKIES
COOK_ES = dict(COMMON_ES, **{
    'title': 'Política de cookies | Amari Living Suites',
    'crumb': 'Política de cookies',
    'desc': 'Qué cookies y tecnologías similares usa el sitio web de Amari Living Suites y cómo puedes gestionar tus preferencias.',
    'h1': 'Política de <em>cookies</em>',
    'intro': 'Las cookies y tecnologías similares (como el almacenamiento local del navegador) son pequeños archivos o datos que un sitio guarda en tu dispositivo. Aquí explicamos cuáles usa este sitio y cómo gestionarlas.',
    'sections': [
        ('uso', 'Qué usa este sitio', [
            ('h', 'Necesario: tu elección de privacidad'),
            ('p', 'Cuando eliges si cargar contenido de terceros, guardamos esa elección en el almacenamiento local de tu navegador (clave <code>amari.consent</code>) durante un máximo de 12 meses. No contiene datos que te identifiquen y no se envía a ningún servidor.'),
            ('h', 'Opcional: mapa de Google Maps'),
            ('p', 'El mapa de ubicación es un servicio de Google. Solo se carga si pulsas «Ver mapa» (recordamos esa elección) o lo aceptas en las preferencias. Al cargarse, Google recibe tu dirección IP y puede instalar sus propias cookies, según la <a href="https://policies.google.com/privacy" target="_blank" rel="noopener">política de privacidad de Google</a>.'),
            ('h', 'Tipografía'),
            ('p', 'Las tipografías (Karla e IvyMode) se cargan desde este mismo sitio, sin conexión a servicios de terceros.'),
            ('h', 'Enlaces a otros sitios'),
            ('p', 'Los enlaces al motor de reservas (Cloudbeds), WhatsApp, Instagram, YouTube y Google Maps abren sitios de terceros, que aplican sus propias políticas de cookies.'),
            ('p', 'Este sitio no usa cookies de analítica ni de publicidad.'),
        ]),
        ('gestion', 'Cómo cambiar tus preferencias', [
            ('p', 'Puedes cambiar o retirar tu elección cuando quieras con el botón «Preferencias de cookies», al pie de cada página. También puedes borrar las cookies y el almacenamiento local desde la configuración de tu navegador.'),
        ]),
        ('version', 'Versión', [
            ('ul', ['Versión: ' + VERSION, 'Fecha de entrada en vigencia: ' + pend('fecha')]),
        ]),
    ],
})

COOK_EN = dict(COMMON_EN, **{
    'title': 'Cookie policy | Amari Living Suites',
    'crumb': 'Cookie policy',
    'desc': 'Which cookies and similar technologies the Amari Living Suites website uses and how you can manage your preferences.',
    'h1': 'Cookie <em>policy</em>',
    'intro': 'Cookies and similar technologies (such as the browser’s local storage) are small files or pieces of data that a website stores on your device. Here we explain which ones this website uses and how to manage them.',
    'sections': [
        ('uso', 'What this website uses', [
            ('h', 'Necessary: your privacy choice'),
            ('p', 'When you choose whether to load third-party content, we save that choice in your browser’s local storage (key <code>amari.consent</code>) for up to 12 months. It contains no data that identifies you and is not sent to any server.'),
            ('h', 'Optional: Google Maps'),
            ('p', 'The location map is a Google service. It only loads if you click “View map” (we remember that choice) or accept it in your preferences. When it loads, Google receives your IP address and may set its own cookies, under <a href="https://policies.google.com/privacy" target="_blank" rel="noopener">Google’s privacy policy</a>.'),
            ('h', 'Typeface'),
            ('p', 'The typefaces (Karla and IvyMode) are loaded from this website itself, without connecting to third-party services.'),
            ('h', 'Links to other websites'),
            ('p', 'Links to the booking engine (Cloudbeds), WhatsApp, Instagram, YouTube and Google Maps open third-party websites, which apply their own cookie policies.'),
            ('p', 'This website does not use analytics or advertising cookies.'),
        ]),
        ('gestion', 'How to change your preferences', [
            ('p', 'You can change or withdraw your choice at any time with the “Cookie preferences” button at the bottom of every page. You can also delete cookies and local storage in your browser settings.'),
        ]),
        ('version', 'Version', [
            ('ul', ['Version: ' + VERSION_EN, 'Effective date: ' + pend('date', True)]),
        ]),
    ],
})

PAGES = [
    (TERMS_ES, 'terms', 'es'), (TERMS_EN, 'terms', 'en'),
    (PRIV_ES, 'privacy', 'es'), (PRIV_EN, 'privacy', 'en'),
    (COOK_ES, 'cookies', 'es'), (COOK_EN, 'cookies', 'en'),
]

for d, key, lang in PAGES:
    here = ROUTES[key][lang]
    alt = ROUTES[key]['en' if lang == 'es' else 'es']
    out = os.path.join(P, here, 'index.html')
    os.makedirs(os.path.dirname(out), exist_ok=True)
    open(out, 'w', encoding='utf-8').write(page(d, here, alt, WA[lang]))
print(P, 'documentos legales ES/EN generados')
