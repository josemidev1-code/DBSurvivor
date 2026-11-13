# Animaciones para Piskel — JIRENGRAY (Forma 0)

Esta carpeta contiene las animaciones listas para abrir y editar en **Piskel** (https://www.piskelapp.com/).

## Cómo abrir en Piskel:
1. Entra a **https://www.piskelapp.com/p/create/sprite** en tu navegador.
2. Haz clic en el icono de carpeta de la barra derecha (**Import**).
3. Elige cualquiera de estas opciones:
   - **Import .piskel file**: selecciona el archivo `.piskel` de cualquier animación.
   - **Import animated GIF**: selecciona el archivo `.gif` (Piskel importa todos los fotogramas y la velocidad al instante).
   - **Import from picture**: selecciona el `_sheet.png` (pon el Frame size que se indica abajo).

## Volver al juego:
`python herramientas/importar_piskel.py editado.piskel --manifiesto piskel_animaciones/jirengray_0/origen.json --heroe jirengray --forma 0 --anim attack --aplicar`
Después: `python herramientas/montar_animaciones.py jirengray` y revisión visual. Solo se aceptan sprites originales exportados.

## Animaciones disponibles:

| Animación | Fotogramas | Tamaño de celda | Archivo .piskel | GIF animado | Hoja Strip |
|---|---|---|---|---|---|
| **Idle** | 2 | 54x54 | [`jirengray_Idle.piskel`](Idle/jirengray_Idle.piskel) | [`jirengray_Idle.gif`](Idle/jirengray_Idle.gif) | [`jirengray_Idle_sheet.png`](Idle/jirengray_Idle_sheet.png) |
| **Walk** | 1 | 50x50 | [`jirengray_Walk.piskel`](Walk/jirengray_Walk.piskel) | [`jirengray_Walk.gif`](Walk/jirengray_Walk.gif) | [`jirengray_Walk_sheet.png`](Walk/jirengray_Walk_sheet.png) |
| **Attack** | 3 | 48x48 | [`jirengray_Attack.piskel`](Attack/jirengray_Attack.piskel) | [`jirengray_Attack.gif`](Attack/jirengray_Attack.gif) | [`jirengray_Attack_sheet.png`](Attack/jirengray_Attack_sheet.png) |
| **Kick** | 2 | 52x52 | [`jirengray_Kick.piskel`](Kick/jirengray_Kick.piskel) | [`jirengray_Kick.gif`](Kick/jirengray_Kick.gif) | [`jirengray_Kick_sheet.png`](Kick/jirengray_Kick_sheet.png) |
| **Cast** | 2 | 52x52 | [`jirengray_Cast.piskel`](Cast/jirengray_Cast.piskel) | [`jirengray_Cast.gif`](Cast/jirengray_Cast.gif) | [`jirengray_Cast_sheet.png`](Cast/jirengray_Cast_sheet.png) |
| **Pow** | 2 | 126x126 | [`jirengray_Pow.piskel`](Pow/jirengray_Pow.piskel) | [`jirengray_Pow.gif`](Pow/jirengray_Pow.gif) | [`jirengray_Pow_sheet.png`](Pow/jirengray_Pow_sheet.png) |
| **Hurt** | 2 | 52x52 | [`jirengray_Hurt.piskel`](Hurt/jirengray_Hurt.piskel) | [`jirengray_Hurt.gif`](Hurt/jirengray_Hurt.gif) | [`jirengray_Hurt_sheet.png`](Hurt/jirengray_Hurt_sheet.png) |
| **Faint** | 1 | 66x66 | [`jirengray_Faint.piskel`](Faint/jirengray_Faint.piskel) | [`jirengray_Faint.gif`](Faint/jirengray_Faint.gif) | [`jirengray_Faint_sheet.png`](Faint/jirengray_Faint_sheet.png) |
| **Attack2** | 2 | 52x52 | [`jirengray_Attack2.piskel`](Attack2/jirengray_Attack2.piskel) | [`jirengray_Attack2.gif`](Attack2/jirengray_Attack2.gif) | [`jirengray_Attack2_sheet.png`](Attack2/jirengray_Attack2_sheet.png) |
| **Attack3** | 2 | 56x56 | [`jirengray_Attack3.piskel`](Attack3/jirengray_Attack3.piskel) | [`jirengray_Attack3.gif`](Attack3/jirengray_Attack3.gif) | [`jirengray_Attack3_sheet.png`](Attack3/jirengray_Attack3_sheet.png) |
| **Kick2** | 2 | 70x70 | [`jirengray_Kick2.piskel`](Kick2/jirengray_Kick2.piskel) | [`jirengray_Kick2.gif`](Kick2/jirengray_Kick2.gif) | [`jirengray_Kick2_sheet.png`](Kick2/jirengray_Kick2_sheet.png) |
| **Up** | 1 | 54x54 | [`jirengray_Up.piskel`](Up/jirengray_Up.piskel) | [`jirengray_Up.gif`](Up/jirengray_Up.gif) | [`jirengray_Up_sheet.png`](Up/jirengray_Up_sheet.png) |