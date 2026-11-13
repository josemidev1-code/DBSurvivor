"""Dibuja el título de la pantalla de inicio en pixel art: «DRAGON BALL» con la
esfera de cuatro estrellas en la O y «SURVIVOR» debajo (estilo de la foto que
mandó Josemi). Sale a ui/titulo.png a tamaño nativo; el juego lo amplía sin
suavizar. También lo incrusta como «titulo» en ui_imagenes.js (sin tocar el
resto: montar_objetos.py volvería a recortar los iconos redibujados).

    python herramientas/generar_titulo.py [--zoom 6]   # --zoom guarda también una vista ampliada
"""
import math
import sys
from pathlib import Path

from PIL import Image

RAIZ = Path(__file__).resolve().parent.parent

# Letras de 8×12 (las estrechas, menos). «#» = relleno.
G = {
 "D": ["######..", "#######.", "###..###", "###...##", "###...##", "###...##",
       "###...##", "###...##", "###...##", "###..###", "#######.", "######.."],
 "R": ["######..", "#######.", "###..###", "###..###", "###..###", "#######.",
       "######..", "###.###.", "###..###", "###..###", "###..###", "###..###"],
 "A": ["..####..", ".######.", "###..###", "###..###", "###..###", "########",
       "########", "###..###", "###..###", "###..###", "###..###", "###..###"],
 "G": [".######.", "########", "###..###", "###.....", "###.....", "###.####",
       "###.####", "###..###", "###..###", "###..###", "########", ".######."],
 "N": ["###..###", "####.###", "####.###", "########", "########", "###.####",
       "###.####", "###..###", "###..###", "###..###", "###..###", "###..###"],
 "B": ["######..", "#######.", "###..###", "###..###", "###.###.", "######..",
       "#######.", "###..###", "###..###", "###..###", "########", "#######."],
 "L": ["###.....", "###.....", "###.....", "###.....", "###.....", "###.....",
       "###.....", "###.....", "###.....", "###.....", "########", "########"],
 "S": [".######.", "########", "###..###", "###.....", "####....", ".######.",
       "..######", "....####", ".....###", "###..###", "########", ".######."],
 "U": ["###..###", "###..###", "###..###", "###..###", "###..###", "###..###",
       "###..###", "###..###", "###..###", "###..###", "########", ".######."],
 "V": ["###...###", "###...###", "###...###", "###...###", "###...###", "###...###",
       ".###.###.", ".###.###.", "..#####..", "..#####..", "...###...", "...###..."],
 "I": ["###", "###", "###", "###", "###", "###", "###", "###", "###", "###", "###", "###"],
 "O": [".######.", "########", "###..###", "###..###", "###..###", "###..###",
       "###..###", "###..###", "###..###", "###..###", "########", ".######."],
}

NEGRO = (16, 10, 24, 255)
SOMBRA = (58, 18, 4, 255)


def hexc(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4)) + (255,)


AMARILLO = [hexc(c) for c in ("#fff6a8", "#ffe63a", "#ffd21f", "#ffb31a", "#f58a0c")]
ROJO = [hexc(c) for c in ("#ffb07a", "#ff6a2a", "#f2421a", "#d8240f", "#a8140a")]
BLANCO = [hexc(c) for c in ("#ffffff", "#ffffff", "#eef0ff", "#d8dcf2", "#b9bfe0")]
MORADO = [hexc(c) for c in ("#c06cff", "#9a4ae8", "#7a33c8", "#5a2496")]
ESFERA = [hexc(c) for c in ("#fff0b0", "#ffd04a", "#ffb21a", "#f58a0c", "#c8640a")]
ESTRELLA = hexc("#e4241a")
ESTRELLA_OSC = hexc("#9a1208")


def bitmap(letra, alto, escala_x):
    """Glifo ampliado: ancho ×escala_x y estirado (vecino más cercano) a `alto`."""
    filas = G[letra]
    w = len(filas[0]) * escala_x
    out = []
    for y in range(alto):
        fy = min(len(filas) - 1, int(y * len(filas) / alto))
        out.append([filas[fy][x // escala_x] == "#" for x in range(w)])
    return out


def degradado(paleta, t, x, y):
    """Color de la paleta para t∈[0,1] con tramado en damero entre tonos."""
    pos = t * (len(paleta) - 1)
    i = int(pos)
    f = pos - i
    if i >= len(paleta) - 1:
        return paleta[-1]
    # 3 niveles de tramado: <0.33 tono i, 0.33-0.66 damero, >0.66 tono i+1
    if f < 0.33:
        return paleta[i]
    if f > 0.66:
        return paleta[i + 1]
    return paleta[i] if (x + y) % 2 == 0 else paleta[i + 1]


def esfera(img, cx, cy, r):
    """Esfera del dragón de cuatro estrellas (centrada en cx, cy)."""
    px = img.load()
    for y in range(cy - r, cy + r + 1):
        for x in range(cx - r, cx + r + 1):
            d = math.hypot(x - cx + 0.5, y - cy + 0.5)
            if d <= r:
                # luz desde arriba a la izquierda
                t = min(1, max(0, (math.hypot(x - (cx - r * 0.35), y - (cy - r * 0.35)) / (r * 1.6))))
                px[x, y] = degradado(ESFERA, t, x, y)
    # estrella de cinco puntas en el centro
    R, ri = r * 0.62, r * 0.26
    pts = []
    for k in range(10):
        a = -math.pi / 2 + k * math.pi / 5
        rr = R if k % 2 == 0 else ri
        pts.append((cx + rr * math.cos(a), cy + 0.6 + rr * math.sin(a)))

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
    for y in range(cy - r, cy + r + 1):
        for x in range(cx - r, cx + r + 1):
            if dentro(x + 0.5, y + 0.5):
                px[x, y] = ESTRELLA if y < cy + 1 else ESTRELLA_OSC
    # brillo
    for (dx, dy) in ((-r // 2, -r // 2), (-r // 2 + 1, -r // 2), (-r // 2, -r // 2 + 1)):
        px[cx + dx, cy + dy] = (255, 255, 255, 255)


def contorno(img, grosor, color):
    """Pinta `color` alrededor de lo opaco (grosor en píxeles, 8 vecinos)."""
    base = img.copy()
    bp = base.load()
    px = img.load()
    W, H = img.size
    for y in range(H):
        for x in range(W):
            if bp[x, y][3]:
                continue
            hit = False
            for dy in range(-grosor, grosor + 1):
                for dx in range(-grosor, grosor + 1):
                    xx, yy = x + dx, y + dy
                    if 0 <= xx < W and 0 <= yy < H and bp[xx, yy][3]:
                        hit = True
                        break
                if hit:
                    break
            if hit:
                px[x, y] = color


def palabra(texto, alto_base, arco, escala_x, paleta, sep=1, esfera_en=None):
    """Capa RGBA con la palabra; las letras crecen hacia el centro (arco)."""
    n = len(texto)
    altos = []
    for i in range(n):
        u = (i - (n - 1) / 2) / max(1, (n - 1) / 2)  # -1..1
        altos.append(round(alto_base + arco * (1 - u * u)))
    H = max(altos)
    anchos = [len(G[c][0]) * escala_x if c != esfera_en else 0 for c in texto]
    # la esfera ocupa un hueco cuadrado del alto de su letra
    for i, c in enumerate(texto):
        if i == esfera_en:
            anchos[i] = altos[i]
    W = sum(anchos) + sep * (n - 1)
    img = Image.new("RGBA", (W, H + 2), (0, 0, 0, 0))
    px = img.load()
    x0 = 0
    for i, c in enumerate(texto):
        h = altos[i]
        top = (H - h) // 2  # centradas: crecen arriba y abajo
        if i == esfera_en:
            r = h // 2
            esfera(img, x0 + r, top + r, r)
        else:
            bm = bitmap(c, h, escala_x)
            for y, fila in enumerate(bm):
                for x, on in enumerate(fila):
                    if on:
                        t = y / max(1, h - 1)
                        col = degradado(paleta, t, x0 + x, top + y)
                        # filo de luz arriba
                        if y == 0 or not bm[y - 1][x]:
                            col = paleta[0]
                        px[x0 + x, top + y] = col
        x0 += anchos[i] + sep
    return img


def con_marco(img, grosor=2):
    W, H = img.size
    m = grosor + 2
    out = Image.new("RGBA", (W + 2 * m, H + 2 * m), (0, 0, 0, 0))
    out.alpha_composite(img, (m, m))
    contorno(out, grosor, NEGRO)
    return out


def sombra(img, dx, dy, color):
    W, H = img.size
    out = Image.new("RGBA", (W + dx, H + dy), (0, 0, 0, 0))
    mask = Image.new("RGBA", img.size, color)
    out.paste(mask, (dx, dy), img.split()[3])
    out.alpha_composite(img, (0, 0))
    return out


def estela(W, H):
    """Pincelada morada en diagonal detrás de BALL, que se deshace hacia la derecha."""
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    px = img.load()
    for y in range(H):
        for x in range(W):
            # banda inclinada
            off = (H - y) * 0.6
            u = (x - off) / W
            if u < 0 or u > 1:
                continue
            t = y / max(1, H - 1)
            col = degradado(MORADO, t, x, y)
            # se deshace a la derecha: tramado de huecos
            if u > 0.7 and ((x // 2 + y) % 3 == 0 or (u > 0.85 and (x + y) % 2)):
                continue
            # rayas horizontales sueltas a la derecha
            if u > 0.55 and y % 4 == 3:
                continue
            px[x, y] = col
    return img


def incrustar(png):
    import base64
    import re
    js = RAIZ / "02 - Código del juego" / "ui_imagenes.js"
    texto = js.read_text(encoding="utf-8")
    uri = "data:image/png;base64," + base64.b64encode(png.read_bytes()).decode()
    texto = re.sub(r'"titulo":"data:image/png;base64,[^"]*",', "", texto, count=1)
    texto = texto.replace("window.UI_IMG={", 'window.UI_IMG={"titulo":"' + uri + '",', 1)
    js.write_text(texto, encoding="utf-8")


def main():
    escala = 2  # cada «píxel» de letra = 2 px nativos
    dragon = palabra("DRAGON", 26, 6, escala, AMARILLO, sep=1, esfera_en=4)
    ball = palabra("BALL", 28, 3, escala, ROJO, sep=1)
    dragon = con_marco(dragon, 2)
    ball = con_marco(ball, 2)
    surv = con_marco(palabra("SURVIVOR", 12, 0, 1, BLANCO, sep=1), 2)

    gap = -2
    W1 = dragon.width + gap + ball.width
    H1 = max(dragon.height, ball.height)
    fila = Image.new("RGBA", (W1 + 24, H1 + 8), (0, 0, 0, 0))
    # estela morada detrás de BALL
    est = estela(ball.width + 26, int(ball.height * 0.62))
    fila.alpha_composite(est, (dragon.width + gap - 4, (H1 - est.height) // 2 - 2))
    fila.alpha_composite(dragon, (0, (H1 - dragon.height) // 2))
    fila.alpha_composite(ball, (dragon.width + gap, (H1 - ball.height) // 2))

    # SURVIVOR montado sobre la parte de abajo, centrado
    W = fila.width
    H = fila.height + surv.height - 10
    out = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    out.alpha_composite(fila, (0, 0))
    out.alpha_composite(surv, ((W1 - surv.width) // 2 + 6, fila.height - 14))
    out = sombra(out, 2, 2, SOMBRA)
    out = out.crop(out.getbbox())

    destino = RAIZ / "ui" / "titulo.png"
    out.save(destino)
    print(f"ui/titulo.png {out.size[0]}×{out.size[1]}")
    incrustar(destino)
    if "--zoom" in sys.argv:
        z = int(sys.argv[sys.argv.index("--zoom") + 1])
        fondo = Image.new("RGBA", out.size, (40, 90, 200, 255))
        fondo.alpha_composite(out)
        fondo.resize((out.width * z, out.height * z), Image.NEAREST).save(RAIZ / "herramientas" / "titulo_zoom.png")


if __name__ == "__main__":
    main()
