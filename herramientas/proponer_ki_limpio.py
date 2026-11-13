"""Propone fotogramas de ki (carga y lanzamiento) sin efectos pintados, para todas las formas.

El juego dibuja su propia bola de ki en la mano al cargar y saca el proyectil o el rayo de la mano del fotograma de
lanzamiento (heroHand en script.js). Si el fotograma del pack ya trae una bola, fuego o un rayo pintado, se ven dos
bolas y el proyectil sale del borde de la bola pintada. Este script busca, en el MISMO pack y a la misma escala que
montar_animaciones.py, un fotograma de carga y otro de lanzamiento limpios.

Uso (desde la raíz del proyecto):
  python herramientas/proponer_ki_limpio.py            # todas las formas con efectos pintados en Cast o Beam
  python herramientas/proponer_ki_limpio.py roshi goku # solo esos personajes
Escribe herramientas/_revisar/ki_limpio_propuestas.json y hojas herramientas/_revisar/ki_limpio_*.png para revisarlas a ojo.
"""
import sys, os, json, copy
import numpy as np
from PIL import Image, ImageDraw

sys.path.insert(0, os.path.dirname(__file__))
import montar_animaciones as M

UMBRAL = 0.05      # fracción de píxeles brillantes que no están en la paleta del personaje: por encima, hay efecto pintado
LIMPIO = 0.03      # para aceptar un fotograma como limpio
VENTANA = 6        # fotogramas del pack alrededor de los de ki que se miran


def rgba(im):
    return np.array(im.convert('RGBA'))


def clave(a):
    return (a[..., 0].astype(np.int32) << 16) | (a[..., 1].astype(np.int32) << 8) | a[..., 2]


def paleta(frames):
    return np.unique(np.concatenate([clave(f)[f[..., 3] > 200] for f in frames]))


def ajeno(f, pal):
    m = f[..., 3] > 200
    if not m.any():
        return 1.0
    brillo = f[..., :3].max(-1)[m] > 150
    return float(((~np.isin(clave(f)[m], pal)) & brillo).sum() / m.sum())


def medidas(f):
    """alto del cuerpo, alcance del brazo hacia delante (desde el centro del tronco) y punto de la mano"""
    m = f[..., 3] > 40
    ys, xs = np.nonzero(m)
    if not len(ys):
        return None
    y0, y1 = ys.min(), ys.max()
    alto = y1 - y0 + 1
    ya, yb = y0 + int(alto * 0.25), y0 + int(alto * 0.7)
    banda = m[ya:yb + 1]
    cols = np.nonzero(banda.any(0))[0]
    if not len(cols):
        return None
    tronco = np.median(np.nonzero(m[y0 + int(alto * 0.35):y0 + int(alto * 0.6) + 1])[1])
    bx = cols.max()
    hy = ya + np.nonzero(banda[:, bx])[0].mean()
    return {'alto': alto, 'alcance': bx - tronco, 'mano': (int(bx), float(hy)), 'pie': int(y1)}


def tiras(res, nombre):
    import base64, io
    a = res['anims'].get(nombre)
    if not a:
        return []
    im = Image.open(io.BytesIO(base64.b64decode(a['url'].split(',')[1]))).convert('RGBA')
    return [im.crop((i * a['w'], 0, (i + 1) * a['w'], a['h'])) for i in range(len(a['du']))]


def proponer(h, f, cfg):
    n_pack = len(M.frames_del_pack(cfg['pack']))
    ki = cfg.get('ki') or []
    beam = cfg.get('beam') or []
    ataque = [i for k in ('attack', 'attack2', 'attack3') for i in cfg.get(k, []) if i < 1000]
    ref = ki + beam
    if not ref:
        return None
    pool = set(ataque)
    for i in ref:
        if i < 1000:
            pool.update(range(max(0, i - VENTANA), min(n_pack, i + VENTANA + 1)))
    rutas = M.frames_del_pack(cfg['pack'])
    pool = sorted(i for i in pool if M.limpiar(rutas[i]).getbbox())  # fuera los fotogramas vacíos
    prueba = copy.deepcopy(cfg)
    prueba['dash'] = pool
    prueba.pop('dashDu', None)
    res = M.montar_forma(prueba)
    base = [rgba(x) for k in ('Idle', 'Walk', 'Hurt') for x in tiras(res, k)]
    pal = paleta(base)
    ref_idle = [medidas(rgba(x)) for x in tiras(res, 'Idle')]
    alto_idle = np.median([m['alto'] for m in ref_idle if m])
    cand = []
    for idx, im in zip(pool, tiras(res, 'Dash')):
        a = rgba(im)
        md = medidas(a)
        if not md:
            continue
        cand.append({'i': idx, 'ajeno': ajeno(a, pal), 'alto': md['alto'] / alto_idle,
                     'alcance': md['alcance'] / alto_idle, 'mano': md['mano'], 'img': im,
                     'ventana': any(abs(idx - r) <= VENTANA for r in ref if r < 1000), 'ataque': idx in ataque})
    # nunca poses que la forma ya usa para otra cosa (daño, muerte, aura, guardia, vuelo, patadas): parecen lanzar y no lo son
    otros = {i for k in ('hurt', 'faint', 'pow', 'idle', 'move', 'dash', 'kick', 'kick2', 'up') for i in cfg.get(k, [])}
    ok = [c for c in cand if c['ajeno'] < LIMPIO and 0.8 <= c['alto'] <= 1.15 and (c['i'] not in otros or c['ataque'])]
    if not ok:
        return {'sin_candidatos': True}
    mejor = max(c['alcance'] for c in ok)
    # lanzamiento: el brazo más estirado; si uno de la zona de ki llega casi igual, mejor ese (es un lanzamiento de verdad)
    # lanzamiento: primero el fotograma de ki que ya estaba elegido si está limpio; si no, los vecinos de los de ki
    # (2 a cada lado) con el brazo estirado; si no, el puñetazo con el brazo más estirado
    ki_set = [i for i in ki if i < 1000]
    def cerca(c, n):
        return any(abs(c['i'] - r) <= n for r in ki_set)
    actual = [c for c in ok if ki_set and c['i'] == ki_set[-1]]
    vecinos = [c for c in ok if cerca(c, 2) and c['alcance'] >= 0.6 * mejor]
    suelta = actual[0] if actual and actual[0]['alcance'] >= 0.28 else max(vecinos or ok, key=lambda c: (c['alcance'] if not vecinos else -min(abs(c['i'] - r) for r in ki_set), c['alcance']))
    if suelta['alcance'] < 0.28:  # nada con el brazo hacia delante: mejor no tocar
        return {'sin_lanzamiento': True}
    # carga: limpio, brazos cerca del cuerpo, preferiblemente justo antes del lanzamiento en el pack
    previos = [c for c in ok if c['i'] != suelta['i'] and c['alcance'] < suelta['alcance'] * 0.8]
    if ki_set and any(c['i'] == ki_set[0] for c in previos):  # la carga que ya estaba, si está limpia
        previos = [c for c in previos if c['i'] == ki_set[0]]
    def nota(c):
        return (0 if c['ventana'] else 1, abs(c['i'] - suelta['i']) if c['i'] < suelta['i'] else 50 + abs(c['i'] - suelta['i']))
    carga = min(previos, key=nota) if previos else None
    if carga is None:  # sin carga limpia: la guardia (el juego dibuja la bola de ki en la mano)
        g = [c for c in cand if c['i'] in cfg.get('idle', [])[:1]]
        if not g:
            prueba2 = copy.deepcopy(cfg); prueba2['dash'] = cfg.get('idle', [])[:1]
            im = tiras(M.montar_forma(prueba2), 'Dash')
            g = [{'i': cfg['idle'][0], 'img': im[0], 'ajeno': 0, 'alcance': 0}] if im else []
        carga = g[0] if g else None
    return {'carga': carga, 'suelta': suelta}


def main():
    C = M.leer_config()
    nombres = sys.argv[1:]
    marcas = json.load(open(os.path.join(os.path.dirname(__file__), '_revisar', 'ki_marcas.json'))) if not nombres and os.path.exists(os.path.join(os.path.dirname(__file__), '_revisar', 'ki_marcas.json')) else None
    salida, hojas = {}, []
    for h in (nombres or C):
        for f, cfg in C[h].items():
            if marcas is not None and f'{h}/{f}' not in marcas:
                continue
            try:
                p = proponer(h, f, cfg)
            except SystemExit as e:
                print('  error', h, f, e); continue
            except Exception as e:
                print('  error', h, f, repr(e)); continue
            if not p:
                continue
            if 'carga' not in p:
                salida[f'{h}/{f}'] = p; continue
            c, s = p['carga'], p['suelta']
            salida[f'{h}/{f}'] = {'carga': c['i'] if c else None, 'suelta': s['i'], 'ki_antes': cfg.get('ki'), 'beam_antes': cfg.get('beam'),
                                  'mano': s['mano'], 'ajeno_suelta': round(s['ajeno'], 3)}
            hojas.append((f'{h}/{f}', cfg, c, s))
            print(h, f, 'ki', cfg.get('ki'), '->', [c['i'] if c else None, s['i']], 'beam', cfg.get('beam'))
    os.makedirs(os.path.join(os.path.dirname(__file__), '_revisar'), exist_ok=True)
    json.dump(salida, open(os.path.join(os.path.dirname(__file__), '_revisar', 'ki_limpio_propuestas.json'), 'w'), indent=1)
    return hojas




def hoja(hojas, actuales, ruta, por=24, cols=4, Z=2):
    """antes (fotogramas de ki que hay ahora) | después (carga, lanzamiento con la mano marcada)"""
    grupos = []
    for nombre, cfg, c, s in hojas:
        antes = actuales.get(nombre, [])
        nuevas = ([c['img']] if c else []) + [s['img']]
        ims = antes + nuevas
        H = max(i.height for i in ims) * Z + 12
        W = sum(i.width * Z + 3 for i in ims) + 10
        g = Image.new('RGB', (W, H), (58, 120, 96))
        d = ImageDraw.Draw(g)
        x = 2
        for k, im in enumerate(ims):
            if k == len(antes):
                d.rectangle((x, 12, x + 3, H), fill=(240, 240, 240)); x += 7
            i2 = im.resize((im.width * Z, im.height * Z), Image.NEAREST)
            g.paste(i2, (x, H - i2.height), i2)
            if im is s['img']:
                mx, my = s['mano']
                d.ellipse((x + mx * Z - 3, H - i2.height + my * Z - 3, x + mx * Z + 3, H - i2.height + my * Z + 3), outline=(255, 0, 0), width=2)
            x += i2.width + 3
        d.text((2, 0), f"{nombre} ki {cfg.get('ki')} -> {[c['i'] if c else None, s['i']]}", fill=(255, 255, 0))
        grupos.append(g)
    salidas = []
    for s0 in range(0, len(grupos), por):
        G = grupos[s0:s0 + por]
        cw = max(g.width for g in G); ch = max(g.height for g in G)
        sh = Image.new('RGB', (cw * cols, ch * ((len(G) + cols - 1) // cols)), (25, 25, 35))
        for k, g in enumerate(G):
            sh.paste(g, ((k % cols) * cw, (k // cols) * ch))
        p = ruta.format(s0 // por); sh.save(p); salidas.append(p)
    return salidas


if __name__ == '__main__':
    import base64, io, re
    hojas = main()
    t = open(os.path.join(os.path.dirname(__file__), '..', '02 - Código del juego', 'animaciones_juego.js'), encoding='utf-8').read()
    AS = json.loads(t[t.index('{', t.index('window.ANIM_SET=')):t.rindex('}') + 1])['h']
    actuales = {}
    for nombre, *_ in hojas:
        h, f = nombre.split('/')
        actuales[nombre] = tiras({'anims': AS[h][f]['anims']}, 'Cast')
    for p in hoja(hojas, actuales, os.path.join(os.path.dirname(__file__), '_revisar', 'ki_limpio_{}.png')):
        print(p)
