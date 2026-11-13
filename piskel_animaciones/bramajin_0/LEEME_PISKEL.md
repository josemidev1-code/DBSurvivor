# Animaciones para Piskel — BRAMAJIN (Forma 0)

Esta carpeta contiene las animaciones listas para abrir y editar en **Piskel** (https://www.piskelapp.com/).

## Cómo abrir en Piskel:
1. Entra a **https://www.piskelapp.com/p/create/sprite** en tu navegador.
2. Haz clic en el icono de carpeta de la barra derecha (**Import**).
3. Elige cualquiera de estas opciones:
   - **Import .piskel file**: selecciona el archivo `.piskel` de cualquier animación.
   - **Import animated GIF**: selecciona el archivo `.gif` (Piskel importa todos los fotogramas y la velocidad al instante).
   - **Import from picture**: selecciona el `_sheet.png` (pon el Frame size que se indica abajo).

## Volver al juego:
`python herramientas/importar_piskel.py editado.piskel --manifiesto piskel_animaciones/bramajin_0/origen.json --heroe bramajin --forma 0 --anim attack --aplicar`
Después: `python herramientas/montar_animaciones.py bramajin` y revisión visual. Solo se aceptan sprites originales exportados.

## Animaciones disponibles:

| Animación | Fotogramas | Tamaño de celda | Archivo .piskel | GIF animado | Hoja Strip |
|---|---|---|---|---|---|
| **Idle** | 2 | 58x58 | [`bramajin_Idle.piskel`](Idle/bramajin_Idle.piskel) | [`bramajin_Idle.gif`](Idle/bramajin_Idle.gif) | [`bramajin_Idle_sheet.png`](Idle/bramajin_Idle_sheet.png) |
| **Walk** | 1 | 36x36 | [`bramajin_Walk.piskel`](Walk/bramajin_Walk.piskel) | [`bramajin_Walk.gif`](Walk/bramajin_Walk.gif) | [`bramajin_Walk_sheet.png`](Walk/bramajin_Walk_sheet.png) |
| **Attack** | 3 | 48x48 | [`bramajin_Attack.piskel`](Attack/bramajin_Attack.piskel) | [`bramajin_Attack.gif`](Attack/bramajin_Attack.gif) | [`bramajin_Attack_sheet.png`](Attack/bramajin_Attack_sheet.png) |
| **Kick** | 2 | 50x50 | [`bramajin_Kick.piskel`](Kick/bramajin_Kick.piskel) | [`bramajin_Kick.gif`](Kick/bramajin_Kick.gif) | [`bramajin_Kick_sheet.png`](Kick/bramajin_Kick_sheet.png) |
| **Cast** | 2 | 54x54 | [`bramajin_Cast.piskel`](Cast/bramajin_Cast.piskel) | [`bramajin_Cast.gif`](Cast/bramajin_Cast.gif) | [`bramajin_Cast_sheet.png`](Cast/bramajin_Cast_sheet.png) |
| **Pow** | 2 | 68x68 | [`bramajin_Pow.piskel`](Pow/bramajin_Pow.piskel) | [`bramajin_Pow.gif`](Pow/bramajin_Pow.gif) | [`bramajin_Pow_sheet.png`](Pow/bramajin_Pow_sheet.png) |
| **Hurt** | 2 | 52x52 | [`bramajin_Hurt.piskel`](Hurt/bramajin_Hurt.piskel) | [`bramajin_Hurt.gif`](Hurt/bramajin_Hurt.gif) | [`bramajin_Hurt_sheet.png`](Hurt/bramajin_Hurt_sheet.png) |
| **Faint** | 1 | 40x40 | [`bramajin_Faint.piskel`](Faint/bramajin_Faint.piskel) | [`bramajin_Faint.gif`](Faint/bramajin_Faint.gif) | [`bramajin_Faint_sheet.png`](Faint/bramajin_Faint_sheet.png) |
| **Attack2** | 2 | 48x48 | [`bramajin_Attack2.piskel`](Attack2/bramajin_Attack2.piskel) | [`bramajin_Attack2.gif`](Attack2/bramajin_Attack2.gif) | [`bramajin_Attack2_sheet.png`](Attack2/bramajin_Attack2_sheet.png) |
| **Attack3** | 2 | 58x58 | [`bramajin_Attack3.piskel`](Attack3/bramajin_Attack3.piskel) | [`bramajin_Attack3.gif`](Attack3/bramajin_Attack3.gif) | [`bramajin_Attack3_sheet.png`](Attack3/bramajin_Attack3_sheet.png) |
| **Kick2** | 2 | 52x52 | [`bramajin_Kick2.piskel`](Kick2/bramajin_Kick2.piskel) | [`bramajin_Kick2.gif`](Kick2/bramajin_Kick2.gif) | [`bramajin_Kick2_sheet.png`](Kick2/bramajin_Kick2_sheet.png) |
| **Beam** | 2 | 56x56 | [`bramajin_Beam.piskel`](Beam/bramajin_Beam.piskel) | [`bramajin_Beam.gif`](Beam/bramajin_Beam.gif) | [`bramajin_Beam_sheet.png`](Beam/bramajin_Beam_sheet.png) |