# Amari Living Suites: versión Full Experience

Es la versión inmersiva del sitio. Está hecha con HTML, CSS y JavaScript nativos y **no tiene dependencias**.

## Ejecutar
```bash
npm start
```
Abre http://localhost:5173. Requiere Node 18 o superior. Sin Node, se puede usar `python3 -m http.server 5173` desde esta carpeta.

## Estructura
```
index.html              Página principal en español (SEO, Open Graph, JSON-LD)
en/index.html           Página principal en inglés
politicas.html          Políticas completas (en/politicas.html en inglés)
public/img/             Fotografías reales del hotel (WebP); galeria/ = las 45 fotos; barranquilla/ = sitios (Wikimedia Commons)
public/brand/           Logotipo oficial (blanco y negro) extraído del PDF del cliente
public/favicon.png      Ícono "Λ" del manual
public/og-image.jpg     Imagen para compartir en redes
src/js/config.js        ★ Datos comerciales: teléfonos, WhatsApp, tarifas, aliados, Cloudbeds
src/js/main.js          Enlaces, formularios (WhatsApp y contacto), menú, galería con visor, textos ES/EN
src/js/motion.js        Animaciones (solo en Full)
src/styles/tokens.css   Colores, tipografía y espaciados del manual de marca
src/styles/base.css     Base, tipografía y botones
src/styles/components.css  Encabezado, menú móvil, campos, botones flotantes
src/styles/sections.css    Estilos de cada sección
src/styles/motion.css      Estados de animación (solo en Full)
src/styles/extras.css   Idioma, comodidades, galería, Barranquilla, reseñas, contacto
src/styles/policies.css Página de políticas
public/fonts/           IvyMode (tipografía oficial)
server.mjs              Servidor local sin dependencias
```

## Secciones
Inicio (hero y barra de consulta) · Lo esencial (5 íconos) · Experiencia (texto oficial de Sobre nosotros) · Suites (Premium, Junior y Superior, con sus detalles) · **Servicios** (4 servicios del hotel, fotos de los espacios comunes, panel de **cowork y sala de juntas** por horas con WhatsApp, y galería completa de 45 fotos con visor) · **Aliados Amari** (restaurante-café y lavandería, 10 %, con WhatsApp individual) · **Conoce Barranquilla** (8 sitios) · Opiniones (6 reseñas reales + calificación de Google) · Antes de llegar · Ubicación, contacto y formulario · Reserva tu suite · Pie de página con políticas, YouTube e idioma. Todo está también en inglés (`en/`).

## Animaciones
- **Animación de inicio con el logo** (`src/styles/intro.css` y `src/js/intro.js`): la "A" aparece sola en el centro. Luego se desliza a la izquierda y la palabra se desenrolla desde su borde con una línea de luz dorada, y cada letra se asienta con un leve desfase. Sigue un destello dorado, después "Living Suites" se abre desde el centro y por último la cortina negra sube. Se salta con un clic, Enter o Escape.
- **Hero tipo video:** reel en bucle de 6 fotos reales con movimiento lento de cámara y fundidos. Es solo CSS, sin controles y no se puede pausar (`src/styles/hero-reel.css`).
- Entrada del hero (empieza cuando sube la cortina del logo): todo el reel pasa de zoom a encuadre, aparece el logo y los titulares surgen línea por línea.
- El encabezado pasa de transparente a sólido y un indicador dorado sigue a la sección activa.
- Revelado de textos al bajar. Las imágenes se descubren con una cortina y una ligera escala.
- Parallax sutil en algunas fotos, solo mientras están en pantalla y con `requestAnimationFrame`.
- Apariciones escalonadas en los íconos, los datos y las opiniones. Los aliados entran por lados opuestos y el 10 % se cuenta hacia arriba.
- Los íconos de cowork y sala de juntas se dibujan con su trazo.
- Botones con relleno animado y flecha deslizante. Hover refinado en tarjetas y galería.
- El menú móvil se abre como cortina y sus enlaces aparecen escalonados.
- En móvil, la barra inferior de reservar se ve siempre. No hay botón flotante de WhatsApp: el contacto está en la barra de consulta, la sección de ubicación, la tarjeta de reserva y el menú.

Solo se animan `transform`, `opacity` y `clip-path`. No hay scroll forzado. Con `prefers-reduced-motion` no se ejecuta ninguna animación y todo el contenido es visible desde el inicio, igual que si JavaScript no carga.

## Mantenimiento
- **Teléfonos, tarifas y aliados**: solo en `src/js/config.js`. Mientras un número de aliado esté en `null`, su botón aparece como "por confirmar" y no lleva enlace.
- **Cambiar fotos**: reemplaza los archivos en `public/img/` con el mismo nombre, o actualiza `src` y `srcset` en `index.html`.
- **IvyMode**: pon el ID del kit de Adobe Fonts en `adobeFontsKitId`.

Los datos pendientes están en el `README.md` de la carpeta principal.
