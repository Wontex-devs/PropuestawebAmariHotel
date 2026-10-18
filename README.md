# Amari Living Suites: rediseño web

Hay dos versiones independientes del sitio de Amari Living Suites (Barranquilla). Las dos parten de la misma información real y de la identidad oficial del manual de marca.

| Carpeta | Versión | Puerto |
|---|---|---|
| `opcion-1-full/` | **Full Experience**: inmersiva, con animaciones cuidadas | 5173 |
| `opcion-2-sencilla/` | **Sencilla**: sobria, rápida y con movimiento mínimo | 5174 |
| `recursos-marca/logos/` | Logotipo e ícono oficiales en PNG transparente, en las 5 variantes del manual | — |
| `contenido compartido por el clienet/` | Archivos originales del cliente (no se modificaron) | — |

## Ejecutar

Ninguna de las dos versiones tiene dependencias ni necesita compilarse: están hechas con HTML, CSS y JavaScript nativos (módulos ES). Cada una se ejecuta sola.

Con Node 18 o superior:

```bash
cd "opcion-1-full" && npm start
```

```bash
cd "opcion-2-sencilla" && npm start
```

Sin Node (Python 3 viene incluido en macOS):

```bash
cd "opcion-1-full" && python3 -m http.server 5173
```

```bash
cd "opcion-2-sencilla" && python3 -m http.server 5174
```

Después abre http://localhost:5173 (Full) o http://localhost:5174 (Sencilla).

> Hace falta un servidor local porque el JavaScript se carga como módulo. Si abres `index.html` con doble clic, los botones no reciben sus enlaces.

### ¿Por qué no se usó React ni Vite?
Este equipo no tiene Node.js instalado. En lugar de instalar herramientas en el sistema, se eligió una base sin dependencias, que tiene sentido para un sitio de una sola página:
- No hay `npm install`, ni compilación, ni paquetes que actualizar.
- Carga rápida: no se descarga ningún framework, solo JS propio: unos 24 KB en Full y 19 KB en Sencilla, sin comprimir.
- Se publica tal cual en cualquier hosting estático (Netlify, Vercel, cPanel, S3…).
- Las animaciones de la versión Full se escribieron a mano (IntersectionObserver y transiciones CSS), sin GSAP.

## Diferencias entre versiones

| | Full | Sencilla |
|---|---|---|
| Animación de inicio (logo) | Sí: la "A" aparece sola y la palabra se desenrolla horizontalmente | Sí: la misma animación |
| Hero | Reel a pantalla completa con entrada cinematográfica (zoom y títulos línea por línea) | Reel a pantalla completa, sin entrada cinematográfica |
| Encabezado | Transparente sobre la foto; se vuelve sólido al bajar. Indicador animado de sección | Igual comportamiento y mismo botón "Reservar ahora". La sección activa se marca con subrayado |
| Desplazamiento | Revelados, cortinas en las imágenes, parallax sutil, apariciones escalonadas, contador del 10 % | Sin animaciones de desplazamiento |
| Suites y servicios | Rejilla asimétrica y editorial | Rejillas regulares |
| Cowork / sala de juntas | Dentro de Servicios: panel negro con íconos que se dibujan | Dentro de Servicios: panel claro en verde salvia |
| Menú móvil | Cortina con enlaces escalonados | Fundido breve de opacidad |
| **WhatsApp de aliados** | **Sí**: un botón para el restaurante-café y otro para la lavandería | **No**: se mantienen los negocios, sus descripciones y el 10 % |

**Hero tipo video (las dos versiones):** es un reel con 6 fotos reales del hotel (Premium Suite, sala común, recepción, Junior Suite, acceso principal y edificio). Cada escena dura 4 s con un movimiento lento de cámara, y entre una y otra hay un fundido. Corre en bucle continuo. No es un video: no tiene controles y no se puede pausar, arrastrar ni seleccionar. Está hecho 100 % con CSS (`src/styles/hero-reel.css`), y las fotos 2 a 6 se cargan después de la primera para no hacer más lenta la carga inicial. Si alguien pidió reducir el movimiento en su dispositivo, solo ve la primera foto, fija. Para cambiar las fotos, edita los bloques `hero-reel__slide` en `index.html`.

Las dos versiones abren con una animación del logotipo oficial (unos 2 s; se salta con un clic, Enter o Escape y no se muestra si el usuario pidió reducir el movimiento). Los archivos son `src/styles/intro.css` y `src/js/intro.js`. Se arma con capas recortadas de la misma imagen del logo, así que el resultado final es el logotipo exacto, sin redibujar.

Las dos versiones incluyen: reserva en Cloudbeds, WhatsApp de Amari (botones y formulario de consulta), suites, servicios, aliados con 10 %, cowork y sala de juntas con WhatsApp, información útil (políticas), ubicación con mapa y contacto. También respetan `prefers-reduced-motion`.

## Contenido de la web actual incluido

Se revisaron todas las páginas de amarilivingsuite.com, una por una: inicio, habitaciones, las tres páginas de suites, Conoce Barranquilla, Sobre nosotros, galería, contacto, políticas y la versión en inglés. Todo su contenido está en el nuevo sitio:

| En la web actual | En el nuevo sitio |
|---|---|
| Habitaciones y páginas de cada suite | Sección **Suites**: Premium (con la foto de su página), Junior y Superior, con sus datos reales |
| Sobre nosotros | Sección de experiencia, con el texto oficial ("Buscamos que la estadía de cada persona sea un regalo…") |
| Galería (≈ 45 fotos) | **Galería completa**: las 45 fotos, con visor ampliable (teclado, flechas y deslizar en celular) |
| Conoce Barranquilla | Nueva sección con **8 sitios**: Gran Malecón, Luna del Río, Ventana de Campeones ("Aleta del Tiburón"), Ventana al Mundo, Museo del Carnaval, Ciénaga de Mallorquín, Museo del Caribe y Catedral. Cada uno con foto, ubicación y enlace "Cómo llegar". Se quitó el Bordillo de Shakira |
| Reseñas (6, en 2 páginas) | Las **6 reseñas reales** con sus nombres, títulos y 5 estrellas (verificadas), más el distintivo real de Google: **4,6 con 61 reseñas** |
| Formulario de contacto | **Formulario de contacto** (nombre, correo, mensaje y aceptación de datos). Abre el correo del visitante con el mensaje listo para enviar |
| Políticas (cancelación, pagos, servicios, términos, privacidad) | **`politicas.html`**: página propia con el texto completo, índice y enlaces desde el pie de página |
| Datos de la Política de servicios | Comodidades confirmadas: Wi‑Fi de cortesía, parqueadero sin costo (1 vehículo por suite, sujeto a disponibilidad), caja de seguridad en cada suite, late check-out sin costo hasta la 1 p. m., espacios libres de humo y tarjetas aceptadas |
| Selector de idioma ES/EN | **Selector ES / EN** en el encabezado, el menú móvil y el pie de página, con versión completa en inglés en `en/` |
| Canal de YouTube | Enlace "Síguenos · YouTube" en el pie de página. El video no se incluyó como sección, porque el hero tipo reel ya cumple esa función |
| Tipografías de la web actual | **IvyMode** oficial, tomada de los archivos de la web actual (`public/fonts/ivymode-regular.woff`) |

No se incluyó el crédito "Designed by 360Webmasters.com", que corresponde al diseño anterior.

## Idiomas (ES / EN)

- **Español:** `index.html`, `politicas.html` y los documentos legales (`terminos-y-condiciones/`, `politica-de-privacidad/`, `politica-de-cookies/`). **Inglés:** los equivalentes dentro de `en/`. Cada versión (Full y Sencilla) tiene los suyos.
- **Traducción:** se tradujo a mano. Donde la web actual tenía textos oficiales en inglés (habitaciones, Sobre nosotros, Conoce Barranquilla), se usaron como base.
- **Textos generados por JavaScript:** los mensajes de WhatsApp, los errores de los formularios, las fechas y las etiquetas del visor salen en el idioma de la página. Los mensajes de WhatsApp en inglés están en `config.js` → `messages.en`.
- **Reseñas:** se muestran en su idioma original (inglés, español o portugués), marcadas con su idioma para los lectores de pantalla.
- **Si cambias un texto en español:** regenera las páginas en inglés con los scripts de `tools/` (ver `tools/README.md`). No edites a mano los archivos de `en/`.

## Dónde se configuran los datos

En cada versión, **todo** está en `src/js/config.js`. Hay que editarlo en las dos carpetas:

- **Teléfonos y WhatsApp** → `contact.amariWhatsApp`, `contact.phoneMobile`, `contact.phoneLandline`
- **WhatsApp de los aliados** → `allies.restaurant.whatsapp`, `allies.laundry.whatsapp` (formato `57XXXXXXXXXX`)
- **Nombres de los aliados** → `allies.restaurant.name`, `allies.laundry.name`
- **Tarifas por hora** → `rates.coworkHourlyRate`, `rates.meetingRoomHourlyRate` (número entero en COP; por ejemplo, `45000` se muestra como "$45.000 COP / hora")
- **Moneda** → `rates.currency`
- **Cloudbeds** → `bookingUrl`. No debe cambiarse. El HTML también trae esa misma URL como respaldo por si JavaScript no carga.
- **Políticas y documentos legales (textos)** → `tools/build_policies.py` y `tools/build_legal.py` (generan las páginas ES/EN)
- **Versión de los documentos legales** (se cita en la constancia del formulario) → `legal.version`

## Identidad visual (manual de marca)

- **Logotipo**: se extrajo directamente de `logo amari.ai.pdf`, sin redibujarlo, con fondo transparente. Las variantes de color corresponden a las de la pág. 16 del manual.
- **Colores** (pág. 14): `#F1A622` dorado, `#C5635B` terracota, `#B0C7BA` salvia y `#000000` negro, más tintes de esas mismas escalas. Están en `src/styles/tokens.css`.
- **Tipografía** (pág. 15): **Karla** para los textos (Google Fonts, licencia OFL) e **IvyMode** para los titulares. El archivo de IvyMode se tomó de la web actual del cliente.
- **Recursos gráficos**: énfasis en itálica dentro de los titulares, títulos pequeños en mayúsculas con espaciado amplio y el ícono "Λ". Todo esto sale de las piezas del propio manual.
- **Textos**: el hero muestra solo el logotipo oficial, sin eslogan. No se usó ningún texto de las imágenes de referencia.
- **Referencias de ChatGPT**: se usaron solo para la composición: encabezado, hero con logo centrado, barra de reserva superpuesta, franja de 5 íconos, bloques de texto e imagen alternados y la tarjeta "Haz tu reserva". No se copiaron su logo, su verde ni su tipografía.

## Auditoría (18-oct-2026)

El informe completo de SEO, rendimiento, seguridad, privacidad y cumplimiento está en [`AUDITORIA.md`](AUDITORIA.md). Ahí están también los datos que debe entregar el hotel.

## ⏳ Pendiente de confirmar antes de publicar

1. **Licencia de IvyMode**: el archivo viene de la propia web del cliente. Conviene confirmar que su licencia web cubre el nuevo sitio.
2. **Restaurante-café**: ✅ confirmado en la versión Full: **Selah Bistró & Café**, WhatsApp +57 300 427 2643 e Instagram [@meetselah](https://www.instagram.com/meetselah/). Se configura en `opcion-1-full/src/js/config.js`. En la versión Sencilla sigue apareciendo como "Restaurante-café aliado". Si quieres el nombre también ahí, se cambia en su `config.js`.
3. **Lavandería**: falta su nombre y su WhatsApp, igual que con el restaurante-café.
4. **Tarifas de cowork y sala de juntas**: no están publicadas. Por ahora se muestra "Consulta la tarifa por hora".
5. **Fotos del cowork, la sala de juntas, el restaurante y la lavandería**: no existen fotos reales. Esas secciones usan bloques gráficos con los colores de la marca, no fotos de otros lugares.
6. **Detalles del cowork y la sala de juntas** (capacidad, equipamiento, horarios): no están documentados y no se inventaron.
7. **Condiciones del 10 %**: solo se publica el descuento.
8. **Documentos legales**: términos, privacidad y cookies ya tienen página propia, como **borradores con `noindex`**. Faltan los datos marcados como «Pendiente» y la revisión jurídica. Ver `AUDITORIA.md` (secciones 13, 17 y 23).
9. **Calificación de Google (4,6 / 61 reseñas)**: es el dato que mostraba el widget de la web actual el 18-oct-2026. Es un número fijo, así que conviene actualizarlo de vez en cuando.
10. **Fotos de Barranquilla**: vienen de Wikimedia Commons, con licencias CC BY-SA 4.0, CC0 o dominio público. Cada foto muestra su autor y su licencia, como exige la licencia. Si el cliente tiene fotos propias, se pueden reemplazar en `public/img/barranquilla/`.
11. **Dominio**: canónica, `hreflang`, Open Graph, `sitemap.xml` y `robots.txt` ya apuntan a `https://amarilivingsuite.com/`. Al publicar, sube **una** versión a la raíz del dominio.
12. **WhatsApp de Amari**: `+57 302 330 7939`, el número publicado en las políticas de la web actual. Conviene confirmar que sigue activo.

## Fuentes consultadas
- `contenido compartido por el clienet/Manual de marca amari final.pdf` (33 págs.): se revisaron el texto y las páginas visuales.
- `contenido compartido por el clienet/logo amari.ai.pdf` (4 variantes de color).
- Dos imágenes de referencia (WhatsApp, 17-oct-2026): la composición de escritorio y la tarjeta de reserva móvil.
- https://amarilivingsuite.com (todas las páginas del mapa del sitio, en español e inglés, y los widgets de reseñas propio y de Google). Las fotografías salen de la galería oficial de ese sitio.
- Sitios de Barranquilla: El Heraldo, El Universal, Infobae, Radio Nacional, Blu Radio y la oficina de turismo del Carnaval, para direcciones y datos. Fotos de Wikimedia Commons, con los créditos que aparecen en cada tarjeta.
