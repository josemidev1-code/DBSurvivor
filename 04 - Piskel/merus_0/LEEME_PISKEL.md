# Animaciones para Piskel — MERUS (Forma 0)

Esta carpeta contiene las animaciones listas para abrir y editar en **Piskel** (https://www.piskelapp.com/).

## Cómo abrir en Piskel:
1. Entra a **https://www.piskelapp.com/p/create/sprite** en tu navegador.
2. Haz clic en el icono de carpeta de la barra derecha (**Import**).
3. Elige cualquiera de estas opciones:
   - **Import .piskel file**: selecciona el archivo `.piskel` de cualquier animación.
   - **Import animated GIF**: selecciona el archivo `.gif` (Piskel importa todos los fotogramas y la velocidad al instante).
   - **Import from picture**: selecciona el `_sheet.png` (pon el Frame size que se indica abajo).

## Volver al juego:
`python herramientas/importar_piskel.py editado.piskel --manifiesto "04 - Piskel/merus_0/origen.json" --heroe merus --forma 0 --anim attack --aplicar`
Después: `python herramientas/montar_animaciones.py merus` y revisión visual. Solo se aceptan sprites originales exportados.

## Animaciones disponibles:

| Animación | Fotogramas | Tamaño de celda | Archivo .piskel | GIF animado | Hoja Strip |
|---|---|---|---|---|---|
| **Idle** | 2 | 54x54 | [`merus_Idle.piskel`](Idle/merus_Idle.piskel) | [`merus_Idle.gif`](Idle/merus_Idle.gif) | [`merus_Idle_sheet.png`](Idle/merus_Idle_sheet.png) |
| **Walk** | 1 | 72x72 | [`merus_Walk.piskel`](Walk/merus_Walk.piskel) | [`merus_Walk.gif`](Walk/merus_Walk.gif) | [`merus_Walk_sheet.png`](Walk/merus_Walk_sheet.png) |
| **Attack** | 3 | 84x84 | [`merus_Attack.piskel`](Attack/merus_Attack.piskel) | [`merus_Attack.gif`](Attack/merus_Attack.gif) | [`merus_Attack_sheet.png`](Attack/merus_Attack_sheet.png) |
| **Kick** | 2 | 72x72 | [`merus_Kick.piskel`](Kick/merus_Kick.piskel) | [`merus_Kick.gif`](Kick/merus_Kick.gif) | [`merus_Kick_sheet.png`](Kick/merus_Kick_sheet.png) |
| **Cast** | 2 | 54x54 | [`merus_Cast.piskel`](Cast/merus_Cast.piskel) | [`merus_Cast.gif`](Cast/merus_Cast.gif) | [`merus_Cast_sheet.png`](Cast/merus_Cast_sheet.png) |
| **Pow** | 2 | 60x60 | [`merus_Pow.piskel`](Pow/merus_Pow.piskel) | [`merus_Pow.gif`](Pow/merus_Pow.gif) | [`merus_Pow_sheet.png`](Pow/merus_Pow_sheet.png) |
| **Hurt** | 2 | 52x52 | [`merus_Hurt.piskel`](Hurt/merus_Hurt.piskel) | [`merus_Hurt.gif`](Hurt/merus_Hurt.gif) | [`merus_Hurt_sheet.png`](Hurt/merus_Hurt_sheet.png) |
| **Faint** | 1 | 56x56 | [`merus_Faint.piskel`](Faint/merus_Faint.piskel) | [`merus_Faint.gif`](Faint/merus_Faint.gif) | [`merus_Faint_sheet.png`](Faint/merus_Faint_sheet.png) |
| **Attack2** | 3 | 54x54 | [`merus_Attack2.piskel`](Attack2/merus_Attack2.piskel) | [`merus_Attack2.gif`](Attack2/merus_Attack2.gif) | [`merus_Attack2_sheet.png`](Attack2/merus_Attack2_sheet.png) |
| **Beam** | 2 | 78x78 | [`merus_Beam.piskel`](Beam/merus_Beam.piskel) | [`merus_Beam.gif`](Beam/merus_Beam.gif) | [`merus_Beam_sheet.png`](Beam/merus_Beam_sheet.png) |