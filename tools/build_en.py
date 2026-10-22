"""Genera en/index.html (inglés) a partir de index.html (español).
Uso: python3 build_en.py <carpeta-proyecto>
- Traduce textos visibles y atributos accesibles con un diccionario revisado a mano.
- Ajusta rutas relativas (../public, ../src) y el selector de idioma.
- Informa cualquier texto que quede sin traducir.
"""
import sys, re, json, html, os

P = sys.argv[1]
src = open(os.path.join(P, 'index.html'), encoding='utf-8').read()

T = {
 # <head>
 'Amari Living Suites · Suites con cocineta en Barranquilla': 'Amari Living Suites · Suites with kitchenettes in Barranquilla',
 'Amari Living Suites: 32 suites totalmente equipadas con cocineta en Barranquilla. Reserva en línea o por WhatsApp. Coworking y sala de juntas por horas, y beneficios del 10 % con nuestros aliados.':
   'Amari Living Suites: 32 fully equipped suites with kitchenettes in Barranquilla, Colombia. Book online or via WhatsApp. Coworking space and meeting room by the hour, plus 10% off with our partner businesses.',
 'Suites totalmente equipadas con cocineta, en una ubicación estratégica de Barranquilla.': 'Fully equipped suites with kitchenettes in a strategic location in Barranquilla.',
 # Navegación
 'Saltar al contenido': 'Skip to content',
 'Toca para entrar': 'Tap to enter',
 'Amari Living Suites, ir al inicio': 'Amari Living Suites, go to home',
 'Principal': 'Main',
 'Servicios': 'Services',
 'Galería': 'Gallery',
 'Beneficios': 'Benefits',
 'Contacto': 'Contact',
 'Reservar ahora': 'Book now',
 'Abrir menú': 'Open menu',
 'Menú móvil': 'Mobile menu',
 'Inicio': 'Home',
 'Servicios y coworking': 'Services & coworking',
 'Conoce Barranquilla': 'Discover Barranquilla',
 'Opiniones': 'Reviews',
 'Ubicación y contacto': 'Location & contact',
 'Reserva': 'Book',
 'Reservar en línea': 'Book online',
 'Escríbenos por WhatsApp': 'Message us on WhatsApp',
 # Barra de consulta y formularios
 'Consultar disponibilidad por WhatsApp': 'Check availability on WhatsApp',
 'Nombre': 'Name',
 'Escribe tu nombre': 'Your name',
 'Llegada': 'Check-in',
 'Salida': 'Check-out',
 'Huéspedes': 'Guests',
 'Selecciona': 'Select',
 '1 persona': '1 guest',
 '2 personas': '2 guests',
 '3 personas': '3 guests',
 '4 personas': '4 guests',
 'Más de 4': 'More than 4',
 'Consultar por WhatsApp': 'Ask on WhatsApp',
 # Destacados
 'Lo esencial de Amari': 'Amari at a glance',
 'Suites con cocineta': 'Suites with kitchenette',
 'Coworking por horas': 'Coworking by the hour',
 'Restaurante-café aliado': 'Partner restaurant-café',
 'Lavandería aliada': 'Partner laundry',
 'Ubicación estratégica': 'Strategic location',
 # Experiencia
 'Creamos Amari para quienes visitan y viven Barranquilla: un lugar con comodidades de alta categoría para descansar, en una ubicación estratégica y con un precio asequible.':
   'We created Amari for visitors and residents of Barranquilla: a place with first-class amenities and a perfect space to rest, in a strategic location and at an affordable price.',
 'Buscamos que la estadía de cada persona sea un regalo, haciendo que cada necesidad sea abarcada con pequeños detalles agradables y perfectamente pensados. Amamos el orden, la limpieza y todo lo que le da un toque especial a cada espacio, ya sea que viajes por turismo, negocios o en familia.':
   'We strive to make each person’s stay a gift by ensuring that every need is met with pleasant and perfectly thought-out little details. We love order, cleanliness and everything that gives each space a special touch, whether you are traveling for leisure, business or with your family.',
 '3:00 p. m.': '3:00 p.m.',
 '12:00 m.': '12:00 noon',
 'Conoce nuestras suites': 'Explore our suites',
 'Sala común de Amari Living Suites con sofá mostaza, sillas tejidas de colores y ventanal': 'Amari Living Suites common lounge with a mustard sofa, colorful woven chairs and a large window',
 'Detalle decorativo: jarrones de cerámica y planta sobre mesa de vidrio': 'Decorative detail: ceramic vases and a plant on a glass table',
 # Suites
 'Habitaciones totalmente equipadas con cocineta, mobiliario y amenities de lujo. Y en cada piso, una sala integrada para el uso de todos los huéspedes.':
   'Rooms fully equipped with a kitchenette, furniture and luxury amenities. And on every floor, a shared lounge for all our guests.',
 'Premium Suite con cama Queen, cabecero iluminado y cortinas': 'Premium Suite with a Queen bed, illuminated headboard and curtains',
 'Ideal para parejas': 'Ideal for couples',
 'Las comodidades perfectas para una pareja, en un ambiente cálido y sereno.': 'The perfect amenities for a couple, in a warm and serene setting.',
 '1 cama Queen': '1 Queen bed',
 'Cocineta': 'Kitchenette',
 'Ver disponibilidad': 'Check availability',
 'Junior Suite con dos camas, escritorio y televisor': 'Junior Suite with two beds, a desk and a TV',
 'Hasta 4 personas · 25 m²': 'Up to 4 guests · 25 m²',
 '2 camas dobles': '2 double beds',
 'Hasta 4 personas': 'Up to 4 guests',
 'Amplitud para familias o grupos que viajan juntos, con 25 m² de área.': 'Room for families or groups traveling together, with 25 m² of space.',
 'Dos camas sencillas para descansar y crear momentos inolvidables.': 'Two single beds to rest and create unforgettable moments.',
 'Superior Suite con dos camas sencillas': 'Superior Suite with two single beds',
 'Un espacio íntimo para descansar': 'An intimate space to rest',
 '2 camas sencillas': '2 single beds',
 'Detalles de las suites': 'Suite details',
 'Cocineta con microondas, nevera y lavaplatos': 'Kitchenette with microwave, refrigerator and sink',
 'Cocineta equipada': 'Equipped kitchenette',
 'Clóset con batas de baño bordadas con el logo de Amari': 'Closet with bathrobes embroidered with the Amari logo',
 'Amenities con la firma Amari': 'Amenities with the Amari signature',
 'Escritorio con silla tapizada y televisor de pared': 'Desk with an upholstered chair and a wall-mounted TV',
 'Mobiliario para trabajar o descansar': 'Furniture for working or relaxing',
 'Cafetera sobre el mesón de granito de la cocineta': 'Coffee maker on the kitchenette’s granite countertop',
 'Tu café, a tu ritmo': 'Your coffee, at your own pace',
 # Servicios
 'Servicios y espacios': 'Services & spaces',
 'Todo lo que necesitas,': 'Everything you need,',
 'bajo un mismo techo': 'under one roof',
 'Amari ofrece a sus huéspedes una completa variedad de servicios: espacios comunes en cada piso, rooftop con coworking y gimnasio, sala de juntas y locales comerciales en el primer piso.':
   'Amari offers its guests a full range of services: common areas on every floor, a rooftop with a coworking space and gym, a meeting room and commercial spaces on the ground floor.',
 'Sala integrada por piso': 'Shared lounge on every floor',
 'Cada piso cuenta con una sala compartida para el uso de todas las suites.': 'Every floor has a shared lounge for all of its suites.',
 'Rooftop y gimnasio': 'Rooftop & gym',
 'En el rooftop están el gimnasio y el espacio de coworking.': 'The rooftop is home to the gym and the coworking space.',
 'Locales en el primer piso': 'Ground-floor shops',
 'Restaurante, lavandería y peluquería en el mismo edificio.': 'A restaurant, a laundry and a hair salon in the same building.',
 'Ver beneficios': 'See benefits',
 'Cocineta, mobiliario y amenities en cada una de las 32 suites.': 'A kitchenette, furniture and amenities in each of our 32 suites.',
 'Ver suites': 'See suites',
 'Wi‑Fi de cortesía': 'Complimentary Wi‑Fi',
 'Parqueadero sin costo, 1 vehículo por suite (sujeto a disponibilidad)': 'Free parking for 1 vehicle per suite (subject to availability)',
 'Caja de seguridad en cada suite': 'In-suite safe',
 'Late check-out hasta la 1:00 p. m. sin costo (sujeto a disponibilidad)': 'Free late check-out until 1:00 p.m. (subject to availability)',
 'Espacios libres de humo': 'Smoke-free property',
 'Visa, Mastercard, Diners y American Express': 'Visa, Mastercard, Diners and American Express',
 'Sala integrada de piso con sofás mostaza y sillas tejidas': 'Shared floor lounge with mustard sofas and woven chairs',
 'Un espacio compartido para todas las suites del piso.': 'A shared space for all the suites on the floor.',
 'Recepción y lobby de Amari Living Suites': 'Amari Living Suites reception and lobby',
 'Recepción y lobby': 'Reception & lobby',
 'Te recibimos desde el primer momento.': 'We welcome you from the very first moment.',
 'Pasillo de habitaciones con iluminación cálida': 'Guest-room hallway with warm lighting',
 'Pasillos serenos': 'Quiet hallways',
 'Silencio y orden para descansar.': 'Peace and order so you can rest.',
 'Espacios de trabajo · Por horas': 'Workspaces · By the hour',
 'Coworking y': 'Coworking &',
 'sala de juntas': 'meeting room',
 'Dos espacios disponibles por horas para tus jornadas de trabajo y reuniones en Barranquilla. Escríbenos para consultar disponibilidad y reservar.':
   'Two spaces available by the hour for your workdays and meetings in Barranquilla. Message us to check availability and book.',
 'Coworking': 'Coworking',
 'Un espacio de coworking en el rooftop de Amari para concentrarte, avanzar en tus pendientes y trabajar cómodo durante tu viaje.':
   'A coworking space on Amari’s rooftop where you can focus, get things done and work comfortably during your trip.',
 'Consulta la tarifa por hora': 'Ask for the hourly rate',
 'Consultar disponibilidad': 'Check availability',
 'Sala de juntas': 'Meeting room',
 'Un espacio privado para reuniones de trabajo, presentaciones o encuentros con tu equipo, disponible por horas.':
   'A private space for business meetings, presentations or get-togethers with your team, available by the hour.',
 # Galería
 'Recorre Amari': 'Explore Amari',
 '45 fotografías del hotel': '45 photos of the hotel',
 'Ver todas las fotos': 'See all photos',
 'Fotografía anterior': 'Previous photo',
 'Fotografía siguiente': 'Next photo',
 'Galería de fotografías, desplazable horizontalmente': 'Photo gallery, scrolls horizontally',
 'Fachada del edificio Amari Living Suites': 'Amari Living Suites building facade',
 'Acceso principal con escaleras y jardín tropical': 'Main entrance with stairs and a tropical garden',
 'Arreglo floral tropical en el pasillo': 'Tropical flower arrangement in the hallway',
 'Zona común con sofá azul y sillas tejidas': 'Common area with a blue sofa and woven chairs',
 'Sala con sofá azul, silla de colores y ventanal': 'Lounge with a blue sofa, a colorful chair and a large window',
 'Vista aérea del edificio y su entorno en Barranquilla': 'Aerial view of the building and its surroundings in Barranquilla',
 'Detalle de silla tejida en colores': 'Detail of a colorful woven chair',
 'Rincón de la sala común con flores tropicales': 'Corner of the common lounge with tropical flowers',
 # Aliados
 'Aliados Amari': 'Amari partners',
 'Beneficios que': 'Benefits that',
 'hacen tu estadía más fácil': 'make your stay easier',
 'Ser huésped de Amari tiene ventajas. Nuestros negocios aliados te ofrecen un descuento exclusivo durante tu estadía.':
   'Staying at Amari has its perks. Our partner businesses offer you an exclusive discount during your stay.',
 '10 % de descuento para huéspedes': '10% discount for guests',
 'de descuento para huéspedes en el restaurante-café y la lavandería': 'off for guests at the restaurant-café and the laundry',
 'Restaurante-café': 'Restaurant-café',
 'Una pausa para el café, un almuerzo tranquilo o una comida sin complicaciones mientras te hospedas en Barranquilla.':
   'A coffee break, a relaxed lunch or an easy meal while you stay in Barranquilla.',
 '10 % de descuento': '10% off',
 'para huéspedes de Amari Living Suites.': 'for Amari Living Suites guests.',
 'WhatsApp del restaurante por confirmar': 'Restaurant WhatsApp to be confirmed',
 'Escribir al restaurante-café': 'Message the restaurant-café',
 'Instagram de Selah Bistró & Café (abre en una pestaña nueva)': 'Selah Bistró & Café on Instagram (opens in a new tab)',
 'Lavandería': 'Laundry',
 'Tu ropa lista para la reunión, el paseo o el regreso a casa, sin ocupar el tiempo de tu viaje.':
   'Your clothes ready for your meeting, your outing or your trip home, without taking time away from your trip.',
 'WhatsApp de la lavandería por confirmar': 'Laundry WhatsApp to be confirmed',
 'Escribir a la lavandería': 'Message the laundry',
 # Barranquilla
 'La Puerta de Oro': 'Colombia’s',
 'de Colombia': 'Golden Gate',
 'Explora los lugares más emblemáticos de Barranquilla: su historia, su cultura y el sabor único de la ciudad. ¡Tu aventura comienza aquí!':
   'Explore Barranquilla’s most iconic places: its history, its culture and the city’s unique flavor. Your adventure begins here!',
 'Foto:': 'Photo:',
 '· Dominio público': '· Public domain',
 'Cinco kilómetros y medio junto al río Magdalena para caminar, montar bicicleta, comer y ver el atardecer.':
   'Five and a half kilometers along the Magdalena River for walking, cycling, dining and watching the sunset.',
 'Cómo llegar': 'Get directions',
 'La rueda de la fortuna del Gran Malecón: 44 cabinas climatizadas con vista panorámica del río y de la ciudad.':
   'The Gran Malecón’s Ferris wheel: 44 air-conditioned cabins with panoramic views of the river and the city.',
 'Conocida como “la Aleta del Tiburón”: un monumento de vidrio de unos 33 metros en homenaje al Junior de Barranquilla.':
   'Known as “the Shark Fin”: a glass monument about 33 meters tall that pays tribute to Junior de Barranquilla, the city’s soccer club.',
 'Junto al puente levadizo del Gran Malecón': 'Next to the Gran Malecón drawbridge',
 'Ícono de colores de la ciudad, inaugurado para los Juegos Centroamericanos y del Caribe de 2018.':
   'A colorful city icon, unveiled for the 2018 Central American and Caribbean Games.',
 'Glorieta de la Circunvalar con Vía 40': 'Circunvalar roundabout at Vía 40',
 'La historia, los disfraces y los personajes del Carnaval de Barranquilla, Patrimonio Cultural Inmaterial de la Humanidad.':
   'The history, costumes and characters of the Barranquilla Carnival, recognized by UNESCO as Intangible Cultural Heritage of Humanity.',
 'Pasarelas sobre el manglar y miradores para observar más de 200 especies de aves, cerca de Bocas de Ceniza.':
   'Boardwalks over the mangroves and lookout points to spot more than 200 bird species, near Bocas de Ceniza.',
 'Corregimiento La Playa': 'La Playa district',
 'Un recorrido por la naturaleza, la cultura y la historia de la región Caribe, en el Parque Cultural del Caribe.':
   'A journey through the nature, culture and history of Colombia’s Caribbean region, at the Parque Cultural del Caribe.',
 'Templo de arquitectura moderna, con vitrales y el gran mosaico de María Reina, frente a la Plaza de la Paz.':
   'A modern church with stained-glass windows and the great María Reina mosaic, facing Plaza de la Paz.',
 'Plaza de la Paz, Centro': 'Plaza de la Paz, Downtown',
 'Te recomendamos confirmar horarios y tarifas en los canales oficiales de cada lugar antes de tu visita.':
   'We recommend checking opening hours and prices on each venue’s official channels before your visit.',
 # Opiniones
 'Lo que': 'What our',
 'nos cuentan': 'guests say',
 '4,6 de 5 estrellas': '4.6 out of 5 stars',
 '4,6': '4.6',
 'Basado en 61 reseñas en Google': 'Based on 61 Google reviews',
 'Reseña en Expedia.com': 'Review on Expedia.com',
 'Reseña en Booking.com': 'Review on Booking.com',
 'Reseña en Google': 'Review on Google',
 '5 de 5 estrellas': '5 out of 5 stars',
 '¿Te hospedaste con nosotros? Escribe tu reseña en Google': 'Stayed with us? Write a review on Google',
 # Antes de llegar
 'Antes de llegar': 'Before you arrive',
 'Información': 'Useful',
 'útil': 'information',
 'Resumen de las políticas publicadas por Amari. Consulta el detalle completo en los enlaces del pie de página.':
   'A summary of Amari’s published policies. See the full details in the links in the footer.',
 'Horarios de check-in y check-out': 'Check-in and check-out times',
 'Check-in desde las 3:00 p. m. y check-out hasta las 12:00 m. El late check-out hasta la 1:00 p. m. no tiene costo y está sujeto a disponibilidad. El early check-in también está sujeto a disponibilidad y puede tener cargo según la hora de llegada.':
   'Check-in from 3:00 p.m. and check-out until 12:00 noon. Late check-out until 1:00 p.m. is free of charge and subject to availability. Early check-in is also subject to availability and may incur a charge depending on your arrival time.',
 '¿La tarifa incluye desayuno?': 'Is breakfast included?',
 'No. La tarifa incluye el alojamiento según la reserva y no incluye desayuno.': 'No. The rate includes accommodation as per your reservation and does not include breakfast.',
 'Estancias con niños': 'Stays with children',
 'Se pueden alojar niños de cualquier edad, siempre acompañados de sus padres o tutores legales. Los niños de hasta 5 años se hospedan sin cargo compartiendo la cama existente (máximo 2). Desde los 6 años se consideran adultos. Es indispensable presentar la identificación de todos los huéspedes, incluidos los menores.':
   'Children of any age are welcome, always accompanied by their parents or legal guardians. Children up to 5 years old stay free of charge when sharing an existing bed (maximum 2). Children aged 6 and over are considered adults. All guests, including minors, must present identification.',
 'Medios de pago e impuestos': 'Payment methods and taxes',
 'Los pagos se realizan en pesos colombianos. Se aceptan tarjetas VISA, Mastercard, Diners y American Express. A los residentes en Colombia se les aplica el 19 % de IVA, que no está incluido en la tarifa y se cobra en el check-in; los extranjeros pueden estar exentos según las condiciones vigentes.':
   'Payments are made in Colombian pesos. We accept VISA, Mastercard, Diners and American Express. Colombian residents are charged 19% VAT, which is not included in the rate and is collected at check-in; foreign guests may be exempt under current regulations.',
 '¿Cómo funciona la reserva?': 'How does booking work?',
 'Puedes reservar en línea a través de nuestro motor de reservas seguro (Cloudbeds), o escribirnos por WhatsApp para consultar disponibilidad. Tu reserva queda confirmada únicamente cuando recibes la confirmación del motor de reservas o de nuestro equipo.':
   'You can book online through our secure booking engine (Cloudbeds) or message us on WhatsApp to check availability. Your reservation is only confirmed once you receive confirmation from the booking engine or from our team.',
 # Ubicación y contacto
 'En el corazón de': 'In the heart of',
 'la Puerta de Oro': 'the Golden Gate',
 'Una ubicación estratégica: a solo minutos de los mejores sectores de Barranquilla, para que explores el Malecón del Río, la Casa del Carnaval y el sabor único de la ciudad.':
   'A strategic location just minutes from Barranquilla’s best neighborhoods, so you can explore the Malecón del Río, the Casa del Carnaval and the city’s unique flavor.',
 'Dirección': 'Address',
 'Teléfonos': 'Phone',
 'Correo': 'Email',
 'Mapa de ubicación de Amari Living Suites en Barranquilla': 'Map showing the location of Amari Living Suites in Barranquilla',
 'Escríbenos': 'Write to us',
 'Déjanos tu mensaje y te responderemos al correo. Al enviarlo se abrirá tu aplicación de correo con el mensaje listo para':
   'Leave us a message and we’ll reply by email. When you send it, your email app will open with the message ready to send to',
 'Correo electrónico': 'Email',
 'tucorreo@ejemplo.com': 'you@example.com',
 'Mensaje': 'Message',
 '¿En qué podemos ayudarte?': 'How can we help you?',
 'Acepto el tratamiento de mis datos personales según la': 'I agree to the processing of my personal data in accordance with the',
 'política de privacidad': 'privacy policy',
 'Enviar mensaje': 'Send message',
 # Tarjeta de reserva
 'Reserva tu suite': 'Book your suite',
 'Reserva en línea al instante o cuéntanos tus fechas y te responderemos por WhatsApp.': 'Book online instantly, or tell us your dates and we’ll reply on WhatsApp.',
 'Serás dirigido a nuestro motor de reservas seguro (Cloudbeds).': 'You’ll be taken to our secure booking engine (Cloudbeds).',
 'o consulta por WhatsApp': 'or ask on WhatsApp',
 'Cantidad de personas': 'Number of guests',
 'Selecciona la cantidad': 'Select how many',
 'Enviar por WhatsApp': 'Send via WhatsApp',
 'Tu mensaje se abre directamente en WhatsApp. Esta página no almacena tus datos.': 'Your message opens directly in WhatsApp. This page does not store your data.',
 # Pie
 'Secciones': 'Sections',
 'Explora': 'Explore',
 'Coworking y sala de juntas': 'Coworking & meeting room',
 'Beneficios para huéspedes': 'Guest benefits',
 'Políticas': 'Policies',
 'Síguenos': 'Follow us',
 'Galería de fotografías': 'Photo gallery',
 'Cerrar galería': 'Close gallery',
}

# Textos alternativos de la galería completa (JSON)
GAL = {
 'premium-01-1': 'Premium Suite with a Queen bed', 'room01': 'Junior Suite with two double beds', 'room-portada': 'Superior Suite with two single beds',
 'dsc03316': 'Suite with a large bed, desk and TV', 'dsc03343': 'Bed with an illuminated headboard', 'dsc02573': 'Room with two single beds',
 'dsc02818': 'Detail of the beds and headboard', 'dsc02575': 'Detail of the bed and bed runner', 'dsc02638': 'Kitchenette with refrigerator and microwave',
 'dsc02867': 'Kitchenette with sink and microwave', 'dsc03012': 'Coffee maker on the kitchenette countertop', 'dsc02595': 'Closet with Amari bathrobes and a safe',
 'dsc02616': 'Desk area and sofa in the suite', 'dsc03186': 'Desk with an upholstered chair', 'dsc03198': 'Desk and wall-mounted TV',
 'img01-1-2': 'Common lounge with a large window and mustard sofa', 'dsc02507': 'Shared floor lounge', 'dsc02494': 'Reception and lobby',
 'dsc02560': 'Reception with water dispensers', 'lobby': 'Panoramic view of the lobby', 'zonas-comunes': 'Common area with a blue sofa and woven chairs',
 'dsc02496': 'Common lounge with woven chairs', 'dsc02506': 'Common lounge with a mustard sofa', 'dsc02509': 'Common lounge with pictures of Barranquilla',
 'dsc02469': 'Mustard sofa and framed pictures', 'dsc02470': 'Sofa and coffee table', 'dsc02474': 'Lounge corner with tropical flowers',
 'dsc02468': 'Decorative vases', 'dsc02878': 'Lounge with a blue sofa and a colorful chair', 'dsc02898': 'Lounge with a glass table and plants',
 'dsc02965': 'Ceramic vases and a plant', 'dsc02972': 'Detail of a colorful woven chair', 'dsc02973': 'Tropical flower arrangement',
 'dsc02974': 'Hallway with a flower arrangement', 'dsc02938': 'Guest-room hallway', 'dsc02940': 'Stairs and hallway',
 'dsc02977': 'Suite door', 'dsc02978': 'Suite door with a plant', 'img01-4': 'Building facade',
 'dji0785': 'Aerial view of the building', 'terraza': 'View of the building and its terrace', 'banner-nosotros': 'Main entrance with stairs and garden',
 'dsc02394': 'Main entrance of the building', 'dsc02445': 'Amari entrance among palm trees', 'image-1': 'Amari sign at the entrance',
}


# ---- Auditoría (oct-2026): SEO, privacidad, documentos legales ----
T.update({
 'Amari Living Suites | Hotel en Barranquilla': 'Amari Living Suites | Hotel in Barranquilla',
 'Amari Living Suites, hotel en Barranquilla con suites equipadas con cocineta, coworking y sala de juntas. Consulta nuestros servicios y reserva tu estadía.':
   'Amari Living Suites, a hotel in Barranquilla with suites equipped with a kitchenette, a coworking space and a meeting room. See our services and book your stay.',
 'Aceptaciones': 'Acceptances',
 'Acepto los': 'I accept the',
 'Términos y Condiciones': 'Terms and Conditions',
 'He leído la': 'I have read the',
 'Política de Privacidad': 'Privacy Policy',
 'Autorizo a Amari Living Suites a tratar mis datos personales (nombre, correo y mensaje) para responder mi solicitud, conforme a la Política de Privacidad.':
   'I authorize Amari Living Suites to process my personal data (name, email and message) to reply to my request, in accordance with the Privacy Policy.',
 'Mapa de ubicación': 'Location map',
 'El mapa es un servicio de Google: al cargarlo, Google recibe tu dirección IP y puede instalar cookies.':
   'The map is a Google service: when it loads, Google receives your IP address and may set cookies.',
 'Más información': 'Learn more',
 'Ver mapa': 'View map',
 'Prendas limpias en un cesto en La Lavandería & Bakery': 'Clean clothes in a basket at La Lavandería & Bakery',
 'Lavandería · Sede Metro': 'Laundry · Metro branch',
 'Tu ropa lista para la reunión, el paseo o el regreso a casa, sin ocupar el tiempo de tu viaje. Queda en el mismo edificio de Amari.': 'Your clothes ready for your meeting, your outing or your trip home, without taking time away from your trip. It is in the same building as Amari.',
 'Instagram de La Lavandería & Bakery (abre en una pestaña nueva)': 'La Lavandería & Bakery on Instagram (opens in a new tab)',
 "Ser huésped de Amari tiene ventajas. Nuestros negocios aliados te ofrecen beneficios exclusivos durante tu estadía.": "Being an Amari guest has its perks. Our partner businesses offer you exclusive benefits during your stay.",
 "10 % de descuento para huéspedes en la lavandería aliada": "10% discount for guests at the partner laundry",
 "de descuento para huéspedes en la lavandería aliada": "off for guests at the partner laundry",
 "Promociones": "Promotions",
 "Accede a promociones": "Enjoy promotions",
 "por ser huésped de Amari Living Suites.": "as an Amari Living Suites guest.",
 "Vista aérea con dron del Gran Malecón junto al río Magdalena": "Drone view of the Gran Malecón along the Magdalena River",
 "La Luna del Río junto al río Magdalena al atardecer": "Luna del Río beside the Magdalena River at sunset",
 "Carrusel del Gran Malecón con la Luna del Río al fondo": "Gran Malecón carousel with Luna del Río in the background",
 "Palmera y Luna del Río al caer el sol": "Palm tree and Luna del Río at sunset",
 "Vista aérea nocturna de la Ventana de Campeones iluminada": "Night aerial view of the illuminated Ventana de Campeones",
 "Ventana de Campeones bajo el cielo azul": "Ventana de Campeones under a blue sky",
 "Paneles con la historia de Barranquilla en la base de la Ventana al Mundo": "Panels on the history of Barranquilla at the base of Ventana al Mundo",
 "Vista aérea con dron del muelle del Ecoparque Ciénaga de Mallorquín": "Drone view of the Ecoparque Ciénaga de Mallorquín boardwalk",
 "Muelle del ecoparque sobre la ciénaga al atardecer": "Eco-park pier over the swamp at sunset",
 "Atardecer sobre la Ciénaga de Mallorquín visto desde el aire": "Sunset over the Ciénaga de Mallorquín seen from the air",
 "Manglar y sendero de madera del ecoparque desde el aire": "Aerial view of the eco-park mangroves and wooden path",
 "Vista aérea de la playa Puerto Mocho con sus carpas frente al mar": "Aerial view of Puerto Mocho beach with its tents by the sea",
 "Botes de pescadores en Bocas de Ceniza, cerca de Puerto Mocho": "Fishing boats at Bocas de Ceniza, near Puerto Mocho",
 "Vía del tren sobre el tajamar hacia Bocas de Ceniza": "Railway on the breakwater towards Bocas de Ceniza",
 "Sendero sobre el tajamar, entre el río Magdalena y el mar": "Path along the breakwater, between the Magdalena River and the sea",
 "Playa Puerto Mocho": "Puerto Mocho Beach",
 "Fotos de Playa Puerto Mocho": "Photos of Puerto Mocho Beach",
 "La playa de Barranquilla, entre el río Magdalena, la Ciénaga de Mallorquín y el mar Caribe. Se llega en el tren turístico de Las Flores, en bicicleta o caminando.": "Barranquilla’s beach, between the Magdalena River, the Ciénaga de Mallorquín and the Caribbean Sea. You can get there on the Las Flores tourist train, by bike or on foot.",
 "Las Flores, acceso por la calle 106": "Las Flores, access via Calle 106",
 "Atardecer en el Jardín del Río del Gran Malecón, con embarcaciones y banderas": "Sunset at the Jardín del Río in the Gran Malecón, with boats and flags",
 "Cielo rosado al atardecer sobre los jardines del Gran Malecón": "Pink sunset sky over the Gran Malecón gardens",
 "Escultura Caimán del Río en el Gran Malecón": "Caimán del Río sculpture on the Gran Malecón",
 "Senderos y jardines junto al río Magdalena en el Gran Malecón": "Paths and gardens by the Magdalena River on the Gran Malecón",
 "Rueda de la fortuna Luna del Río en el Gran Malecón": "Luna del Río Ferris wheel on the Gran Malecón",
 "Ventana de Campeones iluminada de azul al atardecer": "Ventana de Campeones lit in blue at sunset",
 "Ventana de Campeones iluminada de rojo al atardecer": "Ventana de Campeones lit in red at sunset",
 "Monumento de vidrio Ventana de Campeones": "Ventana de Campeones glass monument",
 "Ventana al Mundo bajo el cielo azul": "Ventana al Mundo under a blue sky",
 "Ventana al Mundo iluminada de noche": "Ventana al Mundo lit up at night",
 "Detalle de los colores de la Ventana al Mundo": "Detail of the colors of Ventana al Mundo",
 "Fachada del Museo del Carnaval de Barranquilla": "Facade of the Barranquilla Carnival Museum",
 "Museo del Carnaval al atardecer": "Carnival Museum at sunset",
 "Casa del Carnaval, junto al museo": "Casa del Carnaval, next to the museum",
 "Figuras de carnaval en el interior de la Casa del Carnaval": "Carnival figures inside the Casa del Carnaval",
 "Muelle de madera sobre la Ciénaga de Mallorquín": "Wooden boardwalk over the Ciénaga de Mallorquín",
 "Paisaje de la Ciénaga de Mallorquín con su muelle": "Ciénaga de Mallorquín landscape with its pier",
 "Sendero de madera entre el manglar del ecoparque": "Wooden path through the eco-park mangroves",
 "Garza entre los manglares de la ciénaga": "Heron among the swamp mangroves",
 "Edificio del Museo del Caribe en el Parque Cultural del Caribe": "Museo del Caribe building in the Parque Cultural del Caribe",
 "Museo del Caribe rodeado de jardines": "Museo del Caribe surrounded by gardens",
 "Fachada del Museo del Caribe": "Facade of the Museo del Caribe",
 "Vista de la ciudad desde el Parque Cultural del Caribe": "View of the city from the Parque Cultural del Caribe",
 "Fachada de la Catedral Metropolitana María Reina": "Facade of the Metropolitan Cathedral of Mary Queen",
 "Interior de la catedral con sus vitrales": "Inside the cathedral with its stained glass",
 "Nave central de la catedral": "Central nave of the cathedral",
 "Vitral superior de la catedral": "Upper stained-glass window of the cathedral",
 "Fotos de Gran Malecón del Río": "Photos of Gran Malecón del Río",
 "Fotos de Luna del Río": "Photos of Luna del Río",
 "Fotos de Ventana de Campeones": "Photos of Ventana de Campeones",
 "Fotos de Ventana al Mundo": "Photos of Ventana al Mundo",
 "Fotos de Museo del Carnaval": "Photos of Museo del Carnaval",
 "Fotos de Ecoparque Ciénaga de Mallorquín": "Photos of Ecoparque Ciénaga de Mallorquín",
 "Fotos de Museo del Caribe": "Photos of Museo del Caribe",
 "Fotos de Catedral Metropolitana María Reina": "Photos of Catedral Metropolitana María Reina",
 'Tostada con huevo, aguacate y tocineta servida en un plato de Selah Bistró & Café': 'Toast with egg, avocado and bacon served on a Selah Bistró & Café plate',
 'El mapa es de Google: al abrirlo, Google recibe tu dirección IP y puede usar cookies. Recordaremos tu elección.':
   'The map is provided by Google: when you open it, Google receives your IP address and may use cookies. We will remember your choice.',
 'Vista aérea del edificio Amari Living Suites': 'Aerial view of the Amari Living Suites building',
 'Política de cancelación': 'Cancellation policy',
 'Política de pagos': 'Payment policy',
 'Política de servicios': 'Service policy',
 'Términos y condiciones': 'Terms and conditions',
 'Política de privacidad': 'Privacy policy',
 'Política de cookies': 'Cookie policy',
 'Preferencias de cookies': 'Cookie preferences',
})

missing = set()

def tr_text(m):
    raw = m.group(1)
    t = ' '.join(raw.split())
    if not t or t not in T:
        if t and re.search('[a-záéíóúñ]{3}', t, re.I):
            missing.add(t)
        return m.group(0)
    lead = raw[:len(raw) - len(raw.lstrip())]
    trail = raw[len(raw.rstrip()):]
    return '>' + lead + T[t] + trail + '<'

ATTRS = ('alt', 'aria-label', 'placeholder', 'title', 'content', 'data-pending-label', 'data-map-title')

def tr_attr(m):
    name, val = m.group(1), m.group(2)
    v = html.unescape(val)
    if v.startswith('Ampliar: '):
        inner = v[len('Ampliar: '):]
        return f'{name}="Enlarge: {html.escape(T.get(inner, inner), quote=True)}"'
    if v in T:
        return f'{name}="{html.escape(T[v], quote=True)}"'
    if re.search('[a-záéíóúñ]{3}', v, re.I) and name != 'content':
        missing.add('@' + name + ': ' + v)
    return m.group(0)

s = src

# 1) Proteger <script> y <style> (se procesan aparte)
blocks = []
def stash(m):
    blocks.append(m.group(0)); return f'\x00{len(blocks)-1}\x00'
s = re.sub(r'<script\b[\s\S]*?</script>|<style\b[\s\S]*?</style>', stash, s)

# 2) Selector de idioma y enlaces de cambio de idioma (antes de traducir)
s = s.replace('<html lang="es-CO">', '<html lang="en">')
s = s.replace('''<a class="lang-switch" href="en/" hreflang="en" lang="en" aria-label="English version" data-lang-switch>
            <svg class="icon" aria-hidden="true"><use href="#i-globe" /></svg>
            <span class="lang-switch__opt is-current" aria-hidden="true">ES</span><span class="lang-switch__sep" aria-hidden="true">/</span><span class="lang-switch__opt" aria-hidden="true">EN</span>''',
'''<a class="lang-switch" href="../" hreflang="es" lang="es" aria-label="Versión en español" data-lang-switch>
            <svg class="icon" aria-hidden="true"><use href="#i-globe" /></svg>
            <span class="lang-switch__opt" aria-hidden="true">ES</span><span class="lang-switch__sep" aria-hidden="true">/</span><span class="lang-switch__opt is-current" aria-hidden="true">EN</span>''')
s = s.replace('''<a class="mobile-menu__lang" href="en/" hreflang="en" lang="en">
          <svg class="icon" aria-hidden="true"><use href="#i-globe" /></svg>
          English version''', '''<a class="mobile-menu__lang" href="../" hreflang="es" lang="es">
          <svg class="icon" aria-hidden="true"><use href="#i-globe" /></svg>
          Versión en español''')
s = s.replace('<a class="site-footer__lang" href="en/" hreflang="en" lang="en"><svg class="icon" aria-hidden="true"><use href="#i-globe" /></svg> English</a>',
              '<a class="site-footer__lang" href="../" hreflang="es" lang="es"><svg class="icon" aria-hidden="true"><use href="#i-globe" /></svg> Español</a>')
s = s.replace('<link rel="alternate" hreflang="es" href="./" />', '<link rel="alternate" hreflang="es" href="../" />')
s = s.replace('<link rel="alternate" hreflang="en" href="en/" />', '<link rel="alternate" hreflang="en" href="./" />')
s = s.replace('<meta property="og:locale" content="es_CO" />', '<meta property="og:locale" content="en_US" />\n    <meta property="og:locale:alternate" content="es_CO" />')

# Reseñas originalmente en español: marcar idioma
s = s.replace('<span class="review__title">', '<span class="review__title" lang="es">')
s = s.replace('<p class="review__text">', '<p class="review__text" lang="es">')

# 3) Traducir atributos y textos
s = re.sub(r'\b(' + '|'.join(ATTRS) + r')="([^"]*)"', tr_attr, s)
s = re.sub(r'>([^<>\x00]+)<', tr_text, s)

# 4) Restaurar scripts (JSON de galería traducido)
def restore(m):
    b = blocks[int(m.group(1))]
    if 'data-gallery-data' in b:
        js = re.search(r'>(\[[\s\S]*\])</script>', b).group(1)
        items = json.loads(js)
        for it in items:
            key = os.path.basename(it['src']).replace('-800.webp', '')
            it['alt'] = GAL.get(key) or (missing.add('GAL: ' + it['alt']) or it['alt'])
        b = b.replace(js, json.dumps(items, ensure_ascii=False))
    return b
s = re.sub(r'\x00(\d+)\x00', restore, s)


# 4b) URLs propias del inglés: canónica, og:url, rutas legales y WhatsApp en inglés
from urllib.parse import quote, unquote
BASE = 'https://amarilivingsuite.com/'
s = s.replace(f'<link rel="canonical" href="{BASE}" />', f'<link rel="canonical" href="{BASE}en/" />')
s = s.replace(f'<meta property="og:url" content="{BASE}" />', f'<meta property="og:url" content="{BASE}en/" />')
for es_r, en_r in (('terminos-y-condiciones/', 'terms-and-conditions/'), ('politica-de-privacidad/', 'privacy-policy/'), ('politica-de-cookies/', 'cookie-policy/')):
    s = s.replace(f'href="{es_r}"', f'href="{en_r}"').replace(f'data-policy="{es_r}"', f'data-policy="{en_r}"')
cfg = open(os.path.join(P, 'src/js/config.js'), encoding='utf-8').read()
def msgs(lang):
    blk = cfg[cfg.index(lang + ': {', cfg.index('messages')):]
    blk = blk[:blk.index('},')]
    return dict(re.findall(r"(\w+):\s*\n?\s*'([^']*)'", blk))
ES_M, EN_M = msgs('es'), msgs('en')
def wa_en(m):
    text = unquote(m.group(2))
    for k, v in ES_M.items():
        if v == text and k in EN_M:
            return f'https://wa.me/{m.group(1)}?text=' + quote(EN_M[k], safe="-_.!~*'()")
    missing.add('WA: ' + text[:50])
    return m.group(0)
s = re.sub(r'https://wa\.me/(\d+)\?text=([^"&]*)', wa_en, s)

# 5) Rutas relativas desde /en/
s = re.sub(r'(?<=["\s,(])public/', '../public/', s)
s = re.sub(r'(?<=")src/', '../src/', s)

os.makedirs(os.path.join(P, 'en'), exist_ok=True)
open(os.path.join(P, 'en', 'index.html'), 'w', encoding='utf-8').write(s)
print(P, 'en/index.html generado')
for m in sorted(missing):
    print('  SIN TRADUCIR:', m)
