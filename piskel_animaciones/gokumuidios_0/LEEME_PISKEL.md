# Animaciones para Piskel — GOKUMUIDIOS (Forma 0)

Esta carpeta contiene las animaciones listas para abrir y editar en **Piskel** (https://www.piskelapp.com/).

## Cómo abrir en Piskel:
1. Entra a **https://www.piskelapp.com/p/create/sprite** en tu navegador.
2. Haz clic en el icono de carpeta de la barra derecha (**Import**).
3. Elige cualquiera de estas opciones:
   - **Import .piskel file**: selecciona el archivo `.piskel` de cualquier animación.
   - **Import animated GIF**: selecciona el archivo `.gif` (Piskel importa todos los fotogramas y la velocidad al instante).
   - **Import from picture**: selecciona el `_sheet.png` (pon el Frame size que se indica abajo).

## Volver al juego:
`python herramientas/importar_piskel.py editado.piskel --manifiesto piskel_animaciones/gokumuidios_0/origen.json --heroe gokumuidios --forma 0 --anim attack --aplicar`
Después: `python herramientas/montar_animaciones.py gokumuidios` y revisión visual. Solo se aceptan sprites originales exportados.

## Animaciones disponibles:

| Animación | Fotogramas | Tamaño de celda | Archivo .piskel | GIF animado | Hoja Strip |
|---|---|---|---|---|---|
| **Idle** | 2 | 52x52 | [`gokumuidios_Idle.piskel`](Idle/gokumuidios_Idle.piskel) | [`gokumuidios_Idle.gif`](Idle/gokumuidios_Idle.gif) | [`gokumuidios_Idle_sheet.png`](Idle/gokumuidios_Idle_sheet.png) |
| **Walk** | 1 | 52x52 | [`gokumuidios_Walk.piskel`](Walk/gokumuidios_Walk.piskel) | [`gokumuidios_Walk.gif`](Walk/gokumuidios_Walk.gif) | [`gokumuidios_Walk_sheet.png`](Walk/gokumuidios_Walk_sheet.png) |
| **Attack** | 3 | 62x62 | [`gokumuidios_Attack.piskel`](Attack/gokumuidios_Attack.piskel) | [`gokumuidios_Attack.gif`](Attack/gokumuidios_Attack.gif) | [`gokumuidios_Attack_sheet.png`](Attack/gokumuidios_Attack_sheet.png) |
| **Kick** | 2 | 60x60 | [`gokumuidios_Kick.piskel`](Kick/gokumuidios_Kick.piskel) | [`gokumuidios_Kick.gif`](Kick/gokumuidios_Kick.gif) | [`gokumuidios_Kick_sheet.png`](Kick/gokumuidios_Kick_sheet.png) |
| **Cast** | 2 | 58x58 | [`gokumuidios_Cast.piskel`](Cast/gokumuidios_Cast.piskel) | [`gokumuidios_Cast.gif`](Cast/gokumuidios_Cast.gif) | [`gokumuidios_Cast_sheet.png`](Cast/gokumuidios_Cast_sheet.png) |
| **Pow** | 2 | 90x90 | [`gokumuidios_Pow.piskel`](Pow/gokumuidios_Pow.piskel) | [`gokumuidios_Pow.gif`](Pow/gokumuidios_Pow.gif) | [`gokumuidios_Pow_sheet.png`](Pow/gokumuidios_Pow_sheet.png) |
| **Hurt** | 2 | 60x60 | [`gokumuidios_Hurt.piskel`](Hurt/gokumuidios_Hurt.piskel) | [`gokumuidios_Hurt.gif`](Hurt/gokumuidios_Hurt.gif) | [`gokumuidios_Hurt_sheet.png`](Hurt/gokumuidios_Hurt_sheet.png) |
| **Attack2** | 3 | 64x64 | [`gokumuidios_Attack2.piskel`](Attack2/gokumuidios_Attack2.piskel) | [`gokumuidios_Attack2.gif`](Attack2/gokumuidios_Attack2.gif) | [`gokumuidios_Attack2_sheet.png`](Attack2/gokumuidios_Attack2_sheet.png) |
| **Attack3** | 3 | 60x60 | [`gokumuidios_Attack3.piskel`](Attack3/gokumuidios_Attack3.piskel) | [`gokumuidios_Attack3.gif`](Attack3/gokumuidios_Attack3.gif) | [`gokumuidios_Attack3_sheet.png`](Attack3/gokumuidios_Attack3_sheet.png) |
| **Kick2** | 3 | 60x60 | [`gokumuidios_Kick2.piskel`](Kick2/gokumuidios_Kick2.piskel) | [`gokumuidios_Kick2.gif`](Kick2/gokumuidios_Kick2.gif) | [`gokumuidios_Kick2_sheet.png`](Kick2/gokumuidios_Kick2_sheet.png) |
| **Beam** | 2 | 64x64 | [`gokumuidios_Beam.piskel`](Beam/gokumuidios_Beam.piskel) | [`gokumuidios_Beam.gif`](Beam/gokumuidios_Beam.gif) | [`gokumuidios_Beam_sheet.png`](Beam/gokumuidios_Beam_sheet.png) |
| **Up** | 1 | 58x58 | [`gokumuidios_Up.piskel`](Up/gokumuidios_Up.piskel) | [`gokumuidios_Up.gif`](Up/gokumuidios_Up.gif) | [`gokumuidios_Up_sheet.png`](Up/gokumuidios_Up_sheet.png) |