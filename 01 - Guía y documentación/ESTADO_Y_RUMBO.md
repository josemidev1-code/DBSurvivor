# DBSurvivor: qué tenemos, qué falla y hacia dónde vamos

22 nov. 2026. Escrito para Josemi a partir de lo que dijo: «las animaciones no me gustan aún, los enemigos son siempre los mismos, en los mapas no hay casi colisiones, no hay manera de aguantar si tienes skill y al final se hace aburrido e imposible».

## Hacia dónde vamos

Un survivor de Dragon Ball en el que arrasas hordas con buenos efectos, te transformas como en la serie y los jefes son un reto. Una partida tiene que poder **ganarse con habilidad**: si juegas bien, aguantas; si juegas mal, pierdes. Hoy no pasa eso.

## Lo que ya tenemos

- **118 personajes** con sus sprites, y los 11 principales (Goku, Vegeta, Gohan, Piccolo, Krilin, Trunks, Goten, Freezer, Cell, Buu y Broly) con sus formas de la serie en orden.
- **Transformaciones con barra de ki** (te encantaron): cargas quieto, los enemigos van a por ti y subes forma a forma, con la animación de cada pack. Los de una sola forma tienen el **poder máximo** con aura blanca.
- **24 mapas**, cada uno de una saga, con su clima y sus jefes.
- Kamehameha y otros ataques con efectos de PixelFX, menús para niños, Shenron, tienda, mejoras permanentes, misiones, dificultades y la DB Dex.

## Lo que falla (lo he medido en el código)

### 1. Es imposible aguantar, aunque juegues bien

- Los enemigos **ganan vida con el tiempo y también cuando tú subes de nivel**. Al minuto 10, con nivel 25, cada enemigo tiene unas **7 veces** su vida y pega **3 veces** más. Subir de nivel casi no se nota porque ellos suben contigo.
- Salen cada vez más y más deprisa: al minuto 10 aparecen unos 11 enemigos cada cuarto de segundo, hasta llenar los 280 que caben en pantalla. Encima llegan hordas de hasta 64, emboscadas de 36 y oleadas.
- Resultado: no hay hueco para esquivar. Da igual lo bien que te muevas.

### 2. Los enemigos son siempre los mismos

- En casi todos los mapas la base son los mismos 4 tipos: **saibaman, soldado de Freezer, Cell Jr. y majin**. En Namek, por ejemplo, 6 de cada 10 enemigos son saibamen o soldados.
- Los enemigos especiales (Burter, Cooler, Zamasu…) salen muy de vez en cuando: cada uno es menos de 1 de cada 100 enemigos.
- Casi todos se comportan igual: van hacia ti. Hay pocos que disparen, embistan o exploten, y no se distinguen bien.

### 3. Los mapas son campo abierto

- Los obstáculos ocupan entre el **0,3 % y el 6 %** del suelo. La Sala del Tiempo, Kame House, el Planeta de Kaio y el Torneo del Poder están casi vacíos.
- Los obstáculos son pequeños (árboles, rocas sueltas) y los enemigos los rodean sin problema. No hay paredes, pasillos ni rocas para cubrirte, así que no puedes usar el mapa para aguantar.

### 4. Las animaciones aún no te gustan

- Hay 70 enemigos con un solo fotograma para moverse: se deslizan en vez de andar.
- Me falta saber **qué es lo que no te gusta** de los personajes: ¿cómo andan, cómo pegan, el tamaño, que se vean borrosos…?

## Lo que propongo, en orden

Dejar de añadir cosas nuevas y arreglar el **corazón del juego**. Cada paso se prueba jugando y te mando un GIF antes de seguir.

1. **Dificultad justa** (lo más rápido y lo que más se nota).
   - Los enemigos dejan de hacerse fuertes cuando tú subes de nivel: así cada nivel se nota.
   - Menos enemigos a la vez, pero más peligrosos, y que avisen antes de atacar (un destello antes de disparar o embestir).
   - Meta: en Normal, un buen jugador aguanta hasta el final; uno que no esquiva, no.
2. **Mapas con obstáculos de verdad.** Rocas grandes, paredes, acantilados y pasillos estrechos para cubrirte de los disparos y hacer que la horda se amontone. Algunas rocas se pueden romper con ki. Cada mapa con su estilo: rocas y casas en Namek, ruinas en la Tierra, columnas en la Sala del Tiempo…
3. **Enemigos variados y fieles a cada saga.**
   - Cada mapa con su propio grupo: Namek con soldados de Freezer, Dodoria, Zarbon y las Fuerzas Especiales; la Tierra con saibamen, la Red Ribbon y los androides; Buu con los secuaces de Babidi (Pui Pui, Yamu, Dabra…). Ya hay sprites nuevos de Zarbon, Burter, Recoome, Pui Pui, Yamu, Babidi y otros en la carpeta 05.
   - Cada tipo con su forma de atacar: los que corren en grupo, los que disparan de lejos, los que embisten, los tanques y los que explotan.
   - Que cada minuto cambie el tipo de horda, para que no sea siempre lo mismo. Más adelante, los bocadillos con frases.
4. **Animaciones.** Primero me dices qué no te gusta. Después pulimos **un solo personaje** (Goku) hasta dejarlo perfecto, te mando el GIF y, cuando te guste, hacemos igual con el resto. Lo que falte se crea con Sprite Fusion o ChatGPT, preparándolo bien para no gastar créditos de más.

## Lo que necesito de ti

- Dime con cuál de los 4 empezamos. Yo empezaría por la dificultad, porque es lo que hoy hace el juego imposible.
- Dime qué no te gusta de las animaciones, aunque sea con un ejemplo («Goku anda raro», «los golpes no se notan»…).
