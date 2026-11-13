"""SUSTITUIDO (13 nov.): el título actual sale de herramientas/titulo_desde_foto.py.
No ejecutar este: sobrescribiría ui/titulo.png con la versión dibujada a mano.

Título de la pantalla de inicio en pixel art, copiando el logo de la foto que
mandó Josemi («DRAGON BALL DAIMA», estilo.png) con «SURVIVOR» en lugar de DAIMA.

Rasgos de la foto que se reproducen:
- Letras altas y estrechas; DRAGON baja de tamaño hacia la esfera y BALL vuelve
  a crecer hacia la derecha (forma de «V» suave), con la parte de arriba de cada
  letra cortada en diagonal siguiendo esa línea.
- DRAGON: amarillo plano arriba y tramado en damero hacia naranja abajo.
  BALL: rojo anaranjado arriba y tramado hacia rojo oscuro abajo.
- Contorno negro grueso; los huecos de las letras quedan negros.
- La O es una esfera del dragón naranja con aro amarillo y estrella roja.
- Pincelada lila/morada detrás de BALL, que sube hacia la derecha y se deshace.
- Rótulo de abajo en letras negras con borde blanco y filo negro (como DAIMA),
  y chispas amarillas a la izquierda.

Sale a ui/titulo.png a tamaño nativo y se incrusta como «titulo» en
ui_imagenes.js (sin tocar el resto: montar_objetos.py volvería a recortar los
iconos redibujados).

    python herramientas/generar_titulo.py [--zoom 4]   # --zoom guarda también herramientas/titulo_zoom.png
"""
import base64
import math
import re
import sys
from pathlib import Path

from PIL import Image

RAIZ = Path(__file__).resolve().parent.parent


def hexc(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4)) + (255,)


NEGRO = hexc("#0a0a12")
BLANCO = hexc("#ffffff")
T = (0, 0, 0, 0)

# Letras grandes: 8×16, trazo de 3.
G16 = {
 "D": ["######..", "#######.", "###.####"] + ["###..###"] * 10 + ["###.####", "#######.", "######.."],
 "R": ["######..", "#######.", "###.####"] + ["###..###"] * 3 + ["###.####", "#######.", "######..", "###.###.", "###.####"] + ["###..###"] * 5,
 "A": ["..####..", ".######."] + ["###..###"] * 7 + ["########", "########"] + ["###..###"] * 5,
 "G": [".######.", "########", "###..###"] + ["###....."] * 4 + ["###.####", "###.####"] + ["###..###"] * 5 + ["########", ".######."],
 "N": ["###..###", "####.###", "####.###", "########", "########", "###.####", "###.####"] + ["###..###"] * 9,
 "B": ["######..", "#######.", "###.####"] + ["###..###"] * 3 + ["###.###.", "######..", "#######.", "###.####"] + ["###..###"] * 4 + ["########", "#######."],
 "L": ["###....."] * 14 + ["########", "########"],
}

# Letras del rótulo: 7×9, anchas como las de DAIMA.
G9 = {
 "S": [".#####.", "##...##", "##.....", ".####..", "...###.", ".....##", "##...##", "##...##", ".#####."],
 "U": ["##...##"] * 7 + ["##...##", ".#####."],
 "R": ["######.", "##...##", "##...##", "##...##", "######.", "##.##..", "##..##.", "##...##", "##...##"],
 "V": ["##...##"] * 5 + [".##.##.", ".##.##.", "..###..", "...#..."],
 "I": ["####"] + [".##."] * 7 + ["####"],
 "O": [".#####.", "##...##", "##...##", "##...##", "##...##", "##...##", "##...##", "##...##", ".#####."],
}


def damero(a, b, f, x, y):
    """Tramado ordenado 2×2 entre a y b (f = 0..1)."""
    umbral = [[0.125, 0.625], [0.875, 0.375]][y % 2][x % 2]
    return b if f > umbral else a


class Capa:
    def __init__(self, w, h):
        self.im = Image.new("RGBA", (w, h), T)
        self.px = self.im.load()
        self.w, self.h = w, h

    def p(self, x, y, c):
        if 0 <= x < self.w and 0 <= y < self.h:
            self.px[x, y] = c

    def get(self, x, y):
        if 0 <= x < self.w and 0 <= y < self.h:
            return self.px[x, y]
        return T


def contorno(img, grosor, color):
    base = img.copy().load()
    px = img.load()
    W, H = img.size
    for y in range(H):
        for x in range(W):
            if base[x, y][3]:
                continue
            for dy in range(-grosor, grosor + 1):
                hit = False
                for dx in range(-grosor, grosor + 1):
                    if abs(dx) + abs(dy) > grosor + (1 if grosor > 1 else 0):
                        continue
                    xx, yy = x + dx, y + dy
                    if 0 <= xx < W and 0 <= yy < H and base[xx, yy][3]:
                        hit = True
                        break
                if hit:
                    px[x, y] = color
                    break


def rellenar_huecos(img, color):
    """Pinta de `color` los huecos transparentes encerrados (los ojos de las letras)."""
    W, H = img.size
    px = img.load()
    fuera = set()
    pila = [(x, y) for x in range(W) for y in (0, H - 1)] + [(x, y) for y in range(H) for x in (0, W - 1)]
    while pila:
        x, y = pila.pop()
        if (x, y) in fuera or not (0 <= x < W and 0 <= y < H) or px[x, y][3]:
            continue
        fuera.add((x, y))
        pila += [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
    for y in range(H):
        for x in range(W):
            if not px[x, y][3] and (x, y) not in fuera:
                px[x, y] = color


# ----------------------------------------------------------------- palabra ----
AMA_ARRIBA, AMA_MEDIO, AMA_ABAJO = hexc("#fff21c"), hexc("#ffc80a"), hexc("#ff9000")
ROJO_ARRIBA, ROJO_MEDIO, ROJO_ABAJO = hexc("#ff4a12"), hexc("#f2300c"), hexc("#b81808")


def color_letra(paleta, t, x, y):
    """t: 0 arriba, 1 abajo. Mitad de arriba plana, abajo tramado en dos pasos."""
    arriba, medio, abajo = paleta
    if t < 0.5:
        return arriba
    if t < 0.75:
        return damero(arriba, medio, (t - 0.5) / 0.25, x, y)
    return damero(medio, abajo, min(1, (t - 0.75) / 0.2), x, y)


def letra(c, alto, escala=2):
    filas = G16[c]
    w = len(filas[0]) * escala
    return [[filas[min(15, int(y * 16 / alto))][x // escala] == "#" for x in range(w)] for y in range(alto)], w


def esfera(capa, cx, cy, r):
    aro, cuerpo, cuerpo2 = hexc("#ffd21a"), hexc("#ff9a0c"), hexc("#f07a08")
    for y in range(int(cy - r - 1), int(cy + r + 2)):
        for x in range(int(cx - r - 1), int(cx + r + 2)):
            d = math.hypot(x + 0.5 - cx, y + 0.5 - cy)
            if d <= r:
                if d > r - 2.2:
                    c = aro
                else:
                    c = damero(cuerpo, cuerpo2, max(0, (y - cy) / r), x, y)
                capa.p(x, y, c)
    # estrella roja con filo oscuro
    R, ri = r * 0.6, r * 0.25
    pts = []
    for k in range(10):
        a = -math.pi / 2 + k * math.pi / 5
        rr = R if k % 2 == 0 else ri
        pts.append((cx + rr * math.cos(a), cy + 0.5 + rr * math.sin(a)))

    def dentro(x, y):
        c = False
        j = len(pts) - 1
        for i in range(len(pts)):
            xi, yi = pts[i]
            xj, yj = pts[j]
            if (yi > y) != (yj > y) and x < (xj - xi) * (y - yi) / (yj - yi) + xi:
                c = not c
            j = i
        return c
    estrella = Capa(capa.w, capa.h)
    for y in range(int(cy - r), int(cy + r + 1)):
        for x in range(int(cx - r), int(cx + r + 1)):
            if dentro(x + 0.5, y + 0.5):
                estrella.p(x, y, hexc("#e8201a"))
    contorno(estrella.im, 1, hexc("#8a0c06"))
    capa.im.alpha_composite(estrella.im)


def fila_logo():
    """DRAGON + esfera + BALL con alturas en V y tapas en diagonal."""
    esc = 2
    sep = 3
    # altura de cada letra en su lado izquierdo y derecho (nativo)
    plan = [("D", 46, 44), ("R", 43, 41), ("A", 40, 38), ("G", 37, 35), ("O", 0, 0), ("N", 35, 37),
            None, ("B", 40, 43), ("A", 44, 47), ("L", 48, 51), ("L", 52, 55)]
    hueco_palabras = 7
    r_esfera = 16
    base = 64  # línea de abajo de DRAGON (BALL sube un poco hacia la derecha)
    W = 300
    capa = Capa(W, base + 8)
    x = 4
    cajas = []
    for item in plan:
        if item is None:
            x += hueco_palabras - sep
            continue
        c, h0, h1 = item
        if c == "O":
            cx = x + r_esfera
            esfera(capa, cx, base - r_esfera - 1, r_esfera)
            x += 2 * r_esfera + sep
            continue
        roja = len(cajas) >= 5
        paleta = (ROJO_ARRIBA, ROJO_MEDIO, ROJO_ABAJO) if roja else (AMA_ARRIBA, AMA_MEDIO, AMA_ABAJO)
        hmax = max(h0, h1)
        bm, w = letra(c, hmax, esc)
        subida = 0 if not roja else round((x - 170) * 0.06)  # BALL: la base sube hacia la derecha
        b = base - max(0, subida)
        for col in range(w):
            hcol = h0 + (h1 - h0) * col / max(1, w - 1)
            corte = hmax - round(hcol)  # filas de arriba que se recortan (tapa en diagonal)
            for fy in range(corte, hmax):
                if bm[fy][col]:
                    y = b - hmax + fy
                    t = (fy - corte) / max(1, hmax - corte - 1)
                    capa.p(x + col, y, color_letra(paleta, t, x + col, y))
        cajas.append((c, x, w))
        x += w + sep
    img = capa.im.crop(capa.im.getbbox())
    marco = Image.new("RGBA", (img.width + 8, img.height + 8), T)
    marco.alpha_composite(img, (4, 4))
    rellenar_huecos(marco, NEGRO)
    contorno(marco, 2, NEGRO)
    return marco, cajas


# ------------------------------------------------------------------ estela ----
def estela(w, h):
    """Pincelada lila → morada que sube hacia la derecha y se deshace en el extremo."""
    capa = Capa(w, h)
    cols = [hexc("#f0b4e6"), hexc("#d890f0"), hexc("#b468ff"), hexc("#9044f0"), hexc("#7428d8")]
    for x in range(w):
        u = x / (w - 1)
        top = round(h * 0.42 * (1 - u))            # el borde de arriba sube a la derecha
        bot = round(h - 1 - h * 0.30 * u)
        for y in range(top, bot + 1):
            # rayas horizontales que asoman por los bordes (trazo de pincel)
            if (y - top < 2 or bot - y < 2) and (x // 3 + y) % 4 == 0:
                continue
            if u > 0.78:
                hueco = (u - 0.78) / 0.22
                if ((x * 7 + y * 13) % 10) / 10 < hueco or y % 3 == 0 and u > 0.86:
                    continue
            f = u * (len(cols) - 1)
            i = min(len(cols) - 2, int(f))
            capa.p(x, y, damero(cols[i], cols[i + 1], f - i, x, y))
    return capa.im


# ------------------------------------------------------------------ rótulo ----
def rotulo(texto):
    """Letras negras con borde blanco y filo negro, como «DAIMA»."""
    esc_x, sep = 2, 2
    ancho = sum(len(G9[c][0]) * esc_x for c in texto) + sep * (len(texto) - 1)
    alto = 9 * 2
    capa = Capa(ancho + 12, alto + 12)
    x = 6
    for c in texto:
        filas = G9[c]
        for y in range(alto):
            for col in range(len(filas[0]) * esc_x):
                if filas[y // 2][col // esc_x] == "#":
                    capa.p(x + col, 6 + y, NEGRO)
        x += len(filas[0]) * esc_x + sep
    contorno(capa.im, 2, BLANCO)
    rellenar_huecos(capa.im, BLANCO)
    contorno(capa.im, 1, NEGRO)
    return capa.im.crop(capa.im.getbbox())


def chispas(w, h):
    """Picos amarillos del aura (como los de la foto a la izquierda de DAIMA)."""
    capa = Capa(w, h)

    def tri(pts, c):
        ys = [p[1] for p in pts]
        for y in range(int(min(ys)), int(max(ys)) + 1):
            for x in range(w):
                px, py = x + 0.5, y + 0.5
                s = 0
                for i in range(3):
                    (x1, y1), (x2, y2) = pts[i], pts[(i + 1) % 3]
                    s += (x2 - x1) * (py - y1) - (y2 - y1) * (px - x1) > 0
                if s in (0, 3):
                    capa.p(x, y, c)
    ama, blanco = hexc("#fff21c"), hexc("#fffbd0")
    # tres picos que salen de la derecha hacia la izquierda y abajo
    for (bx, by, tx, ty, g) in ((w - 1, 3, 1, h - 3, 5), (w - 1, 9, 8, h - 1, 4), (w - 3, 0, 4, 4, 3)):
        tri([(bx, by - g / 2), (bx, by + g / 2), (tx, ty)], ama)
        tri([(bx, by - g / 5), (bx, by + g / 5), ((bx + tx) / 2, (by + ty) / 2)], blanco)
    contorno(capa.im, 1, hexc("#e07a00"))
    return capa.im


# ----------------------------------------------------------------- montaje ----
def incrustar(png):
    js = RAIZ / "02 - Código del juego" / "ui_imagenes.js"
    texto = js.read_text(encoding="utf-8")
    uri = "data:image/png;base64," + base64.b64encode(png.read_bytes()).decode()
    texto = re.sub(r'"titulo":"data:image/png;base64,[^"]*",', "", texto, count=1)
    texto = texto.replace("window.UI_IMG={", 'window.UI_IMG={"titulo":"' + uri + '",', 1)
    js.write_text(texto, encoding="utf-8")


def main():
    fila, cajas = fila_logo()
    # posiciones útiles: inicio de la G y de la B
    xg = next(x for c, x, w in cajas if c == "G")
    xn = next(x for c, x, w in cajas if c == "N")
    xb = next(x for c, x, w in cajas if c == "B")
    est = estela(fila.width - xg + 14, int(fila.height * 0.62))
    rot = rotulo("SURVIVOR")
    ch = chispas(34, 20)

    W = fila.width + 14
    H = fila.height + rot.height - 8
    out = Image.new("RGBA", (W, H), T)
    out.alpha_composite(est, (xg + 6, 2))
    out.alpha_composite(fila, (0, 0))
    rx = xn + 4 - rot.width // 2  # centrado bajo la N, como DAIMA en la foto
    ry = fila.height - 7
    out.alpha_composite(ch, (rx - ch.width + 2, ry + 2))
    out.alpha_composite(rot, (rx, ry))
    out = out.crop(out.getbbox())

    destino = RAIZ / "ui" / "titulo.png"
    out.save(destino)
    print(f"ui/titulo.png {out.size[0]}×{out.size[1]}")
    incrustar(destino)
    if "--zoom" in sys.argv:
        z = int(sys.argv[sys.argv.index("--zoom") + 1])
        fondo = Image.new("RGBA", out.size, (40, 110, 230, 255))
        fondo.alpha_composite(out)
        fondo.resize((out.width * z, out.height * z), Image.NEAREST).save(RAIZ / "herramientas" / "titulo_zoom.png")


if __name__ == "__main__":
    main()
