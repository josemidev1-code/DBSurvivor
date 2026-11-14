# Animaciones para Piskel — VEGETAMANGA (Forma 0)

Esta carpeta contiene las animaciones listas para abrir y editar en **Piskel** (https://www.piskelapp.com/).

## Cómo abrir en Piskel:
1. Entra a **https://www.piskelapp.com/p/create/sprite** en tu navegador.
2. Haz clic en el icono de carpeta de la barra derecha (**Import**).
3. Elige cualquiera de estas opciones:
   - **Import .piskel file**: selecciona el archivo `.piskel` de cualquier animación.
   - **Import animated GIF**: selecciona el archivo `.gif` (Piskel importa todos los fotogramas y la velocidad al instante).
   - **Import from picture**: selecciona el `_sheet.png` (pon el Frame size que se indica abajo).

## Volver al juego:
`python herramientas/importar_piskel.py editado.piskel --manifiesto piskel_animaciones/vegetamanga_0/origen.json --heroe vegetamanga --forma 0 --anim attack --aplicar`
Después: `python herramientas/montar_animaciones.py vegetamanga` y revisión visual. Solo se aceptan sprites originales exportados.

## Animaciones disponibles:

| Animación | Fotogramas | Tamaño de celda | Archivo .piskel | GIF animado | Hoja Strip |
|---|---|---|---|---|---|
| **Idle** | 2 | 60x60 | [`vegetamanga_Idle.piskel`](Idle/vegetamanga_Idle.piskel) | [`vegetamanga_Idle.gif`](Idle/vegetamanga_Idle.gif) | [`vegetamanga_Idle_sheet.png`](Idle/vegetamanga_Idle_sheet.png) |
| **Walk** | 1 | 58x58 | [`vegetamanga_Walk.piskel`](Walk/vegetamanga_Walk.piskel) | [`vegetamanga_Walk.gif`](Walk/vegetamanga_Walk.gif) | [`vegetamanga_Walk_sheet.png`](Walk/vegetamanga_Walk_sheet.png) |
| **Attack** | 4 | 64x64 | [`vegetamanga_Attack.piskel`](Attack/vegetamanga_Attack.piskel) | [`vegetamanga_Attack.gif`](Attack/vegetamanga_Attack.gif) | [`vegetamanga_Attack_sheet.png`](Attack/vegetamanga_Attack_sheet.png) |
| **Kick** | 3 | 56x56 | [`vegetamanga_Kick.piskel`](Kick/vegetamanga_Kick.piskel) | [`vegetamanga_Kick.gif`](Kick/vegetamanga_Kick.gif) | [`vegetamanga_Kick_sheet.png`](Kick/vegetamanga_Kick_sheet.png) |
| **Cast** | 2 | 66x66 | [`vegetamanga_Cast.piskel`](Cast/vegetamanga_Cast.piskel) | [`vegetamanga_Cast.gif`](Cast/vegetamanga_Cast.gif) | [`vegetamanga_Cast_sheet.png`](Cast/vegetamanga_Cast_sheet.png) |
| **Pow** | 2 | 78x78 | [`vegetamanga_Pow.piskel`](Pow/vegetamanga_Pow.piskel) | [`vegetamanga_Pow.gif`](Pow/vegetamanga_Pow.gif) | [`vegetamanga_Pow_sheet.png`](Pow/vegetamanga_Pow_sheet.png) |
| **Hurt** | 2 | 54x54 | [`vegetamanga_Hurt.piskel`](Hurt/vegetamanga_Hurt.piskel) | [`vegetamanga_Hurt.gif`](Hurt/vegetamanga_Hurt.gif) | [`vegetamanga_Hurt_sheet.png`](Hurt/vegetamanga_Hurt_sheet.png) |
| **Faint** | 1 | 50x50 | [`vegetamanga_Faint.piskel`](Faint/vegetamanga_Faint.piskel) | [`vegetamanga_Faint.gif`](Faint/vegetamanga_Faint.gif) | [`vegetamanga_Faint_sheet.png`](Faint/vegetamanga_Faint_sheet.png) |
| **Attack2** | 3 | 66x66 | [`vegetamanga_Attack2.piskel`](Attack2/vegetamanga_Attack2.piskel) | [`vegetamanga_Attack2.gif`](Attack2/vegetamanga_Attack2.gif) | [`vegetamanga_Attack2_sheet.png`](Attack2/vegetamanga_Attack2_sheet.png) |
| **Attack3** | 3 | 62x62 | [`vegetamanga_Attack3.piskel`](Attack3/vegetamanga_Attack3.piskel) | [`vegetamanga_Attack3.gif`](Attack3/vegetamanga_Attack3.gif) | [`vegetamanga_Attack3_sheet.png`](Attack3/vegetamanga_Attack3_sheet.png) |
| **Kick2** | 2 | 62x62 | [`vegetamanga_Kick2.piskel`](Kick2/vegetamanga_Kick2.piskel) | [`vegetamanga_Kick2.gif`](Kick2/vegetamanga_Kick2.gif) | [`vegetamanga_Kick2_sheet.png`](Kick2/vegetamanga_Kick2_sheet.png) |
| **Up** | 1 | 70x70 | [`vegetamanga_Up.piskel`](Up/vegetamanga_Up.piskel) | [`vegetamanga_Up.gif`](Up/vegetamanga_Up.gif) | [`vegetamanga_Up_sheet.png`](Up/vegetamanga_Up_sheet.png) |