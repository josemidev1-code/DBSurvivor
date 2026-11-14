# Animaciones para Piskel — BLACKROSEN (Forma 0)

Esta carpeta contiene las animaciones listas para abrir y editar en **Piskel** (https://www.piskelapp.com/).

## Cómo abrir en Piskel:
1. Entra a **https://www.piskelapp.com/p/create/sprite** en tu navegador.
2. Haz clic en el icono de carpeta de la barra derecha (**Import**).
3. Elige cualquiera de estas opciones:
   - **Import .piskel file**: selecciona el archivo `.piskel` de cualquier animación.
   - **Import animated GIF**: selecciona el archivo `.gif` (Piskel importa todos los fotogramas y la velocidad al instante).
   - **Import from picture**: selecciona el `_sheet.png` (pon el Frame size que se indica abajo).

## Volver al juego:
`python herramientas/importar_piskel.py editado.piskel --manifiesto piskel_animaciones/blackrosen_0/origen.json --heroe blackrosen --forma 0 --anim attack --aplicar`
Después: `python herramientas/montar_animaciones.py blackrosen` y revisión visual. Solo se aceptan sprites originales exportados.

## Animaciones disponibles:

| Animación | Fotogramas | Tamaño de celda | Archivo .piskel | GIF animado | Hoja Strip |
|---|---|---|---|---|---|
| **Idle** | 2 | 54x54 | [`blackrosen_Idle.piskel`](Idle/blackrosen_Idle.piskel) | [`blackrosen_Idle.gif`](Idle/blackrosen_Idle.gif) | [`blackrosen_Idle_sheet.png`](Idle/blackrosen_Idle_sheet.png) |
| **Walk** | 1 | 60x60 | [`blackrosen_Walk.piskel`](Walk/blackrosen_Walk.piskel) | [`blackrosen_Walk.gif`](Walk/blackrosen_Walk.gif) | [`blackrosen_Walk_sheet.png`](Walk/blackrosen_Walk_sheet.png) |
| **Attack** | 3 | 54x54 | [`blackrosen_Attack.piskel`](Attack/blackrosen_Attack.piskel) | [`blackrosen_Attack.gif`](Attack/blackrosen_Attack.gif) | [`blackrosen_Attack_sheet.png`](Attack/blackrosen_Attack_sheet.png) |
| **Kick** | 2 | 52x52 | [`blackrosen_Kick.piskel`](Kick/blackrosen_Kick.piskel) | [`blackrosen_Kick.gif`](Kick/blackrosen_Kick.gif) | [`blackrosen_Kick_sheet.png`](Kick/blackrosen_Kick_sheet.png) |
| **Cast** | 2 | 68x68 | [`blackrosen_Cast.piskel`](Cast/blackrosen_Cast.piskel) | [`blackrosen_Cast.gif`](Cast/blackrosen_Cast.gif) | [`blackrosen_Cast_sheet.png`](Cast/blackrosen_Cast_sheet.png) |
| **Pow** | 2 | 50x50 | [`blackrosen_Pow.piskel`](Pow/blackrosen_Pow.piskel) | [`blackrosen_Pow.gif`](Pow/blackrosen_Pow.gif) | [`blackrosen_Pow_sheet.png`](Pow/blackrosen_Pow_sheet.png) |
| **Hurt** | 2 | 60x60 | [`blackrosen_Hurt.piskel`](Hurt/blackrosen_Hurt.piskel) | [`blackrosen_Hurt.gif`](Hurt/blackrosen_Hurt.gif) | [`blackrosen_Hurt_sheet.png`](Hurt/blackrosen_Hurt_sheet.png) |
| **Attack2** | 2 | 52x52 | [`blackrosen_Attack2.piskel`](Attack2/blackrosen_Attack2.piskel) | [`blackrosen_Attack2.gif`](Attack2/blackrosen_Attack2.gif) | [`blackrosen_Attack2_sheet.png`](Attack2/blackrosen_Attack2_sheet.png) |