# DB Survivor Dex

Ficha de cada personaje jugable al estilo de PMD Sprite Collab y PokéAPI. Sirve de **referencia para mejorar las animaciones**.

- **Abrir:** doble clic en `03 - Dex/index.html`. Funciona sin servidor, porque lee los sprites de `02 - Código del juego/animaciones_juego.js`.
- **Lista:** cada personaje muestra su retrato, su rareza y 13 puntos, uno por animación: verde si está animada, amarillo si tiene 1 solo fotograma y rojo si falta.
  - Se puede filtrar por estado (completa, casi, a medias, poca), por rareza, por raza y por **«Le falta: …»**. Por ejemplo, «Le falta: Patada 2» enseña todas las formas que no la tienen.
  - Se puede ordenar por número, nombre, poder de pelea o «menos animados».
- **Ficha:** las 13 animaciones de cada forma, en movimiento y con su número de fotogramas. Las que faltan salen apagadas, con la guardia en su lugar. También trae las estadísticas del juego, el poder de pelea, la raza, el bando, el planeta y el comando de Piskel.
- **API propia:** `03 - Dex/api/v1/personaje/index.json` y `03 - Dex/api/v1/personaje/<id>.json`, en JSON al estilo de PokéAPI.

## Regenerar

Hazlo después de tocar animaciones o personajes:

1. `python herramientas/generar_dex.py`. Si cambian los personajes de `script.js`, añade `--volcar`: abre el juego con Playwright y vuelve a leer `HDEF`.
2. `python herramientas/descargar_dbapi.py`. Solo hace falta si dragonball-api.com añade personajes.

## De dónde salen los datos

- **PV, ataque, velocidad y recarga:** son los del juego. Salen de `HDEF` y suben con cada forma igual que en `stats()`.
- **Raza, bando, planeta, descripción y poder de pelea:** salen de [dragonball-api.com](https://dragonball-api.com) cuando el personaje y la forma están en la API (etiqueta **API**).
- **Lo que no está en la API:** se inventa como en el anime (etiqueta **INVENTADO**).
  - Para las formas de los Saiyan se toma la escala de Goku de la API (SSJ ×50, SSJ2, SSJ3, Dios, Blue, UI…) y se multiplica por la fuerza del personaje.
  - Para los demás, los poderes conocidos del anime (`BASE_ANIME` en `generar_dex.py`) y, si no hay ninguno, un valor según la rareza.
