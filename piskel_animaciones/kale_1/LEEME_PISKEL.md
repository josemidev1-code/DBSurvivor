# Animaciones para Piskel — KALE (Forma 1)

Esta carpeta contiene las animaciones listas para abrir y editar en **Piskel** (https://www.piskelapp.com/).

## Cómo abrir en Piskel:
1. Entra a **https://www.piskelapp.com/p/create/sprite** en tu navegador.
2. Haz clic en el icono de carpeta de la barra derecha (**Import**).
3. Elige cualquiera de estas opciones:
   - **Import .piskel file**: selecciona el archivo `.piskel` de cualquier animación.
   - **Import animated GIF**: selecciona el archivo `.gif` (Piskel importa todos los fotogramas y la velocidad al instante).
   - **Import from picture**: selecciona el `_sheet.png` (pon el Frame size que se indica abajo).

## Volver al juego:
`python herramientas/importar_piskel.py editado.piskel --manifiesto piskel_animaciones/kale_1/origen.json --heroe kale --forma 1 --anim attack --aplicar`
Después: `python herramientas/montar_animaciones.py kale` y revisión visual. Solo se aceptan sprites originales exportados.

## Animaciones disponibles:

| Animación | Fotogramas | Tamaño de celda | Archivo .piskel | GIF animado | Hoja Strip |
|---|---|---|---|---|---|
| **Idle** | 2 | 76x76 | [`kale_Idle.piskel`](Idle/kale_Idle.piskel) | [`kale_Idle.gif`](Idle/kale_Idle.gif) | [`kale_Idle_sheet.png`](Idle/kale_Idle_sheet.png) |
| **Walk** | 1 | 108x108 | [`kale_Walk.piskel`](Walk/kale_Walk.piskel) | [`kale_Walk.gif`](Walk/kale_Walk.gif) | [`kale_Walk_sheet.png`](Walk/kale_Walk_sheet.png) |
| **Attack** | 3 | 80x80 | [`kale_Attack.piskel`](Attack/kale_Attack.piskel) | [`kale_Attack.gif`](Attack/kale_Attack.gif) | [`kale_Attack_sheet.png`](Attack/kale_Attack_sheet.png) |
| **Kick** | 2 | 68x68 | [`kale_Kick.piskel`](Kick/kale_Kick.piskel) | [`kale_Kick.gif`](Kick/kale_Kick.gif) | [`kale_Kick_sheet.png`](Kick/kale_Kick_sheet.png) |
| **Cast** | 2 | 76x76 | [`kale_Cast.piskel`](Cast/kale_Cast.piskel) | [`kale_Cast.gif`](Cast/kale_Cast.gif) | [`kale_Cast_sheet.png`](Cast/kale_Cast_sheet.png) |
| **Pow** | 3 | 148x148 | [`kale_Pow.piskel`](Pow/kale_Pow.piskel) | [`kale_Pow.gif`](Pow/kale_Pow.gif) | [`kale_Pow_sheet.png`](Pow/kale_Pow_sheet.png) |
| **Hurt** | 2 | 80x80 | [`kale_Hurt.piskel`](Hurt/kale_Hurt.piskel) | [`kale_Hurt.gif`](Hurt/kale_Hurt.gif) | [`kale_Hurt_sheet.png`](Hurt/kale_Hurt_sheet.png) |
| **Faint** | 1 | 84x84 | [`kale_Faint.piskel`](Faint/kale_Faint.piskel) | [`kale_Faint.gif`](Faint/kale_Faint.gif) | [`kale_Faint_sheet.png`](Faint/kale_Faint_sheet.png) |
| **Attack2** | 2 | 68x68 | [`kale_Attack2.piskel`](Attack2/kale_Attack2.piskel) | [`kale_Attack2.gif`](Attack2/kale_Attack2.gif) | [`kale_Attack2_sheet.png`](Attack2/kale_Attack2_sheet.png) |
| **Attack3** | 2 | 84x84 | [`kale_Attack3.piskel`](Attack3/kale_Attack3.piskel) | [`kale_Attack3.gif`](Attack3/kale_Attack3.gif) | [`kale_Attack3_sheet.png`](Attack3/kale_Attack3_sheet.png) |
| **Kick2** | 2 | 76x76 | [`kale_Kick2.piskel`](Kick2/kale_Kick2.piskel) | [`kale_Kick2.gif`](Kick2/kale_Kick2.gif) | [`kale_Kick2_sheet.png`](Kick2/kale_Kick2_sheet.png) |
| **Beam** | 2 | 76x76 | [`kale_Beam.piskel`](Beam/kale_Beam.piskel) | [`kale_Beam.gif`](Beam/kale_Beam.gif) | [`kale_Beam_sheet.png`](Beam/kale_Beam_sheet.png) |
| **Up** | 1 | 68x68 | [`kale_Up.piskel`](Up/kale_Up.piskel) | [`kale_Up.gif`](Up/kale_Up.gif) | [`kale_Up_sheet.png`](Up/kale_Up_sheet.png) |