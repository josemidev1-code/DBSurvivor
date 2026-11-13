# Animaciones para Piskel — OMEGA (Forma 0)

Esta carpeta contiene las animaciones listas para abrir y editar en **Piskel** (https://www.piskelapp.com/).

## Cómo abrir en Piskel:
1. Entra a **https://www.piskelapp.com/p/create/sprite** en tu navegador.
2. Haz clic en el icono de carpeta de la barra derecha (**Import**).
3. Elige cualquiera de estas opciones:
   - **Import .piskel file**: selecciona el archivo `.piskel` de cualquier animación.
   - **Import animated GIF**: selecciona el archivo `.gif` (Piskel importa todos los fotogramas y la velocidad al instante).
   - **Import from picture**: selecciona el `_sheet.png` (pon el Frame size que se indica abajo).

## Volver al juego:
`python herramientas/importar_piskel.py editado.piskel --manifiesto piskel_animaciones/omega_0/origen.json --heroe omega --forma 0 --anim attack --aplicar`
Después: `python herramientas/montar_animaciones.py omega` y revisión visual. Solo se aceptan sprites originales exportados.

## Animaciones disponibles:

| Animación | Fotogramas | Tamaño de celda | Archivo .piskel | GIF animado | Hoja Strip |
|---|---|---|---|---|---|
| **Idle** | 2 | 52x52 | [`omega_Idle.piskel`](Idle/omega_Idle.piskel) | [`omega_Idle.gif`](Idle/omega_Idle.gif) | [`omega_Idle_sheet.png`](Idle/omega_Idle_sheet.png) |
| **Walk** | 1 | 48x48 | [`omega_Walk.piskel`](Walk/omega_Walk.piskel) | [`omega_Walk.gif`](Walk/omega_Walk.gif) | [`omega_Walk_sheet.png`](Walk/omega_Walk_sheet.png) |
| **Attack** | 3 | 50x50 | [`omega_Attack.piskel`](Attack/omega_Attack.piskel) | [`omega_Attack.gif`](Attack/omega_Attack.gif) | [`omega_Attack_sheet.png`](Attack/omega_Attack_sheet.png) |
| **Kick** | 2 | 52x52 | [`omega_Kick.piskel`](Kick/omega_Kick.piskel) | [`omega_Kick.gif`](Kick/omega_Kick.gif) | [`omega_Kick_sheet.png`](Kick/omega_Kick_sheet.png) |
| **Cast** | 2 | 68x68 | [`omega_Cast.piskel`](Cast/omega_Cast.piskel) | [`omega_Cast.gif`](Cast/omega_Cast.gif) | [`omega_Cast_sheet.png`](Cast/omega_Cast_sheet.png) |
| **Pow** | 2 | 68x68 | [`omega_Pow.piskel`](Pow/omega_Pow.piskel) | [`omega_Pow.gif`](Pow/omega_Pow.gif) | [`omega_Pow_sheet.png`](Pow/omega_Pow_sheet.png) |
| **Hurt** | 2 | 52x52 | [`omega_Hurt.piskel`](Hurt/omega_Hurt.piskel) | [`omega_Hurt.gif`](Hurt/omega_Hurt.gif) | [`omega_Hurt_sheet.png`](Hurt/omega_Hurt_sheet.png) |
| **Attack2** | 2 | 50x50 | [`omega_Attack2.piskel`](Attack2/omega_Attack2.piskel) | [`omega_Attack2.gif`](Attack2/omega_Attack2.gif) | [`omega_Attack2_sheet.png`](Attack2/omega_Attack2_sheet.png) |
| **Attack3** | 2 | 52x52 | [`omega_Attack3.piskel`](Attack3/omega_Attack3.piskel) | [`omega_Attack3.gif`](Attack3/omega_Attack3.gif) | [`omega_Attack3_sheet.png`](Attack3/omega_Attack3_sheet.png) |
| **Beam** | 2 | 52x52 | [`omega_Beam.piskel`](Beam/omega_Beam.piskel) | [`omega_Beam.gif`](Beam/omega_Beam.gif) | [`omega_Beam_sheet.png`](Beam/omega_Beam_sheet.png) |
| **Up** | 1 | 52x52 | [`omega_Up.piskel`](Up/omega_Up.piskel) | [`omega_Up.gif`](Up/omega_Up.gif) | [`omega_Up_sheet.png`](Up/omega_Up_sheet.png) |