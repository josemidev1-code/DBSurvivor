"""Descarga los personajes y planetas de https://dragonball-api.com (API pública y gratuita) a herramientas/dbapi/.

Uso:  python herramientas/descargar_dbapi.py
Solo hace falta volver a lanzarlo si la API añade personajes; el resto de herramientas leen el JSON guardado.
"""
import json, os, urllib.request

BASE = 'https://dragonball-api.com/api'
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'dbapi')


def get(url):
    with urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'dbsurvivor-dex'}), timeout=30) as r:
        return json.load(r)


def main():
    os.makedirs(OUT, exist_ok=True)
    lista = get(BASE + '/characters?limit=200')['items']
    pjs = []
    for c in lista:
        d = get(f"{BASE}/characters/{c['id']}")
        pjs.append(d)
        print(d['id'], d['name'], len(d.get('transformations') or []))
    json.dump(pjs, open(os.path.join(OUT, 'personajes.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    json.dump(get(BASE + '/planets?limit=200')['items'], open(os.path.join(OUT, 'planetas.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)


if __name__ == '__main__':
    main()
