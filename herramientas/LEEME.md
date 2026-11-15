# herramientas · programas para montar el juego

Programas de Python (y alguno de Node) que preparan lo que usa el juego. No hace falta tocarlos para jugar.

| Carpeta / archivo | Qué es |
|---|---|
| `animaciones/` | **Los fotogramas elegidos de cada personaje** (JSON). Es lo más importante: de aquí sale todo. |
| `GUIA_ANIMACIONES.md` | Cómo elegir y revisar animaciones. Léela antes de tocar personajes. |
| `montar_animaciones.py` | Mete las animaciones en el juego (`02 - Código del juego/animaciones_juego.js`). |
| `ver_pack.py`, `previsualizar.py` | Sacan hojas para mirar un pack o una forma (las guardan en `_revisar/`, que no se sube a git). |
| `generar_dex.py` | Regenera la Dex (`03 - Dex/`). |
| `exportar_piskel_lote.py`, `importar_piskel.py` | Ida y vuelta con Piskel (`04 - Piskel/`). |
| `inventario_animaciones.py` | Escribe `01 - Guía y documentación/INVENTARIO_ANIMACIONES.md`. |
| `propuestas/` | Propuestas automáticas de fotogramas (método del 1/11/2026). |
| `efectos_pixelfx/` | Efectos de ataque. La librería pixelfx no se guarda: `git clone https://github.com/patch-gg/pixelfx herramientas/pixelfx`. |
| `dbapi/` | Datos de poder de los personajes para la Dex. |
| `pruebas/` | Pruebas automáticas (`python -m unittest discover herramientas/pruebas`). |
