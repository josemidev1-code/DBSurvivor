# Animaciones para Piskel — BLACKMAJIN (Forma 0)

Esta carpeta contiene las animaciones listas para abrir y editar en **Piskel** (https://www.piskelapp.com/).

## Cómo abrir en Piskel:
1. Entra a **https://www.piskelapp.com/p/create/sprite** en tu navegador.
2. Haz clic en el icono de carpeta de la barra derecha (**Import**).
3. Elige cualquiera de estas opciones:
   - **Import .piskel file**: selecciona el archivo `.piskel` de cualquier animación.
   - **Import animated GIF**: selecciona el archivo `.gif` (Piskel importa todos los fotogramas y la velocidad al instante).
   - **Import from picture**: selecciona el `_sheet.png` (pon el Frame size que se indica abajo).

## Volver al juego:
`python herramientas/importar_piskel.py editado.piskel --manifiesto piskel_animaciones/blackmajin_0/origen.json --heroe blackmajin --forma 0 --anim attack --aplicar`
Después: `python herramientas/montar_animaciones.py blackmajin` y revisión visual. Solo se aceptan sprites originales exportados.

## Animaciones disponibles:

| Animación | Fotogramas | Tamaño de celda | Archivo .piskel | GIF animado | Hoja Strip |
|---|---|---|---|---|---|
| **Idle** | 2 | 56x56 | [`blackmajin_Idle.piskel`](Idle/blackmajin_Idle.piskel) | [`blackmajin_Idle.gif`](Idle/blackmajin_Idle.gif) | [`blackmajin_Idle_sheet.png`](Idle/blackmajin_Idle_sheet.png) |
| **Walk** | 1 | 64x64 | [`blackmajin_Walk.piskel`](Walk/blackmajin_Walk.piskel) | [`blackmajin_Walk.gif`](Walk/blackmajin_Walk.gif) | [`blackmajin_Walk_sheet.png`](Walk/blackmajin_Walk_sheet.png) |
| **Attack** | 3 | 56x56 | [`blackmajin_Attack.piskel`](Attack/blackmajin_Attack.piskel) | [`blackmajin_Attack.gif`](Attack/blackmajin_Attack.gif) | [`blackmajin_Attack_sheet.png`](Attack/blackmajin_Attack_sheet.png) |
| **Kick** | 2 | 50x50 | [`blackmajin_Kick.piskel`](Kick/blackmajin_Kick.piskel) | [`blackmajin_Kick.gif`](Kick/blackmajin_Kick.gif) | [`blackmajin_Kick_sheet.png`](Kick/blackmajin_Kick_sheet.png) |
| **Cast** | 2 | 58x58 | [`blackmajin_Cast.piskel`](Cast/blackmajin_Cast.piskel) | [`blackmajin_Cast.gif`](Cast/blackmajin_Cast.gif) | [`blackmajin_Cast_sheet.png`](Cast/blackmajin_Cast_sheet.png) |
| **Pow** | 2 | 66x66 | [`blackmajin_Pow.piskel`](Pow/blackmajin_Pow.piskel) | [`blackmajin_Pow.gif`](Pow/blackmajin_Pow.gif) | [`blackmajin_Pow_sheet.png`](Pow/blackmajin_Pow_sheet.png) |
| **Hurt** | 2 | 54x54 | [`blackmajin_Hurt.piskel`](Hurt/blackmajin_Hurt.piskel) | [`blackmajin_Hurt.gif`](Hurt/blackmajin_Hurt.gif) | [`blackmajin_Hurt_sheet.png`](Hurt/blackmajin_Hurt_sheet.png) |
| **Attack2** | 2 | 50x50 | [`blackmajin_Attack2.piskel`](Attack2/blackmajin_Attack2.piskel) | [`blackmajin_Attack2.gif`](Attack2/blackmajin_Attack2.gif) | [`blackmajin_Attack2_sheet.png`](Attack2/blackmajin_Attack2_sheet.png) |