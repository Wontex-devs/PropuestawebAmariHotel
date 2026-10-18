# Auditoría técnica, SEO, rendimiento, seguridad, privacidad y cumplimiento — Amari Living Suites

**Fecha:** 18 de octubre de 2026 · **Alcance:** `opcion-1-full/` y `opcion-2-sencilla/`, en español e inglés (20 páginas en total).
**Estado:** cambios hechos y probados en local, **sin publicar**. No se tocó el DNS, el hosting, GitHub Pages ni ningún servicio externo.

> Este informe no es asesoría jurídica. Las referencias legales buscan orientar la conversación del hotel con su abogado. Los documentos legales creados son **borradores**: no están aprobados y llevan marcados los datos que faltan.

---

## 1. Resumen ejecutivo

| Área | Antes | Ahora |
|---|---|---|
| Validación HTML (W3C) | ~22 errores en la portada Full y equivalentes en Sencilla | **0 errores en las 20 páginas** |
| SEO técnico | Canónica y `hreflang` relativos, `og:image` relativo, sin `sitemap.xml` ni `robots.txt` | Canónica, `hreflang` y Open Graph absolutos hacia `https://amarilivingsuite.com/`. Hay `sitemap.xml` y `robots.txt` |
| Datos estructurados | `Hotel` básico | `Hotel` y `WebSite` en un `@graph`, `BreadcrumbList` en las páginas internas. Solo datos verificados |
| Privacidad | El mapa de Google se cargaba sin consentimiento | El mapa solo se carga con permiso. Hay diálogo de preferencias y política de cookies |
| Legal | Sin rutas de términos, privacidad ni cookies; el formulario tenía una sola casilla | 6 páginas legales (ES/EN) en rutas estables. El formulario tiene 3 casillas separadas y desmarcadas, y deja constancia de la aceptación |
| Seguridad | Sin CSP | CSP en `<meta>` con hash del único script en línea, más política de referer |
| Diseño | — | **Se conserva.** Las medidas coinciden píxel a píxel con las de antes, salvo los elementos legales añadidos (sección 21) |

Para publicar con plenas garantías falta información que **solo el hotel puede dar** (sección 23).

## 2. Metodología

- Revisión del código fuente de las dos versiones.
- Comparación con el sitio actual (`amarilivingsuite.com`): cabeceras HTTP, `robots.txt`, redirecciones y terceros.
- Validador oficial W3C Nu (`validator.w3.org/nu`) sobre cada página.
- Navegador integrado: consola, red, CSP, consentimiento, formularios, menú móvil y desbordes, a 1440 px y a 375 px.
- Medición geométrica antes/después de cada sección, para comprobar que el diseño no cambió.
- Revisión normativa con fuentes públicas oficiales o normogramas de entidades públicas (sección 17).
- **Limitaciones.** La API de PageSpeed Insights devolvió «cuota agotada» y en este equipo no hay Node ni Lighthouse, así que **no hay mediciones de Core Web Vitals** y este informe no las afirma. El panel del navegador estaba oculto y eso limita las animaciones y las capturas; por eso las comprobaciones se hicieron midiendo con JavaScript.

## 3. Diagnóstico inicial

1. HTML no válido en puntos concretos: enlaces `<a>` con `target`/`rel` sin `href` (todos los botones de WhatsApp y de contacto dependían de JS), imágenes sin `src` (escenas 2–6 del hero y el visor de la galería) y `aria-label` sobre `<div>` sin rol.
2. SEO: URLs relativas en canónica, `hreflang` y `og:image`; enlaces legales del pie generados solo por JS (menos rastreables); sin `sitemap.xml` ni `robots.txt` propios.
3. Privacidad: el iframe de Google Maps se cargaba al abrir la página, antes de cualquier elección, y entregaba la IP y posibles cookies de Google.
4. Legal: términos con solo «objetivo y alcance», privacidad «en actualización», sin política de cookies y sin casillas de aceptación separadas.
5. Seguridad: sin CSP. GitHub Pages ya envía HSTS, pero no permite cabeceras propias. El sitio actual (Apache) no envía cabeceras de seguridad y su `robots.txt` tiene `Crawl-delay: 30`.

## 4. Cambios realizados

| Archivo | Cambio |
|---|---|
| `*/index.html` | Cabecera SEO completa, CSP, JSON-LD, `href` reales en WhatsApp, teléfono, correo y «Cómo llegar», hero sin `<img>` vacíos, mapa con consentimiento, 3 casillas en el formulario, enlaces legales estáticos en el pie, licencias enlazadas en los créditos de Commons |
| `*/en/index.html` | Regenerada desde la versión ES: canónica `/en/`, mensajes de WhatsApp en inglés y rutas legales en inglés |
| `*/politicas.html`, `*/en/politicas.html` | Misma plantilla con SEO, CSP, migas (JSON-LD) y pie legal. Las secciones de términos y privacidad ahora remiten a sus páginas propias. **Cancelación, pagos y servicios quedan intactos** |
| `*/terminos-y-condiciones/`, `*/politica-de-privacidad/`, `*/politica-de-cookies/` y sus equivalentes en `en/` | **Nuevas**: borradores con `noindex` |
| `src/js/consent.js` | **Nuevo**: carga el mapa solo con consentimiento, diálogo de preferencias y retirada del consentimiento |
| `src/js/main.js` | El hero y el visor crean sus imágenes; formulario con 3 casillas y constancia de aceptación; integra el consentimiento |
| `src/js/config.js` | `legal.version` (versión citada en la constancia) |
| `src/styles/extras.css`, `policies.css` | Estilos del mapa con consentimiento, del diálogo, de las casillas, del aviso de borrador y de las marcas de «Pendiente» |
| `robots.txt`, `sitemap.xml` | **Nuevos** (por versión, apuntando al dominio de producción) |
| `tools/` | Generadores (EN, políticas y documentos legales) y validador |
| `docs/inventario-imagenes.csv` | Inventario de derechos de imágenes y fuentes |

Lo que se mantiene sin cambios: diseño, textos comerciales, tarifas, políticas de cancelación, pagos y servicios, URL de Cloudbeds, números de WhatsApp y animaciones.

## 5. HTML y semántica

- 0 errores W3C en las 20 páginas. La prueba se repite con `python3 tools/validate.py salida.json`.
- Avisos que se mantienen a propósito:
  - `role="list"` en `<ul>` con `list-style: none`, porque Safari/VoiceOver deja de anunciar la lista si se quita.
  - Las reseñas (`<article>`) no tienen encabezado. Añadirlo cambiaría la jerarquía visual; es opcional.
  - El validador también da avisos de CSP «violada»: aparecen porque analiza el archivo sin origen. En el navegador real no hubo ninguna violación (sección 21).
- Un solo `<h1>` por página, con `lang` correcto (`es-CO` / `en`) y las reseñas en español marcadas con `lang="es"` dentro de la versión EN.

## 6. SEO on-page

| Página | Título | Descripción |
|---|---|---|
| Inicio ES | Amari Living Suites \| Hotel en Barranquilla | Amari Living Suites, hotel en Barranquilla con suites equipadas con cocineta, cowork y sala de juntas. Consulta nuestros servicios y reserva tu estadía. (151 caracteres) |
| Inicio EN | Amari Living Suites \| Hotel in Barranquilla | Equivalente en inglés |
| Políticas | Políticas del hotel \| Amari Living Suites | Cancelación, pagos y servicios, con datos reales del contenido |
| Legales | «Términos y condiciones \| Amari Living Suites», etc. | Propia por documento |

- **Cambio frente a la propuesta del brief:** «suites equipadas, comodidad y espacios para trabajar» pasó a «suites equipadas con cocineta, cowork y sala de juntas», que es lo que el sitio realmente ofrece y puede comprobarse.
- No se usa `meta keywords`.
- Robots: `index, follow, max-image-preview:large` en las páginas públicas y `noindex, follow` en los borradores legales.

## 7. Indexación, dominio canónico y migración

- Dominio canónico: `https://amarilivingsuite.com/` (sin `www`, con HTTPS), igual que las redirecciones 301 actuales del servidor.
- `hreflang` es/en/x-default recíproco y absoluto en todas las páginas.
- `sitemap.xml` incluye la portada y las políticas (ES/EN) con alternativas de idioma. **Los documentos legales se añaden cuando se aprueben** y se les quite el `noindex`.
- `robots.txt` sin `Crawl-delay` (Google lo ignora y ralentiza a otros buscadores). **Solo funciona en la raíz del dominio**: en GitHub Pages, dentro de una subcarpeta, no tiene efecto.
- **Vista previa en GitHub Pages:** como la canónica apunta al dominio oficial, los buscadores no deberían tratarla como contenido duplicado. Aun así, no se debe enlazar públicamente.
- **Al publicar en producción (tarea del hosting):**
  - Subir el contenido de **una** de las versiones a la raíz.
  - Configurar 301 desde las URLs antiguas que existan en el sitio actual (p. ej. `/politica-de-cancelacion`, `/politica-de-pagos`, `/politica-de-servicios`, `/privacy-policy`, `/terms-and-conditions`) hacia `politicas.html#…` o las nuevas rutas. **Hay que confirmar la lista exacta con un rastreo del sitio actual o con Search Console.**

## 8. Datos estructurados (JSON-LD)

- `Hotel` (`@id …/#hotel`) incluye:
  - Nombre, URL, logo, imagen, correo, teléfonos y dirección.
  - `hasMap`, 32 habitaciones, check-in 15:00 y check-out 12:00.
  - `smokingAllowed: false`, `currenciesAccepted: COP` y las tarjetas aceptadas.
  - Servicios: Wi‑Fi, parqueadero sin costo sujeto a disponibilidad, gimnasio, cocineta, cowork y sala de juntas.
  - `sameAs` (YouTube) y `ReserveAction` hacia Cloudbeds.
- `WebSite` con `publisher` → hotel, y `BreadcrumbList` en las páginas internas.
- **No se incluyeron**, a propósito:
  - NIT y razón social: no se han suministrado.
  - Coordenadas: no están verificadas como dato propio.
  - `aggregateRating` y reseñas: son de Google y Booking.com. Marcar como propias reseñas de terceros va contra las directrices de Google.
  - Precios, rango de precios y horario de recepción: no son datos confirmados.
- No se creó un `Organization` aparte: `Hotel` ya es un tipo de organización, y duplicarlo sin razón social no aporta nada.
- Verificación recomendada: [Prueba de resultados enriquecidos](https://search.google.com/test/rich-results) una vez esté en producción.

## 9. Rendimiento y Core Web Vitals

- **No medido**: PSI agotó su cuota y aquí no hay Lighthouse. No se afirman cifras de LCP, INP ni CLS.
- Lo verificable:
  - La portada ya no carga Google Maps al abrir (antes eran un iframe y sus recursos desde `www.google.com`).
  - En la carga inicial, el único tercero que queda es Google Fonts (Karla).
  - Las escenas 2–6 del hero siguen cargándose después del evento `load`.
  - La imagen del primer pintado tiene `preload` y `fetchpriority="high"`.
  - Todas las imágenes declaran `width` y `height`, lo que previene saltos de diseño (CLS).
- Recomendado (pendiente de autorización):
  - **Alojar Karla localmente**, con licencia OFL: elimina dos conexiones a Google y la transferencia de la IP. Implica descargar los archivos `.woff2` de Karla del repositorio oficial de Google Fonts.
  - Medir en producción con PageSpeed Insights y el informe de Core Web Vitals de Search Console.

## 10. Accesibilidad (WCAG 2.2 AA)

Verificado:

- Enlace «Saltar al contenido» y foco visible (`:focus-visible`).
- El menú móvil abre, cierra con Esc, bloquea el fondo (`inert`) y atrapa el foco.
- Diálogo de preferencias nativo (`<dialog>` modal) que devuelve el foco al botón que lo abrió.
- Etiquetas en todos los campos. Los errores se anuncian con `role="status"`, se marcan con `aria-invalid` y el foco va al primer campo con error.
- Las 41 imágenes de la portada tienen `alt`, y las decorativas `alt=""`.
- Se respeta `prefers-reduced-motion` en la animación inicial, el hero y las animaciones de aparición.

Contraste medido automáticamente sobre el texto renderizado:

- Sin fallos reales en el texto de contenido.
- Los únicos avisos fueron falsos positivos (texto blanco sobre fotografía) y las **iniciales de los avatares** sobre terracota (3,95:1). Son decorativas (`aria-hidden`, el nombre aparece al lado), así que no se cambiaron para respetar la paleta.

**Riesgo que debe decidir el cliente:** el hero en bucle no tiene botón de pausa, por decisión expresa del cliente. WCAG 2.2.2 («Pausar, detener, ocultar») pide un mecanismo de pausa para el movimiento automático de más de 5 segundos. Hoy se mitiga desactivándolo con `prefers-reduced-motion`. Para cumplir AA del todo haría falta un pequeño control de pausa.

## 11. Seguridad

En el código:

- CSP en `<meta>`: `default-src 'self'`, scripts solo propios más el hash del script en línea del `<head>`, `frame-src https://www.google.com` (mapa), `object-src 'none'`, `base-uri 'self'`, `form-action 'self'` y `upgrade-insecure-requests`. `style-src` admite `'unsafe-inline'` por los atributos `style` del hero (variables CSS).
- `referrer: strict-origin-when-cross-origin`. Los enlaces externos usan `rel="noopener"`.
- Sin `eval`, sin dependencias externas de JS y sin formularios que envíen datos a un servidor.
- **Hash del script en línea:** si se modifica el script del `<head>` de `index.html`, hay que recalcular el hash y actualizarlo en `tools/site_common.py`:

  ```bash
  python3 -c "import re,hashlib,base64;s=open('opcion-1-full/index.html').read();print(base64.b64encode(hashlib.sha256(re.search(r'<script>([\s\S]*?)</script>',s).group(1).encode()).digest()).decode())"
  ```

En el servidor (no se pueden poner desde el HTML; tarea del hosting):

- `Strict-Transport-Security: max-age=31536000; includeSubDomains`.
- `X-Content-Type-Options: nosniff`.
- `Content-Security-Policy` como cabecera, con `frame-ancestors 'self'` (en `<meta>` no funciona).
- `Permissions-Policy: camera=(), microphone=(), geolocation=()`.
- `Referrer-Policy`, caché larga para `/public/` y compresión (gzip o brotli).

## 12. Cookies y consentimiento

- **Por defecto no se carga nada opcional.** El mapa muestra un aviso con el botón «Cargar mapa» y la casilla desmarcada «Recordar mi elección».
- «Preferencias de cookies» aparece en el pie de **todas** las páginas y abre un diálogo:
  - Categoría «Necesarias», siempre activa.
  - Categoría «Mapas (Google Maps)», desmarcada por defecto.
  - Botones «Rechazar opcionales», «Guardar» y «Aceptar todas», con el mismo peso visual.
- Al retirar el consentimiento, el mapa se quita de la página. Las cookies que Google ya haya puesto no las puede borrar este sitio; la política lo explica.
- La elección se guarda en `localStorage` (`amari.consent`, 12 meses), **solo como preferencia del navegador**, nunca como registro oficial.
- **No se muestra un banner automático**, porque hoy el sitio no usa ninguna cookie opcional al cargar. Si en el futuro se añade analítica o publicidad:
  - Registrarla como categoría en `CATEGORIES` (en `consent.js`).
  - Cargar su script solo cuando `getConsent()[id] === true`.
  - Mostrar un banner en la primera visita.
- Cloudbeds, WhatsApp, Instagram y YouTube son solo enlaces: no cargan nada hasta que la persona hace clic.

## 13. Documentos legales

Las rutas son estables y llevan aviso de «Borrador para revisión», `noindex` y versión «v0.1 · 18-oct-2026»:

| ES | EN |
|---|---|
| `/terminos-y-condiciones/` | `/en/terms-and-conditions/` |
| `/politica-de-privacidad/` | `/en/privacy-policy/` |
| `/politica-de-cookies/` | `/en/cookie-policy/` |

- **Términos:**
  - Conservan literalmente el objetivo y el alcance del sitio actual, y remiten a las políticas de servicios, cancelación y pagos, que no se modificaron.
  - Añaden la identificación del prestador, la reserva a través del sitio (consulta ≠ reserva confirmada) y los PQR.
  - Añaden también protección de menores, propiedad intelectual y ley aplicable, con lo que falta marcado como «Pendiente».
- **Privacidad:** sigue el contenido mínimo del art. 13 del Decreto 1377 de 2013, compilado en el art. 2.2.2.25.3.1 del Decreto 1074 de 2015:
  - Responsable, tratamiento y finalidades por canal.
  - Derechos (art. 8 de la Ley 1581).
  - Área responsable y procedimiento: consultas en 10 + 5 días hábiles y reclamos en 15 + 8 días hábiles (arts. 14 y 15).
  - Vigencia.
- **Cookies:** describe con exactitud lo que usa el sitio (sección 12).

## 14. Formulario de contacto y aceptaciones

- Tres casillas **independientes y desmarcadas**:
  1. «Acepto los [Términos y Condiciones]», con enlace.
  2. «He leído la [Política de Privacidad]», con enlace.
  3. Una **autorización de tratamiento de datos separada**, que indica qué datos se tratan y para qué.
- El envío se bloquea mientras falte cualquiera de las tres, y el mensaje de error dice cuáles.
- No se envía nada a un servidor: se abre el correo de la persona con el mensaje y, al final, una **constancia de aceptación** con:
  - El identificador del formulario.
  - La fecha y hora ISO 8601 con zona Colombia (`-05:00`).
  - La versión de los documentos y la página de origen.
- El formulario de consulta por WhatsApp abre la app con el mensaje; la persona decide si lo envía. Se recomienda que el hotel tenga un aviso de privacidad en su respuesta automática de WhatsApp Business.

## 15. Registro de aceptaciones: arquitectura

- **Hoy:** la constancia viaja dentro del propio correo que recibe el hotel. Así queda la evidencia en el buzón `atencionalcliente@`, con el valor probatorio de los mensajes de datos de la Ley 527 de 1999. El sitio no guarda identidad ni datos.
- **Si se necesita un registro centralizado** (recomendable si aumenta el volumen):
  - Un endpoint propio, por ejemplo una función serverless o un formulario del hosting, que guarde: id de formulario, hash del texto aceptado, versión, fecha y hora del servidor, IP truncada o en hash y user-agent.
  - Tabla de solo inserción, retención definida en la política y acceso restringido.
  - **No se implementó**, porque requiere backend, base de datos y la decisión del hotel.

## 16. Derechos de imágenes y tipografías

Inventario completo: `docs/inventario-imagenes.csv` (80 archivos base).

| Clase | Significado | Archivos |
|---|---|---|
| 1 | Material del cliente (manual de marca) | 3 (logos y favicon) |
| 2 | Publicado por el hotel en su web oficial; autor o licencia sin documentar | 69 fotos del hotel, más `og-image` e IvyMode |
| 3 | Tercero con licencia libre verificada y atribución | 8 fotos de Barranquilla (Wikimedia Commons: CC BY-SA 4.0, CC0, dominio público). Ahora con enlace a la licencia |
| 4 | Origen desconocido, no usar | 0 |

Acciones:

- Pedir al hotel una confirmación escrita de la titularidad o licencia de las fotos, en particular la cesión de derechos patrimoniales del fotógrafo (Ley 23 de 1982).
- Confirmar que la licencia de **IvyMode** cubre su uso web en el nuevo hosting. El archivo viene del sitio actual; si no está cubierto, usar el kit de Adobe Fonts del cliente (`config.adobeFontsKitId`).
- Karla: SIL Open Font License, sin restricción.
- Las dos imágenes de referencia de ChatGPT **no se usan** en el sitio.

## 17. Revisión normativa colombiana

| Norma | Qué exige (resumen) | Estado en el sitio |
|---|---|---|
| Ley 1581 de 2012 (habeas data) | Autorización previa, expresa e informada (art. 9); deber de informar (art. 12); derechos (art. 8); consultas y reclamos (arts. 14 y 15) | Autorización separada en el formulario; política con derechos y plazos. **Falta**: datos del responsable, área PQR, encargados y vigencia |
| Decreto 1377 de 2013 (DUR 1074/2015) | Contenido mínimo de la política (art. 13); aviso de privacidad (arts. 14 y 15); el silencio no es autorización (art. 7) | Estructura completa con «Pendientes». Casillas desmarcadas |
| SIC: cookies | La SIC ha aplicado la Ley 1581 a las cookies que recogen datos en Colombia (casos Google y TikTok) | El contenido de terceros solo se carga con consentimiento |
| Ley 1480 de 2011 (consumidor), art. 50 | Identificación del proveedor (razón social, NIT, notificación judicial), precio total con impuestos, condiciones accesibles, PQR | Sección de identificación con «Pendientes». La transacción ocurre en Cloudbeds |
| Ley 1480, arts. 47 y 51 | Retracto (5 días hábiles en servicios, con excepciones) y reversión del pago | **Riesgo a revisar con el abogado:** las tarifas no reembolsables frente al retracto en ventas a distancia. Se marcó como pendiente, sin conclusión |
| Ley 527 de 1999 | Valor de los mensajes de datos | Constancia de aceptación en el correo (sección 15) |
| Ley 23 de 1982 (derechos de autor) | Autorización del autor | Inventario (sección 16) |
| Ley 1558 de 2012, art. 30 (según el MinCIT) y Ley 2068 de 2020 | Inscripción en el RNT antes de operar; el número del RNT debe ir en toda la publicidad; actualización anual | **Pendiente:** número de RNT. Se recomienda mostrarlo en el pie cuando se reciba |
| Ley 679 de 2001, Ley 1336 de 2009 y Res. MinCIT 3840 de 2009 | Código de conducta contra la ESCNNA, adhesión requerida para el RNT y difusión de la prevención | Sección en los términos con «Pendiente»: texto del código adoptado |
| Ley 1335 de 2009 (antitabaco) | — | Ya está en la política de servicios (sin cambios) |

Fuentes consultadas:

- [Ley 1581 de 2012 (normograma Cancillería)](https://cancilleria.gov.co/sites/default/files/Normograma/docs/ley_1581_2012.htm)
- [Decreto 1377 de 2013 (normograma Cancillería)](https://cancilleria.gov.co/sites/default/files/Normograma/docs/decreto_1377_2013.htm)
- [Decreto 1377 de 2013 (Función Pública)](https://www1.funcionpublica.gov.co/eva/gestornormativo/norma.php?i=53646)
- [Ley 1480 de 2011 (normograma Cancillería)](https://cancilleria.gov.co/sites/default/files/Normograma/docs/ley_1480_2011.htm)
- [MinCIT: qué es el RNT](https://www.mincit.gov.co/minturismo/analisis-sectorial-y-promocion/registro-nacional-de-turismo/que-es-el-registro-nacional-de-turismo)
- [Ley 1336 de 2009 (Función Pública)](https://www1.funcionpublica.gov.co/eva/gestornormativo/norma.php?i=36877)
- [Resolución 3840 de 2009 (Función Pública)](https://www1.funcionpublica.gov.co/eva/gestornormativo/norma.php?i=38492)
- [SIC: orden a TikTok sobre datos y cookies](https://sedeelectronica.sic.gov.co/international-relations/sic-orders-tiktok-comply-colombian-data-protection-standard)
- [Comunicado de la Corte sobre retracto, Sentencia C-192/26 (JEP normograma)](https://jurinfo.jep.gov.co/Normograma/compilacion/docs/C-192_2026.htm)

> Atención a la vigencia: la Ley 2439 de 2024 modificó los arts. 47 y 50 de la Ley 1480, y la Sentencia C-192/26 se refiere al plazo de devolución en el retracto. El abogado debe confirmar el texto vigente antes de redactar la cláusula de retracto.

## 18. SEO local

- NAP coherente en todo el sitio: «Amari Living Suites · Carrera 42F #76-41, Barranquilla · +57 302 330 7939 / +57 605 313 3460».
- Debe coincidir exactamente con el **Perfil de Empresa de Google** (hoy 4,6 ★ con 61 reseñas, consultado el 18-oct-2026), Booking.com y las redes sociales.
- Recomendaciones para el hotel:
  - Verificar la categoría «Hotel» en el Perfil de Empresa, el enlace al sitio y la URL de reservas de Cloudbeds.
  - Subir fotos actuales y responder las reseñas.
  - Mantener la sección «Conoce Barranquilla», que da relevancia local.

## 19. Pruebas de reservas y WhatsApp

- Formulario rápido del hero y formulario de reserva: validan, abren `wa.me/573023307939` con el mensaje (ES o EN según la página) y avisan de que la reserva aún no está confirmada. Probado a 375 px y a 1440 px.
- Todos los enlaces de WhatsApp tienen ahora `href` real sin JS. Restaurante (Full): `wa.me/573004272643`. Lavandería: pendiente, sin enlace ficticio. Sencilla: sin botones individuales de aliados, como pidió el brief.
- Cloudbeds: la URL exacta no se tocó.
- **No se hizo ninguna reserva real en Cloudbeds ni se envió ningún mensaje.** Se recomienda que el hotel haga una reserva de prueba y la cancele, y que confirme qué número recibe los mensajes de WhatsApp.

## 20. Search Console y analítica

Search Console (cuando el sitio esté en producción):

1. Agregar la propiedad de **dominio** `amarilivingsuite.com`, con verificación por registro TXT en el DNS (lo hace quien administre el DNS).
2. Enviar `https://amarilivingsuite.com/sitemap.xml` en Sitemaps.
3. Usar Inspección de URLs en `/` y `/en/` y pedir la indexación.
4. Revisar los informes de Páginas, Core Web Vitals y HTTPS a las 2–4 semanas, y los 404 de las URLs antiguas para completar las 301.

Analítica (si se decide usarla):

- Elegir una herramienta y añadirla **solo detrás del consentimiento** (sección 12).
- Actualizar la política de cookies con el nombre, la finalidad, la duración y el proveedor.
- Si se quiere medir sin cookies, existen alternativas sin identificadores. Aun así, hay que declararlas en la política.

## 21. Pruebas realizadas y resultados

| Prueba | Resultado |
|---|---|
| W3C Nu, 20 páginas | **0 errores** (antes: ~22 en la portada Full) |
| Enlaces internos y recursos (888 referencias, incluidos `srcset` y anclas) | 0 rotos |
| CSP en el navegador (escucha de `securitypolicyviolation`) | 0 violaciones. Las clases `js`, `splash-done` e `is-ready` se aplican: el script en línea con hash se ejecuta |
| Consola | Sin errores. Solo el aviso esperado de la lavandería, cuyo número está pendiente |
| Carga inicial | Sin iframes, sin cookies y sin `www.google.com`. Terceros: solo Google Fonts |
| Mapa | No se carga sin acción. «Cargar mapa» lo inserta; «Recordar» lo persiste; «Rechazar» lo quita; «Aceptar» lo restaura al recargar |
| Formulario | Casillas desmarcadas; bloqueo con mensaje claro; constancia con hora `-05:00` y versión en el cuerpo del correo |
| Geometría Full a 1440 px | Posición y alto idénticos en todas las secciones hasta Ubicación. Ubicación +86 px (casillas); Reserva solo se desplaza; pie +75 px (enlaces legales) |
| Geometría Sencilla a 375 px | Idéntica. Ubicación +89 px y pie +75 px. Sin desborde horizontal (`scrollWidth` = 375) |
| Móvil (Sencilla) | Reserva por WhatsApp visible y funcionando; el menú abre y cierra; 0 imágenes rotas |
| Versión EN | Canónica `/en/`, mensajes en inglés, rutas legales EN y casillas traducidas |

## 22. Priorización

| Prioridad | Tarea | Responsable |
|---|---|---|
| Alta | Entregar los datos legales: razón social, NIT, RNT, dirección de notificación judicial, área PQR, encargados y vigencia | Hotel |
| Alta | Revisión jurídica y aprobación de los 3 documentos, y quitar `noindex` al aprobarlos | Hotel + abogado |
| Alta | Definir la cláusula de retracto frente a las tarifas no reembolsables | Abogado |
| Alta | Confirmar los derechos de las fotos y la licencia de IvyMode | Hotel |
| Media | Autorizar que Karla se aloje localmente (quita Google Fonts) | Cliente → equipo web |
| Media | Cabeceras de seguridad y 301 de URLs antiguas en el hosting de producción | Hosting |
| Media | Search Console y sitemap (sección 20) | Quien administre el DNS |
| Media | Decidir si el hero lleva control de pausa (WCAG 2.2.2) | Cliente |
| Baja | Número de RNT en el pie, número de WhatsApp de la lavandería y tarifas por hora | Hotel |
| Baja | Registro centralizado de aceptaciones (sección 15) | Hotel → equipo web |

## 23. Datos que debe entregar el hotel y próximos pasos

1. Razón social, NIT y dirección de notificación judicial.
2. Número de RNT vigente y texto del código de conducta contra la ESCNNA adoptado.
3. Área o cargo que atiende datos personales y PQR, y plazo de respuesta a PQR.
4. Datos que el hotel recibe de Cloudbeds y del registro de huéspedes, con sus finalidades.
5. Proveedores que tratan datos (hosting, correo, Cloudbeds, WhatsApp Business) y si hay transferencias internacionales.
6. Medidas de seguridad de sus bases de datos y período de vigencia de las bases.
7. Si las tarifas publicadas incluyen impuestos.
8. Confirmación escrita sobre los derechos de las fotografías y sobre la licencia de IvyMode.
9. Fecha de entrada en vigencia de los documentos, tras la revisión jurídica.
10. Si el hotel está obligado a inscribir sus bases en el Registro Nacional de Bases de Datos (RNBD) de la SIC. Debe confirmarlo con su abogado.

**Publicación:** los cambios están confirmados en un commit local. **No se han subido a GitHub ni publicado** en espera de autorización.
