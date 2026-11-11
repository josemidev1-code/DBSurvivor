# Animaciones para Piskel — MAJINKUU (Forma 0)

Esta carpeta contiene las animaciones listas para abrir y editar en **Piskel** (https://www.piskelapp.com/).

## Cómo abrir en Piskel:
1. Entra a **https://www.piskelapp.com/p/create/sprite** en tu navegador.
2. Haz clic en el icono de carpeta de la barra derecha (**Import**).
3. Elige cualquiera de estas opciones:
   - **Import .piskel file**: selecciona el archivo `.piskel` de cualquier animación.
   - **Import animated GIF**: selecciona el archivo `.gif` (Piskel importa todos los fotogramas y la velocidad al instante).
   - **Import from picture**: selecciona el `_sheet.png` (pon el Frame size que se indica abajo).

## Volver al juego:
`python herramientas/importar_piskel.py editado.piskel --manifiesto piskel_animaciones/majinkuu_0/origen.json --heroe majinkuu --forma 0 --anim attack --aplicar`
Después: `python herramientas/montar_animaciones.py majinkuu` y revisión visual. Solo se aceptan sprites originales exportados.

## Animaciones disponibles:

| Animación | Fotogramas | Tamaño de celda | Archivo .piskel | GIF animado | Hoja Strip |
|---|---|---|---|---|---|
| **Idle** | 2 | 52x52 | [`majinkuu_Idle.piskel`](Idle/majinkuu_Idle.piskel) | [`majinkuu_Idle.gif`](Idle/majinkuu_Idle.gif) | [`majinkuu_Idle_sheet.png`](Idle/majinkuu_Idle_sheet.png) |
| **Walk** | 1 | 52x52 | [`majinkuu_Walk.piskel`](Walk/majinkuu_Walk.piskel) | [`majinkuu_Walk.gif`](Walk/majinkuu_Walk.gif) | [`majinkuu_Walk_sheet.png`](Walk/majinkuu_Walk_sheet.png) |
| **Attack** | 3 | 50x50 | [`majinkuu_Attack.piskel`](Attack/majinkuu_Attack.piskel) | [`majinkuu_Attack.gif`](Attack/majinkuu_Attack.gif) | [`majinkuu_Attack_sheet.png`](Attack/majinkuu_Attack_sheet.png) |
| **Kick** | 2 | 60x60 | [`majinkuu_Kick.piskel`](Kick/majinkuu_Kick.piskel) | [`majinkuu_Kick.gif`](Kick/majinkuu_Kick.gif) | [`majinkuu_Kick_sheet.png`](Kick/majinkuu_Kick_sheet.png) |
| **Cast** | 2 | 66x66 | [`majinkuu_Cast.piskel`](Cast/majinkuu_Cast.piskel) | [`majinkuu_Cast.gif`](Cast/majinkuu_Cast.gif) | [`majinkuu_Cast_sheet.png`](Cast/majinkuu_Cast_sheet.png) |
| **Pow** | 2 | 94x94 | [`majinkuu_Pow.piskel`](Pow/majinkuu_Pow.piskel) | [`majinkuu_Pow.gif`](Pow/majinkuu_Pow.gif) | [`majinkuu_Pow_sheet.png`](Pow/majinkuu_Pow_sheet.png) |
| **Hurt** | 2 | 50x50 | [`majinkuu_Hurt.piskel`](Hurt/majinkuu_Hurt.piskel) | [`majinkuu_Hurt.gif`](Hurt/majinkuu_Hurt.gif) | [`majinkuu_Hurt_sheet.png`](Hurt/majinkuu_Hurt_sheet.png) |
| **Attack2** | 2 | 50x50 | [`majinkuu_Attack2.piskel`](Attack2/majinkuu_Attack2.piskel) | [`majinkuu_Attack2.gif`](Attack2/majinkuu_Attack2.gif) | [`majinkuu_Attack2_sheet.png`](Attack2/majinkuu_Attack2_sheet.png) |
| **Attack3** | 2 | 50x50 | [`majinkuu_Attack3.piskel`](Attack3/majinkuu_Attack3.piskel) | [`majinkuu_Attack3.gif`](Attack3/majinkuu_Attack3.gif) | [`majinkuu_Attack3_sheet.png`](Attack3/majinkuu_Attack3_sheet.png) |
| **Kick2** | 2 | 50x50 | [`majinkuu_Kick2.piskel`](Kick2/majinkuu_Kick2.piskel) | [`majinkuu_Kick2.gif`](Kick2/majinkuu_Kick2.gif) | [`majinkuu_Kick2_sheet.png`](Kick2/majinkuu_Kick2_sheet.png) |
| **Beam** | 2 | 66x66 | [`majinkuu_Beam.piskel`](Beam/majinkuu_Beam.piskel) | [`majinkuu_Beam.gif`](Beam/majinkuu_Beam.gif) | [`majinkuu_Beam_sheet.png`](Beam/majinkuu_Beam_sheet.png) |