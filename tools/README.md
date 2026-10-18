# Herramientas de generación (Python 3, sin dependencias)

Ejecutar desde la carpeta `AMARI HOTEL/`, para cada versión:

```bash
python3 tools/build_policies.py opcion-1-full   # politicas.html y en/politicas.html
python3 tools/build_legal.py opcion-1-full      # términos, privacidad y cookies (ES/EN)
python3 tools/build_en.py opcion-1-full         # en/index.html a partir de index.html
```

Repetir con `opcion-2-sencilla`. Regla: **se edita siempre la página en español** (`index.html`)
o los textos de estos scripts; las páginas en inglés se regeneran, no se editan a mano.

- `build_en.py` avisa con `SIN TRADUCIR:` los textos nuevos que no estén en su diccionario
  (los nombres propios y las reseñas en su idioma original son esperados).
- `site_common.py` contiene la CSP y el hash SHA-256 del script en línea del `<head>`.
  Si se modifica ese script, recalcular el hash (ver `AUDITORIA.md`, sección 11).
- `validate.py <salida.json>` envía cada página al validador W3C (validator.w3.org/nu).
