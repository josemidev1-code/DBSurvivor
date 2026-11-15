# Animaciones para Piskel — TRUNKSGT (Forma 0)

Esta carpeta contiene las animaciones listas para abrir y editar en **Piskel** (https://www.piskelapp.com/).

## Cómo abrir en Piskel:
1. Entra a **https://www.piskelapp.com/p/create/sprite** en tu navegador.
2. Haz clic en el icono de carpeta de la barra derecha (**Import**).
3. Elige cualquiera de estas opciones:
   - **Import .piskel file**: selecciona el archivo `.piskel` de cualquier animación.
   - **Import animated GIF**: selecciona el archivo `.gif` (Piskel importa todos los fotogramas y la velocidad al instante).
   - **Import from picture**: selecciona el `_sheet.png` (pon el Frame size que se indica abajo).

## Volver al juego:
`python herramientas/importar_piskel.py editado.piskel --manifiesto "04 - Piskel/trunksgt_0/origen.json" --heroe trunksgt --forma 0 --anim attack --aplicar`
Después: `python herramientas/montar_animaciones.py trunksgt` y revisión visual. Solo se aceptan sprites originales exportados.

## Animaciones disponibles:

| Animación | Fotogramas | Tamaño de celda | Archivo .piskel | GIF animado | Hoja Strip |
|---|---|---|---|---|---|
| **Idle** | 2 | 52x52 | [`trunksgt_Idle.piskel`](Idle/trunksgt_Idle.piskel) | [`trunksgt_Idle.gif`](Idle/trunksgt_Idle.gif) | [`trunksgt_Idle_sheet.png`](Idle/trunksgt_Idle_sheet.png) |
| **Walk** | 1 | 46x46 | [`trunksgt_Walk.piskel`](Walk/trunksgt_Walk.piskel) | [`trunksgt_Walk.gif`](Walk/trunksgt_Walk.gif) | [`trunksgt_Walk_sheet.png`](Walk/trunksgt_Walk_sheet.png) |
| **Attack** | 3 | 46x46 | [`trunksgt_Attack.piskel`](Attack/trunksgt_Attack.piskel) | [`trunksgt_Attack.gif`](Attack/trunksgt_Attack.gif) | [`trunksgt_Attack_sheet.png`](Attack/trunksgt_Attack_sheet.png) |
| **Kick** | 2 | 50x50 | [`trunksgt_Kick.piskel`](Kick/trunksgt_Kick.piskel) | [`trunksgt_Kick.gif`](Kick/trunksgt_Kick.gif) | [`trunksgt_Kick_sheet.png`](Kick/trunksgt_Kick_sheet.png) |
| **Cast** | 3 | 52x52 | [`trunksgt_Cast.piskel`](Cast/trunksgt_Cast.piskel) | [`trunksgt_Cast.gif`](Cast/trunksgt_Cast.gif) | [`trunksgt_Cast_sheet.png`](Cast/trunksgt_Cast_sheet.png) |
| **Pow** | 2 | 54x54 | [`trunksgt_Pow.piskel`](Pow/trunksgt_Pow.piskel) | [`trunksgt_Pow.gif`](Pow/trunksgt_Pow.gif) | [`trunksgt_Pow_sheet.png`](Pow/trunksgt_Pow_sheet.png) |
| **Hurt** | 2 | 46x46 | [`trunksgt_Hurt.piskel`](Hurt/trunksgt_Hurt.piskel) | [`trunksgt_Hurt.gif`](Hurt/trunksgt_Hurt.gif) | [`trunksgt_Hurt_sheet.png`](Hurt/trunksgt_Hurt_sheet.png) |
| **Faint** | 1 | 54x54 | [`trunksgt_Faint.piskel`](Faint/trunksgt_Faint.piskel) | [`trunksgt_Faint.gif`](Faint/trunksgt_Faint.gif) | [`trunksgt_Faint_sheet.png`](Faint/trunksgt_Faint_sheet.png) |
| **Attack2** | 2 | 46x46 | [`trunksgt_Attack2.piskel`](Attack2/trunksgt_Attack2.piskel) | [`trunksgt_Attack2.gif`](Attack2/trunksgt_Attack2.gif) | [`trunksgt_Attack2_sheet.png`](Attack2/trunksgt_Attack2_sheet.png) |
| **Kick2** | 3 | 46x46 | [`trunksgt_Kick2.piskel`](Kick2/trunksgt_Kick2.piskel) | [`trunksgt_Kick2.gif`](Kick2/trunksgt_Kick2.gif) | [`trunksgt_Kick2_sheet.png`](Kick2/trunksgt_Kick2_sheet.png) |