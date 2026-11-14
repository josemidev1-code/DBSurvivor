# Animaciones para Piskel — GOKUSUPER (Forma 2)

Esta carpeta contiene las animaciones listas para abrir y editar en **Piskel** (https://www.piskelapp.com/).

## Cómo abrir en Piskel:
1. Entra a **https://www.piskelapp.com/p/create/sprite** en tu navegador.
2. Haz clic en el icono de carpeta de la barra derecha (**Import**).
3. Elige cualquiera de estas opciones:
   - **Import .piskel file**: selecciona el archivo `.piskel` de cualquier animación.
   - **Import animated GIF**: selecciona el archivo `.gif` (Piskel importa todos los fotogramas y la velocidad al instante).
   - **Import from picture**: selecciona el `_sheet.png` (pon el Frame size que se indica abajo).

## Volver al juego:
`python herramientas/importar_piskel.py editado.piskel --manifiesto piskel_animaciones/gokusuper_2/origen.json --heroe gokusuper --forma 2 --anim attack --aplicar`
Después: `python herramientas/montar_animaciones.py gokusuper` y revisión visual. Solo se aceptan sprites originales exportados.

## Animaciones disponibles:

| Animación | Fotogramas | Tamaño de celda | Archivo .piskel | GIF animado | Hoja Strip |
|---|---|---|---|---|---|
| **Idle** | 2 | 56x56 | [`gokusuper_Idle.piskel`](Idle/gokusuper_Idle.piskel) | [`gokusuper_Idle.gif`](Idle/gokusuper_Idle.gif) | [`gokusuper_Idle_sheet.png`](Idle/gokusuper_Idle_sheet.png) |
| **Walk** | 1 | 50x50 | [`gokusuper_Walk.piskel`](Walk/gokusuper_Walk.piskel) | [`gokusuper_Walk.gif`](Walk/gokusuper_Walk.gif) | [`gokusuper_Walk_sheet.png`](Walk/gokusuper_Walk_sheet.png) |
| **Attack** | 4 | 56x56 | [`gokusuper_Attack.piskel`](Attack/gokusuper_Attack.piskel) | [`gokusuper_Attack.gif`](Attack/gokusuper_Attack.gif) | [`gokusuper_Attack_sheet.png`](Attack/gokusuper_Attack_sheet.png) |
| **Kick** | 3 | 58x58 | [`gokusuper_Kick.piskel`](Kick/gokusuper_Kick.piskel) | [`gokusuper_Kick.gif`](Kick/gokusuper_Kick.gif) | [`gokusuper_Kick_sheet.png`](Kick/gokusuper_Kick_sheet.png) |
| **Cast** | 2 | 56x56 | [`gokusuper_Cast.piskel`](Cast/gokusuper_Cast.piskel) | [`gokusuper_Cast.gif`](Cast/gokusuper_Cast.gif) | [`gokusuper_Cast_sheet.png`](Cast/gokusuper_Cast_sheet.png) |
| **Pow** | 3 | 82x82 | [`gokusuper_Pow.piskel`](Pow/gokusuper_Pow.piskel) | [`gokusuper_Pow.gif`](Pow/gokusuper_Pow.gif) | [`gokusuper_Pow_sheet.png`](Pow/gokusuper_Pow_sheet.png) |
| **Hurt** | 2 | 54x54 | [`gokusuper_Hurt.piskel`](Hurt/gokusuper_Hurt.piskel) | [`gokusuper_Hurt.gif`](Hurt/gokusuper_Hurt.gif) | [`gokusuper_Hurt_sheet.png`](Hurt/gokusuper_Hurt_sheet.png) |