# Animaciones para Piskel — HATCHIYACK (Forma 0)

Esta carpeta contiene las animaciones listas para abrir y editar en **Piskel** (https://www.piskelapp.com/).

## Cómo abrir en Piskel:
1. Entra a **https://www.piskelapp.com/p/create/sprite** en tu navegador.
2. Haz clic en el icono de carpeta de la barra derecha (**Import**).
3. Elige cualquiera de estas opciones:
   - **Import .piskel file**: selecciona el archivo `.piskel` de cualquier animación.
   - **Import animated GIF**: selecciona el archivo `.gif` (Piskel importa todos los fotogramas y la velocidad al instante).
   - **Import from picture**: selecciona el `_sheet.png` (pon el Frame size que se indica abajo).

## Volver al juego:
`python herramientas/importar_piskel.py editado.piskel --manifiesto piskel_animaciones/hatchiyack_0/origen.json --heroe hatchiyack --forma 0 --anim attack --aplicar`
Después: `python herramientas/montar_animaciones.py hatchiyack` y revisión visual. Solo se aceptan sprites originales exportados.

## Animaciones disponibles:

| Animación | Fotogramas | Tamaño de celda | Archivo .piskel | GIF animado | Hoja Strip |
|---|---|---|---|---|---|
| **Idle** | 2 | 52x52 | [`hatchiyack_Idle.piskel`](Idle/hatchiyack_Idle.piskel) | [`hatchiyack_Idle.gif`](Idle/hatchiyack_Idle.gif) | [`hatchiyack_Idle_sheet.png`](Idle/hatchiyack_Idle_sheet.png) |
| **Walk** | 1 | 44x44 | [`hatchiyack_Walk.piskel`](Walk/hatchiyack_Walk.piskel) | [`hatchiyack_Walk.gif`](Walk/hatchiyack_Walk.gif) | [`hatchiyack_Walk_sheet.png`](Walk/hatchiyack_Walk_sheet.png) |
| **Attack** | 3 | 48x48 | [`hatchiyack_Attack.piskel`](Attack/hatchiyack_Attack.piskel) | [`hatchiyack_Attack.gif`](Attack/hatchiyack_Attack.gif) | [`hatchiyack_Attack_sheet.png`](Attack/hatchiyack_Attack_sheet.png) |
| **Kick** | 2 | 52x52 | [`hatchiyack_Kick.piskel`](Kick/hatchiyack_Kick.piskel) | [`hatchiyack_Kick.gif`](Kick/hatchiyack_Kick.gif) | [`hatchiyack_Kick_sheet.png`](Kick/hatchiyack_Kick_sheet.png) |
| **Cast** | 2 | 52x52 | [`hatchiyack_Cast.piskel`](Cast/hatchiyack_Cast.piskel) | [`hatchiyack_Cast.gif`](Cast/hatchiyack_Cast.gif) | [`hatchiyack_Cast_sheet.png`](Cast/hatchiyack_Cast_sheet.png) |
| **Pow** | 3 | 72x72 | [`hatchiyack_Pow.piskel`](Pow/hatchiyack_Pow.piskel) | [`hatchiyack_Pow.gif`](Pow/hatchiyack_Pow.gif) | [`hatchiyack_Pow_sheet.png`](Pow/hatchiyack_Pow_sheet.png) |
| **Hurt** | 2 | 42x42 | [`hatchiyack_Hurt.piskel`](Hurt/hatchiyack_Hurt.piskel) | [`hatchiyack_Hurt.gif`](Hurt/hatchiyack_Hurt.gif) | [`hatchiyack_Hurt_sheet.png`](Hurt/hatchiyack_Hurt_sheet.png) |
| **Attack2** | 2 | 44x44 | [`hatchiyack_Attack2.piskel`](Attack2/hatchiyack_Attack2.piskel) | [`hatchiyack_Attack2.gif`](Attack2/hatchiyack_Attack2.gif) | [`hatchiyack_Attack2_sheet.png`](Attack2/hatchiyack_Attack2_sheet.png) |
| **Attack3** | 2 | 48x48 | [`hatchiyack_Attack3.piskel`](Attack3/hatchiyack_Attack3.piskel) | [`hatchiyack_Attack3.gif`](Attack3/hatchiyack_Attack3.gif) | [`hatchiyack_Attack3_sheet.png`](Attack3/hatchiyack_Attack3_sheet.png) |
| **Beam** | 2 | 52x52 | [`hatchiyack_Beam.piskel`](Beam/hatchiyack_Beam.piskel) | [`hatchiyack_Beam.gif`](Beam/hatchiyack_Beam.gif) | [`hatchiyack_Beam_sheet.png`](Beam/hatchiyack_Beam_sheet.png) |
| **Up** | 1 | 54x54 | [`hatchiyack_Up.piskel`](Up/hatchiyack_Up.piskel) | [`hatchiyack_Up.gif`](Up/hatchiyack_Up.gif) | [`hatchiyack_Up_sheet.png`](Up/hatchiyack_Up_sheet.png) |