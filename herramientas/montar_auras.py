"""Recorta las auras blancas del poder máximo y genera 02 - Código del juego/auras_sprites.js (window.AURA_SPR).

Origen: 05 - Sprites nuevos encontrados/04_Assets_y_Objetos/03_Efectos_FX_y_Auras/DBZ_Auras_Todas_las_Fases_SWL_[JustOruma_Samuca0123].png
Uso: python herramientas/montar_auras.py   (necesita Pillow; en el Mac: ~/.dbsurvivor-venv/bin/python)
"""
import base64, io, json, os
from PIL import Image

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(RAIZ, '05 - Sprites nuevos encontrados/04_Assets_y_Objetos/03_Efectos_FX_y_Auras/DBZ_Auras_Todas_las_Fases_SWL_[JustOruma_Samuca0123].png')
DEST = os.path.join(RAIZ, '02 - Código del juego/auras_sprites.js')
# recuadros (izquierda, arriba, derecha, abajo) de cada fotograma en la hoja, centrados en la llama
CONTORNO = [(315, 40, 383, 110), (381, 40, 449, 110)]   # aura blanca de contorno (bucle)
LLENO = [(62, 17, 146, 105), (161, 17, 245, 105)]       # estallido blanco al empezar


def main():
    im = Image.open(SRC).convert('RGBA'); bg = im.getpixel((2, 2))

    def cut(b):
        c = im.crop(b); px = c.load()
        for y in range(c.size[1]):
            for x in range(c.size[0]):
                p = px[x, y]
                if abs(p[0] - bg[0]) + abs(p[1] - bg[1]) + abs(p[2] - bg[2]) < 30: px[x, y] = (0, 0, 0, 0)
        return c

    def tira(boxes):
        fs = [cut(b) for b in boxes]; w, h = fs[0].size; t = Image.new('RGBA', (w * len(fs), h))
        for i, f in enumerate(fs): t.alpha_composite(f, (i * w, 0))
        bio = io.BytesIO(); t.save(bio, 'PNG', optimize=True)
        return {'url': 'data:image/png;base64,' + base64.b64encode(bio.getvalue()).decode(), 'w': w, 'h': h, 'n': len(fs)}

    d = {'contorno': tira(CONTORNO), 'lleno': tira(LLENO)}
    with open(DEST, 'w', encoding='utf-8') as fh:
        fh.write('// Auras en sprites para el poder máximo (20 nov. 2026). Recortadas de\n'
                 '// 05 - Sprites nuevos encontrados/04_Assets_y_Objetos/03_Efectos_FX_y_Auras/DBZ_Auras_Todas_las_Fases_SWL_[JustOruma_Samuca0123].png\n'
                 '// (créditos en CREDITOS_RECURSOS.md). contorno: aura blanca de contorno en bucle; lleno: estallido al empezar.\n'
                 '// Generado por herramientas/montar_auras.py. No editar a mano.\n')
        fh.write('window.AURA_SPR=' + json.dumps(d, separators=(',', ':')) + ';\n')
    print('escrito', DEST)


if __name__ == '__main__':
    main()
