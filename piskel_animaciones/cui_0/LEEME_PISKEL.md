# Animaciones para Piskel — CUI (Forma 0)

Esta carpeta contiene las animaciones listas para abrir y editar en **Piskel** (https://www.piskelapp.com/).

## Cómo abrir en Piskel:
1. Entra a **https://www.piskelapp.com/p/create/sprite** en tu navegador.
2. Haz clic en el icono de carpeta de la barra derecha (**Import**).
3. Elige cualquiera de estas opciones:
   - **Import .piskel file**: selecciona el archivo `.piskel` de cualquier animación.
   - **Import animated GIF**: selecciona el archivo `.gif` (Piskel importa todos los fotogramas y la velocidad al instante).
   - **Import from picture**: selecciona el `_sheet.png` (pon el Frame size que se indica abajo).

## Volver al juego:
`python herramientas/importar_piskel.py editado.piskel --manifiesto piskel_animaciones/cui_0/origen.json --heroe cui --forma 0 --anim attack --aplicar`
Después: `python herramientas/montar_animaciones.py cui` y revisión visual. Solo se aceptan sprites originales exportados.

## Animaciones disponibles:

| Animación | Fotogramas | Tamaño de celda | Archivo .piskel | GIF animado | Hoja Strip |
|---|---|---|---|---|---|
| **Idle** | 2 | 52x52 | [`cui_Idle.piskel`](Idle/cui_Idle.piskel) | [`cui_Idle.gif`](Idle/cui_Idle.gif) | [`cui_Idle_sheet.png`](Idle/cui_Idle_sheet.png) |
| **Walk** | 1 | 48x48 | [`cui_Walk.piskel`](Walk/cui_Walk.piskel) | [`cui_Walk.gif`](Walk/cui_Walk.gif) | [`cui_Walk_sheet.png`](Walk/cui_Walk_sheet.png) |
| **Attack** | 3 | 46x46 | [`cui_Attack.piskel`](Attack/cui_Attack.piskel) | [`cui_Attack.gif`](Attack/cui_Attack.gif) | [`cui_Attack_sheet.png`](Attack/cui_Attack_sheet.png) |
| **Kick** | 2 | 52x52 | [`cui_Kick.piskel`](Kick/cui_Kick.piskel) | [`cui_Kick.gif`](Kick/cui_Kick.gif) | [`cui_Kick_sheet.png`](Kick/cui_Kick_sheet.png) |
| **Cast** | 2 | 44x44 | [`cui_Cast.piskel`](Cast/cui_Cast.piskel) | [`cui_Cast.gif`](Cast/cui_Cast.gif) | [`cui_Cast_sheet.png`](Cast/cui_Cast_sheet.png) |
| **Pow** | 2 | 60x60 | [`cui_Pow.piskel`](Pow/cui_Pow.piskel) | [`cui_Pow.gif`](Pow/cui_Pow.gif) | [`cui_Pow_sheet.png`](Pow/cui_Pow_sheet.png) |
| **Hurt** | 2 | 46x46 | [`cui_Hurt.piskel`](Hurt/cui_Hurt.piskel) | [`cui_Hurt.gif`](Hurt/cui_Hurt.gif) | [`cui_Hurt_sheet.png`](Hurt/cui_Hurt_sheet.png) |
| **Faint** | 1 | 46x46 | [`cui_Faint.piskel`](Faint/cui_Faint.piskel) | [`cui_Faint.gif`](Faint/cui_Faint.gif) | [`cui_Faint_sheet.png`](Faint/cui_Faint_sheet.png) |
| **Attack2** | 2 | 46x46 | [`cui_Attack2.piskel`](Attack2/cui_Attack2.piskel) | [`cui_Attack2.gif`](Attack2/cui_Attack2.gif) | [`cui_Attack2_sheet.png`](Attack2/cui_Attack2_sheet.png) |
| **Kick2** | 2 | 52x52 | [`cui_Kick2.piskel`](Kick2/cui_Kick2.piskel) | [`cui_Kick2.gif`](Kick2/cui_Kick2.gif) | [`cui_Kick2_sheet.png`](Kick2/cui_Kick2_sheet.png) |
| **Beam** | 2 | 46x46 | [`cui_Beam.piskel`](Beam/cui_Beam.piskel) | [`cui_Beam.gif`](Beam/cui_Beam.gif) | [`cui_Beam_sheet.png`](Beam/cui_Beam_sheet.png) |
| **Up** | 1 | 46x46 | [`cui_Up.piskel`](Up/cui_Up.piskel) | [`cui_Up.gif`](Up/cui_Up.gif) | [`cui_Up_sheet.png`](Up/cui_Up_sheet.png) |