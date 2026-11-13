# Animaciones para Piskel — METALCOOLER (Forma 0)

Esta carpeta contiene las animaciones listas para abrir y editar en **Piskel** (https://www.piskelapp.com/).

## Cómo abrir en Piskel:
1. Entra a **https://www.piskelapp.com/p/create/sprite** en tu navegador.
2. Haz clic en el icono de carpeta de la barra derecha (**Import**).
3. Elige cualquiera de estas opciones:
   - **Import .piskel file**: selecciona el archivo `.piskel` de cualquier animación.
   - **Import animated GIF**: selecciona el archivo `.gif` (Piskel importa todos los fotogramas y la velocidad al instante).
   - **Import from picture**: selecciona el `_sheet.png` (pon el Frame size que se indica abajo).

## Volver al juego:
`python herramientas/importar_piskel.py editado.piskel --manifiesto piskel_animaciones/metalcooler_0/origen.json --heroe metalcooler --forma 0 --anim attack --aplicar`
Después: `python herramientas/montar_animaciones.py metalcooler` y revisión visual. Solo se aceptan sprites originales exportados.

## Animaciones disponibles:

| Animación | Fotogramas | Tamaño de celda | Archivo .piskel | GIF animado | Hoja Strip |
|---|---|---|---|---|---|
| **Idle** | 2 | 52x52 | [`metalcooler_Idle.piskel`](Idle/metalcooler_Idle.piskel) | [`metalcooler_Idle.gif`](Idle/metalcooler_Idle.gif) | [`metalcooler_Idle_sheet.png`](Idle/metalcooler_Idle_sheet.png) |
| **Walk** | 1 | 44x44 | [`metalcooler_Walk.piskel`](Walk/metalcooler_Walk.piskel) | [`metalcooler_Walk.gif`](Walk/metalcooler_Walk.gif) | [`metalcooler_Walk_sheet.png`](Walk/metalcooler_Walk_sheet.png) |
| **Attack** | 3 | 58x58 | [`metalcooler_Attack.piskel`](Attack/metalcooler_Attack.piskel) | [`metalcooler_Attack.gif`](Attack/metalcooler_Attack.gif) | [`metalcooler_Attack_sheet.png`](Attack/metalcooler_Attack_sheet.png) |
| **Kick** | 2 | 50x50 | [`metalcooler_Kick.piskel`](Kick/metalcooler_Kick.piskel) | [`metalcooler_Kick.gif`](Kick/metalcooler_Kick.gif) | [`metalcooler_Kick_sheet.png`](Kick/metalcooler_Kick_sheet.png) |
| **Cast** | 2 | 52x52 | [`metalcooler_Cast.piskel`](Cast/metalcooler_Cast.piskel) | [`metalcooler_Cast.gif`](Cast/metalcooler_Cast.gif) | [`metalcooler_Cast_sheet.png`](Cast/metalcooler_Cast_sheet.png) |
| **Pow** | 2 | 54x54 | [`metalcooler_Pow.piskel`](Pow/metalcooler_Pow.piskel) | [`metalcooler_Pow.gif`](Pow/metalcooler_Pow.gif) | [`metalcooler_Pow_sheet.png`](Pow/metalcooler_Pow_sheet.png) |
| **Hurt** | 2 | 50x50 | [`metalcooler_Hurt.piskel`](Hurt/metalcooler_Hurt.piskel) | [`metalcooler_Hurt.gif`](Hurt/metalcooler_Hurt.gif) | [`metalcooler_Hurt_sheet.png`](Hurt/metalcooler_Hurt_sheet.png) |
| **Faint** | 1 | 62x62 | [`metalcooler_Faint.piskel`](Faint/metalcooler_Faint.piskel) | [`metalcooler_Faint.gif`](Faint/metalcooler_Faint.gif) | [`metalcooler_Faint_sheet.png`](Faint/metalcooler_Faint_sheet.png) |
| **Attack2** | 2 | 52x52 | [`metalcooler_Attack2.piskel`](Attack2/metalcooler_Attack2.piskel) | [`metalcooler_Attack2.gif`](Attack2/metalcooler_Attack2.gif) | [`metalcooler_Attack2_sheet.png`](Attack2/metalcooler_Attack2_sheet.png) |
| **Beam** | 2 | 52x52 | [`metalcooler_Beam.piskel`](Beam/metalcooler_Beam.piskel) | [`metalcooler_Beam.gif`](Beam/metalcooler_Beam.gif) | [`metalcooler_Beam_sheet.png`](Beam/metalcooler_Beam_sheet.png) |