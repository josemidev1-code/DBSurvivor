# Animaciones para Piskel — GOMAH (Forma 0)

Esta carpeta contiene las animaciones listas para abrir y editar en **Piskel** (https://www.piskelapp.com/).

## Cómo abrir en Piskel:
1. Entra a **https://www.piskelapp.com/p/create/sprite** en tu navegador.
2. Haz clic en el icono de carpeta de la barra derecha (**Import**).
3. Elige cualquiera de estas opciones:
   - **Import .piskel file**: selecciona el archivo `.piskel` de cualquier animación.
   - **Import animated GIF**: selecciona el archivo `.gif` (Piskel importa todos los fotogramas y la velocidad al instante).
   - **Import from picture**: selecciona el `_sheet.png` (pon el Frame size que se indica abajo).

## Volver al juego:
`python herramientas/importar_piskel.py editado.piskel --manifiesto piskel_animaciones/gomah_0/origen.json --heroe gomah --forma 0 --anim attack --aplicar`
Después: `python herramientas/montar_animaciones.py gomah` y revisión visual. Solo se aceptan sprites originales exportados.

## Animaciones disponibles:

| Animación | Fotogramas | Tamaño de celda | Archivo .piskel | GIF animado | Hoja Strip |
|---|---|---|---|---|---|
| **Idle** | 3 | 56x56 | [`gomah_Idle.piskel`](Idle/gomah_Idle.piskel) | [`gomah_Idle.gif`](Idle/gomah_Idle.gif) | [`gomah_Idle_sheet.png`](Idle/gomah_Idle_sheet.png) |
| **Walk** | 1 | 52x52 | [`gomah_Walk.piskel`](Walk/gomah_Walk.piskel) | [`gomah_Walk.gif`](Walk/gomah_Walk.gif) | [`gomah_Walk_sheet.png`](Walk/gomah_Walk_sheet.png) |
| **Attack** | 3 | 60x60 | [`gomah_Attack.piskel`](Attack/gomah_Attack.piskel) | [`gomah_Attack.gif`](Attack/gomah_Attack.gif) | [`gomah_Attack_sheet.png`](Attack/gomah_Attack_sheet.png) |
| **Kick** | 2 | 54x54 | [`gomah_Kick.piskel`](Kick/gomah_Kick.piskel) | [`gomah_Kick.gif`](Kick/gomah_Kick.gif) | [`gomah_Kick_sheet.png`](Kick/gomah_Kick_sheet.png) |
| **Cast** | 2 | 62x62 | [`gomah_Cast.piskel`](Cast/gomah_Cast.piskel) | [`gomah_Cast.gif`](Cast/gomah_Cast.gif) | [`gomah_Cast_sheet.png`](Cast/gomah_Cast_sheet.png) |
| **Pow** | 4 | 78x78 | [`gomah_Pow.piskel`](Pow/gomah_Pow.piskel) | [`gomah_Pow.gif`](Pow/gomah_Pow.gif) | [`gomah_Pow_sheet.png`](Pow/gomah_Pow_sheet.png) |
| **Hurt** | 2 | 50x50 | [`gomah_Hurt.piskel`](Hurt/gomah_Hurt.piskel) | [`gomah_Hurt.gif`](Hurt/gomah_Hurt.gif) | [`gomah_Hurt_sheet.png`](Hurt/gomah_Hurt_sheet.png) |
| **Faint** | 1 | 68x68 | [`gomah_Faint.piskel`](Faint/gomah_Faint.piskel) | [`gomah_Faint.gif`](Faint/gomah_Faint.gif) | [`gomah_Faint_sheet.png`](Faint/gomah_Faint_sheet.png) |
| **Attack2** | 2 | 56x56 | [`gomah_Attack2.piskel`](Attack2/gomah_Attack2.piskel) | [`gomah_Attack2.gif`](Attack2/gomah_Attack2.gif) | [`gomah_Attack2_sheet.png`](Attack2/gomah_Attack2_sheet.png) |