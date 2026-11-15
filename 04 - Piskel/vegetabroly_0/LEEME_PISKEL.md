# Animaciones para Piskel — VEGETABROLY (Forma 0)

Esta carpeta contiene las animaciones listas para abrir y editar en **Piskel** (https://www.piskelapp.com/).

## Cómo abrir en Piskel:
1. Entra a **https://www.piskelapp.com/p/create/sprite** en tu navegador.
2. Haz clic en el icono de carpeta de la barra derecha (**Import**).
3. Elige cualquiera de estas opciones:
   - **Import .piskel file**: selecciona el archivo `.piskel` de cualquier animación.
   - **Import animated GIF**: selecciona el archivo `.gif` (Piskel importa todos los fotogramas y la velocidad al instante).
   - **Import from picture**: selecciona el `_sheet.png` (pon el Frame size que se indica abajo).

## Volver al juego:
`python herramientas/importar_piskel.py editado.piskel --manifiesto "04 - Piskel/vegetabroly_0/origen.json" --heroe vegetabroly --forma 0 --anim attack --aplicar`
Después: `python herramientas/montar_animaciones.py vegetabroly` y revisión visual. Solo se aceptan sprites originales exportados.

## Animaciones disponibles:

| Animación | Fotogramas | Tamaño de celda | Archivo .piskel | GIF animado | Hoja Strip |
|---|---|---|---|---|---|
| **Idle** | 2 | 54x54 | [`vegetabroly_Idle.piskel`](Idle/vegetabroly_Idle.piskel) | [`vegetabroly_Idle.gif`](Idle/vegetabroly_Idle.gif) | [`vegetabroly_Idle_sheet.png`](Idle/vegetabroly_Idle_sheet.png) |
| **Walk** | 1 | 48x48 | [`vegetabroly_Walk.piskel`](Walk/vegetabroly_Walk.piskel) | [`vegetabroly_Walk.gif`](Walk/vegetabroly_Walk.gif) | [`vegetabroly_Walk_sheet.png`](Walk/vegetabroly_Walk_sheet.png) |
| **Attack** | 4 | 56x56 | [`vegetabroly_Attack.piskel`](Attack/vegetabroly_Attack.piskel) | [`vegetabroly_Attack.gif`](Attack/vegetabroly_Attack.gif) | [`vegetabroly_Attack_sheet.png`](Attack/vegetabroly_Attack_sheet.png) |
| **Kick** | 3 | 50x50 | [`vegetabroly_Kick.piskel`](Kick/vegetabroly_Kick.piskel) | [`vegetabroly_Kick.gif`](Kick/vegetabroly_Kick.gif) | [`vegetabroly_Kick_sheet.png`](Kick/vegetabroly_Kick_sheet.png) |
| **Cast** | 2 | 56x56 | [`vegetabroly_Cast.piskel`](Cast/vegetabroly_Cast.piskel) | [`vegetabroly_Cast.gif`](Cast/vegetabroly_Cast.gif) | [`vegetabroly_Cast_sheet.png`](Cast/vegetabroly_Cast_sheet.png) |
| **Pow** | 2 | 74x74 | [`vegetabroly_Pow.piskel`](Pow/vegetabroly_Pow.piskel) | [`vegetabroly_Pow.gif`](Pow/vegetabroly_Pow.gif) | [`vegetabroly_Pow_sheet.png`](Pow/vegetabroly_Pow_sheet.png) |
| **Hurt** | 2 | 46x46 | [`vegetabroly_Hurt.piskel`](Hurt/vegetabroly_Hurt.piskel) | [`vegetabroly_Hurt.gif`](Hurt/vegetabroly_Hurt.gif) | [`vegetabroly_Hurt_sheet.png`](Hurt/vegetabroly_Hurt_sheet.png) |
| **Faint** | 1 | 50x50 | [`vegetabroly_Faint.piskel`](Faint/vegetabroly_Faint.piskel) | [`vegetabroly_Faint.gif`](Faint/vegetabroly_Faint.gif) | [`vegetabroly_Faint_sheet.png`](Faint/vegetabroly_Faint_sheet.png) |
| **Attack2** | 3 | 62x62 | [`vegetabroly_Attack2.piskel`](Attack2/vegetabroly_Attack2.piskel) | [`vegetabroly_Attack2.gif`](Attack2/vegetabroly_Attack2.gif) | [`vegetabroly_Attack2_sheet.png`](Attack2/vegetabroly_Attack2_sheet.png) |
| **Attack3** | 2 | 56x56 | [`vegetabroly_Attack3.piskel`](Attack3/vegetabroly_Attack3.piskel) | [`vegetabroly_Attack3.gif`](Attack3/vegetabroly_Attack3.gif) | [`vegetabroly_Attack3_sheet.png`](Attack3/vegetabroly_Attack3_sheet.png) |
| **Kick2** | 2 | 60x60 | [`vegetabroly_Kick2.piskel`](Kick2/vegetabroly_Kick2.piskel) | [`vegetabroly_Kick2.gif`](Kick2/vegetabroly_Kick2.gif) | [`vegetabroly_Kick2_sheet.png`](Kick2/vegetabroly_Kick2_sheet.png) |
| **Up** | 1 | 60x60 | [`vegetabroly_Up.piskel`](Up/vegetabroly_Up.piskel) | [`vegetabroly_Up.gif`](Up/vegetabroly_Up.gif) | [`vegetabroly_Up_sheet.png`](Up/vegetabroly_Up_sheet.png) |