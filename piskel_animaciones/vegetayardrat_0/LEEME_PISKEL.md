# Animaciones para Piskel — VEGETAYARDRAT (Forma 0)

Esta carpeta contiene las animaciones listas para abrir y editar en **Piskel** (https://www.piskelapp.com/).

## Cómo abrir en Piskel:
1. Entra a **https://www.piskelapp.com/p/create/sprite** en tu navegador.
2. Haz clic en el icono de carpeta de la barra derecha (**Import**).
3. Elige cualquiera de estas opciones:
   - **Import .piskel file**: selecciona el archivo `.piskel` de cualquier animación.
   - **Import animated GIF**: selecciona el archivo `.gif` (Piskel importa todos los fotogramas y la velocidad al instante).
   - **Import from picture**: selecciona el `_sheet.png` (pon el Frame size que se indica abajo).

## Volver al juego:
`python herramientas/importar_piskel.py editado.piskel --manifiesto piskel_animaciones/vegetayardrat_0/origen.json --heroe vegetayardrat --forma 0 --anim attack --aplicar`
Después: `python herramientas/montar_animaciones.py vegetayardrat` y revisión visual. Solo se aceptan sprites originales exportados.

## Animaciones disponibles:

| Animación | Fotogramas | Tamaño de celda | Archivo .piskel | GIF animado | Hoja Strip |
|---|---|---|---|---|---|
| **Idle** | 1 | 60x60 | [`vegetayardrat_Idle.piskel`](Idle/vegetayardrat_Idle.piskel) | [`vegetayardrat_Idle.gif`](Idle/vegetayardrat_Idle.gif) | [`vegetayardrat_Idle_sheet.png`](Idle/vegetayardrat_Idle_sheet.png) |
| **Walk** | 1 | 60x60 | [`vegetayardrat_Walk.piskel`](Walk/vegetayardrat_Walk.piskel) | [`vegetayardrat_Walk.gif`](Walk/vegetayardrat_Walk.gif) | [`vegetayardrat_Walk_sheet.png`](Walk/vegetayardrat_Walk_sheet.png) |
| **Attack** | 3 | 60x60 | [`vegetayardrat_Attack.piskel`](Attack/vegetayardrat_Attack.piskel) | [`vegetayardrat_Attack.gif`](Attack/vegetayardrat_Attack.gif) | [`vegetayardrat_Attack_sheet.png`](Attack/vegetayardrat_Attack_sheet.png) |
| **Kick** | 2 | 60x60 | [`vegetayardrat_Kick.piskel`](Kick/vegetayardrat_Kick.piskel) | [`vegetayardrat_Kick.gif`](Kick/vegetayardrat_Kick.gif) | [`vegetayardrat_Kick_sheet.png`](Kick/vegetayardrat_Kick_sheet.png) |
| **Cast** | 2 | 60x60 | [`vegetayardrat_Cast.piskel`](Cast/vegetayardrat_Cast.piskel) | [`vegetayardrat_Cast.gif`](Cast/vegetayardrat_Cast.gif) | [`vegetayardrat_Cast_sheet.png`](Cast/vegetayardrat_Cast_sheet.png) |
| **Pow** | 2 | 62x62 | [`vegetayardrat_Pow.piskel`](Pow/vegetayardrat_Pow.piskel) | [`vegetayardrat_Pow.gif`](Pow/vegetayardrat_Pow.gif) | [`vegetayardrat_Pow_sheet.png`](Pow/vegetayardrat_Pow_sheet.png) |
| **Hurt** | 2 | 44x44 | [`vegetayardrat_Hurt.piskel`](Hurt/vegetayardrat_Hurt.piskel) | [`vegetayardrat_Hurt.gif`](Hurt/vegetayardrat_Hurt.gif) | [`vegetayardrat_Hurt_sheet.png`](Hurt/vegetayardrat_Hurt_sheet.png) |
| **Faint** | 1 | 60x60 | [`vegetayardrat_Faint.piskel`](Faint/vegetayardrat_Faint.piskel) | [`vegetayardrat_Faint.gif`](Faint/vegetayardrat_Faint.gif) | [`vegetayardrat_Faint_sheet.png`](Faint/vegetayardrat_Faint_sheet.png) |
| **Attack2** | 2 | 50x50 | [`vegetayardrat_Attack2.piskel`](Attack2/vegetayardrat_Attack2.piskel) | [`vegetayardrat_Attack2.gif`](Attack2/vegetayardrat_Attack2.gif) | [`vegetayardrat_Attack2_sheet.png`](Attack2/vegetayardrat_Attack2_sheet.png) |
| **Attack3** | 2 | 46x46 | [`vegetayardrat_Attack3.piskel`](Attack3/vegetayardrat_Attack3.piskel) | [`vegetayardrat_Attack3.gif`](Attack3/vegetayardrat_Attack3.gif) | [`vegetayardrat_Attack3_sheet.png`](Attack3/vegetayardrat_Attack3_sheet.png) |
| **Kick2** | 2 | 48x48 | [`vegetayardrat_Kick2.piskel`](Kick2/vegetayardrat_Kick2.piskel) | [`vegetayardrat_Kick2.gif`](Kick2/vegetayardrat_Kick2.gif) | [`vegetayardrat_Kick2_sheet.png`](Kick2/vegetayardrat_Kick2_sheet.png) |
| **Up** | 1 | 60x60 | [`vegetayardrat_Up.piskel`](Up/vegetayardrat_Up.piskel) | [`vegetayardrat_Up.gif`](Up/vegetayardrat_Up.gif) | [`vegetayardrat_Up_sheet.png`](Up/vegetayardrat_Up_sheet.png) |