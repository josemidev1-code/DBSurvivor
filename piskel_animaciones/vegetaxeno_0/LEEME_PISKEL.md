# Animaciones para Piskel — VEGETAXENO (Forma 0)

Esta carpeta contiene las animaciones listas para abrir y editar en **Piskel** (https://www.piskelapp.com/).

## Cómo abrir en Piskel:
1. Entra a **https://www.piskelapp.com/p/create/sprite** en tu navegador.
2. Haz clic en el icono de carpeta de la barra derecha (**Import**).
3. Elige cualquiera de estas opciones:
   - **Import .piskel file**: selecciona el archivo `.piskel` de cualquier animación.
   - **Import animated GIF**: selecciona el archivo `.gif` (Piskel importa todos los fotogramas y la velocidad al instante).
   - **Import from picture**: selecciona el `_sheet.png` (pon el Frame size que se indica abajo).

## Volver al juego:
`python herramientas/importar_piskel.py editado.piskel --manifiesto piskel_animaciones/vegetaxeno_0/origen.json --heroe vegetaxeno --forma 0 --anim attack --aplicar`
Después: `python herramientas/montar_animaciones.py vegetaxeno` y revisión visual. Solo se aceptan sprites originales exportados.

## Animaciones disponibles:

| Animación | Fotogramas | Tamaño de celda | Archivo .piskel | GIF animado | Hoja Strip |
|---|---|---|---|---|---|
| **Idle** | 2 | 60x60 | [`vegetaxeno_Idle.piskel`](Idle/vegetaxeno_Idle.piskel) | [`vegetaxeno_Idle.gif`](Idle/vegetaxeno_Idle.gif) | [`vegetaxeno_Idle_sheet.png`](Idle/vegetaxeno_Idle_sheet.png) |
| **Walk** | 1 | 54x54 | [`vegetaxeno_Walk.piskel`](Walk/vegetaxeno_Walk.piskel) | [`vegetaxeno_Walk.gif`](Walk/vegetaxeno_Walk.gif) | [`vegetaxeno_Walk_sheet.png`](Walk/vegetaxeno_Walk_sheet.png) |
| **Attack** | 3 | 60x60 | [`vegetaxeno_Attack.piskel`](Attack/vegetaxeno_Attack.piskel) | [`vegetaxeno_Attack.gif`](Attack/vegetaxeno_Attack.gif) | [`vegetaxeno_Attack_sheet.png`](Attack/vegetaxeno_Attack_sheet.png) |
| **Kick** | 2 | 56x56 | [`vegetaxeno_Kick.piskel`](Kick/vegetaxeno_Kick.piskel) | [`vegetaxeno_Kick.gif`](Kick/vegetaxeno_Kick.gif) | [`vegetaxeno_Kick_sheet.png`](Kick/vegetaxeno_Kick_sheet.png) |
| **Cast** | 2 | 64x64 | [`vegetaxeno_Cast.piskel`](Cast/vegetaxeno_Cast.piskel) | [`vegetaxeno_Cast.gif`](Cast/vegetaxeno_Cast.gif) | [`vegetaxeno_Cast_sheet.png`](Cast/vegetaxeno_Cast_sheet.png) |
| **Pow** | 2 | 104x104 | [`vegetaxeno_Pow.piskel`](Pow/vegetaxeno_Pow.piskel) | [`vegetaxeno_Pow.gif`](Pow/vegetaxeno_Pow.gif) | [`vegetaxeno_Pow_sheet.png`](Pow/vegetaxeno_Pow_sheet.png) |
| **Hurt** | 2 | 70x70 | [`vegetaxeno_Hurt.piskel`](Hurt/vegetaxeno_Hurt.piskel) | [`vegetaxeno_Hurt.gif`](Hurt/vegetaxeno_Hurt.gif) | [`vegetaxeno_Hurt_sheet.png`](Hurt/vegetaxeno_Hurt_sheet.png) |
| **Faint** | 1 | 60x60 | [`vegetaxeno_Faint.piskel`](Faint/vegetaxeno_Faint.piskel) | [`vegetaxeno_Faint.gif`](Faint/vegetaxeno_Faint.gif) | [`vegetaxeno_Faint_sheet.png`](Faint/vegetaxeno_Faint_sheet.png) |
| **Attack2** | 2 | 60x60 | [`vegetaxeno_Attack2.piskel`](Attack2/vegetaxeno_Attack2.piskel) | [`vegetaxeno_Attack2.gif`](Attack2/vegetaxeno_Attack2.gif) | [`vegetaxeno_Attack2_sheet.png`](Attack2/vegetaxeno_Attack2_sheet.png) |
| **Kick2** | 2 | 70x70 | [`vegetaxeno_Kick2.piskel`](Kick2/vegetaxeno_Kick2.piskel) | [`vegetaxeno_Kick2.gif`](Kick2/vegetaxeno_Kick2.gif) | [`vegetaxeno_Kick2_sheet.png`](Kick2/vegetaxeno_Kick2_sheet.png) |
| **Beam** | 2 | 56x56 | [`vegetaxeno_Beam.piskel`](Beam/vegetaxeno_Beam.piskel) | [`vegetaxeno_Beam.gif`](Beam/vegetaxeno_Beam.gif) | [`vegetaxeno_Beam_sheet.png`](Beam/vegetaxeno_Beam_sheet.png) |