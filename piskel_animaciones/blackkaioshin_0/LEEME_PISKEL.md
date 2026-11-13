# Animaciones para Piskel — BLACKKAIOSHIN (Forma 0)

Esta carpeta contiene las animaciones listas para abrir y editar en **Piskel** (https://www.piskelapp.com/).

## Cómo abrir en Piskel:
1. Entra a **https://www.piskelapp.com/p/create/sprite** en tu navegador.
2. Haz clic en el icono de carpeta de la barra derecha (**Import**).
3. Elige cualquiera de estas opciones:
   - **Import .piskel file**: selecciona el archivo `.piskel` de cualquier animación.
   - **Import animated GIF**: selecciona el archivo `.gif` (Piskel importa todos los fotogramas y la velocidad al instante).
   - **Import from picture**: selecciona el `_sheet.png` (pon el Frame size que se indica abajo).

## Volver al juego:
`python herramientas/importar_piskel.py editado.piskel --manifiesto piskel_animaciones/blackkaioshin_0/origen.json --heroe blackkaioshin --forma 0 --anim attack --aplicar`
Después: `python herramientas/montar_animaciones.py blackkaioshin` y revisión visual. Solo se aceptan sprites originales exportados.

## Animaciones disponibles:

| Animación | Fotogramas | Tamaño de celda | Archivo .piskel | GIF animado | Hoja Strip |
|---|---|---|---|---|---|
| **Idle** | 2 | 56x56 | [`blackkaioshin_Idle.piskel`](Idle/blackkaioshin_Idle.piskel) | [`blackkaioshin_Idle.gif`](Idle/blackkaioshin_Idle.gif) | [`blackkaioshin_Idle_sheet.png`](Idle/blackkaioshin_Idle_sheet.png) |
| **Walk** | 1 | 50x50 | [`blackkaioshin_Walk.piskel`](Walk/blackkaioshin_Walk.piskel) | [`blackkaioshin_Walk.gif`](Walk/blackkaioshin_Walk.gif) | [`blackkaioshin_Walk_sheet.png`](Walk/blackkaioshin_Walk_sheet.png) |
| **Attack** | 3 | 60x60 | [`blackkaioshin_Attack.piskel`](Attack/blackkaioshin_Attack.piskel) | [`blackkaioshin_Attack.gif`](Attack/blackkaioshin_Attack.gif) | [`blackkaioshin_Attack_sheet.png`](Attack/blackkaioshin_Attack_sheet.png) |
| **Kick** | 2 | 56x56 | [`blackkaioshin_Kick.piskel`](Kick/blackkaioshin_Kick.piskel) | [`blackkaioshin_Kick.gif`](Kick/blackkaioshin_Kick.gif) | [`blackkaioshin_Kick_sheet.png`](Kick/blackkaioshin_Kick_sheet.png) |
| **Cast** | 2 | 56x56 | [`blackkaioshin_Cast.piskel`](Cast/blackkaioshin_Cast.piskel) | [`blackkaioshin_Cast.gif`](Cast/blackkaioshin_Cast.gif) | [`blackkaioshin_Cast_sheet.png`](Cast/blackkaioshin_Cast_sheet.png) |
| **Pow** | 2 | 58x58 | [`blackkaioshin_Pow.piskel`](Pow/blackkaioshin_Pow.piskel) | [`blackkaioshin_Pow.gif`](Pow/blackkaioshin_Pow.gif) | [`blackkaioshin_Pow_sheet.png`](Pow/blackkaioshin_Pow_sheet.png) |
| **Hurt** | 2 | 50x50 | [`blackkaioshin_Hurt.piskel`](Hurt/blackkaioshin_Hurt.piskel) | [`blackkaioshin_Hurt.gif`](Hurt/blackkaioshin_Hurt.gif) | [`blackkaioshin_Hurt_sheet.png`](Hurt/blackkaioshin_Hurt_sheet.png) |
| **Attack2** | 2 | 52x52 | [`blackkaioshin_Attack2.piskel`](Attack2/blackkaioshin_Attack2.piskel) | [`blackkaioshin_Attack2.gif`](Attack2/blackkaioshin_Attack2.gif) | [`blackkaioshin_Attack2_sheet.png`](Attack2/blackkaioshin_Attack2_sheet.png) |
| **Attack3** | 2 | 52x52 | [`blackkaioshin_Attack3.piskel`](Attack3/blackkaioshin_Attack3.piskel) | [`blackkaioshin_Attack3.gif`](Attack3/blackkaioshin_Attack3.gif) | [`blackkaioshin_Attack3_sheet.png`](Attack3/blackkaioshin_Attack3_sheet.png) |
| **Beam** | 2 | 56x56 | [`blackkaioshin_Beam.piskel`](Beam/blackkaioshin_Beam.piskel) | [`blackkaioshin_Beam.gif`](Beam/blackkaioshin_Beam.gif) | [`blackkaioshin_Beam_sheet.png`](Beam/blackkaioshin_Beam_sheet.png) |