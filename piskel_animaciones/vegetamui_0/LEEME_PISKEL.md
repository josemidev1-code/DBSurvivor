# Animaciones para Piskel — VEGETAMUI (Forma 0)

Esta carpeta contiene las animaciones listas para abrir y editar en **Piskel** (https://www.piskelapp.com/).

## Cómo abrir en Piskel:
1. Entra a **https://www.piskelapp.com/p/create/sprite** en tu navegador.
2. Haz clic en el icono de carpeta de la barra derecha (**Import**).
3. Elige cualquiera de estas opciones:
   - **Import .piskel file**: selecciona el archivo `.piskel` de cualquier animación.
   - **Import animated GIF**: selecciona el archivo `.gif` (Piskel importa todos los fotogramas y la velocidad al instante).
   - **Import from picture**: selecciona el `_sheet.png` (pon el Frame size que se indica abajo).

## Volver al juego:
`python herramientas/importar_piskel.py editado.piskel --manifiesto piskel_animaciones/vegetamui_0/origen.json --heroe vegetamui --forma 0 --anim attack --aplicar`
Después: `python herramientas/montar_animaciones.py vegetamui` y revisión visual. Solo se aceptan sprites originales exportados.

## Animaciones disponibles:

| Animación | Fotogramas | Tamaño de celda | Archivo .piskel | GIF animado | Hoja Strip |
|---|---|---|---|---|---|
| **Idle** | 2 | 56x56 | [`vegetamui_Idle.piskel`](Idle/vegetamui_Idle.piskel) | [`vegetamui_Idle.gif`](Idle/vegetamui_Idle.gif) | [`vegetamui_Idle_sheet.png`](Idle/vegetamui_Idle_sheet.png) |
| **Walk** | 1 | 52x52 | [`vegetamui_Walk.piskel`](Walk/vegetamui_Walk.piskel) | [`vegetamui_Walk.gif`](Walk/vegetamui_Walk.gif) | [`vegetamui_Walk_sheet.png`](Walk/vegetamui_Walk_sheet.png) |
| **Attack** | 3 | 52x52 | [`vegetamui_Attack.piskel`](Attack/vegetamui_Attack.piskel) | [`vegetamui_Attack.gif`](Attack/vegetamui_Attack.gif) | [`vegetamui_Attack_sheet.png`](Attack/vegetamui_Attack_sheet.png) |
| **Kick** | 2 | 52x52 | [`vegetamui_Kick.piskel`](Kick/vegetamui_Kick.piskel) | [`vegetamui_Kick.gif`](Kick/vegetamui_Kick.gif) | [`vegetamui_Kick_sheet.png`](Kick/vegetamui_Kick_sheet.png) |
| **Cast** | 2 | 54x54 | [`vegetamui_Cast.piskel`](Cast/vegetamui_Cast.piskel) | [`vegetamui_Cast.gif`](Cast/vegetamui_Cast.gif) | [`vegetamui_Cast_sheet.png`](Cast/vegetamui_Cast_sheet.png) |
| **Pow** | 2 | 70x70 | [`vegetamui_Pow.piskel`](Pow/vegetamui_Pow.piskel) | [`vegetamui_Pow.gif`](Pow/vegetamui_Pow.gif) | [`vegetamui_Pow_sheet.png`](Pow/vegetamui_Pow_sheet.png) |
| **Hurt** | 2 | 46x46 | [`vegetamui_Hurt.piskel`](Hurt/vegetamui_Hurt.piskel) | [`vegetamui_Hurt.gif`](Hurt/vegetamui_Hurt.gif) | [`vegetamui_Hurt_sheet.png`](Hurt/vegetamui_Hurt_sheet.png) |
| **Faint** | 1 | 44x44 | [`vegetamui_Faint.piskel`](Faint/vegetamui_Faint.piskel) | [`vegetamui_Faint.gif`](Faint/vegetamui_Faint.gif) | [`vegetamui_Faint_sheet.png`](Faint/vegetamui_Faint_sheet.png) |
| **Attack2** | 2 | 58x58 | [`vegetamui_Attack2.piskel`](Attack2/vegetamui_Attack2.piskel) | [`vegetamui_Attack2.gif`](Attack2/vegetamui_Attack2.gif) | [`vegetamui_Attack2_sheet.png`](Attack2/vegetamui_Attack2_sheet.png) |
| **Attack3** | 2 | 52x52 | [`vegetamui_Attack3.piskel`](Attack3/vegetamui_Attack3.piskel) | [`vegetamui_Attack3.gif`](Attack3/vegetamui_Attack3.gif) | [`vegetamui_Attack3_sheet.png`](Attack3/vegetamui_Attack3_sheet.png) |
| **Kick2** | 2 | 52x52 | [`vegetamui_Kick2.piskel`](Kick2/vegetamui_Kick2.piskel) | [`vegetamui_Kick2.gif`](Kick2/vegetamui_Kick2.gif) | [`vegetamui_Kick2_sheet.png`](Kick2/vegetamui_Kick2_sheet.png) |
| **Beam** | 2 | 44x44 | [`vegetamui_Beam.piskel`](Beam/vegetamui_Beam.piskel) | [`vegetamui_Beam.gif`](Beam/vegetamui_Beam.gif) | [`vegetamui_Beam_sheet.png`](Beam/vegetamui_Beam_sheet.png) |
| **Up** | 1 | 50x50 | [`vegetamui_Up.piskel`](Up/vegetamui_Up.piskel) | [`vegetamui_Up.gif`](Up/vegetamui_Up.gif) | [`vegetamui_Up_sheet.png`](Up/vegetamui_Up_sheet.png) |