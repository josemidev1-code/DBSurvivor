# Animaciones para Piskel — VEGETTOFALSO (Forma 0)

Esta carpeta contiene las animaciones listas para abrir y editar en **Piskel** (https://www.piskelapp.com/).

## Cómo abrir en Piskel:
1. Entra a **https://www.piskelapp.com/p/create/sprite** en tu navegador.
2. Haz clic en el icono de carpeta de la barra derecha (**Import**).
3. Elige cualquiera de estas opciones:
   - **Import .piskel file**: selecciona el archivo `.piskel` de cualquier animación.
   - **Import animated GIF**: selecciona el archivo `.gif` (Piskel importa todos los fotogramas y la velocidad al instante).
   - **Import from picture**: selecciona el `_sheet.png` (pon el Frame size que se indica abajo).

## Volver al juego:
`python herramientas/importar_piskel.py editado.piskel --manifiesto piskel_animaciones/vegettofalso_0/origen.json --heroe vegettofalso --forma 0 --anim attack --aplicar`
Después: `python herramientas/montar_animaciones.py vegettofalso` y revisión visual. Solo se aceptan sprites originales exportados.

## Animaciones disponibles:

| Animación | Fotogramas | Tamaño de celda | Archivo .piskel | GIF animado | Hoja Strip |
|---|---|---|---|---|---|
| **Idle** | 2 | 54x54 | [`vegettofalso_Idle.piskel`](Idle/vegettofalso_Idle.piskel) | [`vegettofalso_Idle.gif`](Idle/vegettofalso_Idle.gif) | [`vegettofalso_Idle_sheet.png`](Idle/vegettofalso_Idle_sheet.png) |
| **Walk** | 1 | 62x62 | [`vegettofalso_Walk.piskel`](Walk/vegettofalso_Walk.piskel) | [`vegettofalso_Walk.gif`](Walk/vegettofalso_Walk.gif) | [`vegettofalso_Walk_sheet.png`](Walk/vegettofalso_Walk_sheet.png) |
| **Attack** | 3 | 54x54 | [`vegettofalso_Attack.piskel`](Attack/vegettofalso_Attack.piskel) | [`vegettofalso_Attack.gif`](Attack/vegettofalso_Attack.gif) | [`vegettofalso_Attack_sheet.png`](Attack/vegettofalso_Attack_sheet.png) |
| **Kick** | 2 | 54x54 | [`vegettofalso_Kick.piskel`](Kick/vegettofalso_Kick.piskel) | [`vegettofalso_Kick.gif`](Kick/vegettofalso_Kick.gif) | [`vegettofalso_Kick_sheet.png`](Kick/vegettofalso_Kick_sheet.png) |
| **Cast** | 2 | 72x72 | [`vegettofalso_Cast.piskel`](Cast/vegettofalso_Cast.piskel) | [`vegettofalso_Cast.gif`](Cast/vegettofalso_Cast.gif) | [`vegettofalso_Cast_sheet.png`](Cast/vegettofalso_Cast_sheet.png) |
| **Pow** | 2 | 54x54 | [`vegettofalso_Pow.piskel`](Pow/vegettofalso_Pow.piskel) | [`vegettofalso_Pow.gif`](Pow/vegettofalso_Pow.gif) | [`vegettofalso_Pow_sheet.png`](Pow/vegettofalso_Pow_sheet.png) |
| **Hurt** | 2 | 50x50 | [`vegettofalso_Hurt.piskel`](Hurt/vegettofalso_Hurt.piskel) | [`vegettofalso_Hurt.gif`](Hurt/vegettofalso_Hurt.gif) | [`vegettofalso_Hurt_sheet.png`](Hurt/vegettofalso_Hurt_sheet.png) |
| **Faint** | 1 | 52x52 | [`vegettofalso_Faint.piskel`](Faint/vegettofalso_Faint.piskel) | [`vegettofalso_Faint.gif`](Faint/vegettofalso_Faint.gif) | [`vegettofalso_Faint_sheet.png`](Faint/vegettofalso_Faint_sheet.png) |
| **Attack2** | 2 | 44x44 | [`vegettofalso_Attack2.piskel`](Attack2/vegettofalso_Attack2.piskel) | [`vegettofalso_Attack2.gif`](Attack2/vegettofalso_Attack2.gif) | [`vegettofalso_Attack2_sheet.png`](Attack2/vegettofalso_Attack2_sheet.png) |
| **Attack3** | 2 | 52x52 | [`vegettofalso_Attack3.piskel`](Attack3/vegettofalso_Attack3.piskel) | [`vegettofalso_Attack3.gif`](Attack3/vegettofalso_Attack3.gif) | [`vegettofalso_Attack3_sheet.png`](Attack3/vegettofalso_Attack3_sheet.png) |
| **Kick2** | 2 | 48x48 | [`vegettofalso_Kick2.piskel`](Kick2/vegettofalso_Kick2.piskel) | [`vegettofalso_Kick2.gif`](Kick2/vegettofalso_Kick2.gif) | [`vegettofalso_Kick2_sheet.png`](Kick2/vegettofalso_Kick2_sheet.png) |
| **Beam** | 2 | 50x50 | [`vegettofalso_Beam.piskel`](Beam/vegettofalso_Beam.piskel) | [`vegettofalso_Beam.gif`](Beam/vegettofalso_Beam.gif) | [`vegettofalso_Beam_sheet.png`](Beam/vegettofalso_Beam_sheet.png) |