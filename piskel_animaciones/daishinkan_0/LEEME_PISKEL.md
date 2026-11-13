# Animaciones para Piskel — DAISHINKAN (Forma 0)

Esta carpeta contiene las animaciones listas para abrir y editar en **Piskel** (https://www.piskelapp.com/).

## Cómo abrir en Piskel:
1. Entra a **https://www.piskelapp.com/p/create/sprite** en tu navegador.
2. Haz clic en el icono de carpeta de la barra derecha (**Import**).
3. Elige cualquiera de estas opciones:
   - **Import .piskel file**: selecciona el archivo `.piskel` de cualquier animación.
   - **Import animated GIF**: selecciona el archivo `.gif` (Piskel importa todos los fotogramas y la velocidad al instante).
   - **Import from picture**: selecciona el `_sheet.png` (pon el Frame size que se indica abajo).

## Volver al juego:
`python herramientas/importar_piskel.py editado.piskel --manifiesto piskel_animaciones/daishinkan_0/origen.json --heroe daishinkan --forma 0 --anim attack --aplicar`
Después: `python herramientas/montar_animaciones.py daishinkan` y revisión visual. Solo se aceptan sprites originales exportados.

## Animaciones disponibles:

| Animación | Fotogramas | Tamaño de celda | Archivo .piskel | GIF animado | Hoja Strip |
|---|---|---|---|---|---|
| **Idle** | 2 | 52x52 | [`daishinkan_Idle.piskel`](Idle/daishinkan_Idle.piskel) | [`daishinkan_Idle.gif`](Idle/daishinkan_Idle.gif) | [`daishinkan_Idle_sheet.png`](Idle/daishinkan_Idle_sheet.png) |
| **Walk** | 1 | 44x44 | [`daishinkan_Walk.piskel`](Walk/daishinkan_Walk.piskel) | [`daishinkan_Walk.gif`](Walk/daishinkan_Walk.gif) | [`daishinkan_Walk_sheet.png`](Walk/daishinkan_Walk_sheet.png) |
| **Attack** | 3 | 54x54 | [`daishinkan_Attack.piskel`](Attack/daishinkan_Attack.piskel) | [`daishinkan_Attack.gif`](Attack/daishinkan_Attack.gif) | [`daishinkan_Attack_sheet.png`](Attack/daishinkan_Attack_sheet.png) |
| **Kick** | 2 | 46x46 | [`daishinkan_Kick.piskel`](Kick/daishinkan_Kick.piskel) | [`daishinkan_Kick.gif`](Kick/daishinkan_Kick.gif) | [`daishinkan_Kick_sheet.png`](Kick/daishinkan_Kick_sheet.png) |
| **Cast** | 2 | 54x54 | [`daishinkan_Cast.piskel`](Cast/daishinkan_Cast.piskel) | [`daishinkan_Cast.gif`](Cast/daishinkan_Cast.gif) | [`daishinkan_Cast_sheet.png`](Cast/daishinkan_Cast_sheet.png) |
| **Pow** | 2 | 74x74 | [`daishinkan_Pow.piskel`](Pow/daishinkan_Pow.piskel) | [`daishinkan_Pow.gif`](Pow/daishinkan_Pow.gif) | [`daishinkan_Pow_sheet.png`](Pow/daishinkan_Pow_sheet.png) |
| **Hurt** | 2 | 54x54 | [`daishinkan_Hurt.piskel`](Hurt/daishinkan_Hurt.piskel) | [`daishinkan_Hurt.gif`](Hurt/daishinkan_Hurt.gif) | [`daishinkan_Hurt_sheet.png`](Hurt/daishinkan_Hurt_sheet.png) |
| **Faint** | 1 | 60x60 | [`daishinkan_Faint.piskel`](Faint/daishinkan_Faint.piskel) | [`daishinkan_Faint.gif`](Faint/daishinkan_Faint.gif) | [`daishinkan_Faint_sheet.png`](Faint/daishinkan_Faint_sheet.png) |
| **Attack2** | 2 | 54x54 | [`daishinkan_Attack2.piskel`](Attack2/daishinkan_Attack2.piskel) | [`daishinkan_Attack2.gif`](Attack2/daishinkan_Attack2.gif) | [`daishinkan_Attack2_sheet.png`](Attack2/daishinkan_Attack2_sheet.png) |
| **Kick2** | 2 | 46x46 | [`daishinkan_Kick2.piskel`](Kick2/daishinkan_Kick2.piskel) | [`daishinkan_Kick2.gif`](Kick2/daishinkan_Kick2.gif) | [`daishinkan_Kick2_sheet.png`](Kick2/daishinkan_Kick2_sheet.png) |
| **Beam** | 2 | 54x54 | [`daishinkan_Beam.piskel`](Beam/daishinkan_Beam.piskel) | [`daishinkan_Beam.gif`](Beam/daishinkan_Beam.gif) | [`daishinkan_Beam_sheet.png`](Beam/daishinkan_Beam_sheet.png) |