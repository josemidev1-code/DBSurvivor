# Resumen de la sesión 24 (20-24 nov. 2026)

Lo que hemos hecho en esta sesión de Claude con Josemi y lo que nos queda, en un solo sitio. El detalle de cada paso está en las entradas «sesión 24» de `BITACORA.md`. La lista de tareas con casillas sigue en `LISTA_PENDIENTES.md`.

Rama: `claude/pensive-maxwell-rmrwmm` (subida a GitHub el 24 nov., sin fusionar en `main`). Caché actual: `script.js?v=227`.

## Lo que hemos hecho

### 20 nov. Herramientas y transformaciones
- **Herramientas:** plugin de Codex (ChatGPT) instalado y comprobado; PixelFX instalado (plugin y copia en `herramientas/pixelfx/`).
- **Transformaciones con barra de ki**, diseño aprobado por Josemi:
  - Se carga manteniendo ESPACIO, quieto y sin atacar. El aura atrae a los enemigos y cada golpe quita carga, para que cargar sea un reto.
  - Se sube forma a forma. Cada forma dura unos 20 s, tiene su sprite del pack y una mejora propia, fiel a la serie.
  - Los personajes de una sola forma tienen «poder máximo»: aura blanca de contorno durante 20 s.
  - Funciona también con un botón KI táctil.
  - A Josemi le encantaron.

### 22 nov. Dificultad y arreglos
- **Dificultad justa:**
  - Los enemigos ya no se hacen más fuertes cuando subes de nivel.
  - Salen menos a la vez, los avisos duran más y nunca son más rápidos que tú.
  - Simulador de partidas para medirlo.
- **Jefes:** aviso rojo antes de embestir.
- **Arreglos:** nombres de fusiones que se acumulaban, jefes élite que te dejaban atrapado en la isla, modo infinito en mapas de 5 jefes y técnicas automáticas marcadas en la pausa.
- **Mantenimiento:** pasan las 10 comprobaciones (`herramientas/comprobar_*.cjs`) y el README está al día.

### 23 nov. Mapas e interfaz
- **Obstáculos de verdad en los 24 mapas:** paredes, esquinas, roquedales y ruedos para cubrirse. Lo programó Codex y lo revisó Claude; después, retoques para que no se monten ni tapen el decorado.
- **Portadas de los mapas** con el escenario de la serie, sin personajes.
- **Interfaz** (hecho por Codex, comprobado por Claude):
  - el radar va bajo el recuadro de KO;
  - ya no aparece el aviso fijo de Shenron;
  - el humo de los golpes es más pequeño;
  - NOTICIAS ya no pisa ZENI;
  - el logo sale al instante.

### 24 nov. Ataques, dex y piloto de Namek
- **Ataques** (propuesta en `ATAQUES_PROPUESTA.md`, aprobada por Josemi y aplicada):
  - Las transformaciones multiplican el daño como mucho ×1,7.
  - Las cartas de Poder dan +8 % cada una, con un máximo de 5.
  - Las técnicas que pegaban el doble que las de su tipo quedan igualadas, y los rayos esperan al menos 2,5 s entre uno y otro.
  - La tecla 1 es la técnica más famosa de cada personaje, sin relleno genérico.
  - Arreglada la estela del acelerón, que rompía el dibujo.
- **Dex regenerada** (`03 - Dex/index.html`): 138 personajes y 224 formas. Ficha nueva «TÉCNICAS (TECLAS 1-6)» con la animación que usa cada técnica en el juego.
- **Piloto de combate en Namek, 0:00-2:00** (petición de `DBSurvivor_Prompt_para_Claude.md`):
  - 0:00: patrulla de Freezer en fila, que obliga a rodearla.
  - 0:30: tiradores con línea roja y mira en el suelo. Fallan si te mueves y las rocas paran sus balas.
  - 1:00: Burter anuncia su embestida con una línea roja. Se esquiva de lado y luego se queda mareado 1,1 s («¡AHORA!»); en ese rato recibe un 50 % más de daño.
  - 1:30: las tres amenazas te cierran por tres lados, con una flecha verde hacia la salida libre.
  - 2:00: Dodoria, como siempre.
  - Arreglos generales para que cada personaje juegue distinto:
    - el Teletransporte salta hacia donde te mueves;
    - las Barreras de 17 y Super 17 protegen de un golpe anunciado.
  - Medido con el entorno de pruebas, no jugado a mano:
    - Burter da 22 de 24 embestidas si te quedas quieto y 4 de 24 si te apartas de lado.
    - Goku alinea la fila para el Kamehameha; Trunks la recibe de frente con la espada; 17 aguanta con la Barrera.

### Forma de trabajar acordada
- Probar siempre con el juego en silencio (botón MUDO).
- Todo en español; solo sprites de `sprites/`; el juego tiene que abrirse con doble clic en `index.html`, sin `fetch`.
- Commits pequeños, apuntar cada petición en la bitácora y mandar capturas o GIF.
- No inventar técnicas: solo las de la serie.
- Las tareas largas se le pasan a Codex.
- Sprite Fusion, más adelante y preguntando antes, porque los créditos son limitados.

## Lo que nos queda

### Ahora
1. **Que Josemi juegue el piloto de Namek** con Goku, Trunks y 17 y diga:
   - si se reconoce cada amenaza;
   - si los avisos (0,75 s y 0,7 s) y el mareo (1,1 s) le parecen justos;
   - si salen demasiados enemigos a la vez.
2. **Llevar la misma pauta a los demás mapas:** tres enemigos comunes con comportamientos distintos, un élite y un jefe por saga.
   - Red Ribbon: un androide pesado y tiradores que controlen pasillos.
   - Futuro de Trunks: clones de Zamasu desde el principio; Black Rosé con barridos de guadaña y una recuperación visible.
3. **Jefes más duros** (paso 3 del pedido de Josemi). Mirar también la mejora «Fuerza» de la tienda, que llega a +200 % y puede seguir acortando los jefes. Falta saber con qué personaje y mejoras jugó Josemi cuando los jefes le duraban poco.

### Problemas vistos que no se han tocado
- Goku Base aguanta poco: su Kamehameha se lanza solo y le frena mucho.
- Desde el 1:30 salen «Saiyan zombi» en todos los mapas, también en Namek, donde no pintan nada.
- En la pausa, Trunks puede tener «Burning Attack» repetido (la técnica de la tecla y la especial).
- Enemigos definidos que no salen en ningún mapa: Guldo, Frost, Androide 21 Majin, Zamasu fusionado, Goku SSJ enemigo y el Saibaman de ki.
- Con Goku, ESPACIO no carga ki si no ha comprado la forma a Shenron. Pregunta abierta para Josemi: ¿quitamos lo de Shenron?
- No se pudo comprobar en el navegador que el juego arranca con doble clic. No se ha añadido ningún archivo ni `fetch` nuevo, así que debería seguir igual.

### Animaciones y efectos
- La Espada del Futuro de Trunks necesita su animación propia; hoy usa la pose de puñetazo.
- Estándar para los jugables: guardia, desplazamiento, puñetazo, patada, disparo de ki, carga, daño y KO, con 2 o 3 técnicas reconocibles por su silueta. Lo que más falta según la dex:
  - brazos arriba: falta en 121 personajes;
  - combo 3: falta en 31;
  - patada 2: falta en 24;
  - muerte: falta en 21;
  - rayo: falta en 20.
- Para los enemigos, lo primero es movimiento, aviso, ataque, recuperación, daño y KO. 70 enemigos tienen un solo fotograma de movimiento (Jiren, Janemba, Nappa, Broly, Bills…). Otra sesión está trabajando en las animaciones de enemigos.
- Mejores efectos de ataque con PixelFX.

### Que Josemi revise o decida
- La dex: qué personajes o animaciones le gustan menos. Más adelante, la dex podría tener una vista previa por acción y el estado de cada una:
  - clip propio;
  - pose compartida;
  - pose alternativa;
  - un fotograma;
  - falta.
- Las transformaciones jugando: tiempos de carga, duración y mejoras.
- El ritmo de niveles y la dificultad de los jefes.
- El título y estilo del 13 nov., los efectos PixelFX del 11 nov. y la carpeta `05 - Sprites nuevos encontrados/`.

### Más adelante
- Fondos de la serie para la Sala del Tiempo, el Torneo de Artes Marciales y Red Ribbon.
- Selector de personajes con retratos, agrupando las variantes que juegan igual.
- Animaciones que falten con Sprite Fusion (preguntando antes por los créditos).
- Usar ChatGPT para pasar a pixel art objetos de Dragon Ball.
- Bocadillos con frases sobre los enemigos.
