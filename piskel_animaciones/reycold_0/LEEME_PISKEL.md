# Animaciones para Piskel — REYCOLD (Forma 0)

Esta carpeta contiene las animaciones listas para abrir y editar en **Piskel** (https://www.piskelapp.com/).

## Cómo abrir en Piskel:
1. Entra a **https://www.piskelapp.com/p/create/sprite** en tu navegador.
2. Haz clic en el icono de carpeta de la barra derecha (**Import**).
3. Elige cualquiera de estas opciones:
   - **Import .piskel file**: selecciona el archivo `.piskel` de cualquier animación.
   - **Import animated GIF**: selecciona el archivo `.gif` (Piskel importa todos los fotogramas y la velocidad al instante).
   - **Import from picture**: selecciona el `_sheet.png` (pon el Frame size que se indica abajo).

## Volver al juego:
`python herramientas/importar_piskel.py editado.piskel --manifiesto piskel_animaciones/reycold_0/origen.json --heroe reycold --forma 0 --anim attack --aplicar`
Después: `python herramientas/montar_animaciones.py reycold` y revisión visual. Solo se aceptan sprites originales exportados.

## Animaciones disponibles:

| Animación | Fotogramas | Tamaño de celda | Archivo .piskel | GIF animado | Hoja Strip |
|---|---|---|---|---|---|
| **Idle** | 2 | 52x52 | [`reycold_Idle.piskel`](Idle/reycold_Idle.piskel) | [`reycold_Idle.gif`](Idle/reycold_Idle.gif) | [`reycold_Idle_sheet.png`](Idle/reycold_Idle_sheet.png) |
| **Walk** | 1 | 48x48 | [`reycold_Walk.piskel`](Walk/reycold_Walk.piskel) | [`reycold_Walk.gif`](Walk/reycold_Walk.gif) | [`reycold_Walk_sheet.png`](Walk/reycold_Walk_sheet.png) |
| **Attack** | 3 | 54x54 | [`reycold_Attack.piskel`](Attack/reycold_Attack.piskel) | [`reycold_Attack.gif`](Attack/reycold_Attack.gif) | [`reycold_Attack_sheet.png`](Attack/reycold_Attack_sheet.png) |
| **Kick** | 2 | 56x56 | [`reycold_Kick.piskel`](Kick/reycold_Kick.piskel) | [`reycold_Kick.gif`](Kick/reycold_Kick.gif) | [`reycold_Kick_sheet.png`](Kick/reycold_Kick_sheet.png) |
| **Cast** | 2 | 50x50 | [`reycold_Cast.piskel`](Cast/reycold_Cast.piskel) | [`reycold_Cast.gif`](Cast/reycold_Cast.gif) | [`reycold_Cast_sheet.png`](Cast/reycold_Cast_sheet.png) |
| **Pow** | 2 | 48x48 | [`reycold_Pow.piskel`](Pow/reycold_Pow.piskel) | [`reycold_Pow.gif`](Pow/reycold_Pow.gif) | [`reycold_Pow_sheet.png`](Pow/reycold_Pow_sheet.png) |
| **Hurt** | 2 | 48x48 | [`reycold_Hurt.piskel`](Hurt/reycold_Hurt.piskel) | [`reycold_Hurt.gif`](Hurt/reycold_Hurt.gif) | [`reycold_Hurt_sheet.png`](Hurt/reycold_Hurt_sheet.png) |
| **Faint** | 1 | 54x54 | [`reycold_Faint.piskel`](Faint/reycold_Faint.piskel) | [`reycold_Faint.gif`](Faint/reycold_Faint.gif) | [`reycold_Faint_sheet.png`](Faint/reycold_Faint_sheet.png) |
| **Attack2** | 2 | 48x48 | [`reycold_Attack2.piskel`](Attack2/reycold_Attack2.piskel) | [`reycold_Attack2.gif`](Attack2/reycold_Attack2.gif) | [`reycold_Attack2_sheet.png`](Attack2/reycold_Attack2_sheet.png) |
| **Beam** | 2 | 50x50 | [`reycold_Beam.piskel`](Beam/reycold_Beam.piskel) | [`reycold_Beam.gif`](Beam/reycold_Beam.gif) | [`reycold_Beam_sheet.png`](Beam/reycold_Beam_sheet.png) |