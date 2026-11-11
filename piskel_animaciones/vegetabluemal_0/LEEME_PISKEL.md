# Animaciones para Piskel — VEGETABLUEMAL (Forma 0)

Esta carpeta contiene las animaciones listas para abrir y editar en **Piskel** (https://www.piskelapp.com/).

## Cómo abrir en Piskel:
1. Entra a **https://www.piskelapp.com/p/create/sprite** en tu navegador.
2. Haz clic en el icono de carpeta de la barra derecha (**Import**).
3. Elige cualquiera de estas opciones:
   - **Import .piskel file**: selecciona el archivo `.piskel` de cualquier animación.
   - **Import animated GIF**: selecciona el archivo `.gif` (Piskel importa todos los fotogramas y la velocidad al instante).
   - **Import from picture**: selecciona el `_sheet.png` (pon el Frame size que se indica abajo).

## Volver al juego:
`python herramientas/importar_piskel.py editado.piskel --manifiesto piskel_animaciones/vegetabluemal_0/origen.json --heroe vegetabluemal --forma 0 --anim attack --aplicar`
Después: `python herramientas/montar_animaciones.py vegetabluemal` y revisión visual. Solo se aceptan sprites originales exportados.

## Animaciones disponibles:

| Animación | Fotogramas | Tamaño de celda | Archivo .piskel | GIF animado | Hoja Strip |
|---|---|---|---|---|---|
| **Idle** | 2 | 54x54 | [`vegetabluemal_Idle.piskel`](Idle/vegetabluemal_Idle.piskel) | [`vegetabluemal_Idle.gif`](Idle/vegetabluemal_Idle.gif) | [`vegetabluemal_Idle_sheet.png`](Idle/vegetabluemal_Idle_sheet.png) |
| **Walk** | 1 | 48x48 | [`vegetabluemal_Walk.piskel`](Walk/vegetabluemal_Walk.piskel) | [`vegetabluemal_Walk.gif`](Walk/vegetabluemal_Walk.gif) | [`vegetabluemal_Walk_sheet.png`](Walk/vegetabluemal_Walk_sheet.png) |
| **Attack** | 3 | 56x56 | [`vegetabluemal_Attack.piskel`](Attack/vegetabluemal_Attack.piskel) | [`vegetabluemal_Attack.gif`](Attack/vegetabluemal_Attack.gif) | [`vegetabluemal_Attack_sheet.png`](Attack/vegetabluemal_Attack_sheet.png) |
| **Kick** | 2 | 52x52 | [`vegetabluemal_Kick.piskel`](Kick/vegetabluemal_Kick.piskel) | [`vegetabluemal_Kick.gif`](Kick/vegetabluemal_Kick.gif) | [`vegetabluemal_Kick_sheet.png`](Kick/vegetabluemal_Kick_sheet.png) |
| **Cast** | 2 | 62x62 | [`vegetabluemal_Cast.piskel`](Cast/vegetabluemal_Cast.piskel) | [`vegetabluemal_Cast.gif`](Cast/vegetabluemal_Cast.gif) | [`vegetabluemal_Cast_sheet.png`](Cast/vegetabluemal_Cast_sheet.png) |
| **Pow** | 2 | 86x86 | [`vegetabluemal_Pow.piskel`](Pow/vegetabluemal_Pow.piskel) | [`vegetabluemal_Pow.gif`](Pow/vegetabluemal_Pow.gif) | [`vegetabluemal_Pow_sheet.png`](Pow/vegetabluemal_Pow_sheet.png) |
| **Hurt** | 2 | 52x52 | [`vegetabluemal_Hurt.piskel`](Hurt/vegetabluemal_Hurt.piskel) | [`vegetabluemal_Hurt.gif`](Hurt/vegetabluemal_Hurt.gif) | [`vegetabluemal_Hurt_sheet.png`](Hurt/vegetabluemal_Hurt_sheet.png) |
| **Attack2** | 2 | 52x52 | [`vegetabluemal_Attack2.piskel`](Attack2/vegetabluemal_Attack2.piskel) | [`vegetabluemal_Attack2.gif`](Attack2/vegetabluemal_Attack2.gif) | [`vegetabluemal_Attack2_sheet.png`](Attack2/vegetabluemal_Attack2_sheet.png) |
| **Attack3** | 2 | 56x56 | [`vegetabluemal_Attack3.piskel`](Attack3/vegetabluemal_Attack3.piskel) | [`vegetabluemal_Attack3.gif`](Attack3/vegetabluemal_Attack3.gif) | [`vegetabluemal_Attack3_sheet.png`](Attack3/vegetabluemal_Attack3_sheet.png) |
| **Kick2** | 2 | 58x58 | [`vegetabluemal_Kick2.piskel`](Kick2/vegetabluemal_Kick2.piskel) | [`vegetabluemal_Kick2.gif`](Kick2/vegetabluemal_Kick2.gif) | [`vegetabluemal_Kick2_sheet.png`](Kick2/vegetabluemal_Kick2_sheet.png) |
| **Beam** | 2 | 56x56 | [`vegetabluemal_Beam.piskel`](Beam/vegetabluemal_Beam.piskel) | [`vegetabluemal_Beam.gif`](Beam/vegetabluemal_Beam.gif) | [`vegetabluemal_Beam_sheet.png`](Beam/vegetabluemal_Beam_sheet.png) |
| **Up** | 1 | 60x60 | [`vegetabluemal_Up.piskel`](Up/vegetabluemal_Up.piskel) | [`vegetabluemal_Up.gif`](Up/vegetabluemal_Up.gif) | [`vegetabluemal_Up_sheet.png`](Up/vegetabluemal_Up_sheet.png) |