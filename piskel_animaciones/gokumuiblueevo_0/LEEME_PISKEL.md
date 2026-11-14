# Animaciones para Piskel — GOKUMUIBLUEEVO (Forma 0)

Esta carpeta contiene las animaciones listas para abrir y editar en **Piskel** (https://www.piskelapp.com/).

## Cómo abrir en Piskel:
1. Entra a **https://www.piskelapp.com/p/create/sprite** en tu navegador.
2. Haz clic en el icono de carpeta de la barra derecha (**Import**).
3. Elige cualquiera de estas opciones:
   - **Import .piskel file**: selecciona el archivo `.piskel` de cualquier animación.
   - **Import animated GIF**: selecciona el archivo `.gif` (Piskel importa todos los fotogramas y la velocidad al instante).
   - **Import from picture**: selecciona el `_sheet.png` (pon el Frame size que se indica abajo).

## Volver al juego:
`python herramientas/importar_piskel.py editado.piskel --manifiesto piskel_animaciones/gokumuiblueevo_0/origen.json --heroe gokumuiblueevo --forma 0 --anim attack --aplicar`
Después: `python herramientas/montar_animaciones.py gokumuiblueevo` y revisión visual. Solo se aceptan sprites originales exportados.

## Animaciones disponibles:

| Animación | Fotogramas | Tamaño de celda | Archivo .piskel | GIF animado | Hoja Strip |
|---|---|---|---|---|---|
| **Idle** | 2 | 54x54 | [`gokumuiblueevo_Idle.piskel`](Idle/gokumuiblueevo_Idle.piskel) | [`gokumuiblueevo_Idle.gif`](Idle/gokumuiblueevo_Idle.gif) | [`gokumuiblueevo_Idle_sheet.png`](Idle/gokumuiblueevo_Idle_sheet.png) |
| **Walk** | 1 | 56x56 | [`gokumuiblueevo_Walk.piskel`](Walk/gokumuiblueevo_Walk.piskel) | [`gokumuiblueevo_Walk.gif`](Walk/gokumuiblueevo_Walk.gif) | [`gokumuiblueevo_Walk_sheet.png`](Walk/gokumuiblueevo_Walk_sheet.png) |
| **Attack** | 3 | 62x62 | [`gokumuiblueevo_Attack.piskel`](Attack/gokumuiblueevo_Attack.piskel) | [`gokumuiblueevo_Attack.gif`](Attack/gokumuiblueevo_Attack.gif) | [`gokumuiblueevo_Attack_sheet.png`](Attack/gokumuiblueevo_Attack_sheet.png) |
| **Kick** | 2 | 60x60 | [`gokumuiblueevo_Kick.piskel`](Kick/gokumuiblueevo_Kick.piskel) | [`gokumuiblueevo_Kick.gif`](Kick/gokumuiblueevo_Kick.gif) | [`gokumuiblueevo_Kick_sheet.png`](Kick/gokumuiblueevo_Kick_sheet.png) |
| **Cast** | 2 | 64x64 | [`gokumuiblueevo_Cast.piskel`](Cast/gokumuiblueevo_Cast.piskel) | [`gokumuiblueevo_Cast.gif`](Cast/gokumuiblueevo_Cast.gif) | [`gokumuiblueevo_Cast_sheet.png`](Cast/gokumuiblueevo_Cast_sheet.png) |
| **Pow** | 2 | 74x74 | [`gokumuiblueevo_Pow.piskel`](Pow/gokumuiblueevo_Pow.piskel) | [`gokumuiblueevo_Pow.gif`](Pow/gokumuiblueevo_Pow.gif) | [`gokumuiblueevo_Pow_sheet.png`](Pow/gokumuiblueevo_Pow_sheet.png) |
| **Hurt** | 2 | 58x58 | [`gokumuiblueevo_Hurt.piskel`](Hurt/gokumuiblueevo_Hurt.piskel) | [`gokumuiblueevo_Hurt.gif`](Hurt/gokumuiblueevo_Hurt.gif) | [`gokumuiblueevo_Hurt_sheet.png`](Hurt/gokumuiblueevo_Hurt_sheet.png) |
| **Faint** | 1 | 64x64 | [`gokumuiblueevo_Faint.piskel`](Faint/gokumuiblueevo_Faint.piskel) | [`gokumuiblueevo_Faint.gif`](Faint/gokumuiblueevo_Faint.gif) | [`gokumuiblueevo_Faint_sheet.png`](Faint/gokumuiblueevo_Faint_sheet.png) |
| **Attack2** | 2 | 50x50 | [`gokumuiblueevo_Attack2.piskel`](Attack2/gokumuiblueevo_Attack2.piskel) | [`gokumuiblueevo_Attack2.gif`](Attack2/gokumuiblueevo_Attack2.gif) | [`gokumuiblueevo_Attack2_sheet.png`](Attack2/gokumuiblueevo_Attack2_sheet.png) |
| **Kick2** | 2 | 66x66 | [`gokumuiblueevo_Kick2.piskel`](Kick2/gokumuiblueevo_Kick2.piskel) | [`gokumuiblueevo_Kick2.gif`](Kick2/gokumuiblueevo_Kick2.gif) | [`gokumuiblueevo_Kick2_sheet.png`](Kick2/gokumuiblueevo_Kick2_sheet.png) |