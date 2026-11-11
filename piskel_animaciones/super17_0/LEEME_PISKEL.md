# Animaciones para Piskel — SUPER17 (Forma 0)

Esta carpeta contiene las animaciones listas para abrir y editar en **Piskel** (https://www.piskelapp.com/).

## Cómo abrir en Piskel:
1. Entra a **https://www.piskelapp.com/p/create/sprite** en tu navegador.
2. Haz clic en el icono de carpeta de la barra derecha (**Import**).
3. Elige cualquiera de estas opciones:
   - **Import .piskel file**: selecciona el archivo `.piskel` de cualquier animación.
   - **Import animated GIF**: selecciona el archivo `.gif` (Piskel importa todos los fotogramas y la velocidad al instante).
   - **Import from picture**: selecciona el `_sheet.png` (pon el Frame size que se indica abajo).

## Volver al juego:
`python herramientas/importar_piskel.py editado.piskel --manifiesto piskel_animaciones/super17_0/origen.json --heroe super17 --forma 0 --anim attack --aplicar`
Después: `python herramientas/montar_animaciones.py super17` y revisión visual. Solo se aceptan sprites originales exportados.

## Animaciones disponibles:

| Animación | Fotogramas | Tamaño de celda | Archivo .piskel | GIF animado | Hoja Strip |
|---|---|---|---|---|---|
| **Idle** | 2 | 52x52 | [`super17_Idle.piskel`](Idle/super17_Idle.piskel) | [`super17_Idle.gif`](Idle/super17_Idle.gif) | [`super17_Idle_sheet.png`](Idle/super17_Idle_sheet.png) |
| **Walk** | 1 | 46x46 | [`super17_Walk.piskel`](Walk/super17_Walk.piskel) | [`super17_Walk.gif`](Walk/super17_Walk.gif) | [`super17_Walk_sheet.png`](Walk/super17_Walk_sheet.png) |
| **Attack** | 3 | 48x48 | [`super17_Attack.piskel`](Attack/super17_Attack.piskel) | [`super17_Attack.gif`](Attack/super17_Attack.gif) | [`super17_Attack_sheet.png`](Attack/super17_Attack_sheet.png) |
| **Kick** | 2 | 46x46 | [`super17_Kick.piskel`](Kick/super17_Kick.piskel) | [`super17_Kick.gif`](Kick/super17_Kick.gif) | [`super17_Kick_sheet.png`](Kick/super17_Kick_sheet.png) |
| **Cast** | 2 | 52x52 | [`super17_Cast.piskel`](Cast/super17_Cast.piskel) | [`super17_Cast.gif`](Cast/super17_Cast.gif) | [`super17_Cast_sheet.png`](Cast/super17_Cast_sheet.png) |
| **Pow** | 2 | 56x56 | [`super17_Pow.piskel`](Pow/super17_Pow.piskel) | [`super17_Pow.gif`](Pow/super17_Pow.gif) | [`super17_Pow_sheet.png`](Pow/super17_Pow_sheet.png) |
| **Hurt** | 2 | 48x48 | [`super17_Hurt.piskel`](Hurt/super17_Hurt.piskel) | [`super17_Hurt.gif`](Hurt/super17_Hurt.gif) | [`super17_Hurt_sheet.png`](Hurt/super17_Hurt_sheet.png) |
| **Faint** | 1 | 52x52 | [`super17_Faint.piskel`](Faint/super17_Faint.piskel) | [`super17_Faint.gif`](Faint/super17_Faint.gif) | [`super17_Faint_sheet.png`](Faint/super17_Faint_sheet.png) |
| **Attack2** | 2 | 46x46 | [`super17_Attack2.piskel`](Attack2/super17_Attack2.piskel) | [`super17_Attack2.gif`](Attack2/super17_Attack2.gif) | [`super17_Attack2_sheet.png`](Attack2/super17_Attack2_sheet.png) |
| **Beam** | 2 | 50x50 | [`super17_Beam.piskel`](Beam/super17_Beam.piskel) | [`super17_Beam.gif`](Beam/super17_Beam.gif) | [`super17_Beam_sheet.png`](Beam/super17_Beam_sheet.png) |
| **Up** | 1 | 56x56 | [`super17_Up.piskel`](Up/super17_Up.piskel) | [`super17_Up.gif`](Up/super17_Up.gif) | [`super17_Up_sheet.png`](Up/super17_Up_sheet.png) |