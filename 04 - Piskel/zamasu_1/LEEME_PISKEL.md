# Animaciones para Piskel — ZAMASU (Forma 1)

Esta carpeta contiene las animaciones listas para abrir y editar en **Piskel** (https://www.piskelapp.com/).

## Cómo abrir en Piskel:
1. Entra a **https://www.piskelapp.com/p/create/sprite** en tu navegador.
2. Haz clic en el icono de carpeta de la barra derecha (**Import**).
3. Elige cualquiera de estas opciones:
   - **Import .piskel file**: selecciona el archivo `.piskel` de cualquier animación.
   - **Import animated GIF**: selecciona el archivo `.gif` (Piskel importa todos los fotogramas y la velocidad al instante).
   - **Import from picture**: selecciona el `_sheet.png` (pon el Frame size que se indica abajo).

## Volver al juego:
`python herramientas/importar_piskel.py editado.piskel --manifiesto "04 - Piskel/zamasu_1/origen.json" --heroe zamasu --forma 1 --anim attack --aplicar`
Después: `python herramientas/montar_animaciones.py zamasu` y revisión visual. Solo se aceptan sprites originales exportados.

## Animaciones disponibles:

| Animación | Fotogramas | Tamaño de celda | Archivo .piskel | GIF animado | Hoja Strip |
|---|---|---|---|---|---|
| **Idle** | 1 | 78x78 | [`zamasu_Idle.piskel`](Idle/zamasu_Idle.piskel) | [`zamasu_Idle.gif`](Idle/zamasu_Idle.gif) | [`zamasu_Idle_sheet.png`](Idle/zamasu_Idle_sheet.png) |
| **Walk** | 1 | 70x70 | [`zamasu_Walk.piskel`](Walk/zamasu_Walk.piskel) | [`zamasu_Walk.gif`](Walk/zamasu_Walk.gif) | [`zamasu_Walk_sheet.png`](Walk/zamasu_Walk_sheet.png) |
| **Attack** | 3 | 78x78 | [`zamasu_Attack.piskel`](Attack/zamasu_Attack.piskel) | [`zamasu_Attack.gif`](Attack/zamasu_Attack.gif) | [`zamasu_Attack_sheet.png`](Attack/zamasu_Attack_sheet.png) |
| **Kick** | 2 | 80x80 | [`zamasu_Kick.piskel`](Kick/zamasu_Kick.piskel) | [`zamasu_Kick.gif`](Kick/zamasu_Kick.gif) | [`zamasu_Kick_sheet.png`](Kick/zamasu_Kick_sheet.png) |
| **Cast** | 2 | 80x80 | [`zamasu_Cast.piskel`](Cast/zamasu_Cast.piskel) | [`zamasu_Cast.gif`](Cast/zamasu_Cast.gif) | [`zamasu_Cast_sheet.png`](Cast/zamasu_Cast_sheet.png) |
| **Pow** | 3 | 96x96 | [`zamasu_Pow.piskel`](Pow/zamasu_Pow.piskel) | [`zamasu_Pow.gif`](Pow/zamasu_Pow.gif) | [`zamasu_Pow_sheet.png`](Pow/zamasu_Pow_sheet.png) |
| **Hurt** | 2 | 80x80 | [`zamasu_Hurt.piskel`](Hurt/zamasu_Hurt.piskel) | [`zamasu_Hurt.gif`](Hurt/zamasu_Hurt.gif) | [`zamasu_Hurt_sheet.png`](Hurt/zamasu_Hurt_sheet.png) |
| **Faint** | 1 | 80x80 | [`zamasu_Faint.piskel`](Faint/zamasu_Faint.piskel) | [`zamasu_Faint.gif`](Faint/zamasu_Faint.gif) | [`zamasu_Faint_sheet.png`](Faint/zamasu_Faint_sheet.png) |
| **Attack2** | 3 | 80x80 | [`zamasu_Attack2.piskel`](Attack2/zamasu_Attack2.piskel) | [`zamasu_Attack2.gif`](Attack2/zamasu_Attack2.gif) | [`zamasu_Attack2_sheet.png`](Attack2/zamasu_Attack2_sheet.png) |
| **Attack3** | 2 | 80x80 | [`zamasu_Attack3.piskel`](Attack3/zamasu_Attack3.piskel) | [`zamasu_Attack3.gif`](Attack3/zamasu_Attack3.gif) | [`zamasu_Attack3_sheet.png`](Attack3/zamasu_Attack3_sheet.png) |
| **Kick2** | 2 | 70x70 | [`zamasu_Kick2.piskel`](Kick2/zamasu_Kick2.piskel) | [`zamasu_Kick2.gif`](Kick2/zamasu_Kick2.gif) | [`zamasu_Kick2_sheet.png`](Kick2/zamasu_Kick2_sheet.png) |
| **Beam** | 2 | 80x80 | [`zamasu_Beam.piskel`](Beam/zamasu_Beam.piskel) | [`zamasu_Beam.gif`](Beam/zamasu_Beam.gif) | [`zamasu_Beam_sheet.png`](Beam/zamasu_Beam_sheet.png) |
| **Up** | 2 | 106x106 | [`zamasu_Up.piskel`](Up/zamasu_Up.piskel) | [`zamasu_Up.gif`](Up/zamasu_Up.gif) | [`zamasu_Up_sheet.png`](Up/zamasu_Up_sheet.png) |