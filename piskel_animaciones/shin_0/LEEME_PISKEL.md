# Animaciones para Piskel — SHIN (Forma 0)

Esta carpeta contiene las animaciones listas para abrir y editar en **Piskel** (https://www.piskelapp.com/).

## Cómo abrir en Piskel:
1. Entra a **https://www.piskelapp.com/p/create/sprite** en tu navegador.
2. Haz clic en el icono de carpeta de la barra derecha (**Import**).
3. Elige cualquiera de estas opciones:
   - **Import .piskel file**: selecciona el archivo `.piskel` de cualquier animación.
   - **Import animated GIF**: selecciona el archivo `.gif` (Piskel importa todos los fotogramas y la velocidad al instante).
   - **Import from picture**: selecciona el `_sheet.png` (pon el Frame size que se indica abajo).

## Volver al juego:
`python herramientas/importar_piskel.py editado.piskel --manifiesto piskel_animaciones/shin_0/origen.json --heroe shin --forma 0 --anim attack --aplicar`
Después: `python herramientas/montar_animaciones.py shin` y revisión visual. Solo se aceptan sprites originales exportados.

## Animaciones disponibles:

| Animación | Fotogramas | Tamaño de celda | Archivo .piskel | GIF animado | Hoja Strip |
|---|---|---|---|---|---|
| **Idle** | 2 | 52x52 | [`shin_Idle.piskel`](Idle/shin_Idle.piskel) | [`shin_Idle.gif`](Idle/shin_Idle.gif) | [`shin_Idle_sheet.png`](Idle/shin_Idle_sheet.png) |
| **Walk** | 1 | 44x44 | [`shin_Walk.piskel`](Walk/shin_Walk.piskel) | [`shin_Walk.gif`](Walk/shin_Walk.gif) | [`shin_Walk_sheet.png`](Walk/shin_Walk_sheet.png) |
| **Attack** | 3 | 52x52 | [`shin_Attack.piskel`](Attack/shin_Attack.piskel) | [`shin_Attack.gif`](Attack/shin_Attack.gif) | [`shin_Attack_sheet.png`](Attack/shin_Attack_sheet.png) |
| **Kick** | 2 | 62x62 | [`shin_Kick.piskel`](Kick/shin_Kick.piskel) | [`shin_Kick.gif`](Kick/shin_Kick.gif) | [`shin_Kick_sheet.png`](Kick/shin_Kick_sheet.png) |
| **Cast** | 2 | 58x58 | [`shin_Cast.piskel`](Cast/shin_Cast.piskel) | [`shin_Cast.gif`](Cast/shin_Cast.gif) | [`shin_Cast_sheet.png`](Cast/shin_Cast_sheet.png) |
| **Pow** | 2 | 50x50 | [`shin_Pow.piskel`](Pow/shin_Pow.piskel) | [`shin_Pow.gif`](Pow/shin_Pow.gif) | [`shin_Pow_sheet.png`](Pow/shin_Pow_sheet.png) |
| **Hurt** | 2 | 50x50 | [`shin_Hurt.piskel`](Hurt/shin_Hurt.piskel) | [`shin_Hurt.gif`](Hurt/shin_Hurt.gif) | [`shin_Hurt_sheet.png`](Hurt/shin_Hurt_sheet.png) |
| **Faint** | 1 | 56x56 | [`shin_Faint.piskel`](Faint/shin_Faint.piskel) | [`shin_Faint.gif`](Faint/shin_Faint.gif) | [`shin_Faint_sheet.png`](Faint/shin_Faint_sheet.png) |
| **Beam** | 2 | 54x54 | [`shin_Beam.piskel`](Beam/shin_Beam.piskel) | [`shin_Beam.gif`](Beam/shin_Beam.gif) | [`shin_Beam_sheet.png`](Beam/shin_Beam_sheet.png) |