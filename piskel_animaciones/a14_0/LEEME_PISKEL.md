# Animaciones para Piskel — A14 (Forma 0)

Esta carpeta contiene las animaciones listas para abrir y editar en **Piskel** (https://www.piskelapp.com/).

## Cómo abrir en Piskel:
1. Entra a **https://www.piskelapp.com/p/create/sprite** en tu navegador.
2. Haz clic en el icono de carpeta de la barra derecha (**Import**).
3. Elige cualquiera de estas opciones:
   - **Import .piskel file**: selecciona el archivo `.piskel` de cualquier animación.
   - **Import animated GIF**: selecciona el archivo `.gif` (Piskel importa todos los fotogramas y la velocidad al instante).
   - **Import from picture**: selecciona el `_sheet.png` (pon el Frame size que se indica abajo).

## Volver al juego:
`python herramientas/importar_piskel.py editado.piskel --manifiesto piskel_animaciones/a14_0/origen.json --heroe a14 --forma 0 --anim attack --aplicar`
Después: `python herramientas/montar_animaciones.py a14` y revisión visual. Solo se aceptan sprites originales exportados.

## Animaciones disponibles:

| Animación | Fotogramas | Tamaño de celda | Archivo .piskel | GIF animado | Hoja Strip |
|---|---|---|---|---|---|
| **Idle** | 2 | 52x52 | [`a14_Idle.piskel`](Idle/a14_Idle.piskel) | [`a14_Idle.gif`](Idle/a14_Idle.gif) | [`a14_Idle_sheet.png`](Idle/a14_Idle_sheet.png) |
| **Walk** | 1 | 40x40 | [`a14_Walk.piskel`](Walk/a14_Walk.piskel) | [`a14_Walk.gif`](Walk/a14_Walk.gif) | [`a14_Walk_sheet.png`](Walk/a14_Walk_sheet.png) |
| **Attack** | 3 | 46x46 | [`a14_Attack.piskel`](Attack/a14_Attack.piskel) | [`a14_Attack.gif`](Attack/a14_Attack.gif) | [`a14_Attack_sheet.png`](Attack/a14_Attack_sheet.png) |
| **Kick** | 2 | 52x52 | [`a14_Kick.piskel`](Kick/a14_Kick.piskel) | [`a14_Kick.gif`](Kick/a14_Kick.gif) | [`a14_Kick_sheet.png`](Kick/a14_Kick_sheet.png) |
| **Cast** | 2 | 52x52 | [`a14_Cast.piskel`](Cast/a14_Cast.piskel) | [`a14_Cast.gif`](Cast/a14_Cast.gif) | [`a14_Cast_sheet.png`](Cast/a14_Cast_sheet.png) |
| **Pow** | 2 | 48x48 | [`a14_Pow.piskel`](Pow/a14_Pow.piskel) | [`a14_Pow.gif`](Pow/a14_Pow.gif) | [`a14_Pow_sheet.png`](Pow/a14_Pow_sheet.png) |
| **Hurt** | 2 | 44x44 | [`a14_Hurt.piskel`](Hurt/a14_Hurt.piskel) | [`a14_Hurt.gif`](Hurt/a14_Hurt.gif) | [`a14_Hurt_sheet.png`](Hurt/a14_Hurt_sheet.png) |
| **Attack2** | 2 | 50x50 | [`a14_Attack2.piskel`](Attack2/a14_Attack2.piskel) | [`a14_Attack2.gif`](Attack2/a14_Attack2.gif) | [`a14_Attack2_sheet.png`](Attack2/a14_Attack2_sheet.png) |
| **Attack3** | 2 | 46x46 | [`a14_Attack3.piskel`](Attack3/a14_Attack3.piskel) | [`a14_Attack3.gif`](Attack3/a14_Attack3.gif) | [`a14_Attack3_sheet.png`](Attack3/a14_Attack3_sheet.png) |
| **Kick2** | 2 | 46x46 | [`a14_Kick2.piskel`](Kick2/a14_Kick2.piskel) | [`a14_Kick2.gif`](Kick2/a14_Kick2.gif) | [`a14_Kick2_sheet.png`](Kick2/a14_Kick2_sheet.png) |
| **Up** | 1 | 48x48 | [`a14_Up.piskel`](Up/a14_Up.piskel) | [`a14_Up.gif`](Up/a14_Up.gif) | [`a14_Up_sheet.png`](Up/a14_Up_sheet.png) |