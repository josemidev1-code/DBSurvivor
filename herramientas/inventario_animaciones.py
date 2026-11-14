"""Inventario de animaciones por forma: qué está animado, qué tiene un solo fotograma y qué falta.

Uso:  python herramientas/inventario_animaciones.py
Escribe: 01 - Guía y documentación/INVENTARIO_ANIMACIONES.md

Para cada forma montada mira las 14 animaciones que usa el juego y cuenta sus fotogramas:
- ANIMADA: 2 fotogramas o más (daño, muerte y retrato valen con 1).
- QUIETA: un solo fotograma en una animación que debería moverse (guardia, moverse, golpes, ki...).
- FALTA: no tiene; el juego usa otra en su lugar.
Una forma está COMPLETA cuando todas sus animaciones están animadas.
Los nombres salen de herramientas/nombres_personajes.json (volcado de AS.HDEF desde el navegador).
"""
import collections, datetime, json, os, re, sys
sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import montar_animaciones as M

RAIZ = M.RAIZ
ANIM = [('idle', 'Guardia'), ('move', 'Moverse'), ('attack', 'Puñetazos'), ('kick', 'Patadas'), ('ki', 'Ki'),
        ('pow', 'Poder/aura'), ('hurt', 'Daño'), ('faint', 'Muerte'), ('portrait', 'Retrato'),
        ('attack2', 'Combo 2'), ('attack3', 'Combo 3'), ('kick2', 'Patada 2'), ('beam', 'Rayo'), ('up', 'Brazos arriba')]
UNO_VALE = {'hurt', 'faint', 'portrait', 'move'}  # moverse: 1 pose de vuelo vale (GUIA_ANIMACIONES)
NO_CUENTA = {'portrait'}  # el retrato no es animación: se enseña, pero no decide si está completa

src = open(os.path.join(RAIZ, '02 - Código del juego', 'script.js'), encoding='utf-8').read()
jugables = set(re.findall(r"\b(\w+):\{name:'[^']+',rar:", src)) | set(re.findall(r"\bHDEF\.(\w+)=\{", src))
ocultos = set(re.findall(r"'(\w+)'", re.sub(r"//[^\n]*", "", re.search(r"DUPLICADOS_ROSTER = new Set\(\[(.*?)\]\)", src, re.S).group(1))))
alias = {(h, f) for h, f in re.findall(r"ah\.\w+\[\d+\]=ah\.(\w+)\[(\d+)\]", src)}
alias |= {(h, f) for h, f in re.findall(r"\d+:ah\.(\w+)\[(\d+)\]", src)}
for lista in re.findall(r"unir\('\w+',\[(.*?)\]\)", src):
    for h in re.findall(r"'(\w+)'", lista):
        ocultos.add(h); alias |= {(h, str(f)) for f in range(20)}
visible = lambda h, f: h in jugables and (h not in ocultos or (h, f) in alias)
try:
    NOM = json.load(open(os.path.join(RAIZ, 'herramientas', 'nombres_personajes.json'), encoding='utf-8'))
except OSError:
    NOM = {}


def nombre(h, f):
    d = NOM.get(h)
    if not d:
        return h
    fs = d.get('f') or []
    fo = fs[int(f)] if f.isdigit() and int(f) < len(fs) else f'forma {f}'
    return f"{d['n'].title()} · {fo.title()}" if len(fs) > 1 else d['n'].title()


filas = []
for h, formas in M.leer_config().items():
    for f, s in formas.items():
        if not s.get('pack'):
            continue
        fr = M.frames_del_pack(s['pack'])
        estado = {}
        for k, _ in ANIM:
            v = s.get(k)
            n = 1 if isinstance(v, int) else len([i for i in (v or []) if isinstance(i, int)])
            estado[k] = 'falta' if n == 0 else ('animada' if n >= 2 or k in UNO_VALE else 'quieta')
        grupo = 'jugable' if visible(h, f) else ('enemigo' if h not in jugables else 'oculto')
        filas.append({'h': h, 'f': f, 'nom': nombre(h, f), 'grupo': grupo, 'fr': len(fr or []), 'e': estado,
                      'pack': s['pack']})

usados = {r['pack'] for r in filas}
packs = {}
for d, _, fs in os.walk(M.SPRITES):
    n = sum(x.lower().endswith(('.png', '.gif', '.jpg', '.jpeg', '.webp', '.bmp')) for x in fs)
    if n:
        packs[os.path.relpath(d, M.SPRITES).replace(os.sep, '/')] = n
NO_PERSONAJE = ('06_Escenarios', '08_Referencias', 'shenron')
sin_montar = {p: n for p, n in packs.items()
              if not p.startswith(NO_PERSONAJE) and not any(p == u or p.startswith(u + '/') or u.startswith(p + '/') for u in usados)}


def nivel(r):
    malas = sum(x != 'animada' for k, x in r['e'].items() if k not in NO_CUENTA)
    return 'COMPLETA' if malas == 0 else 'CASI' if malas <= 2 else 'A MEDIAS' if malas <= 6 else 'POCA'


ICO = {'animada': '✅', 'quieta': '🟡', 'falta': '❌'}
jug = sorted([r for r in filas if r['grupo'] == 'jugable'], key=lambda r: (sum(x != 'animada' for k, x in r['e'].items() if k not in NO_CUENTA), r['nom']), reverse=True)
ene = sorted([r for r in filas if r['grupo'] == 'enemigo'], key=lambda r: r['nom'])
cuenta = collections.Counter(nivel(r) for r in jug)
quietas = collections.Counter(k for r in jug for k, v in r['e'].items() if v == 'quieta')
faltan = collections.Counter(k for r in jug for k, v in r['e'].items() if v == 'falta')
NOMA = dict(ANIM)

def escribir():
    L = [f'# Inventario de animaciones ({datetime.date.today()})', '',
         'Generado con `python herramientas/inventario_animaciones.py`. Para cada forma se miran las 14 animaciones del juego: '
         '✅ animada (2 fotogramas o más; moverse, daño, muerte y retrato valen con 1), 🟡 quieta (un solo fotograma), ❌ falta (el juego usa otra).', '',
         '## Resumen', '',
         'El retrato se enseña pero no cuenta para «completa» (no es una animación; sin él se usa el de otra forma).', '',
         f'- Formas jugables: **{len(jug)}**. Completas: **{cuenta["COMPLETA"]}** · casi (1-2 pendientes): **{cuenta["CASI"]}** · '
         f'a medias (3-6): **{cuenta["A MEDIAS"]}** · poco animadas (7 o más): **{cuenta["POCA"]}**.',
         f'- Formas de enemigos: **{len(ene)}**. Formas ocultas (no se ven en el juego): **{sum(r["grupo"] == "oculto" for r in filas)}**.',
         f'- Carpetas de `sprites/` con personajes que el juego no usa: **{len(sin_montar)}** ({sum(sin_montar.values())} imágenes).', '',
         '**Lo que más se repite en las formas jugables:**', '']
    for k, n in quietas.most_common():
        L.append(f'- {NOMA[k]} con un solo fotograma: {n} formas')
    for k, n in faltan.most_common():
        L.append(f'- {NOMA[k]} sin animación propia: {n} formas')
    L += ['', '## Formas jugables (de menos a más animadas)', '',
          '| Personaje · forma | Estado | ' + ' | '.join(n for _, n in ANIM) + ' |',
          '|---|---|' + '---|' * len(ANIM)]
    for r in jug:
        L.append(f'| {r["nom"]} (`{r["h"]}/{r["f"]}`) | {nivel(r)} | ' + ' | '.join(ICO[r['e'][k]] for k, _ in ANIM) + ' |')
    L += ['', '## Enemigos', '', '| Enemigo | Estado | ' + ' | '.join(n for _, n in ANIM) + ' |', '|---|---|' + '---|' * len(ANIM)]
    for r in ene:
        L.append(f'| {r["nom"]} (`{r["h"]}/{r["f"]}`) | {nivel(r)} | ' + ' | '.join(ICO[r['e'][k]] for k, _ in ANIM) + ' |')
    L += ['', '## Carpetas de personajes sin montar en el juego', '', 'No tienen ninguna animación en el juego todavía.', '']
    for p, n in sorted(sin_montar.items()):
        L.append(f'- `{p}` ({n} imágenes)')
    L += ['', '## Cómo animar con Piskel', '',
          '1. `python herramientas/exportar_piskel_lote.py` deja en `piskel_animaciones/<personaje>_<forma>/` un `.piskel` por animación.',
          '2. Abre el `.piskel` en https://www.piskelapp.com (Abrir → archivo), edita o añade fotogramas y guarda el `.piskel`.',
          '3. `python herramientas/importar_piskel.py` lo devuelve al juego (lee `piskel_animaciones/LEEME.md` antes).', '']
    open(os.path.join(RAIZ, '01 - Guía y documentación', 'INVENTARIO_ANIMACIONES.md'), 'w', encoding='utf-8').write('\n'.join(L))
    print(len(jug), dict(cuenta), len(ene), len(sin_montar))
    print('quietas', quietas.most_common()); print('faltan', faltan.most_common())


if __name__ == '__main__':
    escribir()
