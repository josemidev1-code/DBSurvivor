# Animaciones para Piskel — PANGT (Forma 0)

Esta carpeta contiene las animaciones listas para abrir y editar en **Piskel** (https://www.piskelapp.com/).

## Cómo abrir en Piskel:
1. Entra a **https://www.piskelapp.com/p/create/sprite** en tu navegador.
2. Haz clic en el icono de carpeta de la barra derecha (**Import**).
3. Elige cualquiera de estas opciones:
   - **Import .piskel file**: selecciona el archivo `.piskel` de cualquier animación.
   - **Import animated GIF**: selecciona el archivo `.gif` (Piskel importa todos los fotogramas y la velocidad al instante).
   - **Import from picture**: selecciona el `_sheet.png` (pon el Frame size que se indica abajo).

## Volver al juego:
`python herramientas/importar_piskel.py editado.piskel --manifiesto piskel_animaciones/pangt_0/origen.json --heroe pangt --forma 0 --anim attack --aplicar`
Después: `python herramientas/montar_animaciones.py pangt` y revisión visual. Solo se aceptan sprites originales exportados.

## Animaciones disponibles:

| Animación | Fotogramas | Tamaño de celda | Archivo .piskel | GIF animado | Hoja Strip |
|---|---|---|---|---|---|
| **Idle** | 2 | 52x52 | [`pangt_Idle.piskel`](Idle/pangt_Idle.piskel) | [`pangt_Idle.gif`](Idle/pangt_Idle.gif) | [`pangt_Idle_sheet.png`](Idle/pangt_Idle_sheet.png) |
| **Walk** | 1 | 48x48 | [`pangt_Walk.piskel`](Walk/pangt_Walk.piskel) | [`pangt_Walk.gif`](Walk/pangt_Walk.gif) | [`pangt_Walk_sheet.png`](Walk/pangt_Walk_sheet.png) |
| **Attack** | 3 | 48x48 | [`pangt_Attack.piskel`](Attack/pangt_Attack.piskel) | [`pangt_Attack.gif`](Attack/pangt_Attack.gif) | [`pangt_Attack_sheet.png`](Attack/pangt_Attack_sheet.png) |
| **Kick** | 2 | 60x60 | [`pangt_Kick.piskel`](Kick/pangt_Kick.piskel) | [`pangt_Kick.gif`](Kick/pangt_Kick.gif) | [`pangt_Kick_sheet.png`](Kick/pangt_Kick_sheet.png) |
| **Cast** | 2 | 48x48 | [`pangt_Cast.piskel`](Cast/pangt_Cast.piskel) | [`pangt_Cast.gif`](Cast/pangt_Cast.gif) | [`pangt_Cast_sheet.png`](Cast/pangt_Cast_sheet.png) |
| **Pow** | 2 | 104x104 | [`pangt_Pow.piskel`](Pow/pangt_Pow.piskel) | [`pangt_Pow.gif`](Pow/pangt_Pow.gif) | [`pangt_Pow_sheet.png`](Pow/pangt_Pow_sheet.png) |
| **Hurt** | 2 | 52x52 | [`pangt_Hurt.piskel`](Hurt/pangt_Hurt.piskel) | [`pangt_Hurt.gif`](Hurt/pangt_Hurt.gif) | [`pangt_Hurt_sheet.png`](Hurt/pangt_Hurt_sheet.png) |
| **Faint** | 1 | 56x56 | [`pangt_Faint.piskel`](Faint/pangt_Faint.piskel) | [`pangt_Faint.gif`](Faint/pangt_Faint.gif) | [`pangt_Faint_sheet.png`](Faint/pangt_Faint_sheet.png) |
| **Attack2** | 2 | 56x56 | [`pangt_Attack2.piskel`](Attack2/pangt_Attack2.piskel) | [`pangt_Attack2.gif`](Attack2/pangt_Attack2.gif) | [`pangt_Attack2_sheet.png`](Attack2/pangt_Attack2_sheet.png) |
| **Kick2** | 2 | 48x48 | [`pangt_Kick2.piskel`](Kick2/pangt_Kick2.piskel) | [`pangt_Kick2.gif`](Kick2/pangt_Kick2.gif) | [`pangt_Kick2_sheet.png`](Kick2/pangt_Kick2_sheet.png) |
| **Beam** | 2 | 48x48 | [`pangt_Beam.piskel`](Beam/pangt_Beam.piskel) | [`pangt_Beam.gif`](Beam/pangt_Beam.gif) | [`pangt_Beam_sheet.png`](Beam/pangt_Beam_sheet.png) |