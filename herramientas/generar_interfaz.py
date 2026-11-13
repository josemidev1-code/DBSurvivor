"""Pixel art de la interfaz (13 nov. 2026): marcos de ventana (9 trozos), iconos
del menú principal y fondo de rayas de la pantalla de inicio.

Todo se dibuja aquí a tamaño nativo y se guarda en ui/interfaz/*.png; además
escribe «02 - Código del juego/interfaz.css» con las imágenes incrustadas
(data:) para que el juego siga abriéndose con doble clic.

    python herramientas/generar_interfaz.py [--zoom 6]   # --zoom: hoja ampliada en herramientas/interfaz_zoom.png
"""
import base64
import math
import sys
from pathlib import Path

from PIL import Image

RAIZ = Path(__file__).resolve().parent.parent
SAL = RAIZ / "ui" / "interfaz"


def hx(h, a=255):
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4)) + (a,)


TINTA = hx("#0a0d1a")
T = (0, 0, 0, 0)


class Lienzo:
    def __init__(self, w, h):
        self.im = Image.new("RGBA", (w, h), T)
        self.px = self.im.load()
        self.w, self.h = w, h

    def p(self, x, y, c):
        if 0 <= x < self.w and 0 <= y < self.h:
            self.px[x, y] = c

    def rect(self, x0, y0, x1, y1, c):
        for y in range(y0, y1 + 1):
            for x in range(x0, x1 + 1):
                self.p(x, y, c)

    def circ(self, cx, cy, r, c):
        for y in range(int(cy - r - 1), int(cy + r + 2)):
            for x in range(int(cx - r - 1), int(cx + r + 2)):
                if (x + 0.5 - cx) ** 2 + (y + 0.5 - cy) ** 2 <= r * r:
                    self.p(x, y, c)

    def poly(self, pts, c):
        ys = [q[1] for q in pts]
        for y in range(int(min(ys)), int(max(ys)) + 1):
            for x in range(self.w):
                if dentro(pts, x + 0.5, y + 0.5):
                    self.p(x, y, c)

    def sombrear(self, luz, sombra, borde=None):
        """Aclara los píxeles con hueco arriba/izquierda y oscurece abajo/derecha."""
        base = self.im.copy().load()
        for y in range(self.h):
            for x in range(self.w):
                c = base[x, y]
                if not c[3]:
                    continue
                arriba = y == 0 or base[x, y - 1][3] == 0 or (x > 0 and base[x - 1, y][3] == 0)
                abajo = y == self.h - 1 or base[x, y + 1][3] == 0 or (x < self.w - 1 and base[x + 1, y][3] == 0)
                if arriba and luz:
                    self.px[x, y] = mezcla(c, luz, 0.55)
                elif abajo and sombra:
                    self.px[x, y] = mezcla(c, sombra, 0.45)

    def contorno(self, c=TINTA):
        base = self.im.copy().load()
        for y in range(self.h):
            for x in range(self.w):
                if base[x, y][3]:
                    continue
                for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    xx, yy = x + dx, y + dy
                    if 0 <= xx < self.w and 0 <= yy < self.h and base[xx, yy][3] > 128:
                        self.px[x, y] = c
                        break


def dentro(pts, x, y):
    c = False
    j = len(pts) - 1
    for i in range(len(pts)):
        xi, yi = pts[i]
        xj, yj = pts[j]
        if (yi > y) != (yj > y) and x < (xj - xi) * (y - yi) / (yj - yi) + xi:
            c = not c
        j = i
    return c


def mezcla(a, b, f):
    return tuple(round(a[i] * (1 - f) + b[i] * f) for i in range(3)) + (255,)


BLANCO = hx("#ffffff")
NEGRO = hx("#000000")


# ---------------------------------------------------------------- marcos ----
def marco(borde, luz, sombra, interior, remache):
    """Marco de 18×18 para border-image (trozos de 6). Centro transparente."""
    L = Lienzo(18, 18)
    n = 18
    for i in range(n):
        for j in range(n):
            d = min(i, j, n - 1 - i, n - 1 - j)
            if d == 0:
                c = TINTA
            elif d == 1:
                # bisel: claro arriba/izquierda, oscuro abajo/derecha
                c = luz if (j == 1 or i == 1) and not (j == n - 2 or i == n - 2) else sombra
                if (i, j) in ((1, n - 2), (n - 2, 1)):
                    c = borde
            elif d == 2:
                c = borde
            elif d == 3:
                c = TINTA
            elif d == 4:
                c = interior
            elif d == 5:
                c = mezcla(interior, TINTA, 0.55)  # sin huecos entre el marco y el panel
            else:
                continue
            L.p(i, j, c)
    # esquinas recortadas (pixel art redondeado)
    for (x, y) in ((0, 0), (17, 0), (0, 17), (17, 17)):
        L.p(x, y, T)
    for (x, y) in ((1, 1), (16, 1), (1, 16), (16, 16)):
        L.p(x, y, TINTA)
    # remaches en las esquinas
    for (x, y) in ((2, 2), (14, 2), (2, 14), (14, 14)):
        L.rect(x, y, x + 1, y + 1, remache)
        L.p(x, y, BLANCO)
        L.p(x + 1, y + 1, sombra)
    return L.im


def marco_chip(borde, luz, sombra):
    """Marco pequeño de 12×12 (trozos de 4) para chips y botones."""
    L = Lienzo(12, 12)
    n = 12
    for i in range(n):
        for j in range(n):
            d = min(i, j, n - 1 - i, n - 1 - j)
            if d == 0:
                c = TINTA
            elif d == 1:
                c = luz if (j == 1 or i == 1) and not (j == n - 2 or i == n - 2) else sombra
            elif d == 2:
                c = borde
            elif d == 3:
                c = TINTA
            else:
                continue
            L.p(i, j, c)
    for (x, y) in ((0, 0), (11, 0), (0, 11), (11, 11)):
        L.p(x, y, T)
    return L.im


# ---------------------------------------------------------------- iconos ----
def icono_jugar():
    """Nube Kinton con estela."""
    L = Lienzo(24, 24)
    am, am2, nar = hx("#ffe14a"), hx("#ffc21a"), hx("#f08a0c")
    for (x, y, r) in ((7, 14, 4.5), (12, 11, 5.5), (17, 13, 4.5), (11, 16, 4), (16, 17, 3)):
        L.circ(x, y, r, am2)
    for (x, y, r) in ((7, 13, 3), (12, 10, 4), (17, 12, 3)):
        L.circ(x, y, r, am)
    # estela
    for i, y in enumerate((12, 15, 18)):
        L.rect(0, y, 3 - i, y, am2)
    L.sombrear(hx("#fff8c8"), nar)
    L.contorno()
    for (x, y) in ((10, 7), (11, 7), (10, 8)):
        L.p(x, y, BLANCO)
    return L.im


def icono_personajes():
    """Rastreador (scouter) con lente verde."""
    L = Lienzo(24, 24)
    gris, gris2 = hx("#c8ccd8"), hx("#8a90a6")
    verde, verde2 = hx("#6dff7a"), hx("#16b84a")
    # arco que rodea la oreja
    L.rect(14, 5, 17, 19, gris2)
    L.rect(15, 6, 16, 18, gris)
    L.circ(16, 12, 3.2, gris)
    L.circ(16, 12, 1.6, hx("#e4242a"))
    # brazo hacia la lente
    L.rect(5, 6, 15, 8, gris)
    # lente
    L.poly([(2, 7), (11, 7), (11, 15), (4, 15), (2, 12)], verde2)
    L.poly([(3, 8), (10, 8), (10, 13), (5, 13), (3, 11)], verde)
    L.sombrear(BLANCO, hx("#3a3f55"))
    L.contorno()
    for (x, y) in ((4, 9), (5, 9), (4, 10)):
        L.p(x, y, BLANCO)
    # retícula
    L.rect(7, 10, 9, 10, verde2)
    L.rect(8, 9, 8, 11, verde2)
    return L.im


def icono_mejoras():
    """Pesas de entrenamiento."""
    L = Lienzo(24, 24)
    metal, metal2 = hx("#a8b0c8"), hx("#5a6280")
    rojo, rojo2 = hx("#ff5a3a"), hx("#b81e10")
    L.rect(3, 11, 20, 13, metal)
    for x0 in (3, 17):
        L.rect(x0, 6, x0 + 3, 18, rojo)
    for x0 in (7, 14):
        L.rect(x0, 8, x0 + 2, 16, rojo2)
    L.rect(1, 10, 2, 14, metal2)
    L.rect(21, 10, 22, 14, metal2)
    L.sombrear(hx("#ffd0c0"), hx("#5a0a04"))
    L.contorno()
    L.p(4, 7, BLANCO)
    L.p(18, 7, BLANCO)
    return L.im


def icono_tienda():
    """Cápsula Hoi-Poi tumbada con la franja de la Corporación Cápsula."""
    L = Lienzo(24, 24)
    bl, az, az2 = hx("#f4f6ff"), hx("#3a7bff"), hx("#1a3fb0")
    L.circ(6, 12, 5, bl)
    L.circ(17, 12, 5, bl)
    L.rect(6, 7, 17, 16, bl)
    L.rect(10, 7, 13, 16, az)
    L.rect(19, 10, 22, 13, hx("#8a90a6"))
    L.sombrear(BLANCO, hx("#8a90b8"))
    L.contorno()
    L.rect(10, 7, 13, 7, hx("#9cc0ff"))
    L.rect(10, 16, 13, 16, az2)
    # botón
    L.rect(20, 11, 21, 12, hx("#ff3a3a"))
    for (x, y) in ((4, 9), (5, 8), (6, 8)):
        L.p(x, y, BLANCO)
    return L.im


def icono_capsulas():
    """Máquina de cápsulas: cúpula de cristal con bolitas y base roja."""
    L = Lienzo(24, 24)
    cristal = hx("#bfe8ff")
    L.circ(12, 9, 7, cristal)
    for (x, y, c) in ((9, 11, "#ffd23f"), (13, 12, "#ff5a8a"), (15, 9, "#6dff7a"), (10, 7, "#3a9bff"), (13, 7, "#ffd23f"), (8, 13, "#ff8a2a")):
        L.circ(x, y, 1.6, hx(c))
    L.rect(5, 15, 18, 21, hx("#e4342a"))
    L.rect(4, 15, 19, 16, hx("#ff6a4a"))
    L.rect(10, 18, 13, 20, hx("#2a1a3a"))
    L.sombrear(BLANCO, hx("#6a0a1a"))
    L.contorno()
    L.rect(16, 17, 17, 18, hx("#ffd23f"))
    for (x, y) in ((8, 4), (7, 5), (7, 6)):
        L.p(x, y, BLANCO)
    return L.im


def icono_misiones():
    """Radar del Dragón con la esfera parpadeando."""
    L = Lienzo(24, 24)
    L.rect(10, 1, 13, 4, hx("#a8b0c8"))
    L.circ(12, 13, 10, hx("#e8ecf6"))
    L.circ(12, 13, 7.5, hx("#1f8a3a"))
    L.sombrear(BLANCO, hx("#6a7090"))
    L.contorno()
    # rejilla
    for k in (-4, 0, 4):
        for t in range(-7, 8):
            if (t) ** 2 + k * k <= 52:
                L.p(12 + k, 13 + t, hx("#36c25a"))
                L.p(12 + t, 13 + k, hx("#36c25a"))
    L.rect(15, 9, 16, 10, hx("#ffd23f"))
    L.p(15, 9, BLANCO)
    L.p(11, 13, hx("#ff3a3a"))
    return L.im


def icono_ranking():
    """Copa del Torneo de las Artes Marciales."""
    L = Lienzo(24, 24)
    oro, oro2 = hx("#ffd23f"), hx("#e0901a")
    L.poly([(5, 3), (19, 3), (17, 11), (14, 14), (10, 14), (7, 11)], oro)
    L.rect(11, 14, 12, 17, oro2)
    L.rect(7, 18, 16, 19, oro)
    L.rect(6, 20, 17, 21, hx("#8a4a1a"))
    # asas
    for (x, y) in ((3, 5), (2, 6), (2, 7), (3, 8), (4, 9), (20, 5), (21, 6), (21, 7), (20, 8), (19, 9)):
        L.p(x, y, oro2)
    L.sombrear(hx("#fff6c0"), hx("#9a4a08"))
    L.contorno()
    # estrella
    for (x, y) in ((12, 6), (11, 7), (12, 7), (13, 7), (10, 8), (11, 8), (12, 8), (13, 8), (14, 8), (11, 9), (13, 9)):
        L.p(x, y, hx("#ff4a2a"))
    L.p(7, 4, BLANCO)
    L.p(8, 4, BLANCO)
    return L.im


def icono_ajustes():
    """Engranaje con el centro naranja."""
    L = Lienzo(24, 24)
    met = hx("#b8c0d8")
    L.circ(12, 12, 7, met)
    for k in range(8):
        a = k * math.pi / 4
        cx, cy = 12 + math.cos(a) * 8.5, 12 + math.sin(a) * 8.5
        L.rect(round(cx - 1.5), round(cy - 1.5), round(cx + 1), round(cy + 1), met)
    L.sombrear(BLANCO, hx("#4a5070"))
    L.contorno()
    L.circ(12, 12, 3.5, TINTA)
    L.circ(12, 12, 2.5, hx("#ff8a1a"))
    L.p(11, 11, hx("#ffd08a"))
    return L.im


ICONOS = {
    "menu_jugar": icono_jugar, "menu_personajes": icono_personajes, "menu_mejoras": icono_mejoras,
    "menu_tienda": icono_tienda, "menu_capsulas": icono_capsulas, "menu_misiones": icono_misiones,
    "menu_ranking": icono_ranking, "menu_ajustes": icono_ajustes,
}


# ------------------------------------------------------- fondo de rayas ----
def fondo_rayas(w=320, h=180):
    """Rayas diagonales azules y blancas (como la foto de Josemi). Se repite en horizontal."""
    import random
    rnd = random.Random(7)
    im = Image.new("RGBA", (w, h), hx("#1840c8"))
    px = im.load()
    # degradado vertical de fondo con tramado
    tonos = [hx("#2a64ff"), hx("#1d4fe0"), hx("#1840c8"), hx("#1232a8"), hx("#0c2488")]
    for y in range(h):
        t = y / (h - 1) * (len(tonos) - 1)
        i = int(t)
        f = t - i
        for x in range(w):
            c = tonos[min(i + (1 if (f > 0.5) ^ ((x + y) % 2 == 0 and 0.3 < f < 0.7) else 0), len(tonos) - 1)]
            px[x, y] = c
    # rayas: (color, grosor, cantidad)
    capas = [(hx("#0a0d1a"), (3, 8), 22), (hx("#5a8cff"), (2, 5), 28), (hx("#ffffff"), (2, 7), 20), (hx("#9ec0ff"), (1, 3), 30)]
    pend = -0.75  # inclinación (x por y)
    for col, (g0, g1), n in capas:
        for _ in range(n):
            x0 = rnd.randrange(w)
            y0 = rnd.randrange(h)
            largo = rnd.randrange(20, 90)
            g = rnd.randint(g0, g1)
            for t in range(largo):
                y = y0 + t
                if y >= h:
                    break
                for k in range(g):
                    x = (x0 + int(t * pend) + k) % w
                    px[x, y] = col
    return im


# -------------------------------------------------------------- montaje ----
def uri(im):
    import io
    b = io.BytesIO()
    im.save(b, "PNG")
    return "data:image/png;base64," + base64.b64encode(b.getvalue()).decode()


def main():
    SAL.mkdir(parents=True, exist_ok=True)
    marcos = {
        "marco": marco(hx("#f97316"), hx("#ffd28a"), hx("#9a3412"), hx("#2a3a8a"), hx("#ffd23f")),
        "marco_oro": marco(hx("#ffd23f"), hx("#fff6c0"), hx("#b45309"), hx("#7a3a08"), hx("#ffffff")),
        "marco_azul": marco(hx("#5a7cf0"), hx("#b8c8ff"), hx("#26338a"), hx("#141c50"), hx("#9ec0ff")),
        "chip": marco_chip(hx("#5a7cf0"), hx("#b8c8ff"), hx("#26338a")),
        "chip_oro": marco_chip(hx("#ffd23f"), hx("#fff6c0"), hx("#b45309")),
    }
    imgs = dict(marcos)
    for k, f in ICONOS.items():
        imgs[k] = f()
    imgs["fondo_rayas"] = fondo_rayas()
    for k, im in imgs.items():
        im.save(SAL / f"{k}.png")

    css = ["/* Generado por herramientas/generar_interfaz.py: marcos y fondo pixel art incrustados. */", ":root{"]
    for k in list(marcos) + ["fondo_rayas"]:
        css.append(f"  --px-{k.replace('_', '-')}:url({uri(imgs[k])});")
    css.append("}")
    (RAIZ / "02 - Código del juego" / "interfaz.css").write_text("\n".join(css) + "\n", encoding="utf-8")

    # iconos del menú en ui_imagenes.js (para <img data-ui> y el menú)
    import re
    js = RAIZ / "02 - Código del juego" / "ui_imagenes.js"
    texto = js.read_text(encoding="utf-8")
    for k in ICONOS:
        texto = re.sub(r'"' + k + r'":"data:image/png;base64,[^"]*",', "", texto, count=1)
        texto = texto.replace("window.UI_IMG={", 'window.UI_IMG={"' + k + '":"' + uri(imgs[k]) + '",', 1)
    js.write_text(texto, encoding="utf-8")
    print(f"{len(imgs)} imágenes en ui/interfaz; interfaz.css y ui_imagenes.js actualizados.")

    if "--zoom" in sys.argv:
        z = int(sys.argv[sys.argv.index("--zoom") + 1])
        hoja = Image.new("RGBA", (8 * 30 + 6 * 22 + 10, 34), hx("#202840"))
        x = 4
        for k in ICONOS:
            hoja.alpha_composite(imgs[k], (x, 5))
            x += 30
        for k in marcos:
            hoja.alpha_composite(imgs[k], (x, 5))
            x += 22
        hoja = hoja.resize((hoja.width * z, hoja.height * z), Image.NEAREST)
        hoja.save(RAIZ / "herramientas" / "interfaz_zoom.png")
        imgs["fondo_rayas"].resize((640, 360), Image.NEAREST).save(RAIZ / "herramientas" / "interfaz_fondo.png")


if __name__ == "__main__":
    main()
