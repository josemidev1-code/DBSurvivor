# Animaciones para Piskel — GOKUBROLY (Forma 1)

Esta carpeta contiene las animaciones listas para abrir y editar en **Piskel** (https://www.piskelapp.com/).

## Cómo abrir en Piskel:
1. Entra a **https://www.piskelapp.com/p/create/sprite** en tu navegador.
2. Haz clic en el icono de carpeta de la barra derecha (**Import**).
3. Elige cualquiera de estas opciones:
   - **Import .piskel file**: selecciona el archivo `.piskel` de cualquier animación.
   - **Import animated GIF**: selecciona el archivo `.gif` (Piskel importa todos los fotogramas y la velocidad al instante).
   - **Import from picture**: selecciona el `_sheet.png` (pon el Frame size que se indica abajo).

## Volver al juego:
`python herramientas/importar_piskel.py editado.piskel --manifiesto "04 - Piskel/gokubroly_1/origen.json" --heroe gokubroly --forma 1 --anim attack --aplicar`
Después: `python herramientas/montar_animaciones.py gokubroly` y revisión visual. Solo se aceptan sprites originales exportados.

## Animaciones disponibles:

| Animación | Fotogramas | Tamaño de celda | Archivo .piskel | GIF animado | Hoja Strip |
|---|---|---|---|---|---|
| **Idle** | 2 | 56x56 | [`gokubroly_Idle.piskel`](Idle/gokubroly_Idle.piskel) | [`gokubroly_Idle.gif`](Idle/gokubroly_Idle.gif) | [`gokubroly_Idle_sheet.png`](Idle/gokubroly_Idle_sheet.png) |
| **Walk** | 1 | 70x70 | [`gokubroly_Walk.piskel`](Walk/gokubroly_Walk.piskel) | [`gokubroly_Walk.gif`](Walk/gokubroly_Walk.gif) | [`gokubroly_Walk_sheet.png`](Walk/gokubroly_Walk_sheet.png) |
| **Attack** | 3 | 56x56 | [`gokubroly_Attack.piskel`](Attack/gokubroly_Attack.piskel) | [`gokubroly_Attack.gif`](Attack/gokubroly_Attack.gif) | [`gokubroly_Attack_sheet.png`](Attack/gokubroly_Attack_sheet.png) |
| **Kick** | 2 | 54x54 | [`gokubroly_Kick.piskel`](Kick/gokubroly_Kick.piskel) | [`gokubroly_Kick.gif`](Kick/gokubroly_Kick.gif) | [`gokubroly_Kick_sheet.png`](Kick/gokubroly_Kick_sheet.png) |
| **Cast** | 2 | 56x56 | [`gokubroly_Cast.piskel`](Cast/gokubroly_Cast.piskel) | [`gokubroly_Cast.gif`](Cast/gokubroly_Cast.gif) | [`gokubroly_Cast_sheet.png`](Cast/gokubroly_Cast_sheet.png) |
| **Pow** | 2 | 84x84 | [`gokubroly_Pow.piskel`](Pow/gokubroly_Pow.piskel) | [`gokubroly_Pow.gif`](Pow/gokubroly_Pow.gif) | [`gokubroly_Pow_sheet.png`](Pow/gokubroly_Pow_sheet.png) |
| **Hurt** | 2 | 48x48 | [`gokubroly_Hurt.piskel`](Hurt/gokubroly_Hurt.piskel) | [`gokubroly_Hurt.gif`](Hurt/gokubroly_Hurt.gif) | [`gokubroly_Hurt_sheet.png`](Hurt/gokubroly_Hurt_sheet.png) |
| **Faint** | 1 | 54x54 | [`gokubroly_Faint.piskel`](Faint/gokubroly_Faint.piskel) | [`gokubroly_Faint.gif`](Faint/gokubroly_Faint.gif) | [`gokubroly_Faint_sheet.png`](Faint/gokubroly_Faint_sheet.png) |
| **Attack2** | 3 | 56x56 | [`gokubroly_Attack2.piskel`](Attack2/gokubroly_Attack2.piskel) | [`gokubroly_Attack2.gif`](Attack2/gokubroly_Attack2.gif) | [`gokubroly_Attack2_sheet.png`](Attack2/gokubroly_Attack2_sheet.png) |
| **Kick2** | 2 | 60x60 | [`gokubroly_Kick2.piskel`](Kick2/gokubroly_Kick2.piskel) | [`gokubroly_Kick2.gif`](Kick2/gokubroly_Kick2.gif) | [`gokubroly_Kick2_sheet.png`](Kick2/gokubroly_Kick2_sheet.png) |
| **Beam** | 2 | 58x58 | [`gokubroly_Beam.piskel`](Beam/gokubroly_Beam.piskel) | [`gokubroly_Beam.gif`](Beam/gokubroly_Beam.gif) | [`gokubroly_Beam_sheet.png`](Beam/gokubroly_Beam_sheet.png) |
| **Dash** | 1 | 70x70 | [`gokubroly_Dash.piskel`](Dash/gokubroly_Dash.piskel) | [`gokubroly_Dash.gif`](Dash/gokubroly_Dash.gif) | [`gokubroly_Dash_sheet.png`](Dash/gokubroly_Dash_sheet.png) |