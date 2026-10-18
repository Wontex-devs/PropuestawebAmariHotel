"""Genera politicas.html (ES) y en/politicas.html (EN) para un proyecto.
Textos tomados de amarilivingsuite.com (políticas de cancelación, pagos, servicios y términos).
Uso: python3 build_policies.py <carpeta-proyecto>
"""
import sys, html, os

P = sys.argv[1] if len(sys.argv) > 1 else ''
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
WA = '+57 302 330 7939'
MAIL = 'atencionalcliente@amarilivingsuite.com'

# Cada sección: (id, título, [bloques]); bloque = ('h', texto) | ('p', texto) | ('ul', [items])
ES = {
 'lang': 'es-CO',
 'title': 'Políticas del hotel | Amari Living Suites',
 'crumb': 'Políticas',
 'desc': 'Políticas de cancelación, pagos y servicios de Amari Living Suites en Barranquilla: horarios de check-in y check-out, tarjetas aceptadas, parqueadero, mascotas y más.',
 'eyebrow': 'Información legal',
 'h1': 'Políticas de <em>Amari Living Suites</em>',
 'intro': 'Al realizar una reserva se considera que tienes pleno conocimiento de las políticas de pago, rechazo y cancelación del hotel. Si tienes dudas, escríbenos por WhatsApp o al correo.',
 'toc': 'Contenido',
 'back': 'Volver al inicio',
 'book': 'Reservar ahora',
 'wa': 'Escríbenos por WhatsApp',
 'langLabel': 'English version',
 'langHref': 'en/politicas.html',
 'langCode': ('ES', 'EN'),
 'home': './',
 'copy': 'Amari Living Suites · Barranquilla, Colombia',
 'sections': [
  ('cancelacion', 'Política de cancelación', [
    ('p', 'Hora de check-in: 3:00 p. m. · Hora de check-out: 12:00 m.'),
    ('p', 'El Hotel Amari Living Suites se reserva el derecho de cancelar una reserva en caso de que no se disponga de datos de tarjeta de crédito válidos que garanticen la misma y/o no cuente con ningún pago incorporado.'),
    ('p', 'En el caso de reservas no reembolsables, el monto total de la reserva será debitado automáticamente al momento de confirmar la reserva. No se permiten cambios o cancelaciones y, en caso de no presentarse, no habrá lugar a devoluciones.'),
    ('p', 'Política de tarifas y promociones flexibles: en toda reserva de alojamiento hecha bajo tarifa standard rate o tarifa flexible, 24 horas antes del check-in se realizará el cargo por el valor de la primera noche en la tarjeta de crédito dada como garantía de la reserva, con el fin de garantizar la misma. Si el cliente cancela la reserva con un plazo inferior a 24 horas, no se realizará ninguna devolución del valor cargado como garantía de la primera noche; en caso de hacer el respectivo reembolso, el huésped debe asumir los costos bancarios que se generen al momento de efectuarlo.'),
    ('p', 'La política de cancelación rige siempre y sin excepciones.'),
    ('p', f'Si necesitas más ayuda, llama directamente al hotel o comunícate vía WhatsApp al número {WA}. Si reservaste por canales de internet, deberás gestionar tu reserva por el mismo canal.'),
  ]),
  ('pagos', 'Política de pagos', [
    ('p', 'Al recibir una solicitud, el Hotel Amari Living Suites se reserva el derecho de solicitar la preautorización de la tarjeta de crédito indicada en la misma antes de la llegada. Al realizar una reserva, se considera que tienes pleno conocimiento de las políticas de pago, rechazo y cancelación del hotel.'),
    ('p', 'El débito y el pago de la estadía y de los servicios se realizan en pesos colombianos.'),
    ('p', 'Se aceptan las siguientes tarjetas de crédito: VISA, MASTERCARD, DINERS y AMERICAN EXPRESS.'),
    ('p', f'Para garantizar tu seguridad, cuando el pago de la reserva se solicite con los datos de la tarjeta de una persona o empresa diferente a las personas que se hospedarán, se requerirá una autorización y documentación previa, que se pedirá vía correo electrónico. Por favor comunícate vía WhatsApp al número {WA} y/o escribe a {MAIL}.'),
  ]),
  ('servicios', 'Política de servicios', [
    ('p', 'Amari Living Suites es un hotel que tiene la responsabilidad y el compromiso de seleccionar y promover servicios de alta calidad, diseñar programas de acuerdo con las expectativas de los clientes, facilitar un servicio amable, eficaz y eficiente, y fomentar el cumplimiento de las políticas ambientales en todo momento. Los estándares de calidad aplican desde el primer momento en que los clientes o proveedores entran en contacto con la empresa, hasta el final de los servicios y el seguimiento posventa.'),
    ('p', 'El cliente es lo primero y lo más importante: el Hotel Amari Living Suites hará todo lo posible para satisfacer enteramente las necesidades de los clientes, buscando siempre crear experiencias positivas desde el primer momento de contacto.'),
    ('p', 'Control de calidad del servicio: el Hotel Amari Living Suites estimula la retroalimentación por parte de los clientes y de otras fuentes, con el fin de obtener, interpretar y dirigir información que permita ofrecer de manera sostenida un servicio de calidad.'),
    ('h', 'Tarifa'),
    ('p', 'Incluye el alojamiento según la reserva. La tarifa no incluye desayuno.'),
    ('h', 'Impuestos'),
    ('p', 'Se aplicará un 19 % de IVA a los residentes colombianos. Los ciudadanos extranjeros pueden estar exentos, sujeto a verificación en el check-in. Este monto se cobrará en el hotel y no se refleja en la tarifa de la habitación. Se aplican condiciones. Para las estadías a partir del 1 de enero de 2023 (inclusive), los residentes de Colombia y los extranjeros que permanezcan en el país 60 días consecutivos o más deberán pagar el impuesto sobre las ventas nacional (19 %) en la propiedad durante la estadía. Los extranjeros con visa de turista están exentos de este impuesto. Además, si comparten habitación una persona obligada a pagar el impuesto y otra exenta, es posible que el impuesto se aplique a toda la habitación. El IVA no está incluido en la tarifa reservada; se añadirá al momento del check-in.'),
    ('p', 'Los huéspedes extranjeros y los colombianos residentes fuera del país están exentos del pago del 19 % de IVA al contratar un paquete turístico (alojamiento y servicios). Los turistas extranjeros y los ciudadanos colombianos residentes en el extranjero que cuenten con el sello con el código PT o con los actuales visados TP-7, TP-11 o TP-12 quedan exentos del 19 % de IVA al adquirir un paquete turístico.'),
    ('h', 'Check-in'),
    ('p', f'El horario de llegada es a partir de las 3:00 p. m. Si cuentas con confirmación de reserva, te enviaremos un enlace para realizar tu pre-check-in en línea; así será más ágil tu ingreso al llegar al hotel. Comunícate al WhatsApp {WA} para solicitar o gestionar tu reserva.'),
    ('p', 'Nota: es indispensable presentar identificación oficial de todos los huéspedes al momento de registrarse en el hotel, sin excepción (incluidos los menores de edad: registro civil, tarjeta de identidad y/o pasaporte, según aplique).'),
    ('h', 'Condiciones para estancias con niños'),
    ('ul', ['Se pueden alojar niños de cualquier edad, siempre acompañados de sus padres o tutores legales.',
            'Los niños a partir de 6 años se consideran adultos en este alojamiento.',
            'Los niños de hasta 5 años se hospedan sin cargo compartiendo la cama existente. Máximo 2 niños gratis (la capacidad máxima es de 4 personas en la Junior Suite).',
            'Bebés de hasta 3 años en cuna, sujeto a disponibilidad.',
            f'Para información sobre precios y ocupación, consulta al WhatsApp {WA}.']),
    ('h', 'Registro de menores de edad'),
    ('p', 'Si viajas con tu(s) hijo(s) menor(es) de 18 años, debes presentar el documento de identificación del (los) menor(es) (registro civil) que demuestre el parentesco. Si el (los) menor(es) no viaja(n) en compañía de sus padres, deberás entregar en la recepción, además del documento de identificación del menor, el permiso de los padres autenticado ante notario y acompañado de la copia del documento de identificación de quienes dieron la autorización. Sin esta documentación no se permite el ingreso de menores de edad al hotel, en desarrollo de lo dispuesto en la Ley 679 de 2001, Estatuto para Prevenir la Explotación Sexual de Niños, Niñas y Adolescentes, y sus normas concordantes.'),
    ('h', 'Early check-in'),
    ('ul', ['Sujeto a disponibilidad.', 'Ingreso antes de las 8:00 a. m.: se cobra la totalidad de la noche.', 'Ingreso entre las 8:00 a. m. y la 1:00 p. m.: se cobra media tarifa de la adquirida en tu estadía.', 'Después de la 1:00 p. m. se otorga el ingreso a la habitación como una atención del hotel.']),
    ('h', 'Check-out'),
    ('p', 'La suite debe ser entregada antes de las 12:00 m. del día en que finaliza la estadía.'),
    ('h', 'Late check-out'),
    ('ul', ['Sujeto a disponibilidad.', 'Late check-out hasta la 1:00 p. m. sin cobro.', 'Si el huésped no realiza el check-out a la hora indicada, se aplicará un cargo a la suite así: 50 % entre la 1:00 p. m. y las 6:00 p. m.; después de las 6:00 p. m., cargo del 100 % de la suite.']),
    ('h', 'Salida anticipada'),
    ('ul', ['Informar con un día de anticipación la nueva fecha de salida, a fin de que el hotel pueda disponer de la habitación para su venta. Aplica si la política de la reserva es flexible.', 'Si no se informa, se cobrará(n) al huésped la(s) noche(s).', 'Se cobrará el 100 % de las noches no usadas si la política reservada es no reembolsable.', 'Si reservaste una promoción de tarifa especial de larga estadía, se realizará el cambio de tarifa y se ajustará el cargo de cada noche según corresponda.']),
    ('h', 'Custodia de dinero y objetos de valor'),
    ('p', 'De conformidad con el artículo 1195 del Código de Comercio, los huéspedes podrán entregar bajo recibo al hotel dinero y objetos de valor para su custodia. La entrega deberá hacerse ante el funcionario designado por el hotel y deberá levantarse un acta donde se relacione el dinero o los objetos entregados. La responsabilidad del hotel será la del depositario, en los términos del artículo 1196 del Código de Comercio. Los objetos de valor como joyas, cámaras, dinero, computadores, celulares, equipos o utensilios que el huésped no declare en la recepción y permanezcan en la habitación o en áreas de servicio diferentes a las que el hotel dispone para depósito estarán bajo el único riesgo del huésped, y el hotel no asume responsabilidad alguna en caso de pérdida o deterioro. Siempre se recomienda el uso de la caja de seguridad disponible en cada suite, sin que ello conlleve responsabilidad de custodia para el hotel.'),
    ('h', 'No show'),
    ('p', 'En caso de no presentarse en el establecimiento, y de conformidad con la legislación colombiana (Ley 300 de 1996, artículo 65), el establecimiento podrá cobrar el 20 % del importe total de la reserva o retener el depósito. En cualquier caso, el cobro de no show siempre se realizará conforme a la política de la reserva aceptada por el cliente al momento de realizar la solicitud y enviar la información pertinente para garantizar su alojamiento.'),
    ('h', 'Disciplina para grupos y huéspedes en general'),
    ('p', 'Al reservar más de 5 habitaciones podrán aplicarse condiciones especiales y suplementos. En el caso de grupos, es necesario tener un estricto control, ya que somos un hotel turístico y de descanso; es de suma importancia comunicar a cada integrante del grupo, antes de su llegada, que evite hacer ruido que perturbe el entorno del hotel y/o a los demás huéspedes, tanto en las áreas comunes como en las suites, a cualquier hora. No se acepta ningún tipo de comportamiento sexual en las zonas comunes del hotel o en lugares donde otros huéspedes tengan visibilidad, como terrazas y zonas comunes. Esta situación podrá dar lugar a la expulsión inmediata de los huéspedes sin derecho a reembolso ni reagendamiento.'),
    ('h', 'Visitas'),
    ('p', 'Por seguridad, el hotel no acepta visitas nocturnas en las suites entre las 5:00 p. m. y las 10:00 a. m. Durante el día, de 10:00 a. m. a 5:00 p. m., toda visita deberá ser reportada y registrada previamente en la recepción; los visitantes deberán presentar documento legal y no se admite el ingreso de menores de edad que no estén acompañados por sus padres.'),
    ('p', 'Nota: si el huésped autoriza recibir visitas nocturnas en el hotel, deberá informarlo y registrarlo en la recepción. Si la visita se hospeda, el huésped deberá pagar $150.000 + IVA, correspondiente a la persona adicional que no fue registrada en la reserva.'),
    ('h', 'Parqueadero'),
    ('p', 'Sujeto a disponibilidad; debe solicitarse en la reserva. No tiene costo para 1 vehículo por suite. Aplica la política de custodia de dinero y objetos de valor (el hotel no se hace responsable por objetos dejados dentro del vehículo).'),
    ('h', 'Gimnasio'),
    ('p', 'El uso del gimnasio es bajo la exclusiva responsabilidad del huésped.'),
    ('h', 'Wi‑Fi'),
    ('p', 'El uso del Wi‑Fi es bajo la exclusiva responsabilidad del huésped y es una cortesía del hotel.'),
    ('h', 'Advertencias'),
    ('ul', ['La explotación y el abuso de menores de edad en Colombia son delitos juzgados plenamente con privación de la libertad. De acuerdo con la Ley 679 de 2001, el hotel está autorizado a denunciar ante las autoridades competentes cualquier acto criminal contra menores de edad. El hotel protege a los niños, niñas y adolescentes de todo tipo de explotación sexual y comercial (ESCNNA); por ello, sus empleados han firmado un código de conducta para la prevención de este tipo de acciones.',
            'Todo niño o niña menor de edad deberá permanecer en compañía de sus padres o de un adulto responsable; para esto es indispensable presentar el registro de identidad del menor, que permita al hotel establecer el parentesco entre el menor y el adulto acompañante. El hotel no dará registro de hospedaje a quien no cumpla con esta condición.',
            'En Colombia el tráfico ilegal de especies de flora y fauna es penalizado (Ley 453 de 2011; Resolución 192 de 2014).',
            'En el hotel estamos comprometidos con la promoción de acciones y prácticas en pro de la conservación del medio ambiente y el patrimonio cultural, la optimización de los recursos naturales y el cumplimiento de la legislación vigente en el sector turístico; por ende, el huésped debe acoger nuestras prácticas para contribuir a la optimización de los recursos y la conservación del medio ambiente.']),
    ('h', 'Ley antitabaco'),
    ('p', 'Se prohíbe fumar dentro del establecimiento (Ley 1335 de 2009, Ministerio de la Protección Social). En Colombia existe legislación sobre los espacios libres de humo y la afectación que el humo del cigarrillo o tabaco tiene sobre las demás personas. El huésped que incumpla esta disposición deberá pagar 80 USD o $320.000, correspondientes a la limpieza, desinfección y desodorización de la suite y de los elementos que contiene (sábanas, almohadas, toallas, cojines, etc.).'),
    ('h', 'Mascotas y manejo de animales silvestres'),
    ('p', 'No se autoriza el ingreso de mascotas; se aceptan perros de asistencia para personas con discapacidad certificada. El Hotel Amari Living Suites prohíbe el maltrato o la explotación de los animales y de la fauna y flora silvestres que se encuentren en la zona del hotel; en ese caso, el hotel impondrá una sanción al huésped y denunciará tales conductas ante la entidad competente.'),
    ('h', 'Política anticorrupción y antifraude'),
    ('p', 'No se permiten conductas o prácticas deshonestas que atenten contra la integridad empresarial, como ofrecer o aceptar regalos, invitaciones u otro tipo de incentivos que puedan recompensar o influir para que se tome o se deje de tomar alguna medida comercial o legal; ocultar, alterar, falsificar u omitir información intencionalmente en beneficio propio o de otros; o incurrir en eventuales conflictos de interés que antepongan prioridades personales a las colectivas. Promovemos una cultura de ética, transparencia y rectitud en el desarrollo de las actividades.'),
    ('h', 'Declaración de origen y destino de fondos'),
    ('p', 'Declaro que los recursos económicos y/o físicos no provienen ni serán destinados a actividades ilícitas de las contempladas en el Código Penal colombiano o en cualquier norma que lo modifique o adicione.'),
  ]),
  ('terminos', 'Términos y condiciones', [
    ('p', 'Los términos y condiciones de la prestación del servicio están en su propia página: <a href="terminos-y-condiciones/">Términos y condiciones</a>.'),
  ]),
  ('privacidad', 'Política de privacidad y tratamiento de datos personales', [
    ('p', 'Consulta cómo tratamos tus datos personales en la <a href="politica-de-privacidad/">Política de privacidad</a> y el uso de cookies en la <a href="politica-de-cookies/">Política de cookies</a>.'),
  ]),
 ],
}

EN = {
 'lang': 'en',
 'title': 'Hotel policies | Amari Living Suites',
 'crumb': 'Policies',
 'desc': 'Cancellation, payment and service policies of Amari Living Suites in Barranquilla, Colombia: check-in and check-out times, accepted cards, parking, pets and more.',
 'eyebrow': 'Legal information',
 'h1': 'Amari Living Suites <em>policies</em>',
 'intro': 'By making a reservation, you are deemed to be fully aware of the hotel’s payment, rejection and cancellation policies. If you have any questions, contact us on WhatsApp or by email.',
 'toc': 'Contents',
 'back': 'Back to home',
 'book': 'Book now',
 'wa': 'Message us on WhatsApp',
 'langLabel': 'Versión en español',
 'langHref': '../politicas.html',
 'langCode': ('EN', 'ES'),
 'home': './',
 'copy': 'Amari Living Suites · Barranquilla, Colombia',
 'note': 'This is a translation for reference. In case of any discrepancy, the Spanish version shall prevail.',
 'sections': [
  ('cancelacion', 'Cancellation policy', [
    ('p', 'Check-in time: 3:00 p.m. · Check-out time: 12:00 noon.'),
    ('p', 'Hotel Amari Living Suites reserves the right to cancel a reservation if valid credit card details guaranteeing it are not available and/or no payment has been made.'),
    ('p', 'For non-refundable reservations, the full amount of the reservation will be charged automatically when the reservation is confirmed. Changes and cancellations are not allowed, and no refunds will be given in the event of a no-show.'),
    ('p', 'Flexible rate and promotions policy: for any accommodation booked under the standard rate or flexible rate, the value of the first night will be charged to the credit card provided as a guarantee 24 hours before check-in, in order to secure the reservation. If the guest cancels less than 24 hours in advance, the amount charged as a guarantee for the first night will not be refunded; if a refund is made, the guest must cover any bank fees incurred.'),
    ('p', 'The cancellation policy always applies, without exception.'),
    ('p', f'If you need further assistance, call the hotel directly or contact us on WhatsApp at {WA}. If you booked through an online channel, please manage your reservation through that same channel.'),
  ]),
  ('pagos', 'Payment policy', [
    ('p', 'Upon receiving a request, Hotel Amari Living Suites reserves the right to request pre-authorization of the credit card provided before arrival. By making a reservation, you are deemed to be fully aware of the hotel’s payment, rejection and cancellation policies.'),
    ('p', 'Payment for the stay and for services is made in Colombian pesos.'),
    ('p', 'The following credit cards are accepted: VISA, MASTERCARD, DINERS and AMERICAN EXPRESS.'),
    ('p', f'For your security, if payment is to be made with the card of a person or company other than the guests staying at the hotel, prior authorization and documentation will be required and requested by email. Please contact us on WhatsApp at {WA} and/or write to {MAIL}.'),
  ]),
  ('servicios', 'Service policy', [
    ('p', 'Amari Living Suites is a hotel that is responsible for and committed to selecting and promoting high-quality services, designing programs in line with guests’ expectations, providing friendly, effective and efficient service, and encouraging compliance with environmental policies at all times. Our quality standards apply from the moment guests or suppliers first contact the company until the end of the service and after-sales follow-up.'),
    ('p', 'The guest comes first: Hotel Amari Living Suites will do everything possible to fully meet our guests’ needs, always seeking to create positive experiences from the very first contact.'),
    ('p', 'Service quality control: Hotel Amari Living Suites encourages feedback from guests and other sources in order to obtain, interpret and act on information that allows us to consistently deliver quality service.'),
    ('h', 'Rate'),
    ('p', 'Includes accommodation as per the reservation. The rate does not include breakfast.'),
    ('h', 'Taxes'),
    ('p', 'A 19% VAT applies to Colombian residents. Foreign citizens may be exempt, subject to verification at check-in. This amount is charged at the hotel and is not reflected in the room rate. Conditions apply. For stays from January 1, 2023 (inclusive), Colombian residents and foreigners who remain in the country for 60 consecutive days or more must pay the national sales tax (19%) at the property during their stay. Foreigners with a tourist visa are exempt from this tax. In addition, if a person required to pay the tax shares a room with an exempt person, the tax may apply to the entire room. VAT is not included in the booked rate and will be added at check-in.'),
    ('p', 'Foreign guests and Colombians residing abroad are exempt from the 19% VAT when purchasing a tourist package (accommodation and services). Foreign tourists and Colombian citizens residing abroad who hold the PT entry stamp or the current TP-7, TP-11 or TP-12 visas are exempt from the 19% VAT when purchasing a tourist package.'),
    ('h', 'Check-in'),
    ('p', f'Check-in is from 3:00 p.m. If you have a confirmed reservation, we will send you a link to complete your online pre-check-in, making your arrival at the hotel faster. Contact us on WhatsApp at {WA} to request or manage a reservation.'),
    ('p', 'Note: all guests must present official identification when registering at the hotel, without exception (including minors: birth certificate, identity card and/or passport, as applicable).'),
    ('h', 'Stays with children'),
    ('ul', ['Children of any age are welcome, always accompanied by their parents or legal guardians.',
            'Children aged 6 and over are considered adults at this property.',
            'Children up to 5 years old stay free of charge when sharing an existing bed. Maximum of 2 children free of charge (maximum capacity is 4 people in the Junior Suite).',
            'Cribs for babies up to 3 years old, subject to availability.',
            f'For information on prices and occupancy, contact us on WhatsApp at {WA}.']),
    ('h', 'Registration of minors'),
    ('p', 'If you are traveling with your child(ren) under 18, you must present the minor’s identification document (birth certificate) proving the family relationship. If the minor(s) are not traveling with their parents, in addition to the minor’s identification document you must provide at reception the parents’ authorization, notarized and accompanied by a copy of the identification document of those who gave the authorization. Without this documentation, minors will not be allowed into the hotel, in accordance with Law 679 of 2001 (Statute to Prevent the Sexual Exploitation of Children and Adolescents) and related regulations.'),
    ('h', 'Early check-in'),
    ('ul', ['Subject to availability.', 'Arrival before 8:00 a.m.: the full night is charged.', 'Arrival between 8:00 a.m. and 1:00 p.m.: half of the booked nightly rate is charged.', 'After 1:00 p.m., access to the room is granted as a courtesy of the hotel.']),
    ('h', 'Check-out'),
    ('p', 'The suite must be vacated before 12:00 noon on the last day of your stay.'),
    ('h', 'Late check-out'),
    ('ul', ['Subject to availability.', 'Late check-out until 1:00 p.m. free of charge.', 'If the guest does not check out at the indicated time, the following charges will apply to the suite: 50% between 1:00 p.m. and 6:00 p.m.; after 6:00 p.m., 100% of the suite rate.']),
    ('h', 'Early departure'),
    ('ul', ['Please notify us one day in advance of your new early departure date, so the hotel can make the room available for sale. Applies if the reservation policy is flexible.', 'If we are not informed, the guest will be charged for the night(s).', '100% of unused nights will be charged if the booked policy is non-refundable.', 'If you booked a special long-stay rate promotion, the rate will be changed and the nightly charge adjusted accordingly.']),
    ('h', 'Safekeeping of money and valuables'),
    ('p', 'In accordance with article 1195 of the Colombian Commercial Code, guests may deposit money and valuables with the hotel for safekeeping against a receipt. The deposit must be made before the staff member designated by the hotel, and a record listing the money or items deposited must be drawn up. The hotel’s liability will be that of a depositary, under the terms of article 1196 of the Commercial Code. Valuables such as jewelry, cameras, money, computers, mobile phones, equipment or utensils that the guest does not declare at reception and that remain in the room or in service areas other than those provided by the hotel for deposit are at the guest’s sole risk, and the hotel assumes no liability in case of loss or damage. We always recommend using the safe available in each suite, without this implying any custody liability for the hotel.'),
    ('h', 'No-show'),
    ('p', 'In the event of a no-show, and in accordance with Colombian law (Law 300 of 1996, article 65), the property may charge 20% of the total amount of the reservation or retain the deposit. In any case, the no-show charge will always be applied according to the reservation policy accepted by the guest when making the request and providing the information required to guarantee the stay.'),
    ('h', 'Conduct for groups and guests in general'),
    ('p', 'When booking more than 5 rooms, special conditions and supplements may apply. Groups must be kept under strict control, as we are a tourist and rest hotel; it is very important to inform every member of the group before arrival to avoid making noise that disturbs the hotel environment and/or other guests, both in common areas and in the suites, at any time. No sexual behavior of any kind is permitted in the hotel’s common areas or in places visible to other guests, such as terraces and common areas. Such conduct may result in the immediate expulsion of the guests without refund or rescheduling.'),
    ('h', 'Visitors'),
    ('p', 'For security reasons, the hotel does not allow overnight visitors in the suites between 5:00 p.m. and 10:00 a.m. During the day, from 10:00 a.m. to 5:00 p.m., all visitors must be reported and registered in advance at reception; visitors must present a legal identity document, and minors are not admitted unless accompanied by their parents.'),
    ('p', 'Note: if the guest authorizes overnight visitors at the hotel, they must inform and register them at reception. If the visitor stays overnight, the guest must pay COP $150,000 + VAT for the additional person who was not registered in the reservation.'),
    ('h', 'Parking'),
    ('p', 'Subject to availability; must be requested in the reservation. Free of charge for 1 vehicle per suite. The policy on safekeeping of money and valuables applies (the hotel is not responsible for items left inside vehicles).'),
    ('h', 'Gym'),
    ('p', 'Use of the gym is at the guest’s sole responsibility.'),
    ('h', 'Wi‑Fi'),
    ('p', 'Use of the Wi‑Fi is at the guest’s sole responsibility and is a courtesy of the hotel.'),
    ('h', 'Warnings'),
    ('ul', ['The exploitation and abuse of minors in Colombia are crimes fully prosecuted with imprisonment. Under Law 679 of 2001, the hotel is authorized to report any criminal act against minors to the competent authorities. The hotel protects children and adolescents from all forms of commercial sexual exploitation (ESCNNA); for this reason, its employees have signed a code of conduct to prevent such acts.',
            'All minors must remain in the company of their parents or a responsible adult; for this purpose, the minor’s identity document must be presented so the hotel can establish the relationship between the minor and the accompanying adult. The hotel will not register guests who do not meet this condition.',
            'In Colombia, illegal trafficking of wild flora and fauna is a punishable offense (Law 453 of 2011; Resolution 192 of 2014).',
            'At the hotel we are committed to promoting actions and practices that support the conservation of the environment and cultural heritage, the efficient use of natural resources and compliance with current tourism legislation; therefore, guests are expected to follow our practices to help optimize resources and protect the environment.']),
    ('h', 'Anti-smoking law'),
    ('p', 'Smoking is prohibited inside the property (Law 1335 of 2009, Ministry of Social Protection). Colombia has legislation on smoke-free spaces and on the effects of cigarette or tobacco smoke on other people. Guests who fail to comply must pay USD 80 or COP $320,000 for the cleaning, disinfection and deodorization of the suite and its contents (sheets, pillows, towels, cushions, etc.).'),
    ('h', 'Pets and wildlife'),
    ('p', 'Pets are not allowed; assistance dogs for people with a certified disability are accepted. Hotel Amari Living Suites prohibits the mistreatment or exploitation of animals and of wild flora and fauna in the hotel’s surroundings; in such cases, the hotel will penalize the guest and report the conduct to the competent authority.'),
    ('h', 'Anti-corruption and anti-fraud policy'),
    ('p', 'Dishonest conduct or practices that undermine corporate integrity are not permitted, such as offering or accepting gifts, invitations or other incentives that may reward or influence the taking or not taking of any commercial or legal action; intentionally concealing, altering, falsifying or omitting information for one’s own or another’s benefit; or engaging in conflicts of interest that place personal priorities above collective ones. We promote a culture of ethics, transparency and integrity in all our activities.'),
    ('h', 'Declaration of origin and destination of funds'),
    ('p', 'I declare that the economic and/or physical resources do not come from, nor will they be used for, any unlawful activities covered by the Colombian Criminal Code or any law that amends or supplements it.'),
  ]),
  ('terminos', 'Terms and conditions', [
    ('p', 'The terms and conditions of service are on their own page: <a href="terms-and-conditions/">Terms and conditions</a>.'),
  ]),
  ('privacidad', 'Privacy and personal data policy', [
    ('p', 'See how we process your personal data in the <a href="privacy-policy/">Privacy policy</a> and how cookies are used in the <a href="cookie-policy/">Cookie policy</a>.'),
  ]),
 ],
}

SPRITE = '''    <svg width="0" height="0" style="position: absolute" aria-hidden="true" focusable="false">
      <symbol id="i-arrow" viewBox="0 0 24 24"><path d="M5 12h14M13 6l6 6-6 6" /></symbol>
      <symbol id="i-close" viewBox="0 0 24 24"><path d="M6 6l12 12M18 6L6 18" /></symbol>
      <symbol id="i-arrow-left" viewBox="0 0 24 24"><path d="M19 12H5M11 6l-6 6 6 6" /></symbol>
      <symbol id="i-globe" viewBox="0 0 24 24"><circle cx="12" cy="12" r="9" /><path d="M3 12h18M12 3c2.5 2.6 3.8 5.6 3.8 9s-1.3 6.4-3.8 9c-2.5-2.6-3.8-5.6-3.8-9S9.5 5.6 12 3z" /></symbol>
      <symbol id="i-whatsapp" viewBox="0 0 24 24"><path d="M17.47 14.38c-.3-.15-1.76-.87-2.03-.97-.27-.1-.47-.15-.67.15-.2.3-.77.97-.94 1.16-.17.2-.35.22-.64.08-.3-.15-1.26-.46-2.4-1.48-.88-.79-1.48-1.76-1.65-2.06-.17-.3-.02-.46.13-.6.13-.14.3-.35.45-.52.15-.18.2-.3.3-.5.1-.2.05-.37-.03-.52-.07-.15-.67-1.61-.92-2.2-.24-.58-.48-.5-.67-.51h-.57c-.2 0-.52.07-.79.37-.27.3-1.04 1.02-1.04 2.48 0 1.46 1.07 2.88 1.21 3.07.15.2 2.1 3.2 5.08 4.49.71.3 1.26.49 1.7.62.71.23 1.36.2 1.87.12.57-.09 1.76-.72 2-1.41.25-.7.25-1.29.18-1.41-.08-.13-.27-.2-.57-.35m-5.42 7.4h-.01a9.87 9.87 0 0 1-5.03-1.37l-.36-.22-3.74.98 1-3.65-.24-.37a9.86 9.86 0 0 1-1.51-5.26c0-5.45 4.44-9.88 9.89-9.88 2.64 0 5.12 1.03 6.99 2.9a9.83 9.83 0 0 1 2.89 6.99c0 5.45-4.44 9.88-9.88 9.88m8.41-18.3A11.82 11.82 0 0 0 12.05 0C5.5 0 .16 5.34.16 11.89c0 2.1.55 4.14 1.59 5.95L.06 24l6.3-1.65a11.88 11.88 0 0 0 5.69 1.45h.01c6.55 0 11.89-5.34 11.89-11.89a11.82 11.82 0 0 0-3.48-8.41z" /></symbol>
    </svg>'''

def blocks(bl):
    out = []
    for kind, val in bl:
        if kind == 'h':
            out.append(f'          <h3 class="policy__h">{html.escape(val)}</h3>')
        elif kind == 'p':
            out.append(f'          <p>{val if "<" in val else html.escape(val)}</p>')
        else:
            out.append('          <ul>\n' + '\n'.join(f'            <li>{i if "<" in i else html.escape(i)}</li>' for i in val) + '\n          </ul>')
    return '\n'.join(out)

def page(d, here, alt_here, wa_href, extra_head_ld=''):
    """Página secundaria. here / alt_here: rutas del sitio (ver site_common.ROUTES)."""
    from site_common import BASE, csp, rel, legal_links, breadcrumb_ld, LABELS
    lang = 'en' if d['lang'] == 'en' else 'es'
    depth = here.count('/')
    prefix = '../' * depth
    home_href = rel(here, ROUTES_HOME[lang])
    lang_switch_href = rel(here, alt_here)
    toc = '\n'.join(f'            <li><a href="#{sid}">{html.escape(t)}</a></li>' for sid, t, _ in d['sections'])
    secs = '\n'.join(f"""        <section class="policy" id="{sid}" aria-labelledby="{sid}-title">
          <h2 class="policy__title" id="{sid}-title">{html.escape(t)}</h2>
{blocks(bl)}
        </section>""" for sid, t, bl in d['sections'])
    note = f'\n        <p class="policies__note">{d["note"]}</p>' if d.get('note') else ''
    notice = f'\n        <div class="policies__notice" role="note">{d["notice"]}</div>' if d.get('notice') else ''
    cur, other = d['langCode']
    hl_self, hl_alt = ('en', 'es') if lang == 'en' else ('es', 'en')
    links = '\n            '.join(legal_links(lang, here))
    crumb = breadcrumb_ld(lang, here, d['crumb'])
    return f"""<!doctype html>
<html lang="{d['lang']}">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover" />
    <meta http-equiv="Content-Security-Policy" content="{csp()}" />
    <meta name="referrer" content="strict-origin-when-cross-origin" />
    <title>{d['title']}</title>
    <meta name="description" content="{d['desc']}" />
    <meta name="robots" content="{d.get('robots', 'index, follow')}" />
    <link rel="canonical" href="{BASE}{here}" />
    <link rel="alternate" hreflang="{hl_self}" href="{BASE}{here}" />
    <link rel="alternate" hreflang="{hl_alt}" href="{BASE}{alt_here}" />
    <link rel="alternate" hreflang="x-default" href="{BASE}{here if lang == 'es' else alt_here}" />
    <meta name="theme-color" content="#000000" />
    <link rel="icon" type="image/png" href="{prefix}public/favicon.png" />
    <meta property="og:type" content="website" />
    <meta property="og:site_name" content="Amari Living Suites" />
    <meta property="og:locale" content="{'en_US' if lang == 'en' else 'es_CO'}" />
    <meta property="og:title" content="{d['title']}" />
    <meta property="og:description" content="{d['desc']}" />
    <meta property="og:url" content="{BASE}{here}" />
    <meta property="og:image" content="{BASE}public/og-image.jpg" />
    <link rel="stylesheet" href="{prefix}src/styles/tokens.css?v=2" />
    <link rel="stylesheet" href="{prefix}src/styles/base.css" />
    <link rel="stylesheet" href="{prefix}src/styles/components.css?v=2" />
    <link rel="stylesheet" href="{prefix}src/styles/sections.css?v=6" />
    <link rel="stylesheet" href="{prefix}src/styles/extras.css?v=8" />
    <link rel="stylesheet" href="{prefix}src/styles/policies.css?v=2" />
    <script type="application/ld+json">
      {crumb}
    </script>
  </head>
  <body class="policies-page">
{SPRITE}
    <a class="skip-link" href="#contenido">{'Skip to content' if lang == 'en' else 'Saltar al contenido'}</a>
    <header class="site-header is-solid" data-header data-header-solid>
      <div class="site-header__inner container">
        <a class="site-header__logo" href="{home_href}" aria-label="{'Amari Living Suites, home' if lang == 'en' else 'Amari Living Suites, ir al inicio'}">
          <img class="logo" src="{prefix}public/brand/amari-logo-black-sm.png" alt="" width="400" height="152" />
        </a>
        <div class="site-header__actions">
          <a class="policies__back" href="{home_href}"><svg class="icon" aria-hidden="true"><use href="#i-arrow-left" /></svg><span>{d['back']}</span></a>
          <a class="lang-switch" href="{lang_switch_href}" hreflang="{other.lower()}" lang="{other.lower()}" aria-label="{d['langLabel']}">
            <svg class="icon" aria-hidden="true"><use href="#i-globe" /></svg>
            <span class="lang-switch__opt is-current" aria-hidden="true">{cur}</span><span class="lang-switch__sep" aria-hidden="true">/</span><span class="lang-switch__opt" aria-hidden="true">{other}</span>
          </a>
          <a class="site-header__cta" href="https://hotels.cloudbeds.com/en/reservation/FuhJUM?currency=cop" data-booking target="_blank" rel="noopener">
            <span class="site-header__cta-label">{d['book']}</span>
            <span class="site-header__cta-icon" aria-hidden="true"><svg class="icon"><use href="#i-arrow" /></svg></span>
          </a>
        </div>
      </div>
    </header>

    <main id="contenido" class="policies">
      <div class="container policies__layout">
        <header class="policies__head">
          <p class="eyebrow">{d['eyebrow']}</p>
          <h1 class="h2">{d['h1']}</h1>
          <p class="lead">{d['intro']}</p>{notice}
          <a class="btn btn--sm" href="{wa_href}" data-wa="amari" target="_blank" rel="noopener">
            <svg class="icon icon--fill" aria-hidden="true"><use href="#i-whatsapp" /></svg>
            {d['wa']}
          </a>{note}
        </header>
        <nav class="policies__toc" aria-label="{d['toc']}">
          <p class="policies__toc-title">{d['toc']}</p>
          <ul role="list">
{toc}
          </ul>
        </nav>
        <div class="policies__body">
{secs}
        </div>
      </div>
    </main>

    <footer class="site-footer on-dark">
      <nav class="container policies__legal" aria-label="{LABELS[lang]['legal']}">
        <ul>
            {links}
        </ul>
      </nav>
      <div class="container site-footer__bottom">
        <p>© <span data-year>2026</span> {d['copy']}</p>
        <a class="site-footer__lang" href="{lang_switch_href}" hreflang="{other.lower()}" lang="{other.lower()}"><svg class="icon" aria-hidden="true"><use href="#i-globe" /></svg> {d['langLabel']}</a>
      </div>
    </footer>

    <script type="module" src="{prefix}src/js/main.js?v=7"></script>
  </body>
</html>
"""

ROUTES_HOME = {'es': '', 'en': 'en/'}

if __name__ == '__main__':
    from urllib.parse import quote
    WA_URL = {
        'es': 'https://wa.me/573023307939?text=' + quote('Hola, me gustaría hospedarme en Amari Living Suites. ¿Me ayudan a consultar disponibilidad y opciones de reserva?', safe="-_.!~*'()"),
        'en': 'https://wa.me/573023307939?text=' + quote('Hello, I would like to stay at Amari Living Suites. Could you help me check availability and booking options?', safe="-_.!~*'()"),
    }
    open(os.path.join(P, 'politicas.html'), 'w', encoding='utf-8').write(page(ES, 'politicas.html', 'en/politicas.html', WA_URL['es']))
    os.makedirs(os.path.join(P, 'en'), exist_ok=True)
    open(os.path.join(P, 'en', 'politicas.html'), 'w', encoding='utf-8').write(page(EN, 'en/politicas.html', 'politicas.html', WA_URL['en']))
    print(P, 'políticas ES/EN generadas')
