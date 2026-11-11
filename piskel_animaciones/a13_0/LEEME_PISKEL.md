# Animaciones para Piskel — A13 (Forma 0)

Esta carpeta contiene las animaciones listas para abrir y editar en **Piskel** (https://www.piskelapp.com/).

## Cómo abrir en Piskel:
1. Entra a **https://www.piskelapp.com/p/create/sprite** en tu navegador.
2. Haz clic en el icono de carpeta de la barra derecha (**Import**).
3. Elige cualquiera de estas opciones:
   - **Import .piskel file**: selecciona el archivo `.piskel` de cualquier animación.
   - **Import animated GIF**: selecciona el archivo `.gif` (Piskel importa todos los fotogramas y la velocidad al instante).
   - **Import from picture**: selecciona el `_sheet.png` (pon el Frame size que se indica abajo).

## Volver al juego:
`python herramientas/importar_piskel.py editado.piskel --manifiesto piskel_animaciones/a13_0/origen.json --heroe a13 --forma 0 --anim attack --aplicar`
Después: `python herramientas/montar_animaciones.py a13` y revisión visual. Solo se aceptan sprites originales exportados.

## Animaciones disponibles:

| Animación | Fotogramas | Tamaño de celda | Archivo .piskel | GIF animado | Hoja Strip |
|---|---|---|---|---|---|
| **Idle** | 2 | 52x52 | [`a13_Idle.piskel`](Idle/a13_Idle.piskel) | [`a13_Idle.gif`](Idle/a13_Idle.gif) | [`a13_Idle_sheet.png`](Idle/a13_Idle_sheet.png) |
| **Walk** | 1 | 50x50 | [`a13_Walk.piskel`](Walk/a13_Walk.piskel) | [`a13_Walk.gif`](Walk/a13_Walk.gif) | [`a13_Walk_sheet.png`](Walk/a13_Walk_sheet.png) |
| **Attack** | 3 | 58x58 | [`a13_Attack.piskel`](Attack/a13_Attack.piskel) | [`a13_Attack.gif`](Attack/a13_Attack.gif) | [`a13_Attack_sheet.png`](Attack/a13_Attack_sheet.png) |
| **Kick** | 2 | 52x52 | [`a13_Kick.piskel`](Kick/a13_Kick.piskel) | [`a13_Kick.gif`](Kick/a13_Kick.gif) | [`a13_Kick_sheet.png`](Kick/a13_Kick_sheet.png) |
| **Cast** | 2 | 54x54 | [`a13_Cast.piskel`](Cast/a13_Cast.piskel) | [`a13_Cast.gif`](Cast/a13_Cast.gif) | [`a13_Cast_sheet.png`](Cast/a13_Cast_sheet.png) |
| **Pow** | 2 | 100x100 | [`a13_Pow.piskel`](Pow/a13_Pow.piskel) | [`a13_Pow.gif`](Pow/a13_Pow.gif) | [`a13_Pow_sheet.png`](Pow/a13_Pow_sheet.png) |
| **Hurt** | 2 | 48x48 | [`a13_Hurt.piskel`](Hurt/a13_Hurt.piskel) | [`a13_Hurt.gif`](Hurt/a13_Hurt.gif) | [`a13_Hurt_sheet.png`](Hurt/a13_Hurt_sheet.png) |
| **Attack2** | 2 | 46x46 | [`a13_Attack2.piskel`](Attack2/a13_Attack2.piskel) | [`a13_Attack2.gif`](Attack2/a13_Attack2.gif) | [`a13_Attack2_sheet.png`](Attack2/a13_Attack2_sheet.png) |
| **Attack3** | 2 | 58x58 | [`a13_Attack3.piskel`](Attack3/a13_Attack3.piskel) | [`a13_Attack3.gif`](Attack3/a13_Attack3.gif) | [`a13_Attack3_sheet.png`](Attack3/a13_Attack3_sheet.png) |
| **Kick2** | 2 | 42x42 | [`a13_Kick2.piskel`](Kick2/a13_Kick2.piskel) | [`a13_Kick2.gif`](Kick2/a13_Kick2.gif) | [`a13_Kick2_sheet.png`](Kick2/a13_Kick2_sheet.png) |
| **Beam** | 2 | 56x56 | [`a13_Beam.piskel`](Beam/a13_Beam.piskel) | [`a13_Beam.gif`](Beam/a13_Beam.gif) | [`a13_Beam_sheet.png`](Beam/a13_Beam_sheet.png) |