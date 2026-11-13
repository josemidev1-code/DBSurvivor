# Animaciones para Piskel — TAOPAIPAI (Forma 0)

Esta carpeta contiene las animaciones listas para abrir y editar en **Piskel** (https://www.piskelapp.com/).

## Cómo abrir en Piskel:
1. Entra a **https://www.piskelapp.com/p/create/sprite** en tu navegador.
2. Haz clic en el icono de carpeta de la barra derecha (**Import**).
3. Elige cualquiera de estas opciones:
   - **Import .piskel file**: selecciona el archivo `.piskel` de cualquier animación.
   - **Import animated GIF**: selecciona el archivo `.gif` (Piskel importa todos los fotogramas y la velocidad al instante).
   - **Import from picture**: selecciona el `_sheet.png` (pon el Frame size que se indica abajo).

## Volver al juego:
`python herramientas/importar_piskel.py editado.piskel --manifiesto piskel_animaciones/taopaipai_0/origen.json --heroe taopaipai --forma 0 --anim attack --aplicar`
Después: `python herramientas/montar_animaciones.py taopaipai` y revisión visual. Solo se aceptan sprites originales exportados.

## Animaciones disponibles:

| Animación | Fotogramas | Tamaño de celda | Archivo .piskel | GIF animado | Hoja Strip |
|---|---|---|---|---|---|
| **Idle** | 2 | 52x52 | [`taopaipai_Idle.piskel`](Idle/taopaipai_Idle.piskel) | [`taopaipai_Idle.gif`](Idle/taopaipai_Idle.gif) | [`taopaipai_Idle_sheet.png`](Idle/taopaipai_Idle_sheet.png) |
| **Walk** | 1 | 42x42 | [`taopaipai_Walk.piskel`](Walk/taopaipai_Walk.piskel) | [`taopaipai_Walk.gif`](Walk/taopaipai_Walk.gif) | [`taopaipai_Walk_sheet.png`](Walk/taopaipai_Walk_sheet.png) |
| **Attack** | 3 | 50x50 | [`taopaipai_Attack.piskel`](Attack/taopaipai_Attack.piskel) | [`taopaipai_Attack.gif`](Attack/taopaipai_Attack.gif) | [`taopaipai_Attack_sheet.png`](Attack/taopaipai_Attack_sheet.png) |
| **Kick** | 2 | 54x54 | [`taopaipai_Kick.piskel`](Kick/taopaipai_Kick.piskel) | [`taopaipai_Kick.gif`](Kick/taopaipai_Kick.gif) | [`taopaipai_Kick_sheet.png`](Kick/taopaipai_Kick_sheet.png) |
| **Cast** | 2 | 50x50 | [`taopaipai_Cast.piskel`](Cast/taopaipai_Cast.piskel) | [`taopaipai_Cast.gif`](Cast/taopaipai_Cast.gif) | [`taopaipai_Cast_sheet.png`](Cast/taopaipai_Cast_sheet.png) |
| **Pow** | 2 | 46x46 | [`taopaipai_Pow.piskel`](Pow/taopaipai_Pow.piskel) | [`taopaipai_Pow.gif`](Pow/taopaipai_Pow.gif) | [`taopaipai_Pow_sheet.png`](Pow/taopaipai_Pow_sheet.png) |
| **Hurt** | 2 | 50x50 | [`taopaipai_Hurt.piskel`](Hurt/taopaipai_Hurt.piskel) | [`taopaipai_Hurt.gif`](Hurt/taopaipai_Hurt.gif) | [`taopaipai_Hurt_sheet.png`](Hurt/taopaipai_Hurt_sheet.png) |
| **Attack2** | 2 | 48x48 | [`taopaipai_Attack2.piskel`](Attack2/taopaipai_Attack2.piskel) | [`taopaipai_Attack2.gif`](Attack2/taopaipai_Attack2.gif) | [`taopaipai_Attack2_sheet.png`](Attack2/taopaipai_Attack2_sheet.png) |
| **Kick2** | 2 | 50x50 | [`taopaipai_Kick2.piskel`](Kick2/taopaipai_Kick2.piskel) | [`taopaipai_Kick2.gif`](Kick2/taopaipai_Kick2.gif) | [`taopaipai_Kick2_sheet.png`](Kick2/taopaipai_Kick2_sheet.png) |