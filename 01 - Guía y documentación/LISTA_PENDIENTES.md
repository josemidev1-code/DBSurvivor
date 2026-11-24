# Lo que queda por hacer en DBSurvivor

Actualizada el 24 nov. 2026 (sesión 24). Resumen de todo en `RESUMEN_SESION_24.md`. Josemi elige el orden; vamos poco a poco y se marca con [x] lo que esté hecho.

## 0. Lo más importante ahora (22 nov.)

Josemi: los enemigos son siempre los mismos, los mapas casi no tienen obstáculos y es imposible aguantar aunque juegues bien. Detalle y datos en `ESTADO_Y_RUMBO.md`.

- [x] Dificultad justa: los enemigos no se hacen más fuertes cuando subes de nivel; menos enemigos a la vez, avisos más largos y nunca más rápidos que tú (22 nov.).
- [x] Los jefes avisan antes de embestir (22 nov.).
- [ ] Que Josemi juegue (mañana en clase) y diga si ya se puede aguantar con habilidad.
- [x] Arreglado el nombre de las fusiones que se acumulaba y aclaradas las técnicas «repetidas» de la pausa (22 nov.).
- [x] Arreglados los jefes élite que te dejaban atrapado en la isla y el modo infinito en mapas de 5 jefes (22 nov.).
- [x] Portadas de los mapas con escenarios de la serie, sin personajes (23 nov., aprobado por Josemi con ese cambio).
- [ ] Buscar fondos de la serie para la Sala del Tiempo, el Torneo de Artes Marciales y Red Ribbon (hoy usan una foto del juego).
- [x] Mapas con obstáculos de verdad (paredes, esquinas, roquedales y ruedos) para cubrirse y usar el terreno (22-23 nov., programado por Codex).
- [ ] Enemigos propios de cada saga, cada tipo con su forma de atacar, y hordas que cambian cada minuto.
  - [x] Piloto en Namek de 0:00 a 2:00: patrulla, tiradores, Burter con embestida anunciada y cierre con salida (24 nov.).
  - [ ] Que Josemi juegue el piloto y diga qué ajustar.
  - [ ] La misma pauta en los demás mapas: tres enemigos comunes, un élite y un jefe por saga.
  - [x] Enemigos de cada mapa según el lore, por zonas, con 15 comunes y élites nuevos (24 nov.). Tabla en `REPARTO_ENEMIGOS.md`.
  - [ ] Pedir a Josemi los sprites de la lista de `REPARTO_ENEMIGOS.md` (Red Ribbon, esbirros de las películas, clase baja, Super…): hay mapas con solo 2-3 comunes.
- [x] **Corregir los mapas (24 nov., Josemi):** los obstáculos siguen sin gustarle; los quiere más naturales y fieles a la serie (no paredes y ruedos de juego, sino lo que hay en cada escenario).
  - [x] Hecho el 24 nov.: paisaje natural por mapa (`const PAISAJE=` en `script.js`): arboledas, pedregales y peñascos agrupados con ruido, según el escenario de la serie; sin huecos cerrados en ningún mapa.
  - [ ] Que Josemi lo vea jugando y diga qué mapa ajustar (cada uno se cambia en su línea de `PAISAJE`).
- [ ] Jefes más duros (mirar también la mejora «Fuerza» de la tienda).
- [ ] Animaciones: que Josemi diga qué no le gusta; pulir a Goku como modelo y luego el resto.

## A. Transformaciones (diseño hablado el 20 nov.)

- [x] 1. Escribir el diseño completo y enseñar a Josemi la lista de mejoras de cada forma, fiel a la serie.
- [x] 2. Barra de ki por tramos: se carga manteniendo una tecla, quieto y sin atacar; el aura atrae a los enemigos y los golpes quitan carga.
- [x] 3. Transformación de unos 20 segundos con su sprite y un aura del color de la forma.
- [x] 4. Poder máximo con aura blanca para los personajes de una sola forma.
- [x] 5. Crear las auras y la carga de ki con PixelFX y mandar un GIF a Josemi.

- [x] Transformaciones con los sprites de cada pack (aprobado por Josemi el 20 nov.).
- [x] Poder máximo (personajes de una sola forma): aura blanca de contorno en sprites durante los 20 s.
- [ ] Que Josemi juegue: ajustar tiempos de carga, duraciones y mejoras.

## B. Jugar y ajustar

- [ ] 6. Josemi juega y valora el ritmo de niveles y la dificultad de los jefes.

## C. Ataques y animaciones

- [ ] 7. Pulir los ataques y las animaciones de cada personaje, uno a uno.
- [ ] 8. 70 enemigos con un solo fotograma de movimiento (Jiren, Janemba, Nappa, Broly, Bills…).
- [x] 9. Ataques propios de cada personaje y época, en lugar de «Ráfaga de Ki» o «Combo de golpes». Antes de aplicarla, enseñar la lista a Josemi.
  - 24 nov.: propuesta en `ATAQUES_PROPUESTA.md` (bajar la potencia y las listas con la animación de cada sprite). Aprobada y aplicada el 24 nov. Siguiente: más enemigos y jefes más duros (pidió ese orden).

## D. Recursos

- [ ] 10. Que Josemi valore el título y el estilo del 13 nov., los efectos PixelFX del 11 nov. y la carpeta `05 - Sprites nuevos encontrados`.
- [ ] 11. Más adelante: crear con Sprite Fusion las animaciones que falten (los créditos son limitados, así que antes hay que preparar bien lo que se pide).
- [ ] 12. Usar ChatGPT para lo que Claude no pueda hacer, como pasar a pixel art objetos de Dragon Ball.

## F. Ideas para el futuro

- [ ] 16. Bocadillos de diálogo sobre los enemigos con alguna frase suya (Josemi, 20 nov.: «molaría que les saliese un bocadillo a los enemigos y dijeran alguna frase»).

## E. Mantenimiento

- [x] 13. Arreglar las comprobaciones que fallan: pasan las 10 (22 nov.).
- [x] 14. Actualizar el README (22 nov.).
- [x] 15. Subir a GitHub los commits de esta rama (24 nov., lo pidió Josemi).

## Ya hecho (20 nov.)

- [x] Plugin de Codex (ChatGPT) instalado y comprobado.
- [x] PixelFX instalado: plugin y copia en `herramientas/pixelfx/`.
- [x] Se acabaron los cuelgues después de los jefes; los rayos apuntan a la horda; niveles y jefes van más lentos.
