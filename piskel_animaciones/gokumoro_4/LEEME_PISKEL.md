# Animaciones para Piskel — GOKUMORO (Forma 4)

Esta carpeta contiene las animaciones listas para abrir y editar en **Piskel** (https://www.piskelapp.com/).

## Cómo abrir en Piskel:
1. Entra a **https://www.piskelapp.com/p/create/sprite** en tu navegador.
2. Haz clic en el icono de carpeta de la barra derecha (**Import**).
3. Elige cualquiera de estas opciones:
   - **Import .piskel file**: selecciona el archivo `.piskel` de cualquier animación.
   - **Import animated GIF**: selecciona el archivo `.gif` (Piskel importa todos los fotogramas y la velocidad al instante).
   - **Import from picture**: selecciona el `_sheet.png` (pon el Frame size que se indica abajo).

## Volver al juego:
`python herramientas/importar_piskel.py editado.piskel --manifiesto piskel_animaciones/gokumoro_4/origen.json --heroe gokumoro --forma 4 --anim attack --aplicar`
Después: `python herramientas/montar_animaciones.py gokumoro` y revisión visual. Solo se aceptan sprites originales exportados.

## Animaciones disponibles:

| Animación | Fotogramas | Tamaño de celda | Archivo .piskel | GIF animado | Hoja Strip |
|---|---|---|---|---|---|
| **Idle** | 2 | 54x54 | [`gokumoro_Idle.piskel`](Idle/gokumoro_Idle.piskel) | [`gokumoro_Idle.gif`](Idle/gokumoro_Idle.gif) | [`gokumoro_Idle_sheet.png`](Idle/gokumoro_Idle_sheet.png) |
| **Walk** | 1 | 46x46 | [`gokumoro_Walk.piskel`](Walk/gokumoro_Walk.piskel) | [`gokumoro_Walk.gif`](Walk/gokumoro_Walk.gif) | [`gokumoro_Walk_sheet.png`](Walk/gokumoro_Walk_sheet.png) |
| **Attack** | 2 | 50x50 | [`gokumoro_Attack.piskel`](Attack/gokumoro_Attack.piskel) | [`gokumoro_Attack.gif`](Attack/gokumoro_Attack.gif) | [`gokumoro_Attack_sheet.png`](Attack/gokumoro_Attack_sheet.png) |
| **Kick** | 2 | 54x54 | [`gokumoro_Kick.piskel`](Kick/gokumoro_Kick.piskel) | [`gokumoro_Kick.gif`](Kick/gokumoro_Kick.gif) | [`gokumoro_Kick_sheet.png`](Kick/gokumoro_Kick_sheet.png) |
| **Cast** | 2 | 62x62 | [`gokumoro_Cast.piskel`](Cast/gokumoro_Cast.piskel) | [`gokumoro_Cast.gif`](Cast/gokumoro_Cast.gif) | [`gokumoro_Cast_sheet.png`](Cast/gokumoro_Cast_sheet.png) |
| **Pow** | 2 | 62x62 | [`gokumoro_Pow.piskel`](Pow/gokumoro_Pow.piskel) | [`gokumoro_Pow.gif`](Pow/gokumoro_Pow.gif) | [`gokumoro_Pow_sheet.png`](Pow/gokumoro_Pow_sheet.png) |
| **Hurt** | 2 | 54x54 | [`gokumoro_Hurt.piskel`](Hurt/gokumoro_Hurt.piskel) | [`gokumoro_Hurt.gif`](Hurt/gokumoro_Hurt.gif) | [`gokumoro_Hurt_sheet.png`](Hurt/gokumoro_Hurt_sheet.png) |