# Amari Living Suites: versión Sencilla

Es la versión sobria, directa y rápida. Comparte identidad, contenido y funciones esenciales con la versión Full, pero casi no tiene movimiento. Está hecha con HTML, CSS y JavaScript nativos y **no tiene dependencias**.

## Ejecutar
```bash
npm start
```
Abre http://localhost:5174. Requiere Node 18 o superior. Sin Node, se puede usar `python3 -m http.server 5174` desde esta carpeta.

## Estructura
```
index.html              Página principal en español (SEO, Open Graph, JSON-LD)
en/index.html           Página principal en inglés
politicas.html          Políticas completas (en/politicas.html en inglés)
public/img/             Fotografías reales del hotel (WebP); galeria/ = las 45 fotos; barranquilla/ = sitios (Wikimedia Commons)
public/brand/           Logotipo oficial (blanco y negro)
src/js/config.js        ★ Datos comerciales: teléfonos, WhatsApp, tarifas, aliados, Cloudbeds
src/js/main.js          Enlaces, formularios (WhatsApp y contacto), menú, galería con visor, textos ES/EN
src/styles/tokens.css   Colores y tipografía del manual de marca
src/styles/base.css · components.css · sections.css   Estilos compartidos
src/styles/simple.css   Ajustes propios de esta versión (hero enmarcado, rejillas regulares)
src/styles/extras.css   Idioma, comodidades, galería, Barranquilla, reseñas, contacto
src/styles/policies.css Página de políticas
public/fonts/           IvyMode (tipografía oficial)
server.mjs              Servidor local sin dependencias
```

## Animación de inicio
Comparte con la versión Full la animación del logotipo (`src/styles/intro.css` y `src/js/intro.js`): la "A" aparece sola y el resto de la palabra se desenrolla horizontalmente. Es la única animación elaborada de esta versión.

## Qué la diferencia de la versión Full
- Sin entrada cinematográfica del hero, sin parallax, sin revelados al bajar y sin apariciones escalonadas.
- El encabezado y el botón "Reservar ahora" funcionan igual que en la Full: son transparentes sobre el hero y se vuelven sólidos al bajar, solo con cambio de color. El hero ocupa la pantalla completa con el mismo reel tipo video de la Full (6 fotos en bucle, sin controles), pero sin la entrada cinematográfica.
- Rejillas regulares para suites y servicios.
- Solo hay movimiento funcional: cambios de color en botones, apertura del menú móvil por opacidad (200 ms) y desplazamiento suave hacia las secciones.
- **Aliados (restaurante-café y lavandería)**: se mantienen la sección, las descripciones y el **10 % de descuento**, pero **no hay botones individuales de WhatsApp**. En `config.js` está definido `features.allyWhatsAppButtons: false`.

## Incluye
Reserva en Cloudbeds · WhatsApp de Amari (botones, barra móvil y formulario de consulta) · suites · servicios · aliados con 10 % · cowork y sala de juntas con su WhatsApp y tarifa por hora configurable · políticas · ubicación con mapa · contacto.

## Mantenimiento
Todos los datos se editan en `src/js/config.js`. Los datos pendientes están en el `README.md` de la carpeta principal.
