# Animaciones para Piskel — GOKUUI (Forma 2)

Esta carpeta contiene las animaciones listas para abrir y editar en **Piskel** (https://www.piskelapp.com/).

## Cómo abrir en Piskel:
1. Entra a **https://www.piskelapp.com/p/create/sprite** en tu navegador.
2. Haz clic en el icono de carpeta de la barra derecha (**Import**).
3. Elige cualquiera de estas opciones:
   - **Import .piskel file**: selecciona el archivo `.piskel` de cualquier animación.
   - **Import animated GIF**: selecciona el archivo `.gif` (Piskel importa todos los fotogramas y la velocidad al instante).
   - **Import from picture**: selecciona el `_sheet.png` (pon el Frame size que se indica abajo).

## Volver al juego:
`python herramientas/importar_piskel.py editado.piskel --manifiesto "04 - Piskel/gokuui_2/origen.json" --heroe gokuui --forma 2 --anim attack --aplicar`
Después: `python herramientas/montar_animaciones.py gokuui` y revisión visual. Solo se aceptan sprites originales exportados.

## Animaciones disponibles:

| Animación | Fotogramas | Tamaño de celda | Archivo .piskel | GIF animado | Hoja Strip |
|---|---|---|---|---|---|
| **Idle** | 3 | 56x56 | [`gokuui_Idle.piskel`](Idle/gokuui_Idle.piskel) | [`gokuui_Idle.gif`](Idle/gokuui_Idle.gif) | [`gokuui_Idle_sheet.png`](Idle/gokuui_Idle_sheet.png) |
| **Walk** | 1 | 104x104 | [`gokuui_Walk.piskel`](Walk/gokuui_Walk.piskel) | [`gokuui_Walk.gif`](Walk/gokuui_Walk.gif) | [`gokuui_Walk_sheet.png`](Walk/gokuui_Walk_sheet.png) |
| **Attack** | 4 | 56x56 | [`gokuui_Attack.piskel`](Attack/gokuui_Attack.piskel) | [`gokuui_Attack.gif`](Attack/gokuui_Attack.gif) | [`gokuui_Attack_sheet.png`](Attack/gokuui_Attack_sheet.png) |
| **Kick** | 4 | 64x64 | [`gokuui_Kick.piskel`](Kick/gokuui_Kick.piskel) | [`gokuui_Kick.gif`](Kick/gokuui_Kick.gif) | [`gokuui_Kick_sheet.png`](Kick/gokuui_Kick_sheet.png) |
| **Cast** | 2 | 64x64 | [`gokuui_Cast.piskel`](Cast/gokuui_Cast.piskel) | [`gokuui_Cast.gif`](Cast/gokuui_Cast.gif) | [`gokuui_Cast_sheet.png`](Cast/gokuui_Cast_sheet.png) |
| **Pow** | 2 | 94x94 | [`gokuui_Pow.piskel`](Pow/gokuui_Pow.piskel) | [`gokuui_Pow.gif`](Pow/gokuui_Pow.gif) | [`gokuui_Pow_sheet.png`](Pow/gokuui_Pow_sheet.png) |
| **Hurt** | 2 | 62x62 | [`gokuui_Hurt.piskel`](Hurt/gokuui_Hurt.piskel) | [`gokuui_Hurt.gif`](Hurt/gokuui_Hurt.gif) | [`gokuui_Hurt_sheet.png`](Hurt/gokuui_Hurt_sheet.png) |