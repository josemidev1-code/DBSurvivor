"""Título copiado del logo de la foto de Josemi («DRAGON BALL DAIMA», estilo.png en
Gwenview) con «SURVIVOR» en lugar de DAIMA (13 nov. 2026).

titulo_foto/recorte_foto.png es la zona de la pantalla de la foto, ya girada 3°
para enderezarla (solo la pantalla). El logo se lee píxel a píxel: cada píxel
del original ocupa 2,76 px de la foto. Pasos: muestreo en rejilla, clasificación
de cada píxel en la paleta del logo, limpieza (fuera el fondo de rayas, el aura
amarilla de Goku y el rótulo DAIMA), tramado regular y rótulo SURVIVOR con la
letra de DAIMA (negra, borde blanco de 3 px y filo negro).
Si Josemi manda el estilo.png original, conviene recortar el logo de ahí.

    python herramientas/titulo_desde_foto.py [--zoom 3]
"""
import base64, re, sys
from pathlib import Path
import numpy as np, cv2
from scipy import ndimage as nd
from PIL import Image
RAIZ = Path(__file__).resolve().parent.parent

def muestrear():
    r = cv2.imread(str(RAIZ / "herramientas/titulo_foto/recorte_foto.png")).astype(np.float32)
    s, ox, oy = 2.76, 2.0, 0.5
    xs = np.arange(ox, 880, s); ys = np.arange(oy, 300, s)
    A = np.zeros((len(ys), len(xs), 3), np.uint8)
    for j, y in enumerate(ys):
        for i, x in enumerate(xs):
            a = int(round(y + s * 0.3)); b = max(a + 1, int(round(y + s * 0.7)))
            c = int(round(x + s * 0.3)); d = max(c + 1, int(round(x + s * 0.7)))
            A[j, i] = np.median(r[a:b, c:d].reshape(-1, 3), 0)
    return A

def clasificar(A):
    A = A[:, :, ::-1].astype(np.float32)
    P=[((32,27,31),'K'),((69,43,10),'K'),((131,116,28),'K'),((10,8,12),'K'),
       ((248,240,24),'Y'),((247,237,62),'Y'),((255,250,120),'Y'),
       ((225,181,21),'O'),((216,188,76),'O'),((220,150,30),'O'),
       ((239,60,26),'R'),((255,90,40),'R'),
       ((159,42,48),'D'),((120,30,40),'D'),
       ((241,248,252),'W'),((184,192,224),'B'),
       ((138,51,225),'P'),((114,102,134),'P'),((179,119,217),'L'),((206,179,166),'S'),
       ((10,121,242),'B'),((63,121,221),'B'),((39,46,103),'B'),((90,160,250),'B')]
    cols=np.array([p[0] for p in P],np.float32);roles=[p[1] for p in P]
    d=((A[:,:,None,:]-cols[None,None])**2).sum(-1)
    R=np.array(roles)[d.argmin(-1)]

    return R

def limpiar(R):
    H, W = R.shape
    col=np.isin(R,list('YORDPLS'))
    # 1) DAIMA fuera: rótulo blanco y letras negras bajo las letras grandes
    dai=np.zeros_like(col); dai[83:,90:208]=True
    R[dai & np.isin(R,list('WKBPLS'))]='B'
    R[85:,90:208]='B'
    # 2) aura amarilla (componentes amarillos/naranjas abajo a la izquierda y fuera del logo)
    lab,n=nd.label(np.isin(R,list('YO')))
    for i in range(1,n+1):
        ys,xs=np.where(lab==i)
        if len(ys)<40 or ys.mean()>78 or xs.max()<16: R[lab==i]='B'
    lab,n=nd.label(np.isin(R,list('RD')))
    for i in range(1,n+1):
        if (lab==i).sum()<40: R[lab==i]='B'
    # 2b) estela: solo la mancha grande; fuera motas lilas sueltas
    lab,n=nd.label(np.isin(R,list('PLS')))
    if n:
        sz=nd.sum(np.ones_like(lab),lab,range(1,n+1))
        for i in range(1,n+1):
            if sz[i-1]<120: R[lab==i]='B'
    # 3) sin la estela morada (Josemi, 14 nov.: solo las letras de DRAGON BALL)
    R[np.isin(R,list('PLS'))]='B'
    col=np.isin(R,list('YORD'))
    # 4) negro solo pegado al logo (≤2 px) o encerrado
    near=nd.binary_dilation(col,iterations=2)
    encl=nd.binary_fill_holes(col|((R=='K')&near))
    keepK=(R=='K')&(near|encl)
    alpha=col|keepK
    R[~alpha]='.'
    # 5) contorno negro de 2 px alrededor de todo lo de color
    ring=nd.binary_dilation(alpha,iterations=2)&~alpha
    R[ring]='K'

    return R

# Letra de «DAIMA» en la foto: negra, recta, muy gruesa (trazo ≈6 px), huecos de 2 px y
# escalones de 2 px. Se dibuja en bloques de 2×2 (7×11 bloques = 14×22 px) sobre un rótulo
# blanco continuo con filo negro.
DAIMA = {
 'S': [".#####.", "#######", "###.###", "###....", "####...", ".#####.", "...####", "....###", "###.###", "#######", ".#####."],
 'U': ["###.###"] * 9 + ["#######", ".#####."],
 'R': ["######.", "#######", "###.###", "###.###", "#######", "######.", "###.###", "###.###", "###.###", "###.###", "###.###"],
 'V': ["###.###"] * 6 + [".#####."] * 2 + ["..###.."] * 3,
 'I': ["###"] * 11,
 'O': [".#####.", "#######"] + ["###.###"] * 7 + ["#######", ".#####."],
}


# Elegida por Josemi (14 nov., «este perfecto»): esquinas en diagonal, rebote y sombra tramada.
# Probadas y descartadas: esfera en la O (esfera=True) y aura de Super Saiyan (OPC_AURA=True).
OPC_SURVIVOR = {'chaflan': 2, 'rebote': 2, 'sombra': True}  # opciones del rótulo (chaflan, rebote, sombra, esfera)
OPC_AURA = False  # aura dorada de Super Saiyan detrás de todo el logo


def bola(diam):
    """Esfera del dragón como la O de DRAGON: aro amarillo, centro tramado a naranja, estrella roja."""
    r = diam / 2
    B = np.full((diam, diam), '.', dtype='<U1')
    bay = np.array([[0, 2], [3, 1]]) / 4 + 0.125
    for y in range(diam):
        for x in range(diam):
            d = np.hypot(x + 0.5 - r, y + 0.5 - r)
            if d <= r:
                if d > r - 2.2:
                    B[y, x] = 'Y'
                else:
                    f = (y + 0.5) / diam
                    q = 0.25 if f < 0.45 else 0.5 if f < 0.7 else 0.75
                    B[y, x] = 'O' if q > bay[y % 2, x % 2] else 'Y'
    pts = []
    for k in range(10):
        a = -np.pi / 2 + k * np.pi / 5
        rr = r * 0.58 if k % 2 == 0 else r * 0.24
        pts.append((r + rr * np.cos(a), r + 0.6 + rr * np.sin(a)))
    est = np.zeros((diam, diam), bool)
    for y in range(diam):
        for x in range(diam):
            px, py, dentro = x + 0.5, y + 0.5, False
            j = len(pts) - 1
            for i in range(len(pts)):
                (xi, yi), (xj, yj) = pts[i], pts[j]
                if (yi > py) != (yj > py) and px < (xj - xi) * (py - yi) / (yj - yi) + xi:
                    dentro = not dentro
                j = i
            est[y, x] = dentro
    B[est] = 'R'
    B[nd.binary_dilation(est) & ~est & (B != '.')] = 'D'
    return B


def rotulo_daima(texto, sep=2, bloque=2, blanco=4, filo=2, chaflan=0, rebote=0, sombra=False, esfera=False):
    """chaflan: corta las esquinas en diagonal (como DAIMA); rebote: sube/baja letras alternas;
    sombra: tramado gris azulado en la parte baja del rótulo blanco (como el tramado de DRAGON)."""
    H = len(DAIMA['S']) * bloque
    Wt = sum((H if (esfera and c == 'O') else len(DAIMA[c][0]) * bloque) for c in texto) + sep * (len(texto) - 1)
    pad = blanco + filo + 1 + rebote
    m = np.zeros((H + 2 * pad, Wt + 2 * pad), bool)
    x = pad
    bolas = []
    for i, c in enumerate(texto):
        filas = DAIMA[c]
        if esfera and c == 'O':   # la O es una esfera del dragón, como en DRAGON
            B = bola(H + 2)
            dy = (-rebote if i % 2 else rebote) if rebote else 0
            bolas.append((pad + dy - 1, x - 1, B))
            m[pad + dy - 1:pad + dy - 1 + B.shape[0], x - 1:x - 1 + B.shape[1]] |= B != '.'
            x += B.shape[1] - 2 + sep
            continue
        g = np.zeros((H, len(filas[0]) * bloque), bool)
        for y, fila in enumerate(filas):
            for xx, ch in enumerate(fila):
                if ch == '#':
                    g[y * bloque:(y + 1) * bloque, xx * bloque:(xx + 1) * bloque] = True
        if chaflan:
            g2 = np.pad(g, chaflan + 1)
            g2 = nd.binary_opening(g2, structure=nd.generate_binary_structure(2, 1), iterations=chaflan)
            g = g2[chaflan + 1:-chaflan - 1, chaflan + 1:-chaflan - 1]
        dy = (-rebote if i % 2 else rebote) if rebote else 0
        m[pad + dy:pad + dy + H, x:x + g.shape[1]] |= g
        x += g.shape[1] + sep
    R = np.full(m.shape, '.', dtype='<U1')
    w = nd.binary_dilation(m, iterations=blanco) & ~m
    w |= nd.binary_fill_holes(m | w) & ~m & ~w
    k = nd.binary_dilation(m | w, iterations=filo) & ~(m | w)
    R[k] = 'K'; R[w] = 'W'; R[m] = 'K'
    for (y0, x0, B) in bolas:
        sel = B != '.'
        sub = R[y0:y0 + B.shape[0], x0:x0 + B.shape[1]]
        sub[sel] = B[sel]
        borde = nd.binary_dilation(sel, iterations=1) & ~sel
        sub[borde] = 'K'
    if sombra:
        ys = np.where(w.any(1))[0]; y0, y1 = ys.min(), ys.max()
        bay = np.array([[0, 2], [3, 1]]) / 4 + 0.125
        for y in range(y0, y1 + 1):
            f = (y - y0) / max(1, y1 - y0)
            q = 0 if f < 0.6 else 0.25 if f < 0.75 else 0.5 if f < 0.88 else 0.75
            for xx in np.where(w[y])[0]:
                if q > bay[y % 2, xx % 2]:
                    R[y, xx] = 'G'
    return R


def aura(R, semilla=4):
    """Aura dorada de Super Saiyan: llamas que suben por detrás del logo, en pixel art tramado."""
    rnd = np.random.RandomState(semilla)
    mt, ml = 36, 10
    H, W = R.shape
    big = np.full((H + mt + 6, W + 2 * ml), '.', dtype='<U1'); big[mt:mt + H, ml:ml + W] = R
    A = big != '.'
    Hb, Wb = big.shape
    dist = nd.distance_transform_edt(~A)
    # alto de la llama por columna: dientes en sierra de anchura y altura variables
    llama = np.zeros(Wb)
    x = 0
    while x < Wb:
        w = rnd.randint(6, 14); h = rnd.randint(9, 32)
        for k in range(w):
            if x + k < Wb:
                llama[x + k] = h * (1 - abs(k - (w - 1) / 2) / ((w + 1) / 2)) ** 1.6
        x += w
    top = np.array([np.where(A[:, max(0, c - 3):c + 4].any(1))[0].min() if A[:, max(0, c - 3):c + 4].any() else Hb for c in range(Wb)])
    au = np.zeros_like(A); f = np.zeros(A.shape)
    for c in range(Wb):
        for y in range(Hb):
            if A[y, c]:
                continue
            if dist[y, c] <= 3:
                au[y, c] = True; f[y, c] = dist[y, c] / 3 * 0.45
            elif y < top[c] and top[c] - y <= llama[c] + 3 and top[c] < Hb:
                au[y, c] = True; f[y, c] = 0.45 + 0.55 * (top[c] - y - 3) / max(1, llama[c])
    bay = np.array([[0, 2], [3, 1]]) / 4 + 0.125
    for y, c in zip(*np.where(au)):
        v = f[y, c]; th = bay[y % 2, c % 2]
        if v < 0.3:
            big[y, c] = 'a' if v / 0.3 < th + 0.25 else 'b'
        elif v < 0.7:
            big[y, c] = 'b' if (v - 0.3) / 0.4 < th else 'c'
        else:
            big[y, c] = 'c'
    borde = nd.binary_dilation(au) & ~au & ~A
    big[borde] = 'e'
    return big


def montar(R):
    H, W = R.shape
    bay=np.array([[0,2],[3,1]])/4+0.125
    def tramar(a,b):
        m=np.isin(R,[a,b]);ok=m&~nd.binary_dilation(R=='K',iterations=2)
        fb=nd.uniform_filter(((R==b)&ok).astype(float),(3,15))/np.maximum(nd.uniform_filter(ok.astype(float),(3,15)),1e-6)
        q=np.select([fb<0.18,fb<0.38,fb<0.62,fb<0.85],[0,0.25,0.5,0.75],1.0)
        yy,xx=np.mgrid[0:H,0:W];th=bay[yy%2,xx%2]
        R[m]=np.where(q[m]>th[m],b,a)
    tramar('Y','O');tramar('R','D')
    # --- SURVIVOR con la letra de DAIMA (Josemi, 14 nov.: «como DAIMA, igualito»)
    S_ = rotulo_daima('SURVIVOR', **OPC_SURVIVOR)
    cx = int(np.median(np.where(np.isin(R, list('YORD')))[1]))
    fondo = np.where(np.isin(R, list('YORDK')))[0].max()
    ox = cx - S_.shape[1] // 2; oy = fondo - 4
    big = np.full((max(H, oy + S_.shape[0] + 2), max(W, ox + S_.shape[1])), '.', dtype='<U1'); big[:H, :W] = R
    m = S_ != '.'
    ys, xs = np.where(m); big[ys + oy, xs + ox] = S_[m]
    R = big
    if OPC_AURA:
        R = aura(R)
    CLEAN={'a':(255,250,190),'b':(255,226,40),'c':(255,160,16),'e':(214,96,8),'G':(176,190,232),'K':(16,12,20),'Y':(255,238,0),'O':(240,150,0),'R':(242,58,20),'D':(170,26,30),'W':(255,255,255),'P':(140,52,230),'L':(186,122,236),'S':(236,180,190)}
    out=np.zeros(R.shape+(4,),np.uint8)
    for k,v in CLEAN.items(): out[R==k]=v+(255,)
    ys,xs=np.where(out[:,:,3]>0);out=out[ys.min():ys.max()+1,xs.min():xs.max()+1]

    return out

def main():
    out = montar(limpiar(clasificar(muestrear())))
    im = Image.fromarray(out, "RGBA")
    destino = RAIZ / "ui" / "titulo.png"
    im.save(destino)
    js = RAIZ / "02 - Código del juego" / "ui_imagenes.js"
    texto = js.read_text(encoding="utf-8")
    uri = "data:image/png;base64," + base64.b64encode(destino.read_bytes()).decode()
    texto = re.sub(r'"titulo":"data:image/png;base64,[^"]*",', "", texto, count=1)
    texto = texto.replace("window.UI_IMG={", 'window.UI_IMG={"titulo":"' + uri + '",', 1)
    js.write_text(texto, encoding="utf-8")
    print(f"ui/titulo.png {im.width}×{im.height}")
    if "--zoom" in sys.argv:
        z = int(sys.argv[sys.argv.index("--zoom") + 1])
        bg = Image.new("RGBA", im.size, (40, 110, 230, 255)); bg.alpha_composite(im)
        bg.resize((im.width * z, im.height * z), Image.NEAREST).save(RAIZ / "herramientas" / "titulo_zoom.png")


if __name__ == "__main__":
    main()
