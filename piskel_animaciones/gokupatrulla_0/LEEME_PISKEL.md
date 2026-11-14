# Animaciones para Piskel — GOKUPATRULLA (Forma 0)

Esta carpeta contiene las animaciones listas para abrir y editar en **Piskel** (https://www.piskelapp.com/).

## Cómo abrir en Piskel:
1. Entra a **https://www.piskelapp.com/p/create/sprite** en tu navegador.
2. Haz clic en el icono de carpeta de la barra derecha (**Import**).
3. Elige cualquiera de estas opciones:
   - **Import .piskel file**: selecciona el archivo `.piskel` de cualquier animación.
   - **Import animated GIF**: selecciona el archivo `.gif` (Piskel importa todos los fotogramas y la velocidad al instante).
   - **Import from picture**: selecciona el `_sheet.png` (pon el Frame size que se indica abajo).

## Volver al juego:
`python herramientas/importar_piskel.py editado.piskel --manifiesto piskel_animaciones/gokupatrulla_0/origen.json --heroe gokupatrulla --forma 0 --anim attack --aplicar`
Después: `python herramientas/montar_animaciones.py gokupatrulla` y revisión visual. Solo se aceptan sprites originales exportados.

## Animaciones disponibles:

| Animación | Fotogramas | Tamaño de celda | Archivo .piskel | GIF animado | Hoja Strip |
|---|---|---|---|---|---|
| **Idle** | 2 | 56x56 | [`gokupatrulla_Idle.piskel`](Idle/gokupatrulla_Idle.piskel) | [`gokupatrulla_Idle.gif`](Idle/gokupatrulla_Idle.gif) | [`gokupatrulla_Idle_sheet.png`](Idle/gokupatrulla_Idle_sheet.png) |
| **Walk** | 1 | 54x54 | [`gokupatrulla_Walk.piskel`](Walk/gokupatrulla_Walk.piskel) | [`gokupatrulla_Walk.gif`](Walk/gokupatrulla_Walk.gif) | [`gokupatrulla_Walk_sheet.png`](Walk/gokupatrulla_Walk_sheet.png) |
| **Attack** | 3 | 56x56 | [`gokupatrulla_Attack.piskel`](Attack/gokupatrulla_Attack.piskel) | [`gokupatrulla_Attack.gif`](Attack/gokupatrulla_Attack.gif) | [`gokupatrulla_Attack_sheet.png`](Attack/gokupatrulla_Attack_sheet.png) |
| **Kick** | 2 | 54x54 | [`gokupatrulla_Kick.piskel`](Kick/gokupatrulla_Kick.piskel) | [`gokupatrulla_Kick.gif`](Kick/gokupatrulla_Kick.gif) | [`gokupatrulla_Kick_sheet.png`](Kick/gokupatrulla_Kick_sheet.png) |
| **Cast** | 2 | 56x56 | [`gokupatrulla_Cast.piskel`](Cast/gokupatrulla_Cast.piskel) | [`gokupatrulla_Cast.gif`](Cast/gokupatrulla_Cast.gif) | [`gokupatrulla_Cast_sheet.png`](Cast/gokupatrulla_Cast_sheet.png) |
| **Pow** | 2 | 88x88 | [`gokupatrulla_Pow.piskel`](Pow/gokupatrulla_Pow.piskel) | [`gokupatrulla_Pow.gif`](Pow/gokupatrulla_Pow.gif) | [`gokupatrulla_Pow_sheet.png`](Pow/gokupatrulla_Pow_sheet.png) |
| **Hurt** | 2 | 50x50 | [`gokupatrulla_Hurt.piskel`](Hurt/gokupatrulla_Hurt.piskel) | [`gokupatrulla_Hurt.gif`](Hurt/gokupatrulla_Hurt.gif) | [`gokupatrulla_Hurt_sheet.png`](Hurt/gokupatrulla_Hurt_sheet.png) |
| **Faint** | 1 | 68x68 | [`gokupatrulla_Faint.piskel`](Faint/gokupatrulla_Faint.piskel) | [`gokupatrulla_Faint.gif`](Faint/gokupatrulla_Faint.gif) | [`gokupatrulla_Faint_sheet.png`](Faint/gokupatrulla_Faint_sheet.png) |
| **Attack2** | 3 | 54x54 | [`gokupatrulla_Attack2.piskel`](Attack2/gokupatrulla_Attack2.piskel) | [`gokupatrulla_Attack2.gif`](Attack2/gokupatrulla_Attack2.gif) | [`gokupatrulla_Attack2_sheet.png`](Attack2/gokupatrulla_Attack2_sheet.png) |
| **Attack3** | 2 | 54x54 | [`gokupatrulla_Attack3.piskel`](Attack3/gokupatrulla_Attack3.piskel) | [`gokupatrulla_Attack3.gif`](Attack3/gokupatrulla_Attack3.gif) | [`gokupatrulla_Attack3_sheet.png`](Attack3/gokupatrulla_Attack3_sheet.png) |
| **Beam** | 2 | 58x58 | [`gokupatrulla_Beam.piskel`](Beam/gokupatrulla_Beam.piskel) | [`gokupatrulla_Beam.gif`](Beam/gokupatrulla_Beam.gif) | [`gokupatrulla_Beam_sheet.png`](Beam/gokupatrulla_Beam_sheet.png) |
| **Up** | 1 | 62x62 | [`gokupatrulla_Up.piskel`](Up/gokupatrulla_Up.piskel) | [`gokupatrulla_Up.gif`](Up/gokupatrulla_Up.gif) | [`gokupatrulla_Up_sheet.png`](Up/gokupatrulla_Up_sheet.png) |
| **Dash** | 1 | 54x54 | [`gokupatrulla_Dash.piskel`](Dash/gokupatrulla_Dash.piskel) | [`gokupatrulla_Dash.gif`](Dash/gokupatrulla_Dash.gif) | [`gokupatrulla_Dash_sheet.png`](Dash/gokupatrulla_Dash_sheet.png) |