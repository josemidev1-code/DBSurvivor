# Animaciones para Piskel — GOKUSUPER (Forma 3)

Esta carpeta contiene las animaciones listas para abrir y editar en **Piskel** (https://www.piskelapp.com/).

## Cómo abrir en Piskel:
1. Entra a **https://www.piskelapp.com/p/create/sprite** en tu navegador.
2. Haz clic en el icono de carpeta de la barra derecha (**Import**).
3. Elige cualquiera de estas opciones:
   - **Import .piskel file**: selecciona el archivo `.piskel` de cualquier animación.
   - **Import animated GIF**: selecciona el archivo `.gif` (Piskel importa todos los fotogramas y la velocidad al instante).
   - **Import from picture**: selecciona el `_sheet.png` (pon el Frame size que se indica abajo).

## Volver al juego:
`python herramientas/importar_piskel.py editado.piskel --manifiesto "04 - Piskel/gokusuper_3/origen.json" --heroe gokusuper --forma 3 --anim attack --aplicar`
Después: `python herramientas/montar_animaciones.py gokusuper` y revisión visual. Solo se aceptan sprites originales exportados.

## Animaciones disponibles:

| Animación | Fotogramas | Tamaño de celda | Archivo .piskel | GIF animado | Hoja Strip |
|---|---|---|---|---|---|
| **Idle** | 3 | 88x88 | [`gokusuper_Idle.piskel`](Idle/gokusuper_Idle.piskel) | [`gokusuper_Idle.gif`](Idle/gokusuper_Idle.gif) | [`gokusuper_Idle_sheet.png`](Idle/gokusuper_Idle_sheet.png) |
| **Walk** | 1 | 80x80 | [`gokusuper_Walk.piskel`](Walk/gokusuper_Walk.piskel) | [`gokusuper_Walk.gif`](Walk/gokusuper_Walk.gif) | [`gokusuper_Walk_sheet.png`](Walk/gokusuper_Walk_sheet.png) |
| **Attack** | 4 | 80x80 | [`gokusuper_Attack.piskel`](Attack/gokusuper_Attack.piskel) | [`gokusuper_Attack.gif`](Attack/gokusuper_Attack.gif) | [`gokusuper_Attack_sheet.png`](Attack/gokusuper_Attack_sheet.png) |
| **Kick** | 2 | 80x80 | [`gokusuper_Kick.piskel`](Kick/gokusuper_Kick.piskel) | [`gokusuper_Kick.gif`](Kick/gokusuper_Kick.gif) | [`gokusuper_Kick_sheet.png`](Kick/gokusuper_Kick_sheet.png) |
| **Cast** | 2 | 104x104 | [`gokusuper_Cast.piskel`](Cast/gokusuper_Cast.piskel) | [`gokusuper_Cast.gif`](Cast/gokusuper_Cast.gif) | [`gokusuper_Cast_sheet.png`](Cast/gokusuper_Cast_sheet.png) |
| **Pow** | 2 | 108x108 | [`gokusuper_Pow.piskel`](Pow/gokusuper_Pow.piskel) | [`gokusuper_Pow.gif`](Pow/gokusuper_Pow.gif) | [`gokusuper_Pow_sheet.png`](Pow/gokusuper_Pow_sheet.png) |
| **Hurt** | 2 | 64x64 | [`gokusuper_Hurt.piskel`](Hurt/gokusuper_Hurt.piskel) | [`gokusuper_Hurt.gif`](Hurt/gokusuper_Hurt.gif) | [`gokusuper_Hurt_sheet.png`](Hurt/gokusuper_Hurt_sheet.png) |
| **Faint** | 1 | 80x80 | [`gokusuper_Faint.piskel`](Faint/gokusuper_Faint.piskel) | [`gokusuper_Faint.gif`](Faint/gokusuper_Faint.gif) | [`gokusuper_Faint_sheet.png`](Faint/gokusuper_Faint_sheet.png) |
| **Attack2** | 2 | 80x80 | [`gokusuper_Attack2.piskel`](Attack2/gokusuper_Attack2.piskel) | [`gokusuper_Attack2.gif`](Attack2/gokusuper_Attack2.gif) | [`gokusuper_Attack2_sheet.png`](Attack2/gokusuper_Attack2_sheet.png) |
| **Attack3** | 2 | 72x72 | [`gokusuper_Attack3.piskel`](Attack3/gokusuper_Attack3.piskel) | [`gokusuper_Attack3.gif`](Attack3/gokusuper_Attack3.gif) | [`gokusuper_Attack3_sheet.png`](Attack3/gokusuper_Attack3_sheet.png) |
| **Kick2** | 2 | 80x80 | [`gokusuper_Kick2.piskel`](Kick2/gokusuper_Kick2.piskel) | [`gokusuper_Kick2.gif`](Kick2/gokusuper_Kick2.gif) | [`gokusuper_Kick2_sheet.png`](Kick2/gokusuper_Kick2_sheet.png) |
| **Beam** | 2 | 72x72 | [`gokusuper_Beam.piskel`](Beam/gokusuper_Beam.piskel) | [`gokusuper_Beam.gif`](Beam/gokusuper_Beam.gif) | [`gokusuper_Beam_sheet.png`](Beam/gokusuper_Beam_sheet.png) |
| **Up** | 1 | 96x96 | [`gokusuper_Up.piskel`](Up/gokusuper_Up.piskel) | [`gokusuper_Up.gif`](Up/gokusuper_Up.gif) | [`gokusuper_Up_sheet.png`](Up/gokusuper_Up_sheet.png) |
| **Dash** | 1 | 80x80 | [`gokusuper_Dash.piskel`](Dash/gokusuper_Dash.piskel) | [`gokusuper_Dash.gif`](Dash/gokusuper_Dash.gif) | [`gokusuper_Dash_sheet.png`](Dash/gokusuper_Dash_sheet.png) |