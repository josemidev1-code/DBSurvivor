# Animaciones para Piskel — KIBITO (Forma 0)

Esta carpeta contiene las animaciones listas para abrir y editar en **Piskel** (https://www.piskelapp.com/).

## Cómo abrir en Piskel:
1. Entra a **https://www.piskelapp.com/p/create/sprite** en tu navegador.
2. Haz clic en el icono de carpeta de la barra derecha (**Import**).
3. Elige cualquiera de estas opciones:
   - **Import .piskel file**: selecciona el archivo `.piskel` de cualquier animación.
   - **Import animated GIF**: selecciona el archivo `.gif` (Piskel importa todos los fotogramas y la velocidad al instante).
   - **Import from picture**: selecciona el `_sheet.png` (pon el Frame size que se indica abajo).

## Volver al juego:
`python herramientas/importar_piskel.py editado.piskel --manifiesto piskel_animaciones/kibito_0/origen.json --heroe kibito --forma 0 --anim attack --aplicar`
Después: `python herramientas/montar_animaciones.py kibito` y revisión visual. Solo se aceptan sprites originales exportados.

## Animaciones disponibles:

| Animación | Fotogramas | Tamaño de celda | Archivo .piskel | GIF animado | Hoja Strip |
|---|---|---|---|---|---|
| **Idle** | 2 | 52x52 | [`kibito_Idle.piskel`](Idle/kibito_Idle.piskel) | [`kibito_Idle.gif`](Idle/kibito_Idle.gif) | [`kibito_Idle_sheet.png`](Idle/kibito_Idle_sheet.png) |
| **Walk** | 1 | 42x42 | [`kibito_Walk.piskel`](Walk/kibito_Walk.piskel) | [`kibito_Walk.gif`](Walk/kibito_Walk.gif) | [`kibito_Walk_sheet.png`](Walk/kibito_Walk_sheet.png) |
| **Attack** | 3 | 44x44 | [`kibito_Attack.piskel`](Attack/kibito_Attack.piskel) | [`kibito_Attack.gif`](Attack/kibito_Attack.gif) | [`kibito_Attack_sheet.png`](Attack/kibito_Attack_sheet.png) |
| **Kick** | 2 | 46x46 | [`kibito_Kick.piskel`](Kick/kibito_Kick.piskel) | [`kibito_Kick.gif`](Kick/kibito_Kick.gif) | [`kibito_Kick_sheet.png`](Kick/kibito_Kick_sheet.png) |
| **Cast** | 3 | 52x52 | [`kibito_Cast.piskel`](Cast/kibito_Cast.piskel) | [`kibito_Cast.gif`](Cast/kibito_Cast.gif) | [`kibito_Cast_sheet.png`](Cast/kibito_Cast_sheet.png) |
| **Pow** | 2 | 94x94 | [`kibito_Pow.piskel`](Pow/kibito_Pow.piskel) | [`kibito_Pow.gif`](Pow/kibito_Pow.gif) | [`kibito_Pow_sheet.png`](Pow/kibito_Pow_sheet.png) |
| **Hurt** | 2 | 42x42 | [`kibito_Hurt.piskel`](Hurt/kibito_Hurt.piskel) | [`kibito_Hurt.gif`](Hurt/kibito_Hurt.gif) | [`kibito_Hurt_sheet.png`](Hurt/kibito_Hurt_sheet.png) |
| **Faint** | 1 | 48x48 | [`kibito_Faint.piskel`](Faint/kibito_Faint.piskel) | [`kibito_Faint.gif`](Faint/kibito_Faint.gif) | [`kibito_Faint_sheet.png`](Faint/kibito_Faint_sheet.png) |
| **Attack2** | 3 | 52x52 | [`kibito_Attack2.piskel`](Attack2/kibito_Attack2.piskel) | [`kibito_Attack2.gif`](Attack2/kibito_Attack2.gif) | [`kibito_Attack2_sheet.png`](Attack2/kibito_Attack2_sheet.png) |
| **Attack3** | 2 | 46x46 | [`kibito_Attack3.piskel`](Attack3/kibito_Attack3.piskel) | [`kibito_Attack3.gif`](Attack3/kibito_Attack3.gif) | [`kibito_Attack3_sheet.png`](Attack3/kibito_Attack3_sheet.png) |
| **Kick2** | 2 | 42x42 | [`kibito_Kick2.piskel`](Kick2/kibito_Kick2.piskel) | [`kibito_Kick2.gif`](Kick2/kibito_Kick2.gif) | [`kibito_Kick2_sheet.png`](Kick2/kibito_Kick2_sheet.png) |
| **Beam** | 2 | 46x46 | [`kibito_Beam.piskel`](Beam/kibito_Beam.piskel) | [`kibito_Beam.gif`](Beam/kibito_Beam.gif) | [`kibito_Beam_sheet.png`](Beam/kibito_Beam_sheet.png) |