# Animaciones para Piskel — KYABE (Forma 0)

Esta carpeta contiene las animaciones listas para abrir y editar en **Piskel** (https://www.piskelapp.com/).

## Cómo abrir en Piskel:
1. Entra a **https://www.piskelapp.com/p/create/sprite** en tu navegador.
2. Haz clic en el icono de carpeta de la barra derecha (**Import**).
3. Elige cualquiera de estas opciones:
   - **Import .piskel file**: selecciona el archivo `.piskel` de cualquier animación.
   - **Import animated GIF**: selecciona el archivo `.gif` (Piskel importa todos los fotogramas y la velocidad al instante).
   - **Import from picture**: selecciona el `_sheet.png` (pon el Frame size que se indica abajo).

## Volver al juego:
`python herramientas/importar_piskel.py editado.piskel --manifiesto piskel_animaciones/kyabe_0/origen.json --heroe kyabe --forma 0 --anim attack --aplicar`
Después: `python herramientas/montar_animaciones.py kyabe` y revisión visual. Solo se aceptan sprites originales exportados.

## Animaciones disponibles:

| Animación | Fotogramas | Tamaño de celda | Archivo .piskel | GIF animado | Hoja Strip |
|---|---|---|---|---|---|
| **Idle** | 2 | 52x52 | [`kyabe_Idle.piskel`](Idle/kyabe_Idle.piskel) | [`kyabe_Idle.gif`](Idle/kyabe_Idle.gif) | [`kyabe_Idle_sheet.png`](Idle/kyabe_Idle_sheet.png) |
| **Walk** | 1 | 50x50 | [`kyabe_Walk.piskel`](Walk/kyabe_Walk.piskel) | [`kyabe_Walk.gif`](Walk/kyabe_Walk.gif) | [`kyabe_Walk_sheet.png`](Walk/kyabe_Walk_sheet.png) |
| **Attack** | 3 | 76x76 | [`kyabe_Attack.piskel`](Attack/kyabe_Attack.piskel) | [`kyabe_Attack.gif`](Attack/kyabe_Attack.gif) | [`kyabe_Attack_sheet.png`](Attack/kyabe_Attack_sheet.png) |
| **Kick** | 2 | 56x56 | [`kyabe_Kick.piskel`](Kick/kyabe_Kick.piskel) | [`kyabe_Kick.gif`](Kick/kyabe_Kick.gif) | [`kyabe_Kick_sheet.png`](Kick/kyabe_Kick_sheet.png) |
| **Cast** | 2 | 56x56 | [`kyabe_Cast.piskel`](Cast/kyabe_Cast.piskel) | [`kyabe_Cast.gif`](Cast/kyabe_Cast.gif) | [`kyabe_Cast_sheet.png`](Cast/kyabe_Cast_sheet.png) |
| **Pow** | 2 | 106x106 | [`kyabe_Pow.piskel`](Pow/kyabe_Pow.piskel) | [`kyabe_Pow.gif`](Pow/kyabe_Pow.gif) | [`kyabe_Pow_sheet.png`](Pow/kyabe_Pow_sheet.png) |
| **Hurt** | 2 | 64x64 | [`kyabe_Hurt.piskel`](Hurt/kyabe_Hurt.piskel) | [`kyabe_Hurt.gif`](Hurt/kyabe_Hurt.gif) | [`kyabe_Hurt_sheet.png`](Hurt/kyabe_Hurt_sheet.png) |
| **Faint** | 1 | 62x62 | [`kyabe_Faint.piskel`](Faint/kyabe_Faint.piskel) | [`kyabe_Faint.gif`](Faint/kyabe_Faint.gif) | [`kyabe_Faint_sheet.png`](Faint/kyabe_Faint_sheet.png) |
| **Attack2** | 3 | 56x56 | [`kyabe_Attack2.piskel`](Attack2/kyabe_Attack2.piskel) | [`kyabe_Attack2.gif`](Attack2/kyabe_Attack2.gif) | [`kyabe_Attack2_sheet.png`](Attack2/kyabe_Attack2_sheet.png) |
| **Attack3** | 2 | 62x62 | [`kyabe_Attack3.piskel`](Attack3/kyabe_Attack3.piskel) | [`kyabe_Attack3.gif`](Attack3/kyabe_Attack3.gif) | [`kyabe_Attack3_sheet.png`](Attack3/kyabe_Attack3_sheet.png) |
| **Kick2** | 3 | 54x54 | [`kyabe_Kick2.piskel`](Kick2/kyabe_Kick2.piskel) | [`kyabe_Kick2.gif`](Kick2/kyabe_Kick2.gif) | [`kyabe_Kick2_sheet.png`](Kick2/kyabe_Kick2_sheet.png) |