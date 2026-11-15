"""Genera la DB Dex: ficha de cada personaje jugable con sus animaciones, estadísticas y datos del anime.

Uso:  python herramientas/generar_dex.py
Escribe:
- 03 - Dex/datos.js                         (window.DEX, lo lee 03 - Dex/index.html; funciona con doble clic)
- 03 - Dex/api/v1/personaje/index.json      (lista, al estilo de PokéAPI)
- 03 - Dex/api/v1/personaje/<id>.json       (ficha completa de cada personaje)

De dónde sale cada dato:
- Estadísticas del juego (PV, ataque, velocidad, recarga): HDEF de script.js, con la misma subida por forma que stats().
  Se leen de herramientas/hdef.json (volcado del navegador; ver --volcar).
- Raza, planeta, afiliación, descripción y poder de pelea: herramientas/dbapi/personajes.json (dragonball-api.com,
  bajado con descargar_dbapi.py). Si la API no tiene el personaje o la forma, el poder se inventa con las reglas de
  PODER_FORMA y BASE_ANIME (como en el anime), y la ficha lo marca con fuente «inventado».
- Estado de las animaciones: inventario_animaciones.py.
"""
import json, math, os, re, subprocess, sys, unicodedata
sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import inventario_animaciones as INV

RAIZ = INV.RAIZ
HERR = os.path.join(RAIZ, 'herramientas')
DEX = os.path.join(RAIZ, '03 - Dex')

RAREZA = {0: 'INICIAL', 3: 'RARO', 4: 'ÉPICO', 5: 'LEGENDARIO'}
ANIM_HOJA = {'idle': 'Idle', 'move': 'Walk', 'attack': 'Attack', 'kick': 'Kick', 'ki': 'Cast', 'pow': 'Pow', 'hurt': 'Hurt',
             'faint': 'Faint', 'attack2': 'Attack2', 'attack3': 'Attack3', 'kick2': 'Kick2', 'beam': 'Beam', 'up': 'Up'}


def norm(s):
    s = unicodedata.normalize('NFD', s.upper())
    return ''.join(c for c in s if unicodedata.category(c) != 'Mn')


# ---------- personaje del juego -> personaje de la API ----------
# Por prefijo del id (el más largo gana). Las variantes (gokussj4gt, vegetablueevo...) caen en el personaje base.
API_DE = {
    'goku': 'Goku', 'gokunino': None, 'gokureymono': 'Goku', 'vegeta': 'Vegeta', 'babyvegeta': None, 'piccolo': 'Piccolo',
    'krilin': 'Krillin', 'yamcha': 'Yamcha', 'gohan': 'Gohan', 'trunks': 'Trunks', 'a18': 'Android 18', 'a17': 'Android 17',
    'a16': 'Android 16', 'a13': 'Android 13', 'a14': 'Android 14', 'bardock': 'Bardock', 'broly': 'Broly', 'brolyfan': 'Broly',
    'vegetto': 'Vegetto', 'vegito': 'Vegetto', 'gogeta': 'Gogeta', 'gotenks': 'Gotenks', 'roshi': 'Master Roshi',
    'raditz': 'Raditz', 'freezer': 'Freezer', 'cell': 'Celula', 'buu': 'Majin Buu', 'janemba': 'Janemba', 'bills': 'Bills',
    'jiren': 'Jiren', 'toppo': 'Toppo', 'dyspo': 'Dyspo', 'kibito': 'Kibito', 'kibitoshin': 'Kibito-Shin', 'ginyu': 'Ginyu',
    'mrsatan': 'Mr. Satan', 'bulma': 'Bulma', 'tenshinhan': 'Tenshinhan', 'daishinkan': 'Grand Priest', 'shin': 'Kaio-shin del Este',
    'ginyucuerpogoku': 'Ginyu', 'gohanb': 'Gohan',
}

# Poder de pelea de la forma base cuando la API no lo trae (valores del anime y de las guías; los que no salen, a ojo).
BASE_ANIME = {
    'saibaman': 1_200, 'nappa': 4_000, 'raditz': 1_500, 'jeice': 40_000, 'guldo': 13_500, 'ginyu': 120_000,
    'cui': 18_000, 'tarble': 100_000, 'paragus': 30_000_000, 'turles': 3_000_000, 'slug': 4_000_000, 'cooler': 9_000_000,
    'metalcooler': 400_000_000, 'reycold': 3_000_000, 'frost': 100_000_000_000, 'kyabe': 2_000_000_000,
    'caulifla': 4_000_000_000, 'kale': 3_000_000_000, 'kefla': 3_000_000_000_000_000, 'hit': 9_000_000_000_000_000,
    'zamasu': 1_000_000_000_000_000, 'moro': 5e18, 'gas': 6e18, 'granola': 5e18, 'cumber': 9e18, 'a21': 5e17,
    'super17': 1e15, 'nuova': 5e14, 'omega': 3e15, 'babyvegeta': 9e14, 'uub': 8e9, 'pangt': 3e8, 'bra': 2e9, 'goten': 4e9,
    'gokunino': 260, 'trunksnino': 3e7, 'videl': 300, 'taopaipai': 160, 'magetta': 5e12, 'glorio': 9e14, 'gomah': 5e15,
    'majinkuu': 3e15, 'majinduu': 3e15, 'hatchiyack': 1e12, 'merus': 1e22, 'dlrx': 5e17, 'tora': 1e4, 'zombies': 1e7,
    'gohanposeido': 4e9, 'gohanfut': 1e9, 'a17npc': 3.2e8, 'a18npc': 2.8e8, 'kibito': 6e7, 'shin': 9e7,
    'trunkscell': 5e7, 'gokuxeno': 6e16, 'vegetaxeno': 5e16, 'blacktime': 8e15, 'blackfan': 6e15,
    'gohanmanga': 4.5e7, 'black': 6e15, 'trunksarmor': 5e16, 'zamasufusion': 3e19,
}
BASE_RAREZA = {0: 5e7, 3: 5e6, 4: 3e8, 5: 6e9}

# Cada forma se reduce a una clave (la primera regla que encaja), igual para el juego y para la API.
CANON = [
    (r'UI.*BLUE.*EVOL', 'UIBLUEEVO'), (r'UI.*BLUE', 'UIBLUE'), (r'UI DIOS|UI.*\bDIOS', 'UIDIOS'), (r'VERDADERO', 'UITRUE'),
    (r'ROSE.*(UI|ULTRA INSTINTO)', 'ROSEUI'), (r'DOMINADO|\bMUI\b|ULTRA INSTINC$', 'MUI'), (r'\bUI\b|ULTRA INSTINTO|SENAL', 'UI'),
    (r'\bEGO\b|MEGA INSTINC', 'EGO'), (r'BESTIA|BEAST', 'BESTIA'), (r'NARANJA|ORANGE', 'NARANJA'),
    (r'ROSE.*EVOL', 'ROSEEVO'), (r'ROSE.*KAIOKEN', 'ROSEKK'), (r'ROSE 3', 'ROSE3'), (r'ROSE', 'ROSE'),
    (r'(BLUE|SSJB).*(EVOL)|^EVOLUTION', 'BLUEEVO'), (r'BLUE.*KAIOKEN|KAIOKEN.*BLUE', 'BLUEKK'), (r'BLUE FULL', 'BLUEFP'),
    (r'SSJ4 BLUE', 'SSJ4BLUE'), (r'BLUE MALIGNO', 'BLUEEVIL'), (r'BLUE PERFECTO', 'BLUEFP'), (r'BLUE|SSJB', 'BLUE'),
    (r'SSJ4 DIOS', 'SSJ4DIOS'), (r'SSJ4|SUPER SAIYAN 4', 'SSJ4'), (r'ULTRA SSJ DIOS', 'ULTRADIOS'), (r'DIOS BERSERK', 'DIOSBERSERK'),
    (r'DIOS KAIOKEN', 'DIOSKK'), (r'DESTRUCTOR|HAKAISHIN', 'HAKAI'), (r'SSJ DIOS|SSJ GOD|\bDIOS\b', 'DIOS'),
    (r'LEGENDAR', 'LEGEND'), (r'SUPREMO', 'SUPREMO'), (r'RAGE|IKARI', 'RAGE'), (r'BERSERK', 'BERSERK'),
    (r'SSJ3|SUPER SAIYAN 3', 'SSJ3'), (r'MAJIN|MALIGNO', 'MAJIN'), (r'SSJ2|SUPER SAIYAN 2|SUPER VEGETTO 2', 'SSJ2'),
    (r'ULTRA SSJ', 'USSJ'), (r'SUPER VEGETA\b', 'SVEGETA'), (r'SSJ KAIOKEN', 'SSJKK'), (r'FULL POWER', 'SSJFP'),
    (r'REY MONO', 'SSJMONO'), (r'SSJ|SUPER SAIYAN|SUPER VEGETTO|SUPER GOGETA|FALSO', 'SSJ'), (r'KAIOKEN', 'KK'),
    (r'2ND FORM', 'F2'), (r'1. FORMA', 'F1'), (r'3RD FORM|3. FORMA', 'F3'), (r'PERFECT FORM \(GOLDEN\)|GOLDEN', 'GOLDEN'),
    (r'^PERFECT FORM$|FORMA FINAL', 'FINAL'), (r'100%', 'F100'), (r'IMPERFECT', 'IMPERF'), (r'SEMI ?PERFECT', 'SEMI'),
    (r'SUPER PERFECT|PERFECTO', 'PERF'), (r'GORDO', 'GORDO'), (r'SUPER BUU', 'SUPERBUU'), (r'BUU.*GOHAN', 'BUUGOHAN'),
    (r'KID BUU|\(PURE\)', 'KIDBUU'), (r'SUPER JANEMBA', 'SUPERJAN'), (r'ULTIMATE|DEFINITIV|MISTICO', 'DEF'),
    (r'MAXIMO PODER', 'MAX'), (r'MONSTER', 'MONSTRUO'), (r'SUPER NAMEKIAN', 'SNAMEK'),
]
# Poder de Goku en cada clave (escala de la propia dragonball-api); el de otro personaje se multiplica por su fuerza.
TIER = {
    '': 6e7, 'KK': 1.2e9, 'SSJ': 3e9, 'SVEGETA': 3.6e9, 'USSJ': 4.2e9, 'SSJFP': 4.5e9, 'SSJMONO': 3.5e9, 'SSJ2': 6e9, 'MAJIN': 7e9,
    'SSJKK': 1.2e10, 'SSJ3': 2.4e10, 'DEF': 4.3e10, 'SSJ4': 2e15, 'DIOS': 5e17, 'DIOSKK': 2e18, 'DIOSBERSERK': 3e18,
    'SUPREMO': 3e18, 'BERSERK': 2e18, 'ULTRADIOS': 4e18, 'BLUE': 9e18, 'BLUEEVIL': 1e19, 'RAGE': 1.75e19, 'BLUEFP': 2e19,
    'SSJ4DIOS': 5e19, 'NARANJA': 4.1e19, 'BLUEKK': 9e19, 'BLUEEVO': 1.2e20, 'SSJ4BLUE': 2e20, 'ROSE': 9e18, 'ROSEKK': 9e19,
    'ROSE3': 1e20, 'ROSEEVO': 1.2e20, 'UI': 9e24, 'ROSEUI': 1e25, 'LEGEND': 1.1e25, 'EGO': 2e25, 'BESTIA': 2.56e25,
    'MUI': 9e25, 'UIBLUE': 1e26, 'UITRUE': 1.2e26, 'UIDIOS': 1.5e26, 'UIBLUEEVO': 2e26,
}
# Formas propias de un personaje que la API no trae (valores del anime o a ojo, absolutos).
PROPIO = {'GOLDEN': 1e20, 'F100': 1.2e8, 'HAKAI': 2.4e20, 'MAX': 1.8e20, 'SUPERJAN': 7.5e10, ('freezer', 'BLACK'): 1e21}


def canon(t):
    t = norm(t).replace('É', 'E')
    for pat, k in CANON:
        if re.search(pat, t):
            return k
    return ''


def parse_ki(s):
    """'60.000.000', '280,000,000', '3 Billion', '2.175 Billion', '969 Googolplex' -> número (o None)."""
    if not s:
        return None
    s = s.strip().lower()
    esc = {'thousand': 1e3, 'million': 1e6, 'billion': 1e9, 'trillion': 1e12, 'quadrillion': 1e15, 'quintillion': 1e18,
           'sextillion': 1e21, 'septillion': 1e24, 'octillion': 1e27, 'googolplex': 1e100}
    m = re.match(r'([\d.,]+)\s*([a-z]*)', s)
    if not m:
        return None
    num, pal = m.groups()
    if pal and pal in esc:
        return float(num.replace(',', '.')) * esc[pal] if num.count('.') + num.count(',') <= 1 else float(re.sub(r'[.,]', '', num)) * esc[pal]
    if pal:
        return None
    v = float(re.sub(r'[.,]', '', num))
    return v or None


def texto_poder(v):
    """Escala larga en español, como el doblaje: millones, miles de millones, billones, trillones..."""
    if v is None:
        return 'Desconocido'
    if v < 1e6:
        return f'{int(round(v)):,}'.replace(',', '.')
    if v >= 1e60:
        return 'Incalculable'
    esc = [(6, 'millón', 'millones'), (12, 'billón', 'billones'), (18, 'trillón', 'trillones'), (24, 'cuatrillón', 'cuatrillones'),
           (30, 'quintillón', 'quintillones'), (36, 'sextillón', 'sextillones'), (42, 'septillón', 'septillones'), (48, 'octillón', 'octillones')]
    exp, uno, varios = [e for e in esc if v >= 10 ** e[0]][-1]
    x = v / 10 ** exp
    mil = x >= 1e3
    if mil:
        x /= 1e3
    t = f'{x:.1f}'.rstrip('0').rstrip('.').replace('.', ',')
    if mil:
        return f'{"" if t == "1" else t + " "}mil {varios}'
    return f'{t} {uno if t == "1" else varios}'


RAZA_ES = {'Saiyan': 'Saiyan', 'Human': 'Humano', 'Namekian': 'Namekiano', 'Frieza Race': 'Raza de Freezer', 'Android': 'Androide',
           'Majin': 'Majin', 'God': 'Dios', 'Angel': 'Ángel', 'Evil': 'Demonio', 'Jiren Race': 'Raza de Jiren',
           'Nucleico': 'Kaioshin', 'Nucleico benigno': 'Kaio', 'Unknown': 'Desconocida'}
AFIL_ES = {'Z Fighter': 'Guerreros Z', 'Army of Frieza': 'Ejército de Freezer', 'Freelancer': 'Por libre', 'Villain': 'Villano',
           'Pride Troopers': 'Tropas del Orgullo', 'Assistant of Vermoud': 'Ayudante de Vermoud', 'Assistant of Beerus': 'Ayudante de Bills',
           'Other': 'Otros', 'Red Ribbon Army': 'Patrulla Roja'}

# Raza y bando cuando la API no los tiene: (prefijo de id, raza, bando)
RAZA_JUEGO = [
    ('saibaman', 'Saibaman', 'Ejército de Freezer'), ('nappa', 'Saiyan', 'Ejército de Freezer'), ('turles', 'Saiyan', 'Villano'),
    ('paragus', 'Saiyan', 'Villano'), ('tarble', 'Saiyan', 'Por libre'), ('kyabe', 'Saiyan', 'Universo 6'),
    ('caulifla', 'Saiyan', 'Universo 6'), ('kale', 'Saiyan', 'Universo 6'), ('kefla', 'Saiyan (fusión)', 'Universo 6'),
    ('goten', 'Saiyan', 'Guerreros Z'), ('bra', 'Saiyan', 'Guerreros Z'), ('pangt', 'Saiyan', 'Guerreros Z'),
    ('trunks', 'Saiyan', 'Guerreros Z'), ('jeice', 'Raza de Jeice', 'Fuerzas Especiales Ginyu'),
    ('guldo', 'Raza de Guldo', 'Fuerzas Especiales Ginyu'), ('cui', 'Raza de Cui', 'Ejército de Freezer'),
    ('cooler', 'Raza de Freezer', 'Villano'), ('metalcooler', 'Máquina', 'Villano'), ('reycold', 'Raza de Freezer', 'Villano'),
    ('frost', 'Raza de Freezer', 'Universo 6'), ('slug', 'Namekiano', 'Villano'), ('hit', 'Raza de Hit', 'Universo 6'),
    ('zamasu', 'Kaioshin', 'Villano'), ('moro', 'Raza de Moro', 'Villano'), ('gas', 'Heeter', 'Villano'),
    ('granola', 'Cereal', 'Por libre'), ('cumber', 'Saiyan', 'Villano'), ('a21', 'Androide', 'Patrulla Roja'),
    ('super17', 'Androide', 'Villano'), ('nuova', 'Dragón Shadow', 'Villano'), ('omega', 'Dragón Shadow', 'Villano'),
    ('babyvegeta', 'Tsufur', 'Villano'), ('uub', 'Humano', 'Guerreros Z'), ('videl', 'Humana', 'Guerreros Z'),
    ('taopaipai', 'Humano', 'Patrulla Roja'), ('magetta', 'Metal', 'Universo 6'), ('glorio', 'Majin', 'Villano'),
    ('gomah', 'Demonio', 'Villano'), ('majinkuu', 'Majin', 'Villano'), ('majinduu', 'Majin', 'Villano'),
    ('hatchiyack', 'Máquina Tuffle', 'Villano'), ('merus', 'Ángel', 'Patrulla Galáctica'), ('dlrx', 'Demonio', 'Villano'),
    ('tora', 'Saiyan', 'Ejército de Freezer'), ('zombies', 'Saiyan', 'Villano'), ('black', 'Kaioshin (cuerpo de Goku)', 'Villano'),
    ('gokuxeno', 'Saiyan', 'Patrulla del Tiempo'), ('vegetaxeno', 'Saiyan', 'Patrulla del Tiempo'),
    ('gokupatrulla', 'Saiyan', 'Patrulla del Tiempo'), ('goku', 'Saiyan', 'Guerreros Z'), ('vegeta', 'Saiyan', 'Guerreros Z'),
    ('gohan', 'Saiyan', 'Guerreros Z'), ('a17', 'Androide', 'Guerreros Z'), ('a18', 'Androide', 'Guerreros Z'),
]


def volcar_hdef():
    js = r"""
const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage();
await p.goto('file://'+process.argv[2]);await p.waitForFunction(()=>window.AS&&window.AS.HDEF);
const r=await p.evaluate(()=>{const o={};for(const[k,v]of Object.entries(AS.HDEF)){o[k]={};for(const a of ['name','rar','hp','spd','atk','start','desc','forms','aura','regen'])if(v[a]!==undefined)o[k][a]=v[a]}
 const M={};for(const k of new Set(Object.values(AS.HDEF).map(h=>h.start)))M[k]=(window.AS.MOVES&&AS.MOVES[k]?.name)||k;return {h:o}});
require('fs').writeFileSync(process.argv[3],JSON.stringify(r.h,null,1));await b.close()})();
"""
    tmp = os.path.join(HERR, '_volcar_hdef.js')
    open(tmp, 'w').write(js)
    try:
        subprocess.run(['node', tmp, os.path.join(RAIZ, 'index.html'), os.path.join(HERR, 'hdef.json')], check=True)
    finally:
        os.remove(tmp)


def nombres_tecnicas():
    src = INV.src
    out = {}
    for k, n in re.findall(r"\n\s*(\w+):\{name:'([^']+)',(?:only|kind):", src) + re.findall(r"\n\s*(\w+):(?:\{\.\.\.)?[A-Z]+\('([^']+)'", src):
        out.setdefault(k, n)
    return out


def main():
    if '--volcar' in sys.argv or not os.path.exists(os.path.join(HERR, 'hdef.json')):
        volcar_hdef()
    HD = json.load(open(os.path.join(HERR, 'hdef.json'), encoding='utf-8'))
    API = {c['name'].strip(): c for c in json.load(open(os.path.join(HERR, 'dbapi', 'personajes.json'), encoding='utf-8'))}
    TEC = nombres_tecnicas()

    def api_de(h):
        k = max((p for p in API_DE if h.startswith(p)), key=len, default=None)
        return API.get(API_DE[k]) if k and API_DE[k] else None

    def raza_juego(h):
        for p, r, b in RAZA_JUEGO:
            if h.startswith(p):
                return r, b
        return 'Desconocida', 'Otros'

    filas = {}
    for r in INV.filas:
        if r['grupo'] == 'jugable':
            filas.setdefault(r['h'], {})[r['f']] = r

    personajes = []
    for h, d in HD.items():
        if h not in filas:
            continue
        api = api_de(h)
        nombre = d['name'].title().replace('Ssj', 'SSJ').replace('Gt', 'GT').replace('Ui ', 'UI ').replace('Hd)', 'HD)').replace('Dbs', 'DBS').replace('Lsw', 'LSW').replace('Swl', 'SWL').replace('Dlrx', 'DLRX')
        if api:
            raza = RAZA_ES.get(api['race'], api['race'])
            bando = AFIL_ES.get(api['affiliation'], api['affiliation'])
            planeta = (api.get('originPlanet') or {}).get('name')
            desc_anime = api.get('description')
        else:
            raza, bando = raza_juego(h)
            planeta = None
            desc_anime = None
        if h in ('black', 'blackfan', 'blacktime') or h.startswith('black'):
            raza, bando = 'Kaioshin (cuerpo de Goku)', 'Villano'
        base_api = parse_ki(api['ki']) if api else None
        formas = []
        nombre_n = norm(d['name'])
        tr_api = {}
        for t in (api or {}).get('transformations') or []:
            k = canon(re.sub(r'^' + re.escape(norm(api['name'])) + r'\s*', '', norm(t['name'])))
            if k and k not in tr_api:
                tr_api[k] = parse_ki(t['ki'])
        clave0 = canon(d['forms'][0]) or canon(nombre_n)
        if h in BASE_ANIME:
            base, fuerza = BASE_ANIME[h], BASE_ANIME[h] / TIER.get(clave0, 6e7)
        elif base_api:
            base = tr_api.get(clave0) or (TIER[clave0] * base_api / 6e7 if clave0 in TIER else base_api)
            fuerza = base_api / 6e7
        elif clave0 in TIER and clave0:
            base, fuerza = TIER[clave0], 1.0
        else:
            base = BASE_RAREZA.get(d['rar'], 1e8)
            fuerza = base / TIER.get(clave0, 6e7)
        for i, fn in enumerate(d['forms']):
            f = str(i)
            if f not in filas[h]:
                continue
            r = filas[h][f]
            clave = (canon(fn) or canon(nombre_n)) if i == 0 else canon(fn)
            if clave in tr_api and tr_api[clave]:
                poder, fuente = tr_api[clave], 'dragonball-api'
            elif i == 0 and (not clave or clave not in TIER) and base_api and h not in BASE_ANIME:
                poder, fuente = base_api, 'dragonball-api'
            elif i == 0:
                poder, fuente = base, 'inventado'
            elif clave and clave in TIER:
                poder, fuente = max(base * 1.2, TIER[clave] * min(max(fuerza, 0.3), 2.0)), 'inventado'
            elif (h, norm(fn)) in PROPIO or (clave and clave in PROPIO):
                poder, fuente = max(base * 1.2, PROPIO.get((h, norm(fn))) or PROPIO[clave]), 'inventado'
            else:
                poder, fuente = base * (1 + 0.5 * i), 'inventado'
            hp = d['hp'] + 15 * i
            formas.append({
                'n': i, 'nombre': fn.title().replace('Ssj', 'SSJ').replace('Gt', 'GT').replace('Ui ', 'UI ').replace('Dbs', 'DBS').replace('Mui', 'MUI'),
                'aura': (d.get('aura') or [None] * 20)[i] if i < len(d.get('aura') or []) else None,
                'poder': {'valor': poder, 'texto': texto_poder(poder), 'fuente': fuente},
                'stats': {'pv': hp, 'ataque': round(d['atk'] * (1 + 0.25 * i) * 100), 'velocidad': round(1.3 * d['spd'] * (1 + 0.06 * i)),
                          'recarga': round((1 - 0.05 * i) * 100)},
                'estado': INV.nivel(r),
                'animaciones': {k: r['e'][k] for k, _ in INV.ANIM},
                'pack': r['pack'],
            })
        if not formas:
            continue
        personajes.append({
            'id': h, 'nombre': nombre, 'rareza': d['rar'], 'rarezaNombre': RAREZA.get(d['rar'], str(d['rar'])),
            'tecnica': TEC.get(d['start'], d['start']), 'descJuego': d['desc'], 'regen': d.get('regen', 0),
            'raza': raza, 'bando': bando, 'planeta': planeta, 'descripcion': desc_anime,
            'api': {'id': api['id'], 'nombre': api['name'], 'url': f"https://dragonball-api.com/api/characters/{api['id']}",
                    'ki': api['ki'], 'maxKi': api['maxKi']} if api else None,
            'formas': formas,
        })

    orden = list(HD)
    personajes.sort(key=lambda p: orden.index(p['id']))
    for n, p in enumerate(personajes, 1):
        p['num'] = n
    os.makedirs(os.path.join(DEX, 'api', 'v1', 'personaje'), exist_ok=True)
    datos = {'generado': str(INV.datetime.date.today()), 'anim': [[k, n, ANIM_HOJA[k]] for k, n in INV.ANIM if k in ANIM_HOJA] + [['portrait', 'Retrato', None]],
             'personajes': personajes}
    open(os.path.join(DEX, 'datos.js'), 'w', encoding='utf-8').write(
        '// Generado por herramientas/generar_dex.py. No editar a mano.\nwindow.DEX=' + json.dumps(datos, ensure_ascii=False, separators=(',', ':')) + ';\n')
    api_dir = os.path.join(DEX, 'api', 'v1', 'personaje')
    for fn in os.listdir(api_dir):
        os.remove(os.path.join(api_dir, fn))
    json.dump({'total': len(personajes), 'resultados': [{'num': p['num'], 'id': p['id'], 'nombre': p['nombre'], 'url': f"personaje/{p['id']}.json"} for p in personajes]},
              open(os.path.join(api_dir, 'index.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    for p in personajes:
        json.dump(p, open(os.path.join(api_dir, p['id'] + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    inv = sum(f['poder']['fuente'] == 'inventado' for p in personajes for f in p['formas'])
    tot = sum(len(p['formas']) for p in personajes)
    print(f"{len(personajes)} personajes, {tot} formas; poder de la API en {tot - inv}, inventado en {inv}")


if __name__ == '__main__':
    main()
