"""Piezas comunes de las páginas secundarias (políticas y documentos legales)."""
import json, html

BASE = 'https://amarilivingsuite.com/'
# Hash SHA-256 del script en línea del <head> de index.html (clase .js / no-splash).
# Si ese script cambia, hay que recalcular el hash (ver AUDITORIA.md §9).
INLINE_HASH = "'sha256-sEbc6UqGsZQyK3BfL7TqWzgOfJC9F9mRGzhoEtkxyHU='"

def csp(inline_script=False):
    script = "'self'" + (' ' + INLINE_HASH if inline_script else '')
    return (
        "default-src 'self'; "
        f"script-src {script}; "
        "style-src 'self' 'unsafe-inline'; "
        "font-src 'self'; "
        "img-src 'self' data:; "
        "frame-src https://www.google.com; "
        "connect-src 'self'; "
        "object-src 'none'; "
        "base-uri 'self'; "
        "form-action 'self'; "
        "upgrade-insecure-requests"
    )

# Rutas por idioma, relativas a la raíz del sitio
ROUTES = {
    'home': {'es': '', 'en': 'en/'},
    'policies': {'es': 'politicas.html', 'en': 'en/politicas.html'},
    'terms': {'es': 'terminos-y-condiciones/', 'en': 'en/terms-and-conditions/'},
    'privacy': {'es': 'politica-de-privacidad/', 'en': 'en/privacy-policy/'},
    'cookies': {'es': 'politica-de-cookies/', 'en': 'en/cookie-policy/'},
}

LABELS = {
    'es': {
        'cancel': 'Política de cancelación', 'pay': 'Política de pagos', 'serv': 'Política de servicios',
        'terms': 'Términos y condiciones', 'privacy': 'Política de privacidad', 'cookies': 'Política de cookies',
        'prefs': 'Preferencias de cookies', 'home': 'Inicio', 'policies': 'Políticas', 'legal': 'Información legal',
    },
    'en': {
        'cancel': 'Cancellation policy', 'pay': 'Payment policy', 'serv': 'Service policy',
        'terms': 'Terms and conditions', 'privacy': 'Privacy policy', 'cookies': 'Cookie policy',
        'prefs': 'Cookie preferences', 'home': 'Home', 'policies': 'Policies', 'legal': 'Legal information',
    },
}

def rel(from_route, to_route):
    """Ruta relativa entre dos rutas del sitio (p. ej. 'en/privacy-policy/' → '../politicas.html')."""
    import posixpath
    frag = ''
    if '#' in to_route:
        to_route, frag = to_route.split('#', 1)
        frag = '#' + frag
    from_dir = from_route.rsplit('/', 1)[0] if '/' in from_route else ''
    if to_route == from_route and frag:
        return frag
    target = to_route or '.'
    r = posixpath.relpath(target, from_dir or '.')
    if to_route.endswith('/') or to_route == '':
        r = r.rstrip('/') + '/'
        if r == './' and from_dir == (to_route.rstrip('/')):
            r = './'
    if r == './':
        pass
    return r + frag

def legal_links(lang, here):
    L = LABELS[lang]
    items = [
        (ROUTES['policies'][lang] + ('#cancelacion'), L['cancel']),
        (ROUTES['policies'][lang] + '#pagos', L['pay']),
        (ROUTES['policies'][lang] + '#servicios', L['serv']),
        (ROUTES['terms'][lang], L['terms']),
        (ROUTES['privacy'][lang], L['privacy']),
        (ROUTES['cookies'][lang], L['cookies']),
    ]
    out = []
    for route, label in items:
        href = rel(here, route)
        out.append(f'<li><a href="{href}">{html.escape(label)}</a></li>')
    out.append(f'<li><button class="site-footer__prefs" type="button" data-cookie-prefs data-policy="{rel(here, ROUTES["cookies"][lang])}">{L["prefs"]}</button></li>')
    return out

def breadcrumb_ld(lang, here, name):
    L = LABELS[lang]
    data = {
        '@context': 'https://schema.org',
        '@type': 'BreadcrumbList',
        'itemListElement': [
            {'@type': 'ListItem', 'position': 1, 'name': L['home'], 'item': BASE + ROUTES['home'][lang]},
            {'@type': 'ListItem', 'position': 2, 'name': name, 'item': BASE + here},
        ],
    }
    return json.dumps(data, ensure_ascii=False, indent=2).replace('\n', '\n      ')
