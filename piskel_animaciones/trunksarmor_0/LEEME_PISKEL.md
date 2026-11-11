# Animaciones para Piskel — TRUNKSARMOR (Forma 0)

Esta carpeta contiene las animaciones listas para abrir y editar en **Piskel** (https://www.piskelapp.com/).

## Cómo abrir en Piskel:
1. Entra a **https://www.piskelapp.com/p/create/sprite** en tu navegador.
2. Haz clic en el icono de carpeta de la barra derecha (**Import**).
3. Elige cualquiera de estas opciones:
   - **Import .piskel file**: selecciona el archivo `.piskel` de cualquier animación.
   - **Import animated GIF**: selecciona el archivo `.gif` (Piskel importa todos los fotogramas y la velocidad al instante).
   - **Import from picture**: selecciona el `_sheet.png` (pon el Frame size que se indica abajo).

## Volver al juego:
`python herramientas/importar_piskel.py editado.piskel --manifiesto piskel_animaciones/trunksarmor_0/origen.json --heroe trunksarmor --forma 0 --anim attack --aplicar`
Después: `python herramientas/montar_animaciones.py trunksarmor` y revisión visual. Solo se aceptan sprites originales exportados.

## Animaciones disponibles:

| Animación | Fotogramas | Tamaño de celda | Archivo .piskel | GIF animado | Hoja Strip |
|---|---|---|---|---|---|
| **Idle** | 2 | 52x52 | [`trunksarmor_Idle.piskel`](Idle/trunksarmor_Idle.piskel) | [`trunksarmor_Idle.gif`](Idle/trunksarmor_Idle.gif) | [`trunksarmor_Idle_sheet.png`](Idle/trunksarmor_Idle_sheet.png) |
| **Walk** | 1 | 48x48 | [`trunksarmor_Walk.piskel`](Walk/trunksarmor_Walk.piskel) | [`trunksarmor_Walk.gif`](Walk/trunksarmor_Walk.gif) | [`trunksarmor_Walk_sheet.png`](Walk/trunksarmor_Walk_sheet.png) |
| **Attack** | 2 | 46x46 | [`trunksarmor_Attack.piskel`](Attack/trunksarmor_Attack.piskel) | [`trunksarmor_Attack.gif`](Attack/trunksarmor_Attack.gif) | [`trunksarmor_Attack_sheet.png`](Attack/trunksarmor_Attack_sheet.png) |
| **Kick** | 2 | 52x52 | [`trunksarmor_Kick.piskel`](Kick/trunksarmor_Kick.piskel) | [`trunksarmor_Kick.gif`](Kick/trunksarmor_Kick.gif) | [`trunksarmor_Kick_sheet.png`](Kick/trunksarmor_Kick_sheet.png) |
| **Cast** | 2 | 46x46 | [`trunksarmor_Cast.piskel`](Cast/trunksarmor_Cast.piskel) | [`trunksarmor_Cast.gif`](Cast/trunksarmor_Cast.gif) | [`trunksarmor_Cast_sheet.png`](Cast/trunksarmor_Cast_sheet.png) |
| **Pow** | 2 | 102x102 | [`trunksarmor_Pow.piskel`](Pow/trunksarmor_Pow.piskel) | [`trunksarmor_Pow.gif`](Pow/trunksarmor_Pow.gif) | [`trunksarmor_Pow_sheet.png`](Pow/trunksarmor_Pow_sheet.png) |
| **Hurt** | 2 | 50x50 | [`trunksarmor_Hurt.piskel`](Hurt/trunksarmor_Hurt.piskel) | [`trunksarmor_Hurt.gif`](Hurt/trunksarmor_Hurt.gif) | [`trunksarmor_Hurt_sheet.png`](Hurt/trunksarmor_Hurt_sheet.png) |
| **Faint** | 1 | 56x56 | [`trunksarmor_Faint.piskel`](Faint/trunksarmor_Faint.piskel) | [`trunksarmor_Faint.gif`](Faint/trunksarmor_Faint.gif) | [`trunksarmor_Faint_sheet.png`](Faint/trunksarmor_Faint_sheet.png) |
| **Attack2** | 2 | 46x46 | [`trunksarmor_Attack2.piskel`](Attack2/trunksarmor_Attack2.piskel) | [`trunksarmor_Attack2.gif`](Attack2/trunksarmor_Attack2.gif) | [`trunksarmor_Attack2_sheet.png`](Attack2/trunksarmor_Attack2_sheet.png) |
| **Kick2** | 2 | 50x50 | [`trunksarmor_Kick2.piskel`](Kick2/trunksarmor_Kick2.piskel) | [`trunksarmor_Kick2.gif`](Kick2/trunksarmor_Kick2.gif) | [`trunksarmor_Kick2_sheet.png`](Kick2/trunksarmor_Kick2_sheet.png) |
| **Up** | 1 | 54x54 | [`trunksarmor_Up.piskel`](Up/trunksarmor_Up.piskel) | [`trunksarmor_Up.gif`](Up/trunksarmor_Up.gif) | [`trunksarmor_Up_sheet.png`](Up/trunksarmor_Up_sheet.png) |