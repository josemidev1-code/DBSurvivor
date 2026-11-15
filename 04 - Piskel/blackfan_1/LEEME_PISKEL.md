# Animaciones para Piskel — BLACKFAN (Forma 1)

Esta carpeta contiene las animaciones listas para abrir y editar en **Piskel** (https://www.piskelapp.com/).

## Cómo abrir en Piskel:
1. Entra a **https://www.piskelapp.com/p/create/sprite** en tu navegador.
2. Haz clic en el icono de carpeta de la barra derecha (**Import**).
3. Elige cualquiera de estas opciones:
   - **Import .piskel file**: selecciona el archivo `.piskel` de cualquier animación.
   - **Import animated GIF**: selecciona el archivo `.gif` (Piskel importa todos los fotogramas y la velocidad al instante).
   - **Import from picture**: selecciona el `_sheet.png` (pon el Frame size que se indica abajo).

## Volver al juego:
`python herramientas/importar_piskel.py editado.piskel --manifiesto "04 - Piskel/blackfan_1/origen.json" --heroe blackfan --forma 1 --anim attack --aplicar`
Después: `python herramientas/montar_animaciones.py blackfan` y revisión visual. Solo se aceptan sprites originales exportados.

## Animaciones disponibles:

| Animación | Fotogramas | Tamaño de celda | Archivo .piskel | GIF animado | Hoja Strip |
|---|---|---|---|---|---|
| **Idle** | 2 | 58x58 | [`blackfan_Idle.piskel`](Idle/blackfan_Idle.piskel) | [`blackfan_Idle.gif`](Idle/blackfan_Idle.gif) | [`blackfan_Idle_sheet.png`](Idle/blackfan_Idle_sheet.png) |
| **Walk** | 2 | 54x54 | [`blackfan_Walk.piskel`](Walk/blackfan_Walk.piskel) | [`blackfan_Walk.gif`](Walk/blackfan_Walk.gif) | [`blackfan_Walk_sheet.png`](Walk/blackfan_Walk_sheet.png) |
| **Attack** | 4 | 52x52 | [`blackfan_Attack.piskel`](Attack/blackfan_Attack.piskel) | [`blackfan_Attack.gif`](Attack/blackfan_Attack.gif) | [`blackfan_Attack_sheet.png`](Attack/blackfan_Attack_sheet.png) |
| **Kick** | 3 | 46x46 | [`blackfan_Kick.piskel`](Kick/blackfan_Kick.piskel) | [`blackfan_Kick.gif`](Kick/blackfan_Kick.gif) | [`blackfan_Kick_sheet.png`](Kick/blackfan_Kick_sheet.png) |
| **Cast** | 2 | 56x56 | [`blackfan_Cast.piskel`](Cast/blackfan_Cast.piskel) | [`blackfan_Cast.gif`](Cast/blackfan_Cast.gif) | [`blackfan_Cast_sheet.png`](Cast/blackfan_Cast_sheet.png) |
| **Pow** | 2 | 128x128 | [`blackfan_Pow.piskel`](Pow/blackfan_Pow.piskel) | [`blackfan_Pow.gif`](Pow/blackfan_Pow.gif) | [`blackfan_Pow_sheet.png`](Pow/blackfan_Pow_sheet.png) |
| **Hurt** | 2 | 54x54 | [`blackfan_Hurt.piskel`](Hurt/blackfan_Hurt.piskel) | [`blackfan_Hurt.gif`](Hurt/blackfan_Hurt.gif) | [`blackfan_Hurt_sheet.png`](Hurt/blackfan_Hurt_sheet.png) |
| **Faint** | 1 | 60x60 | [`blackfan_Faint.piskel`](Faint/blackfan_Faint.piskel) | [`blackfan_Faint.gif`](Faint/blackfan_Faint.gif) | [`blackfan_Faint_sheet.png`](Faint/blackfan_Faint_sheet.png) |
| **Attack2** | 2 | 50x50 | [`blackfan_Attack2.piskel`](Attack2/blackfan_Attack2.piskel) | [`blackfan_Attack2.gif`](Attack2/blackfan_Attack2.gif) | [`blackfan_Attack2_sheet.png`](Attack2/blackfan_Attack2_sheet.png) |
| **Attack3** | 3 | 60x60 | [`blackfan_Attack3.piskel`](Attack3/blackfan_Attack3.piskel) | [`blackfan_Attack3.gif`](Attack3/blackfan_Attack3.gif) | [`blackfan_Attack3_sheet.png`](Attack3/blackfan_Attack3_sheet.png) |
| **Kick2** | 2 | 52x52 | [`blackfan_Kick2.piskel`](Kick2/blackfan_Kick2.piskel) | [`blackfan_Kick2.gif`](Kick2/blackfan_Kick2.gif) | [`blackfan_Kick2_sheet.png`](Kick2/blackfan_Kick2_sheet.png) |
| **Beam** | 2 | 56x56 | [`blackfan_Beam.piskel`](Beam/blackfan_Beam.piskel) | [`blackfan_Beam.gif`](Beam/blackfan_Beam.gif) | [`blackfan_Beam_sheet.png`](Beam/blackfan_Beam_sheet.png) |
| **Up** | 1 | 60x60 | [`blackfan_Up.piskel`](Up/blackfan_Up.piskel) | [`blackfan_Up.gif`](Up/blackfan_Up.gif) | [`blackfan_Up_sheet.png`](Up/blackfan_Up_sheet.png) |