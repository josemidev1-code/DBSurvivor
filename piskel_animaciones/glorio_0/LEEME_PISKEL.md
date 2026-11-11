# Animaciones para Piskel — GLORIO (Forma 0)

Esta carpeta contiene las animaciones listas para abrir y editar en **Piskel** (https://www.piskelapp.com/).

## Cómo abrir en Piskel:
1. Entra a **https://www.piskelapp.com/p/create/sprite** en tu navegador.
2. Haz clic en el icono de carpeta de la barra derecha (**Import**).
3. Elige cualquiera de estas opciones:
   - **Import .piskel file**: selecciona el archivo `.piskel` de cualquier animación.
   - **Import animated GIF**: selecciona el archivo `.gif` (Piskel importa todos los fotogramas y la velocidad al instante).
   - **Import from picture**: selecciona el `_sheet.png` (pon el Frame size que se indica abajo).

## Volver al juego:
`python herramientas/importar_piskel.py editado.piskel --manifiesto piskel_animaciones/glorio_0/origen.json --heroe glorio --forma 0 --anim attack --aplicar`
Después: `python herramientas/montar_animaciones.py glorio` y revisión visual. Solo se aceptan sprites originales exportados.

## Animaciones disponibles:

| Animación | Fotogramas | Tamaño de celda | Archivo .piskel | GIF animado | Hoja Strip |
|---|---|---|---|---|---|
| **Idle** | 2 | 52x52 | [`glorio_Idle.piskel`](Idle/glorio_Idle.piskel) | [`glorio_Idle.gif`](Idle/glorio_Idle.gif) | [`glorio_Idle_sheet.png`](Idle/glorio_Idle_sheet.png) |
| **Walk** | 1 | 58x58 | [`glorio_Walk.piskel`](Walk/glorio_Walk.piskel) | [`glorio_Walk.gif`](Walk/glorio_Walk.gif) | [`glorio_Walk_sheet.png`](Walk/glorio_Walk_sheet.png) |
| **Attack** | 3 | 50x50 | [`glorio_Attack.piskel`](Attack/glorio_Attack.piskel) | [`glorio_Attack.gif`](Attack/glorio_Attack.gif) | [`glorio_Attack_sheet.png`](Attack/glorio_Attack_sheet.png) |
| **Kick** | 2 | 52x52 | [`glorio_Kick.piskel`](Kick/glorio_Kick.piskel) | [`glorio_Kick.gif`](Kick/glorio_Kick.gif) | [`glorio_Kick_sheet.png`](Kick/glorio_Kick_sheet.png) |
| **Cast** | 3 | 56x56 | [`glorio_Cast.piskel`](Cast/glorio_Cast.piskel) | [`glorio_Cast.gif`](Cast/glorio_Cast.gif) | [`glorio_Cast_sheet.png`](Cast/glorio_Cast_sheet.png) |
| **Pow** | 2 | 104x104 | [`glorio_Pow.piskel`](Pow/glorio_Pow.piskel) | [`glorio_Pow.gif`](Pow/glorio_Pow.gif) | [`glorio_Pow_sheet.png`](Pow/glorio_Pow_sheet.png) |
| **Hurt** | 2 | 46x46 | [`glorio_Hurt.piskel`](Hurt/glorio_Hurt.piskel) | [`glorio_Hurt.gif`](Hurt/glorio_Hurt.gif) | [`glorio_Hurt_sheet.png`](Hurt/glorio_Hurt_sheet.png) |
| **Faint** | 1 | 54x54 | [`glorio_Faint.piskel`](Faint/glorio_Faint.piskel) | [`glorio_Faint.gif`](Faint/glorio_Faint.gif) | [`glorio_Faint_sheet.png`](Faint/glorio_Faint_sheet.png) |
| **Attack2** | 2 | 54x54 | [`glorio_Attack2.piskel`](Attack2/glorio_Attack2.piskel) | [`glorio_Attack2.gif`](Attack2/glorio_Attack2.gif) | [`glorio_Attack2_sheet.png`](Attack2/glorio_Attack2_sheet.png) |
| **Attack3** | 2 | 46x46 | [`glorio_Attack3.piskel`](Attack3/glorio_Attack3.piskel) | [`glorio_Attack3.gif`](Attack3/glorio_Attack3.gif) | [`glorio_Attack3_sheet.png`](Attack3/glorio_Attack3_sheet.png) |
| **Kick2** | 2 | 48x48 | [`glorio_Kick2.piskel`](Kick2/glorio_Kick2.piskel) | [`glorio_Kick2.gif`](Kick2/glorio_Kick2.gif) | [`glorio_Kick2_sheet.png`](Kick2/glorio_Kick2_sheet.png) |
| **Beam** | 2 | 56x56 | [`glorio_Beam.piskel`](Beam/glorio_Beam.piskel) | [`glorio_Beam.gif`](Beam/glorio_Beam.gif) | [`glorio_Beam_sheet.png`](Beam/glorio_Beam_sheet.png) |
| **Up** | 1 | 54x54 | [`glorio_Up.piskel`](Up/glorio_Up.piskel) | [`glorio_Up.gif`](Up/glorio_Up.gif) | [`glorio_Up_sheet.png`](Up/glorio_Up_sheet.png) |