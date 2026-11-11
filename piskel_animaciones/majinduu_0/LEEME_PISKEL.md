# Animaciones para Piskel — MAJINDUU (Forma 0)

Esta carpeta contiene las animaciones listas para abrir y editar en **Piskel** (https://www.piskelapp.com/).

## Cómo abrir en Piskel:
1. Entra a **https://www.piskelapp.com/p/create/sprite** en tu navegador.
2. Haz clic en el icono de carpeta de la barra derecha (**Import**).
3. Elige cualquiera de estas opciones:
   - **Import .piskel file**: selecciona el archivo `.piskel` de cualquier animación.
   - **Import animated GIF**: selecciona el archivo `.gif` (Piskel importa todos los fotogramas y la velocidad al instante).
   - **Import from picture**: selecciona el `_sheet.png` (pon el Frame size que se indica abajo).

## Volver al juego:
`python herramientas/importar_piskel.py editado.piskel --manifiesto piskel_animaciones/majinduu_0/origen.json --heroe majinduu --forma 0 --anim attack --aplicar`
Después: `python herramientas/montar_animaciones.py majinduu` y revisión visual. Solo se aceptan sprites originales exportados.

## Animaciones disponibles:

| Animación | Fotogramas | Tamaño de celda | Archivo .piskel | GIF animado | Hoja Strip |
|---|---|---|---|---|---|
| **Idle** | 2 | 52x52 | [`majinduu_Idle.piskel`](Idle/majinduu_Idle.piskel) | [`majinduu_Idle.gif`](Idle/majinduu_Idle.gif) | [`majinduu_Idle_sheet.png`](Idle/majinduu_Idle_sheet.png) |
| **Walk** | 1 | 48x48 | [`majinduu_Walk.piskel`](Walk/majinduu_Walk.piskel) | [`majinduu_Walk.gif`](Walk/majinduu_Walk.gif) | [`majinduu_Walk_sheet.png`](Walk/majinduu_Walk_sheet.png) |
| **Attack** | 3 | 52x52 | [`majinduu_Attack.piskel`](Attack/majinduu_Attack.piskel) | [`majinduu_Attack.gif`](Attack/majinduu_Attack.gif) | [`majinduu_Attack_sheet.png`](Attack/majinduu_Attack_sheet.png) |
| **Kick** | 2 | 54x54 | [`majinduu_Kick.piskel`](Kick/majinduu_Kick.piskel) | [`majinduu_Kick.gif`](Kick/majinduu_Kick.gif) | [`majinduu_Kick_sheet.png`](Kick/majinduu_Kick_sheet.png) |
| **Cast** | 2 | 52x52 | [`majinduu_Cast.piskel`](Cast/majinduu_Cast.piskel) | [`majinduu_Cast.gif`](Cast/majinduu_Cast.gif) | [`majinduu_Cast_sheet.png`](Cast/majinduu_Cast_sheet.png) |
| **Pow** | 2 | 78x78 | [`majinduu_Pow.piskel`](Pow/majinduu_Pow.piskel) | [`majinduu_Pow.gif`](Pow/majinduu_Pow.gif) | [`majinduu_Pow_sheet.png`](Pow/majinduu_Pow_sheet.png) |
| **Hurt** | 2 | 46x46 | [`majinduu_Hurt.piskel`](Hurt/majinduu_Hurt.piskel) | [`majinduu_Hurt.gif`](Hurt/majinduu_Hurt.gif) | [`majinduu_Hurt_sheet.png`](Hurt/majinduu_Hurt_sheet.png) |
| **Faint** | 1 | 48x48 | [`majinduu_Faint.piskel`](Faint/majinduu_Faint.piskel) | [`majinduu_Faint.gif`](Faint/majinduu_Faint.gif) | [`majinduu_Faint_sheet.png`](Faint/majinduu_Faint_sheet.png) |
| **Attack2** | 3 | 52x52 | [`majinduu_Attack2.piskel`](Attack2/majinduu_Attack2.piskel) | [`majinduu_Attack2.gif`](Attack2/majinduu_Attack2.gif) | [`majinduu_Attack2_sheet.png`](Attack2/majinduu_Attack2_sheet.png) |
| **Attack3** | 2 | 54x54 | [`majinduu_Attack3.piskel`](Attack3/majinduu_Attack3.piskel) | [`majinduu_Attack3.gif`](Attack3/majinduu_Attack3.gif) | [`majinduu_Attack3_sheet.png`](Attack3/majinduu_Attack3_sheet.png) |
| **Kick2** | 2 | 52x52 | [`majinduu_Kick2.piskel`](Kick2/majinduu_Kick2.piskel) | [`majinduu_Kick2.gif`](Kick2/majinduu_Kick2.gif) | [`majinduu_Kick2_sheet.png`](Kick2/majinduu_Kick2_sheet.png) |
| **Up** | 1 | 56x56 | [`majinduu_Up.piskel`](Up/majinduu_Up.piskel) | [`majinduu_Up.gif`](Up/majinduu_Up.gif) | [`majinduu_Up_sheet.png`](Up/majinduu_Up_sheet.png) |