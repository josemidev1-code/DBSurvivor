# Animaciones para Piskel — PARAGUS (Forma 0)

Esta carpeta contiene las animaciones listas para abrir y editar en **Piskel** (https://www.piskelapp.com/).

## Cómo abrir en Piskel:
1. Entra a **https://www.piskelapp.com/p/create/sprite** en tu navegador.
2. Haz clic en el icono de carpeta de la barra derecha (**Import**).
3. Elige cualquiera de estas opciones:
   - **Import .piskel file**: selecciona el archivo `.piskel` de cualquier animación.
   - **Import animated GIF**: selecciona el archivo `.gif` (Piskel importa todos los fotogramas y la velocidad al instante).
   - **Import from picture**: selecciona el `_sheet.png` (pon el Frame size que se indica abajo).

## Volver al juego:
`python herramientas/importar_piskel.py editado.piskel --manifiesto piskel_animaciones/paragus_0/origen.json --heroe paragus --forma 0 --anim attack --aplicar`
Después: `python herramientas/montar_animaciones.py paragus` y revisión visual. Solo se aceptan sprites originales exportados.

## Animaciones disponibles:

| Animación | Fotogramas | Tamaño de celda | Archivo .piskel | GIF animado | Hoja Strip |
|---|---|---|---|---|---|
| **Idle** | 2 | 54x54 | [`paragus_Idle.piskel`](Idle/paragus_Idle.piskel) | [`paragus_Idle.gif`](Idle/paragus_Idle.gif) | [`paragus_Idle_sheet.png`](Idle/paragus_Idle_sheet.png) |
| **Walk** | 1 | 46x46 | [`paragus_Walk.piskel`](Walk/paragus_Walk.piskel) | [`paragus_Walk.gif`](Walk/paragus_Walk.gif) | [`paragus_Walk_sheet.png`](Walk/paragus_Walk_sheet.png) |
| **Attack** | 3 | 48x48 | [`paragus_Attack.piskel`](Attack/paragus_Attack.piskel) | [`paragus_Attack.gif`](Attack/paragus_Attack.gif) | [`paragus_Attack_sheet.png`](Attack/paragus_Attack_sheet.png) |
| **Kick** | 2 | 52x52 | [`paragus_Kick.piskel`](Kick/paragus_Kick.piskel) | [`paragus_Kick.gif`](Kick/paragus_Kick.gif) | [`paragus_Kick_sheet.png`](Kick/paragus_Kick_sheet.png) |
| **Cast** | 2 | 60x60 | [`paragus_Cast.piskel`](Cast/paragus_Cast.piskel) | [`paragus_Cast.gif`](Cast/paragus_Cast.gif) | [`paragus_Cast_sheet.png`](Cast/paragus_Cast_sheet.png) |
| **Pow** | 2 | 90x90 | [`paragus_Pow.piskel`](Pow/paragus_Pow.piskel) | [`paragus_Pow.gif`](Pow/paragus_Pow.gif) | [`paragus_Pow_sheet.png`](Pow/paragus_Pow_sheet.png) |
| **Hurt** | 2 | 50x50 | [`paragus_Hurt.piskel`](Hurt/paragus_Hurt.piskel) | [`paragus_Hurt.gif`](Hurt/paragus_Hurt.gif) | [`paragus_Hurt_sheet.png`](Hurt/paragus_Hurt_sheet.png) |
| **Faint** | 1 | 56x56 | [`paragus_Faint.piskel`](Faint/paragus_Faint.piskel) | [`paragus_Faint.gif`](Faint/paragus_Faint.gif) | [`paragus_Faint_sheet.png`](Faint/paragus_Faint_sheet.png) |
| **Attack2** | 3 | 58x58 | [`paragus_Attack2.piskel`](Attack2/paragus_Attack2.piskel) | [`paragus_Attack2.gif`](Attack2/paragus_Attack2.gif) | [`paragus_Attack2_sheet.png`](Attack2/paragus_Attack2_sheet.png) |
| **Attack3** | 2 | 50x50 | [`paragus_Attack3.piskel`](Attack3/paragus_Attack3.piskel) | [`paragus_Attack3.gif`](Attack3/paragus_Attack3.gif) | [`paragus_Attack3_sheet.png`](Attack3/paragus_Attack3_sheet.png) |
| **Beam** | 2 | 60x60 | [`paragus_Beam.piskel`](Beam/paragus_Beam.piskel) | [`paragus_Beam.gif`](Beam/paragus_Beam.gif) | [`paragus_Beam_sheet.png`](Beam/paragus_Beam_sheet.png) |