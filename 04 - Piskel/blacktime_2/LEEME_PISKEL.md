# Animaciones para Piskel — BLACKTIME (Forma 2)

Esta carpeta contiene las animaciones listas para abrir y editar en **Piskel** (https://www.piskelapp.com/).

## Cómo abrir en Piskel:
1. Entra a **https://www.piskelapp.com/p/create/sprite** en tu navegador.
2. Haz clic en el icono de carpeta de la barra derecha (**Import**).
3. Elige cualquiera de estas opciones:
   - **Import .piskel file**: selecciona el archivo `.piskel` de cualquier animación.
   - **Import animated GIF**: selecciona el archivo `.gif` (Piskel importa todos los fotogramas y la velocidad al instante).
   - **Import from picture**: selecciona el `_sheet.png` (pon el Frame size que se indica abajo).

## Volver al juego:
`python herramientas/importar_piskel.py editado.piskel --manifiesto "04 - Piskel/blacktime_2/origen.json" --heroe blacktime --forma 2 --anim attack --aplicar`
Después: `python herramientas/montar_animaciones.py blacktime` y revisión visual. Solo se aceptan sprites originales exportados.

## Animaciones disponibles:

| Animación | Fotogramas | Tamaño de celda | Archivo .piskel | GIF animado | Hoja Strip |
|---|---|---|---|---|---|
| **Idle** | 2 | 56x56 | [`blacktime_Idle.piskel`](Idle/blacktime_Idle.piskel) | [`blacktime_Idle.gif`](Idle/blacktime_Idle.gif) | [`blacktime_Idle_sheet.png`](Idle/blacktime_Idle_sheet.png) |
| **Walk** | 2 | 48x48 | [`blacktime_Walk.piskel`](Walk/blacktime_Walk.piskel) | [`blacktime_Walk.gif`](Walk/blacktime_Walk.gif) | [`blacktime_Walk_sheet.png`](Walk/blacktime_Walk_sheet.png) |
| **Attack** | 4 | 52x52 | [`blacktime_Attack.piskel`](Attack/blacktime_Attack.piskel) | [`blacktime_Attack.gif`](Attack/blacktime_Attack.gif) | [`blacktime_Attack_sheet.png`](Attack/blacktime_Attack_sheet.png) |
| **Kick** | 3 | 52x52 | [`blacktime_Kick.piskel`](Kick/blacktime_Kick.piskel) | [`blacktime_Kick.gif`](Kick/blacktime_Kick.gif) | [`blacktime_Kick_sheet.png`](Kick/blacktime_Kick_sheet.png) |
| **Cast** | 2 | 58x58 | [`blacktime_Cast.piskel`](Cast/blacktime_Cast.piskel) | [`blacktime_Cast.gif`](Cast/blacktime_Cast.gif) | [`blacktime_Cast_sheet.png`](Cast/blacktime_Cast_sheet.png) |
| **Pow** | 2 | 134x134 | [`blacktime_Pow.piskel`](Pow/blacktime_Pow.piskel) | [`blacktime_Pow.gif`](Pow/blacktime_Pow.gif) | [`blacktime_Pow_sheet.png`](Pow/blacktime_Pow_sheet.png) |
| **Hurt** | 2 | 48x48 | [`blacktime_Hurt.piskel`](Hurt/blacktime_Hurt.piskel) | [`blacktime_Hurt.gif`](Hurt/blacktime_Hurt.gif) | [`blacktime_Hurt_sheet.png`](Hurt/blacktime_Hurt_sheet.png) |
| **Faint** | 1 | 52x52 | [`blacktime_Faint.piskel`](Faint/blacktime_Faint.piskel) | [`blacktime_Faint.gif`](Faint/blacktime_Faint.gif) | [`blacktime_Faint_sheet.png`](Faint/blacktime_Faint_sheet.png) |
| **Attack2** | 3 | 50x50 | [`blacktime_Attack2.piskel`](Attack2/blacktime_Attack2.piskel) | [`blacktime_Attack2.gif`](Attack2/blacktime_Attack2.gif) | [`blacktime_Attack2_sheet.png`](Attack2/blacktime_Attack2_sheet.png) |
| **Attack3** | 2 | 52x52 | [`blacktime_Attack3.piskel`](Attack3/blacktime_Attack3.piskel) | [`blacktime_Attack3.gif`](Attack3/blacktime_Attack3.gif) | [`blacktime_Attack3_sheet.png`](Attack3/blacktime_Attack3_sheet.png) |
| **Kick2** | 2 | 50x50 | [`blacktime_Kick2.piskel`](Kick2/blacktime_Kick2.piskel) | [`blacktime_Kick2.gif`](Kick2/blacktime_Kick2.gif) | [`blacktime_Kick2_sheet.png`](Kick2/blacktime_Kick2_sheet.png) |
| **Beam** | 2 | 58x58 | [`blacktime_Beam.piskel`](Beam/blacktime_Beam.piskel) | [`blacktime_Beam.gif`](Beam/blacktime_Beam.gif) | [`blacktime_Beam_sheet.png`](Beam/blacktime_Beam_sheet.png) |
| **Up** | 2 | 60x60 | [`blacktime_Up.piskel`](Up/blacktime_Up.piskel) | [`blacktime_Up.gif`](Up/blacktime_Up.gif) | [`blacktime_Up_sheet.png`](Up/blacktime_Up_sheet.png) |