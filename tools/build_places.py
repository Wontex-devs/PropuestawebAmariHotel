"""Galerías de «Conoce Barranquilla»: una galería con flechas por lugar.
Uso: python3 tools/build_places.py <carpeta-proyecto>
Lee docs/fotos-barranquilla.json (autor, licencia y página de cada foto:
Wikimedia Commons, Pexels o Unsplash) y reescribe el bloque <figure class="place__media"> o
<div class="place__media place-gallery"> de cada tarjeta en index.html (ES).
"""
import sys, os, re, json, html

P = sys.argv[1]
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = json.load(open(os.path.join(ROOT, 'docs', 'fotos-barranquilla.json'), encoding='utf-8'))
ORDER = ['malecon', 'luna', 'campeones', 'ventana', 'carnaval', 'mallorquin', 'puertomocho', 'caribe', 'catedral']

def credit(it):
    """Crédito visible: autor (enlace a la página de la foto) · licencia (enlace)."""
    a = f'<a href="{html.escape(it["page"])}" target="_blank" rel="noopener">{html.escape(it["artist"])}</a>'
    source = it.get('source', 'Wikimedia Commons')
    lic_text = {'Pexels': 'Pexels', 'Unsplash': 'Unsplash'}.get(source, it['license'])
    if it['licenseUrl']:
        lic = f'<a href="{html.escape(it["licenseUrl"])}" target="_blank" rel="noopener license">{html.escape(lic_text)}</a>'
    else:
        lic = 'Dominio público'
    return f'<figcaption class="place__credit">Foto: {a} · {lic}</figcaption>'

def pos(it):
    """Encuadre opcional de la foto («pos» en el JSON, p. ej. "80% 50%")."""
    return f' style="object-position: {it["pos"]}"' if it.get('pos') else ''

def gallery(slug, name):
    items = DATA[slug]['photos']
    slides = '\n'.join(
        f'''                  <figure class="place-gallery__slide">
                    <img src="public/img/barranquilla/{it["file"]}" alt="{html.escape(it["alt"])}" width="{it["w"]}" height="{it["h"]}"{pos(it)} loading="lazy" decoding="async" />
                    {credit(it)}
                  </figure>''' for it in items)
    if len(items) == 1:
        return f'''<div class="place__media place-gallery">
                <div class="place-gallery__track">
{slides}
                </div>
              </div>'''
    return f'''<div class="place__media place-gallery" data-place-gallery>
                <div class="place-gallery__track" data-place-track tabindex="0" role="region" aria-label="Fotos de {html.escape(name)}">
{slides}
                </div>
                <button class="place-gallery__btn place-gallery__btn--prev" type="button" data-place-prev aria-label="Fotografía anterior" disabled><svg class="icon" aria-hidden="true"><use href="#i-arrow-left" /></svg></button>
                <button class="place-gallery__btn place-gallery__btn--next" type="button" data-place-next aria-label="Fotografía siguiente"><svg class="icon" aria-hidden="true"><use href="#i-arrow" /></svg></button>
                <span class="place-gallery__count" aria-hidden="true" data-place-count>1 / {len(items)}</span>
              </div>'''

f = os.path.join(P, 'index.html')
s = open(f, encoding='utf-8').read()
blocks = list(re.finditer(r'<figure class="place__media">[\s\S]*?</figure>|<div class="place__media place-gallery"[\s\S]*?\n              </div>', s))
names = re.findall(r'place__name">([^<]*)', s)
assert len(blocks) == len(ORDER) == len(names), (len(blocks), len(names))
for m, slug, name in reversed(list(zip(blocks, ORDER, names))):
    s = s[:m.start()] + gallery(slug, html.unescape(name)) + s[m.end():]
open(f, 'w', encoding='utf-8').write(s)
print(P, 'galerías de Barranquilla actualizadas')
