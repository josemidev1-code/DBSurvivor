# Animaciones para Piskel — TRUNKSNINO (Forma 0)

Esta carpeta contiene las animaciones listas para abrir y editar en **Piskel** (https://www.piskelapp.com/).

## Cómo abrir en Piskel:
1. Entra a **https://www.piskelapp.com/p/create/sprite** en tu navegador.
2. Haz clic en el icono de carpeta de la barra derecha (**Import**).
3. Elige cualquiera de estas opciones:
   - **Import .piskel file**: selecciona el archivo `.piskel` de cualquier animación.
   - **Import animated GIF**: selecciona el archivo `.gif` (Piskel importa todos los fotogramas y la velocidad al instante).
   - **Import from picture**: selecciona el `_sheet.png` (pon el Frame size que se indica abajo).

## Volver al juego:
`python herramientas/importar_piskel.py editado.piskel --manifiesto piskel_animaciones/trunksnino_0/origen.json --heroe trunksnino --forma 0 --anim attack --aplicar`
Después: `python herramientas/montar_animaciones.py trunksnino` y revisión visual. Solo se aceptan sprites originales exportados.

## Animaciones disponibles:

| Animación | Fotogramas | Tamaño de celda | Archivo .piskel | GIF animado | Hoja Strip |
|---|---|---|---|---|---|
| **Idle** | 2 | 52x52 | [`trunksnino_Idle.piskel`](Idle/trunksnino_Idle.piskel) | [`trunksnino_Idle.gif`](Idle/trunksnino_Idle.gif) | [`trunksnino_Idle_sheet.png`](Idle/trunksnino_Idle_sheet.png) |
| **Walk** | 1 | 74x74 | [`trunksnino_Walk.piskel`](Walk/trunksnino_Walk.piskel) | [`trunksnino_Walk.gif`](Walk/trunksnino_Walk.gif) | [`trunksnino_Walk_sheet.png`](Walk/trunksnino_Walk_sheet.png) |
| **Attack** | 3 | 54x54 | [`trunksnino_Attack.piskel`](Attack/trunksnino_Attack.piskel) | [`trunksnino_Attack.gif`](Attack/trunksnino_Attack.gif) | [`trunksnino_Attack_sheet.png`](Attack/trunksnino_Attack_sheet.png) |
| **Kick** | 2 | 60x60 | [`trunksnino_Kick.piskel`](Kick/trunksnino_Kick.piskel) | [`trunksnino_Kick.gif`](Kick/trunksnino_Kick.gif) | [`trunksnino_Kick_sheet.png`](Kick/trunksnino_Kick_sheet.png) |
| **Cast** | 2 | 64x64 | [`trunksnino_Cast.piskel`](Cast/trunksnino_Cast.piskel) | [`trunksnino_Cast.gif`](Cast/trunksnino_Cast.gif) | [`trunksnino_Cast_sheet.png`](Cast/trunksnino_Cast_sheet.png) |
| **Pow** | 2 | 94x94 | [`trunksnino_Pow.piskel`](Pow/trunksnino_Pow.piskel) | [`trunksnino_Pow.gif`](Pow/trunksnino_Pow.gif) | [`trunksnino_Pow_sheet.png`](Pow/trunksnino_Pow_sheet.png) |
| **Hurt** | 2 | 56x56 | [`trunksnino_Hurt.piskel`](Hurt/trunksnino_Hurt.piskel) | [`trunksnino_Hurt.gif`](Hurt/trunksnino_Hurt.gif) | [`trunksnino_Hurt_sheet.png`](Hurt/trunksnino_Hurt_sheet.png) |
| **Faint** | 1 | 54x54 | [`trunksnino_Faint.piskel`](Faint/trunksnino_Faint.piskel) | [`trunksnino_Faint.gif`](Faint/trunksnino_Faint.gif) | [`trunksnino_Faint_sheet.png`](Faint/trunksnino_Faint_sheet.png) |
| **Attack3** | 2 | 52x52 | [`trunksnino_Attack3.piskel`](Attack3/trunksnino_Attack3.piskel) | [`trunksnino_Attack3.gif`](Attack3/trunksnino_Attack3.gif) | [`trunksnino_Attack3_sheet.png`](Attack3/trunksnino_Attack3_sheet.png) |
| **Kick2** | 2 | 54x54 | [`trunksnino_Kick2.piskel`](Kick2/trunksnino_Kick2.piskel) | [`trunksnino_Kick2.gif`](Kick2/trunksnino_Kick2.gif) | [`trunksnino_Kick2_sheet.png`](Kick2/trunksnino_Kick2_sheet.png) |
| **Beam** | 2 | 52x52 | [`trunksnino_Beam.piskel`](Beam/trunksnino_Beam.piskel) | [`trunksnino_Beam.gif`](Beam/trunksnino_Beam.gif) | [`trunksnino_Beam_sheet.png`](Beam/trunksnino_Beam_sheet.png) |
| **Up** | 2 | 56x56 | [`trunksnino_Up.piskel`](Up/trunksnino_Up.piskel) | [`trunksnino_Up.gif`](Up/trunksnino_Up.gif) | [`trunksnino_Up_sheet.png`](Up/trunksnino_Up_sheet.png) |