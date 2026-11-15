# Animaciones para Piskel — GOKUALT (Forma 0)

Esta carpeta contiene las animaciones listas para abrir y editar en **Piskel** (https://www.piskelapp.com/).

## Cómo abrir en Piskel:
1. Entra a **https://www.piskelapp.com/p/create/sprite** en tu navegador.
2. Haz clic en el icono de carpeta de la barra derecha (**Import**).
3. Elige cualquiera de estas opciones:
   - **Import .piskel file**: selecciona el archivo `.piskel` de cualquier animación.
   - **Import animated GIF**: selecciona el archivo `.gif` (Piskel importa todos los fotogramas y la velocidad al instante).
   - **Import from picture**: selecciona el `_sheet.png` (pon el Frame size que se indica abajo).

## Volver al juego:
`python herramientas/importar_piskel.py editado.piskel --manifiesto "04 - Piskel/gokualt_0/origen.json" --heroe gokualt --forma 0 --anim attack --aplicar`
Después: `python herramientas/montar_animaciones.py gokualt` y revisión visual. Solo se aceptan sprites originales exportados.

## Animaciones disponibles:

| Animación | Fotogramas | Tamaño de celda | Archivo .piskel | GIF animado | Hoja Strip |
|---|---|---|---|---|---|
| **Idle** | 2 | 58x58 | [`gokualt_Idle.piskel`](Idle/gokualt_Idle.piskel) | [`gokualt_Idle.gif`](Idle/gokualt_Idle.gif) | [`gokualt_Idle_sheet.png`](Idle/gokualt_Idle_sheet.png) |
| **Walk** | 1 | 68x68 | [`gokualt_Walk.piskel`](Walk/gokualt_Walk.piskel) | [`gokualt_Walk.gif`](Walk/gokualt_Walk.gif) | [`gokualt_Walk_sheet.png`](Walk/gokualt_Walk_sheet.png) |
| **Attack** | 4 | 62x62 | [`gokualt_Attack.piskel`](Attack/gokualt_Attack.piskel) | [`gokualt_Attack.gif`](Attack/gokualt_Attack.gif) | [`gokualt_Attack_sheet.png`](Attack/gokualt_Attack_sheet.png) |
| **Kick** | 2 | 56x56 | [`gokualt_Kick.piskel`](Kick/gokualt_Kick.piskel) | [`gokualt_Kick.gif`](Kick/gokualt_Kick.gif) | [`gokualt_Kick_sheet.png`](Kick/gokualt_Kick_sheet.png) |
| **Cast** | 2 | 62x62 | [`gokualt_Cast.piskel`](Cast/gokualt_Cast.piskel) | [`gokualt_Cast.gif`](Cast/gokualt_Cast.gif) | [`gokualt_Cast_sheet.png`](Cast/gokualt_Cast_sheet.png) |
| **Pow** | 2 | 124x124 | [`gokualt_Pow.piskel`](Pow/gokualt_Pow.piskel) | [`gokualt_Pow.gif`](Pow/gokualt_Pow.gif) | [`gokualt_Pow_sheet.png`](Pow/gokualt_Pow_sheet.png) |
| **Hurt** | 2 | 68x68 | [`gokualt_Hurt.piskel`](Hurt/gokualt_Hurt.piskel) | [`gokualt_Hurt.gif`](Hurt/gokualt_Hurt.gif) | [`gokualt_Hurt_sheet.png`](Hurt/gokualt_Hurt_sheet.png) |
| **Faint** | 1 | 72x72 | [`gokualt_Faint.piskel`](Faint/gokualt_Faint.piskel) | [`gokualt_Faint.gif`](Faint/gokualt_Faint.gif) | [`gokualt_Faint_sheet.png`](Faint/gokualt_Faint_sheet.png) |
| **Attack2** | 2 | 62x62 | [`gokualt_Attack2.piskel`](Attack2/gokualt_Attack2.piskel) | [`gokualt_Attack2.gif`](Attack2/gokualt_Attack2.gif) | [`gokualt_Attack2_sheet.png`](Attack2/gokualt_Attack2_sheet.png) |
| **Attack3** | 3 | 56x56 | [`gokualt_Attack3.piskel`](Attack3/gokualt_Attack3.piskel) | [`gokualt_Attack3.gif`](Attack3/gokualt_Attack3.gif) | [`gokualt_Attack3_sheet.png`](Attack3/gokualt_Attack3_sheet.png) |
| **Kick2** | 2 | 80x80 | [`gokualt_Kick2.piskel`](Kick2/gokualt_Kick2.piskel) | [`gokualt_Kick2.gif`](Kick2/gokualt_Kick2.gif) | [`gokualt_Kick2_sheet.png`](Kick2/gokualt_Kick2_sheet.png) |
| **Beam** | 2 | 58x58 | [`gokualt_Beam.piskel`](Beam/gokualt_Beam.piskel) | [`gokualt_Beam.gif`](Beam/gokualt_Beam.gif) | [`gokualt_Beam_sheet.png`](Beam/gokualt_Beam_sheet.png) |
| **Up** | 2 | 70x70 | [`gokualt_Up.piskel`](Up/gokualt_Up.piskel) | [`gokualt_Up.gif`](Up/gokualt_Up.gif) | [`gokualt_Up_sheet.png`](Up/gokualt_Up_sheet.png) |
| **Dash** | 1 | 68x68 | [`gokualt_Dash.piskel`](Dash/gokualt_Dash.piskel) | [`gokualt_Dash.gif`](Dash/gokualt_Dash.gif) | [`gokualt_Dash_sheet.png`](Dash/gokualt_Dash_sheet.png) |