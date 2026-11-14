# Animaciones para Piskel — GOKUREYMONO (Forma 0)

Esta carpeta contiene las animaciones listas para abrir y editar en **Piskel** (https://www.piskelapp.com/).

## Cómo abrir en Piskel:
1. Entra a **https://www.piskelapp.com/p/create/sprite** en tu navegador.
2. Haz clic en el icono de carpeta de la barra derecha (**Import**).
3. Elige cualquiera de estas opciones:
   - **Import .piskel file**: selecciona el archivo `.piskel` de cualquier animación.
   - **Import animated GIF**: selecciona el archivo `.gif` (Piskel importa todos los fotogramas y la velocidad al instante).
   - **Import from picture**: selecciona el `_sheet.png` (pon el Frame size que se indica abajo).

## Volver al juego:
`python herramientas/importar_piskel.py editado.piskel --manifiesto piskel_animaciones/gokureymono_0/origen.json --heroe gokureymono --forma 0 --anim attack --aplicar`
Después: `python herramientas/montar_animaciones.py gokureymono` y revisión visual. Solo se aceptan sprites originales exportados.

## Animaciones disponibles:

| Animación | Fotogramas | Tamaño de celda | Archivo .piskel | GIF animado | Hoja Strip |
|---|---|---|---|---|---|
| **Idle** | 2 | 58x58 | [`gokureymono_Idle.piskel`](Idle/gokureymono_Idle.piskel) | [`gokureymono_Idle.gif`](Idle/gokureymono_Idle.gif) | [`gokureymono_Idle_sheet.png`](Idle/gokureymono_Idle_sheet.png) |
| **Walk** | 1 | 50x50 | [`gokureymono_Walk.piskel`](Walk/gokureymono_Walk.piskel) | [`gokureymono_Walk.gif`](Walk/gokureymono_Walk.gif) | [`gokureymono_Walk_sheet.png`](Walk/gokureymono_Walk_sheet.png) |
| **Attack** | 3 | 60x60 | [`gokureymono_Attack.piskel`](Attack/gokureymono_Attack.piskel) | [`gokureymono_Attack.gif`](Attack/gokureymono_Attack.gif) | [`gokureymono_Attack_sheet.png`](Attack/gokureymono_Attack_sheet.png) |
| **Kick** | 2 | 62x62 | [`gokureymono_Kick.piskel`](Kick/gokureymono_Kick.piskel) | [`gokureymono_Kick.gif`](Kick/gokureymono_Kick.gif) | [`gokureymono_Kick_sheet.png`](Kick/gokureymono_Kick_sheet.png) |
| **Cast** | 2 | 60x60 | [`gokureymono_Cast.piskel`](Cast/gokureymono_Cast.piskel) | [`gokureymono_Cast.gif`](Cast/gokureymono_Cast.gif) | [`gokureymono_Cast_sheet.png`](Cast/gokureymono_Cast_sheet.png) |
| **Pow** | 2 | 104x104 | [`gokureymono_Pow.piskel`](Pow/gokureymono_Pow.piskel) | [`gokureymono_Pow.gif`](Pow/gokureymono_Pow.gif) | [`gokureymono_Pow_sheet.png`](Pow/gokureymono_Pow_sheet.png) |
| **Hurt** | 2 | 64x64 | [`gokureymono_Hurt.piskel`](Hurt/gokureymono_Hurt.piskel) | [`gokureymono_Hurt.gif`](Hurt/gokureymono_Hurt.gif) | [`gokureymono_Hurt_sheet.png`](Hurt/gokureymono_Hurt_sheet.png) |
| **Faint** | 1 | 82x82 | [`gokureymono_Faint.piskel`](Faint/gokureymono_Faint.piskel) | [`gokureymono_Faint.gif`](Faint/gokureymono_Faint.gif) | [`gokureymono_Faint_sheet.png`](Faint/gokureymono_Faint_sheet.png) |
| **Attack2** | 3 | 50x50 | [`gokureymono_Attack2.piskel`](Attack2/gokureymono_Attack2.piskel) | [`gokureymono_Attack2.gif`](Attack2/gokureymono_Attack2.gif) | [`gokureymono_Attack2_sheet.png`](Attack2/gokureymono_Attack2_sheet.png) |