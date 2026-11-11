# Animaciones para Piskel — ZAMASUFUSION (Forma 0)

Esta carpeta contiene las animaciones listas para abrir y editar en **Piskel** (https://www.piskelapp.com/).

## Cómo abrir en Piskel:
1. Entra a **https://www.piskelapp.com/p/create/sprite** en tu navegador.
2. Haz clic en el icono de carpeta de la barra derecha (**Import**).
3. Elige cualquiera de estas opciones:
   - **Import .piskel file**: selecciona el archivo `.piskel` de cualquier animación.
   - **Import animated GIF**: selecciona el archivo `.gif` (Piskel importa todos los fotogramas y la velocidad al instante).
   - **Import from picture**: selecciona el `_sheet.png` (pon el Frame size que se indica abajo).

## Volver al juego:
`python herramientas/importar_piskel.py editado.piskel --manifiesto piskel_animaciones/zamasufusion_0/origen.json --heroe zamasufusion --forma 0 --anim attack --aplicar`
Después: `python herramientas/montar_animaciones.py zamasufusion` y revisión visual. Solo se aceptan sprites originales exportados.

## Animaciones disponibles:

| Animación | Fotogramas | Tamaño de celda | Archivo .piskel | GIF animado | Hoja Strip |
|---|---|---|---|---|---|
| **Idle** | 2 | 60x60 | [`zamasufusion_Idle.piskel`](Idle/zamasufusion_Idle.piskel) | [`zamasufusion_Idle.gif`](Idle/zamasufusion_Idle.gif) | [`zamasufusion_Idle_sheet.png`](Idle/zamasufusion_Idle_sheet.png) |
| **Walk** | 1 | 62x62 | [`zamasufusion_Walk.piskel`](Walk/zamasufusion_Walk.piskel) | [`zamasufusion_Walk.gif`](Walk/zamasufusion_Walk.gif) | [`zamasufusion_Walk_sheet.png`](Walk/zamasufusion_Walk_sheet.png) |
| **Attack** | 3 | 64x64 | [`zamasufusion_Attack.piskel`](Attack/zamasufusion_Attack.piskel) | [`zamasufusion_Attack.gif`](Attack/zamasufusion_Attack.gif) | [`zamasufusion_Attack_sheet.png`](Attack/zamasufusion_Attack_sheet.png) |
| **Kick** | 2 | 64x64 | [`zamasufusion_Kick.piskel`](Kick/zamasufusion_Kick.piskel) | [`zamasufusion_Kick.gif`](Kick/zamasufusion_Kick.gif) | [`zamasufusion_Kick_sheet.png`](Kick/zamasufusion_Kick_sheet.png) |
| **Cast** | 2 | 66x66 | [`zamasufusion_Cast.piskel`](Cast/zamasufusion_Cast.piskel) | [`zamasufusion_Cast.gif`](Cast/zamasufusion_Cast.gif) | [`zamasufusion_Cast_sheet.png`](Cast/zamasufusion_Cast_sheet.png) |
| **Pow** | 2 | 70x70 | [`zamasufusion_Pow.piskel`](Pow/zamasufusion_Pow.piskel) | [`zamasufusion_Pow.gif`](Pow/zamasufusion_Pow.gif) | [`zamasufusion_Pow_sheet.png`](Pow/zamasufusion_Pow_sheet.png) |
| **Hurt** | 2 | 60x60 | [`zamasufusion_Hurt.piskel`](Hurt/zamasufusion_Hurt.piskel) | [`zamasufusion_Hurt.gif`](Hurt/zamasufusion_Hurt.gif) | [`zamasufusion_Hurt_sheet.png`](Hurt/zamasufusion_Hurt_sheet.png) |
| **Faint** | 1 | 66x66 | [`zamasufusion_Faint.piskel`](Faint/zamasufusion_Faint.piskel) | [`zamasufusion_Faint.gif`](Faint/zamasufusion_Faint.gif) | [`zamasufusion_Faint_sheet.png`](Faint/zamasufusion_Faint_sheet.png) |
| **Attack2** | 2 | 62x62 | [`zamasufusion_Attack2.piskel`](Attack2/zamasufusion_Attack2.piskel) | [`zamasufusion_Attack2.gif`](Attack2/zamasufusion_Attack2.gif) | [`zamasufusion_Attack2_sheet.png`](Attack2/zamasufusion_Attack2_sheet.png) |
| **Kick2** | 2 | 54x54 | [`zamasufusion_Kick2.piskel`](Kick2/zamasufusion_Kick2.piskel) | [`zamasufusion_Kick2.gif`](Kick2/zamasufusion_Kick2.gif) | [`zamasufusion_Kick2_sheet.png`](Kick2/zamasufusion_Kick2_sheet.png) |
| **Beam** | 2 | 72x72 | [`zamasufusion_Beam.piskel`](Beam/zamasufusion_Beam.piskel) | [`zamasufusion_Beam.gif`](Beam/zamasufusion_Beam.gif) | [`zamasufusion_Beam_sheet.png`](Beam/zamasufusion_Beam_sheet.png) |
| **Up** | 1 | 80x80 | [`zamasufusion_Up.piskel`](Up/zamasufusion_Up.piskel) | [`zamasufusion_Up.gif`](Up/zamasufusion_Up.gif) | [`zamasufusion_Up_sheet.png`](Up/zamasufusion_Up_sheet.png) |