# Animaciones para Piskel — MAGETTA (Forma 0)

Esta carpeta contiene las animaciones listas para abrir y editar en **Piskel** (https://www.piskelapp.com/).

## Cómo abrir en Piskel:
1. Entra a **https://www.piskelapp.com/p/create/sprite** en tu navegador.
2. Haz clic en el icono de carpeta de la barra derecha (**Import**).
3. Elige cualquiera de estas opciones:
   - **Import .piskel file**: selecciona el archivo `.piskel` de cualquier animación.
   - **Import animated GIF**: selecciona el archivo `.gif` (Piskel importa todos los fotogramas y la velocidad al instante).
   - **Import from picture**: selecciona el `_sheet.png` (pon el Frame size que se indica abajo).

## Volver al juego:
`python herramientas/importar_piskel.py editado.piskel --manifiesto piskel_animaciones/magetta_0/origen.json --heroe magetta --forma 0 --anim attack --aplicar`
Después: `python herramientas/montar_animaciones.py magetta` y revisión visual. Solo se aceptan sprites originales exportados.

## Animaciones disponibles:

| Animación | Fotogramas | Tamaño de celda | Archivo .piskel | GIF animado | Hoja Strip |
|---|---|---|---|---|---|
| **Idle** | 2 | 52x52 | [`magetta_Idle.piskel`](Idle/magetta_Idle.piskel) | [`magetta_Idle.gif`](Idle/magetta_Idle.gif) | [`magetta_Idle_sheet.png`](Idle/magetta_Idle_sheet.png) |
| **Walk** | 1 | 54x54 | [`magetta_Walk.piskel`](Walk/magetta_Walk.piskel) | [`magetta_Walk.gif`](Walk/magetta_Walk.gif) | [`magetta_Walk_sheet.png`](Walk/magetta_Walk_sheet.png) |
| **Attack** | 3 | 62x62 | [`magetta_Attack.piskel`](Attack/magetta_Attack.piskel) | [`magetta_Attack.gif`](Attack/magetta_Attack.gif) | [`magetta_Attack_sheet.png`](Attack/magetta_Attack_sheet.png) |
| **Kick** | 2 | 62x62 | [`magetta_Kick.piskel`](Kick/magetta_Kick.piskel) | [`magetta_Kick.gif`](Kick/magetta_Kick.gif) | [`magetta_Kick_sheet.png`](Kick/magetta_Kick_sheet.png) |
| **Cast** | 2 | 64x64 | [`magetta_Cast.piskel`](Cast/magetta_Cast.piskel) | [`magetta_Cast.gif`](Cast/magetta_Cast.gif) | [`magetta_Cast_sheet.png`](Cast/magetta_Cast_sheet.png) |
| **Pow** | 2 | 64x64 | [`magetta_Pow.piskel`](Pow/magetta_Pow.piskel) | [`magetta_Pow.gif`](Pow/magetta_Pow.gif) | [`magetta_Pow_sheet.png`](Pow/magetta_Pow_sheet.png) |
| **Hurt** | 2 | 52x52 | [`magetta_Hurt.piskel`](Hurt/magetta_Hurt.piskel) | [`magetta_Hurt.gif`](Hurt/magetta_Hurt.gif) | [`magetta_Hurt_sheet.png`](Hurt/magetta_Hurt_sheet.png) |
| **Attack2** | 2 | 58x58 | [`magetta_Attack2.piskel`](Attack2/magetta_Attack2.piskel) | [`magetta_Attack2.gif`](Attack2/magetta_Attack2.gif) | [`magetta_Attack2_sheet.png`](Attack2/magetta_Attack2_sheet.png) |
| **Attack3** | 2 | 56x56 | [`magetta_Attack3.piskel`](Attack3/magetta_Attack3.piskel) | [`magetta_Attack3.gif`](Attack3/magetta_Attack3.gif) | [`magetta_Attack3_sheet.png`](Attack3/magetta_Attack3_sheet.png) |
| **Kick2** | 2 | 54x54 | [`magetta_Kick2.piskel`](Kick2/magetta_Kick2.piskel) | [`magetta_Kick2.gif`](Kick2/magetta_Kick2.gif) | [`magetta_Kick2_sheet.png`](Kick2/magetta_Kick2_sheet.png) |
| **Beam** | 2 | 54x54 | [`magetta_Beam.piskel`](Beam/magetta_Beam.piskel) | [`magetta_Beam.gif`](Beam/magetta_Beam.gif) | [`magetta_Beam_sheet.png`](Beam/magetta_Beam_sheet.png) |
| **Up** | 1 | 56x56 | [`magetta_Up.piskel`](Up/magetta_Up.piskel) | [`magetta_Up.gif`](Up/magetta_Up.gif) | [`magetta_Up_sheet.png`](Up/magetta_Up_sheet.png) |