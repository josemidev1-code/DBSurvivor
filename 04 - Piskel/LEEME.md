# 04 - Piskel · animaciones listas para editar

Una carpeta por personaje y forma: `<personaje>_<forma>/` (por ejemplo `goku_0` es Goku base).
Dentro hay una subcarpeta por animación (`Idle`, `Attack`, `Kick`, `Beam`…) con su `.piskel`, un GIF y una hoja PNG,
y un `LEEME_PISKEL.md` con los pasos para ese personaje.

1. Abre https://www.piskelapp.com/p/create/sprite e importa el `.piskel` que quieras.
2. Reordena, duplica o quita fotogramas (no se dibujan sprites nuevos) y guarda el `.piskel`.
3. Devuélvelo al juego con `python herramientas/importar_piskel.py` (los pasos exactos están en el `LEEME_PISKEL.md` de cada carpeta).

Todo esto se regenera con `python herramientas/exportar_piskel_lote.py <personaje>`.
