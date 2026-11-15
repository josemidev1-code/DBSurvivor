# Animaciones para Piskel — GOKUGT (Forma 1)

Esta carpeta contiene las animaciones listas para abrir y editar en **Piskel** (https://www.piskelapp.com/).

## Cómo abrir en Piskel:
1. Entra a **https://www.piskelapp.com/p/create/sprite** en tu navegador.
2. Haz clic en el icono de carpeta de la barra derecha (**Import**).
3. Elige cualquiera de estas opciones:
   - **Import .piskel file**: selecciona el archivo `.piskel` de cualquier animación.
   - **Import animated GIF**: selecciona el archivo `.gif` (Piskel importa todos los fotogramas y la velocidad al instante).
   - **Import from picture**: selecciona el `_sheet.png` (pon el Frame size que se indica abajo).

## Volver al juego:
`python herramientas/importar_piskel.py editado.piskel --manifiesto "04 - Piskel/gokugt_1/origen.json" --heroe gokugt --forma 1 --anim attack --aplicar`
Después: `python herramientas/montar_animaciones.py gokugt` y revisión visual. Solo se aceptan sprites originales exportados.

## Animaciones disponibles:

| Animación | Fotogramas | Tamaño de celda | Archivo .piskel | GIF animado | Hoja Strip |
|---|---|---|---|---|---|
| **Idle** | 2 | 54x54 | [`gokugt_Idle.piskel`](Idle/gokugt_Idle.piskel) | [`gokugt_Idle.gif`](Idle/gokugt_Idle.gif) | [`gokugt_Idle_sheet.png`](Idle/gokugt_Idle_sheet.png) |
| **Walk** | 1 | 52x52 | [`gokugt_Walk.piskel`](Walk/gokugt_Walk.piskel) | [`gokugt_Walk.gif`](Walk/gokugt_Walk.gif) | [`gokugt_Walk_sheet.png`](Walk/gokugt_Walk_sheet.png) |
| **Attack** | 3 | 56x56 | [`gokugt_Attack.piskel`](Attack/gokugt_Attack.piskel) | [`gokugt_Attack.gif`](Attack/gokugt_Attack.gif) | [`gokugt_Attack_sheet.png`](Attack/gokugt_Attack_sheet.png) |
| **Kick** | 2 | 60x60 | [`gokugt_Kick.piskel`](Kick/gokugt_Kick.piskel) | [`gokugt_Kick.gif`](Kick/gokugt_Kick.gif) | [`gokugt_Kick_sheet.png`](Kick/gokugt_Kick_sheet.png) |
| **Cast** | 2 | 54x54 | [`gokugt_Cast.piskel`](Cast/gokugt_Cast.piskel) | [`gokugt_Cast.gif`](Cast/gokugt_Cast.gif) | [`gokugt_Cast_sheet.png`](Cast/gokugt_Cast_sheet.png) |
| **Pow** | 3 | 94x94 | [`gokugt_Pow.piskel`](Pow/gokugt_Pow.piskel) | [`gokugt_Pow.gif`](Pow/gokugt_Pow.gif) | [`gokugt_Pow_sheet.png`](Pow/gokugt_Pow_sheet.png) |
| **Hurt** | 2 | 62x62 | [`gokugt_Hurt.piskel`](Hurt/gokugt_Hurt.piskel) | [`gokugt_Hurt.gif`](Hurt/gokugt_Hurt.gif) | [`gokugt_Hurt_sheet.png`](Hurt/gokugt_Hurt_sheet.png) |
| **Attack2** | 3 | 62x62 | [`gokugt_Attack2.piskel`](Attack2/gokugt_Attack2.piskel) | [`gokugt_Attack2.gif`](Attack2/gokugt_Attack2.gif) | [`gokugt_Attack2_sheet.png`](Attack2/gokugt_Attack2_sheet.png) |
| **Attack3** | 3 | 54x54 | [`gokugt_Attack3.piskel`](Attack3/gokugt_Attack3.piskel) | [`gokugt_Attack3.gif`](Attack3/gokugt_Attack3.gif) | [`gokugt_Attack3_sheet.png`](Attack3/gokugt_Attack3_sheet.png) |
| **Kick2** | 2 | 60x60 | [`gokugt_Kick2.piskel`](Kick2/gokugt_Kick2.piskel) | [`gokugt_Kick2.gif`](Kick2/gokugt_Kick2.gif) | [`gokugt_Kick2_sheet.png`](Kick2/gokugt_Kick2_sheet.png) |
| **Beam** | 2 | 52x52 | [`gokugt_Beam.piskel`](Beam/gokugt_Beam.piskel) | [`gokugt_Beam.gif`](Beam/gokugt_Beam.gif) | [`gokugt_Beam_sheet.png`](Beam/gokugt_Beam_sheet.png) |
| **Dash** | 1 | 52x52 | [`gokugt_Dash.piskel`](Dash/gokugt_Dash.piskel) | [`gokugt_Dash.gif`](Dash/gokugt_Dash.gif) | [`gokugt_Dash_sheet.png`](Dash/gokugt_Dash_sheet.png) |