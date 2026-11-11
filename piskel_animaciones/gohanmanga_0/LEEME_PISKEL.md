# Animaciones para Piskel — GOHANMANGA (Forma 0)

Esta carpeta contiene las animaciones listas para abrir y editar en **Piskel** (https://www.piskelapp.com/).

## Cómo abrir en Piskel:
1. Entra a **https://www.piskelapp.com/p/create/sprite** en tu navegador.
2. Haz clic en el icono de carpeta de la barra derecha (**Import**).
3. Elige cualquiera de estas opciones:
   - **Import .piskel file**: selecciona el archivo `.piskel` de cualquier animación.
   - **Import animated GIF**: selecciona el archivo `.gif` (Piskel importa todos los fotogramas y la velocidad al instante).
   - **Import from picture**: selecciona el `_sheet.png` (pon el Frame size que se indica abajo).

## Volver al juego:
`python herramientas/importar_piskel.py editado.piskel --manifiesto piskel_animaciones/gohanmanga_0/origen.json --heroe gohanmanga --forma 0 --anim attack --aplicar`
Después: `python herramientas/montar_animaciones.py gohanmanga` y revisión visual. Solo se aceptan sprites originales exportados.

## Animaciones disponibles:

| Animación | Fotogramas | Tamaño de celda | Archivo .piskel | GIF animado | Hoja Strip |
|---|---|---|---|---|---|
| **Idle** | 2 | 54x54 | [`gohanmanga_Idle.piskel`](Idle/gohanmanga_Idle.piskel) | [`gohanmanga_Idle.gif`](Idle/gohanmanga_Idle.gif) | [`gohanmanga_Idle_sheet.png`](Idle/gohanmanga_Idle_sheet.png) |
| **Walk** | 1 | 44x44 | [`gohanmanga_Walk.piskel`](Walk/gohanmanga_Walk.piskel) | [`gohanmanga_Walk.gif`](Walk/gohanmanga_Walk.gif) | [`gohanmanga_Walk_sheet.png`](Walk/gohanmanga_Walk_sheet.png) |
| **Attack** | 3 | 50x50 | [`gohanmanga_Attack.piskel`](Attack/gohanmanga_Attack.piskel) | [`gohanmanga_Attack.gif`](Attack/gohanmanga_Attack.gif) | [`gohanmanga_Attack_sheet.png`](Attack/gohanmanga_Attack_sheet.png) |
| **Kick** | 2 | 56x56 | [`gohanmanga_Kick.piskel`](Kick/gohanmanga_Kick.piskel) | [`gohanmanga_Kick.gif`](Kick/gohanmanga_Kick.gif) | [`gohanmanga_Kick_sheet.png`](Kick/gohanmanga_Kick_sheet.png) |
| **Cast** | 2 | 54x54 | [`gohanmanga_Cast.piskel`](Cast/gohanmanga_Cast.piskel) | [`gohanmanga_Cast.gif`](Cast/gohanmanga_Cast.gif) | [`gohanmanga_Cast_sheet.png`](Cast/gohanmanga_Cast_sheet.png) |
| **Pow** | 2 | 82x82 | [`gohanmanga_Pow.piskel`](Pow/gohanmanga_Pow.piskel) | [`gohanmanga_Pow.gif`](Pow/gohanmanga_Pow.gif) | [`gohanmanga_Pow_sheet.png`](Pow/gohanmanga_Pow_sheet.png) |
| **Hurt** | 2 | 54x54 | [`gohanmanga_Hurt.piskel`](Hurt/gohanmanga_Hurt.piskel) | [`gohanmanga_Hurt.gif`](Hurt/gohanmanga_Hurt.gif) | [`gohanmanga_Hurt_sheet.png`](Hurt/gohanmanga_Hurt_sheet.png) |
| **Faint** | 1 | 54x54 | [`gohanmanga_Faint.piskel`](Faint/gohanmanga_Faint.piskel) | [`gohanmanga_Faint.gif`](Faint/gohanmanga_Faint.gif) | [`gohanmanga_Faint_sheet.png`](Faint/gohanmanga_Faint_sheet.png) |
| **Attack2** | 2 | 52x52 | [`gohanmanga_Attack2.piskel`](Attack2/gohanmanga_Attack2.piskel) | [`gohanmanga_Attack2.gif`](Attack2/gohanmanga_Attack2.gif) | [`gohanmanga_Attack2_sheet.png`](Attack2/gohanmanga_Attack2_sheet.png) |
| **Beam** | 2 | 54x54 | [`gohanmanga_Beam.piskel`](Beam/gohanmanga_Beam.piskel) | [`gohanmanga_Beam.gif`](Beam/gohanmanga_Beam.gif) | [`gohanmanga_Beam_sheet.png`](Beam/gohanmanga_Beam_sheet.png) |
| **Up** | 1 | 50x50 | [`gohanmanga_Up.piskel`](Up/gohanmanga_Up.piskel) | [`gohanmanga_Up.gif`](Up/gohanmanga_Up.gif) | [`gohanmanga_Up_sheet.png`](Up/gohanmanga_Up_sheet.png) |