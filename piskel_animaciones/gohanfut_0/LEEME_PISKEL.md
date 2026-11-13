# Animaciones para Piskel — GOHANFUT (Forma 0)

Esta carpeta contiene las animaciones listas para abrir y editar en **Piskel** (https://www.piskelapp.com/).

## Cómo abrir en Piskel:
1. Entra a **https://www.piskelapp.com/p/create/sprite** en tu navegador.
2. Haz clic en el icono de carpeta de la barra derecha (**Import**).
3. Elige cualquiera de estas opciones:
   - **Import .piskel file**: selecciona el archivo `.piskel` de cualquier animación.
   - **Import animated GIF**: selecciona el archivo `.gif` (Piskel importa todos los fotogramas y la velocidad al instante).
   - **Import from picture**: selecciona el `_sheet.png` (pon el Frame size que se indica abajo).

## Volver al juego:
`python herramientas/importar_piskel.py editado.piskel --manifiesto piskel_animaciones/gohanfut_0/origen.json --heroe gohanfut --forma 0 --anim attack --aplicar`
Después: `python herramientas/montar_animaciones.py gohanfut` y revisión visual. Solo se aceptan sprites originales exportados.

## Animaciones disponibles:

| Animación | Fotogramas | Tamaño de celda | Archivo .piskel | GIF animado | Hoja Strip |
|---|---|---|---|---|---|
| **Idle** | 3 | 52x52 | [`gohanfut_Idle.piskel`](Idle/gohanfut_Idle.piskel) | [`gohanfut_Idle.gif`](Idle/gohanfut_Idle.gif) | [`gohanfut_Idle_sheet.png`](Idle/gohanfut_Idle_sheet.png) |
| **Walk** | 1 | 48x48 | [`gohanfut_Walk.piskel`](Walk/gohanfut_Walk.piskel) | [`gohanfut_Walk.gif`](Walk/gohanfut_Walk.gif) | [`gohanfut_Walk_sheet.png`](Walk/gohanfut_Walk_sheet.png) |
| **Attack** | 3 | 48x48 | [`gohanfut_Attack.piskel`](Attack/gohanfut_Attack.piskel) | [`gohanfut_Attack.gif`](Attack/gohanfut_Attack.gif) | [`gohanfut_Attack_sheet.png`](Attack/gohanfut_Attack_sheet.png) |
| **Kick** | 2 | 46x46 | [`gohanfut_Kick.piskel`](Kick/gohanfut_Kick.piskel) | [`gohanfut_Kick.gif`](Kick/gohanfut_Kick.gif) | [`gohanfut_Kick_sheet.png`](Kick/gohanfut_Kick_sheet.png) |
| **Cast** | 3 | 52x52 | [`gohanfut_Cast.piskel`](Cast/gohanfut_Cast.piskel) | [`gohanfut_Cast.gif`](Cast/gohanfut_Cast.gif) | [`gohanfut_Cast_sheet.png`](Cast/gohanfut_Cast_sheet.png) |
| **Pow** | 2 | 82x82 | [`gohanfut_Pow.piskel`](Pow/gohanfut_Pow.piskel) | [`gohanfut_Pow.gif`](Pow/gohanfut_Pow.gif) | [`gohanfut_Pow_sheet.png`](Pow/gohanfut_Pow_sheet.png) |
| **Hurt** | 2 | 52x52 | [`gohanfut_Hurt.piskel`](Hurt/gohanfut_Hurt.piskel) | [`gohanfut_Hurt.gif`](Hurt/gohanfut_Hurt.gif) | [`gohanfut_Hurt_sheet.png`](Hurt/gohanfut_Hurt_sheet.png) |
| **Faint** | 1 | 56x56 | [`gohanfut_Faint.piskel`](Faint/gohanfut_Faint.piskel) | [`gohanfut_Faint.gif`](Faint/gohanfut_Faint.gif) | [`gohanfut_Faint_sheet.png`](Faint/gohanfut_Faint_sheet.png) |
| **Kick2** | 3 | 46x46 | [`gohanfut_Kick2.piskel`](Kick2/gohanfut_Kick2.piskel) | [`gohanfut_Kick2.gif`](Kick2/gohanfut_Kick2.gif) | [`gohanfut_Kick2_sheet.png`](Kick2/gohanfut_Kick2_sheet.png) |
| **Beam** | 2 | 48x48 | [`gohanfut_Beam.piskel`](Beam/gohanfut_Beam.piskel) | [`gohanfut_Beam.gif`](Beam/gohanfut_Beam.gif) | [`gohanfut_Beam_sheet.png`](Beam/gohanfut_Beam_sheet.png) |