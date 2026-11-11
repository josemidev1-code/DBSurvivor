# Animaciones para Piskel — DYSPO (Forma 0)

Esta carpeta contiene las animaciones listas para abrir y editar en **Piskel** (https://www.piskelapp.com/).

## Cómo abrir en Piskel:
1. Entra a **https://www.piskelapp.com/p/create/sprite** en tu navegador.
2. Haz clic en el icono de carpeta de la barra derecha (**Import**).
3. Elige cualquiera de estas opciones:
   - **Import .piskel file**: selecciona el archivo `.piskel` de cualquier animación.
   - **Import animated GIF**: selecciona el archivo `.gif` (Piskel importa todos los fotogramas y la velocidad al instante).
   - **Import from picture**: selecciona el `_sheet.png` (pon el Frame size que se indica abajo).

## Volver al juego:
`python herramientas/importar_piskel.py editado.piskel --manifiesto piskel_animaciones/dyspo_0/origen.json --heroe dyspo --forma 0 --anim attack --aplicar`
Después: `python herramientas/montar_animaciones.py dyspo` y revisión visual. Solo se aceptan sprites originales exportados.

## Animaciones disponibles:

| Animación | Fotogramas | Tamaño de celda | Archivo .piskel | GIF animado | Hoja Strip |
|---|---|---|---|---|---|
| **Idle** | 3 | 54x54 | [`dyspo_Idle.piskel`](Idle/dyspo_Idle.piskel) | [`dyspo_Idle.gif`](Idle/dyspo_Idle.gif) | [`dyspo_Idle_sheet.png`](Idle/dyspo_Idle_sheet.png) |
| **Walk** | 1 | 54x54 | [`dyspo_Walk.piskel`](Walk/dyspo_Walk.piskel) | [`dyspo_Walk.gif`](Walk/dyspo_Walk.gif) | [`dyspo_Walk_sheet.png`](Walk/dyspo_Walk_sheet.png) |
| **Attack** | 3 | 52x52 | [`dyspo_Attack.piskel`](Attack/dyspo_Attack.piskel) | [`dyspo_Attack.gif`](Attack/dyspo_Attack.gif) | [`dyspo_Attack_sheet.png`](Attack/dyspo_Attack_sheet.png) |
| **Kick** | 2 | 50x50 | [`dyspo_Kick.piskel`](Kick/dyspo_Kick.piskel) | [`dyspo_Kick.gif`](Kick/dyspo_Kick.gif) | [`dyspo_Kick_sheet.png`](Kick/dyspo_Kick_sheet.png) |
| **Cast** | 3 | 50x50 | [`dyspo_Cast.piskel`](Cast/dyspo_Cast.piskel) | [`dyspo_Cast.gif`](Cast/dyspo_Cast.gif) | [`dyspo_Cast_sheet.png`](Cast/dyspo_Cast_sheet.png) |
| **Pow** | 3 | 80x80 | [`dyspo_Pow.piskel`](Pow/dyspo_Pow.piskel) | [`dyspo_Pow.gif`](Pow/dyspo_Pow.gif) | [`dyspo_Pow_sheet.png`](Pow/dyspo_Pow_sheet.png) |
| **Hurt** | 2 | 50x50 | [`dyspo_Hurt.piskel`](Hurt/dyspo_Hurt.piskel) | [`dyspo_Hurt.gif`](Hurt/dyspo_Hurt.gif) | [`dyspo_Hurt_sheet.png`](Hurt/dyspo_Hurt_sheet.png) |
| **Faint** | 1 | 58x58 | [`dyspo_Faint.piskel`](Faint/dyspo_Faint.piskel) | [`dyspo_Faint.gif`](Faint/dyspo_Faint.gif) | [`dyspo_Faint_sheet.png`](Faint/dyspo_Faint_sheet.png) |
| **Attack2** | 2 | 50x50 | [`dyspo_Attack2.piskel`](Attack2/dyspo_Attack2.piskel) | [`dyspo_Attack2.gif`](Attack2/dyspo_Attack2.gif) | [`dyspo_Attack2_sheet.png`](Attack2/dyspo_Attack2_sheet.png) |
| **Attack3** | 2 | 50x50 | [`dyspo_Attack3.piskel`](Attack3/dyspo_Attack3.piskel) | [`dyspo_Attack3.gif`](Attack3/dyspo_Attack3.gif) | [`dyspo_Attack3_sheet.png`](Attack3/dyspo_Attack3_sheet.png) |
| **Kick2** | 2 | 50x50 | [`dyspo_Kick2.piskel`](Kick2/dyspo_Kick2.piskel) | [`dyspo_Kick2.gif`](Kick2/dyspo_Kick2.gif) | [`dyspo_Kick2_sheet.png`](Kick2/dyspo_Kick2_sheet.png) |
| **Up** | 1 | 56x56 | [`dyspo_Up.piskel`](Up/dyspo_Up.piskel) | [`dyspo_Up.gif`](Up/dyspo_Up.gif) | [`dyspo_Up_sheet.png`](Up/dyspo_Up_sheet.png) |