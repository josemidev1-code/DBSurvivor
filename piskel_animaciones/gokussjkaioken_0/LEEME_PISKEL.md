# Animaciones para Piskel — GOKUSSJKAIOKEN (Forma 0)

Esta carpeta contiene las animaciones listas para abrir y editar en **Piskel** (https://www.piskelapp.com/).

## Cómo abrir en Piskel:
1. Entra a **https://www.piskelapp.com/p/create/sprite** en tu navegador.
2. Haz clic en el icono de carpeta de la barra derecha (**Import**).
3. Elige cualquiera de estas opciones:
   - **Import .piskel file**: selecciona el archivo `.piskel` de cualquier animación.
   - **Import animated GIF**: selecciona el archivo `.gif` (Piskel importa todos los fotogramas y la velocidad al instante).
   - **Import from picture**: selecciona el `_sheet.png` (pon el Frame size que se indica abajo).

## Volver al juego:
`python herramientas/importar_piskel.py editado.piskel --manifiesto piskel_animaciones/gokussjkaioken_0/origen.json --heroe gokussjkaioken --forma 0 --anim attack --aplicar`
Después: `python herramientas/montar_animaciones.py gokussjkaioken` y revisión visual. Solo se aceptan sprites originales exportados.

## Animaciones disponibles:

| Animación | Fotogramas | Tamaño de celda | Archivo .piskel | GIF animado | Hoja Strip |
|---|---|---|---|---|---|
| **Idle** | 2 | 66x66 | [`gokussjkaioken_Idle.piskel`](Idle/gokussjkaioken_Idle.piskel) | [`gokussjkaioken_Idle.gif`](Idle/gokussjkaioken_Idle.gif) | [`gokussjkaioken_Idle_sheet.png`](Idle/gokussjkaioken_Idle_sheet.png) |
| **Walk** | 1 | 66x66 | [`gokussjkaioken_Walk.piskel`](Walk/gokussjkaioken_Walk.piskel) | [`gokussjkaioken_Walk.gif`](Walk/gokussjkaioken_Walk.gif) | [`gokussjkaioken_Walk_sheet.png`](Walk/gokussjkaioken_Walk_sheet.png) |
| **Attack** | 3 | 64x64 | [`gokussjkaioken_Attack.piskel`](Attack/gokussjkaioken_Attack.piskel) | [`gokussjkaioken_Attack.gif`](Attack/gokussjkaioken_Attack.gif) | [`gokussjkaioken_Attack_sheet.png`](Attack/gokussjkaioken_Attack_sheet.png) |
| **Kick** | 2 | 74x74 | [`gokussjkaioken_Kick.piskel`](Kick/gokussjkaioken_Kick.piskel) | [`gokussjkaioken_Kick.gif`](Kick/gokussjkaioken_Kick.gif) | [`gokussjkaioken_Kick_sheet.png`](Kick/gokussjkaioken_Kick_sheet.png) |
| **Cast** | 2 | 64x64 | [`gokussjkaioken_Cast.piskel`](Cast/gokussjkaioken_Cast.piskel) | [`gokussjkaioken_Cast.gif`](Cast/gokussjkaioken_Cast.gif) | [`gokussjkaioken_Cast_sheet.png`](Cast/gokussjkaioken_Cast_sheet.png) |
| **Pow** | 1 | 90x90 | [`gokussjkaioken_Pow.piskel`](Pow/gokussjkaioken_Pow.piskel) | [`gokussjkaioken_Pow.gif`](Pow/gokussjkaioken_Pow.gif) | [`gokussjkaioken_Pow_sheet.png`](Pow/gokussjkaioken_Pow_sheet.png) |
| **Hurt** | 2 | 62x62 | [`gokussjkaioken_Hurt.piskel`](Hurt/gokussjkaioken_Hurt.piskel) | [`gokussjkaioken_Hurt.gif`](Hurt/gokussjkaioken_Hurt.gif) | [`gokussjkaioken_Hurt_sheet.png`](Hurt/gokussjkaioken_Hurt_sheet.png) |
| **Faint** | 1 | 74x74 | [`gokussjkaioken_Faint.piskel`](Faint/gokussjkaioken_Faint.piskel) | [`gokussjkaioken_Faint.gif`](Faint/gokussjkaioken_Faint.gif) | [`gokussjkaioken_Faint_sheet.png`](Faint/gokussjkaioken_Faint_sheet.png) |
| **Attack2** | 3 | 58x58 | [`gokussjkaioken_Attack2.piskel`](Attack2/gokussjkaioken_Attack2.piskel) | [`gokussjkaioken_Attack2.gif`](Attack2/gokussjkaioken_Attack2.gif) | [`gokussjkaioken_Attack2_sheet.png`](Attack2/gokussjkaioken_Attack2_sheet.png) |
| **Attack3** | 2 | 60x60 | [`gokussjkaioken_Attack3.piskel`](Attack3/gokussjkaioken_Attack3.piskel) | [`gokussjkaioken_Attack3.gif`](Attack3/gokussjkaioken_Attack3.gif) | [`gokussjkaioken_Attack3_sheet.png`](Attack3/gokussjkaioken_Attack3_sheet.png) |
| **Kick2** | 2 | 68x68 | [`gokussjkaioken_Kick2.piskel`](Kick2/gokussjkaioken_Kick2.piskel) | [`gokussjkaioken_Kick2.gif`](Kick2/gokussjkaioken_Kick2.gif) | [`gokussjkaioken_Kick2_sheet.png`](Kick2/gokussjkaioken_Kick2_sheet.png) |
| **Beam** | 2 | 64x64 | [`gokussjkaioken_Beam.piskel`](Beam/gokussjkaioken_Beam.piskel) | [`gokussjkaioken_Beam.gif`](Beam/gokussjkaioken_Beam.gif) | [`gokussjkaioken_Beam_sheet.png`](Beam/gokussjkaioken_Beam_sheet.png) |
| **Up** | 1 | 66x66 | [`gokussjkaioken_Up.piskel`](Up/gokussjkaioken_Up.piskel) | [`gokussjkaioken_Up.gif`](Up/gokussjkaioken_Up.gif) | [`gokussjkaioken_Up_sheet.png`](Up/gokussjkaioken_Up_sheet.png) |
| **Dash** | 1 | 66x66 | [`gokussjkaioken_Dash.piskel`](Dash/gokussjkaioken_Dash.piskel) | [`gokussjkaioken_Dash.gif`](Dash/gokussjkaioken_Dash.gif) | [`gokussjkaioken_Dash_sheet.png`](Dash/gokussjkaioken_Dash_sheet.png) |