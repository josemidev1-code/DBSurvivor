# Transformaciones en partida — diseño (borrador para Josemi)

Hablado con Josemi el 20 nov. 2026 (sesión 24). Es un borrador: no se programa hasta que Josemi lo apruebe.
Lo marcado **(propuesta de Claude)** no lo ha decidido Josemi y se puede cambiar.

## Por qué

Josemi quiere un juego «dopamínico»: arrasar hordas con buenos efectos y que los jefes supongan un reto.
Transformarse tiene que ser un subidón que **cueste ganarse**: «si es fácil cargar ki sin que te disparen o te lo dejen difícil, no tiene gracia».
Las transformaciones tienen que ser fieles a la serie, y cada forma ha de notarse distinta.

## Cómo funciona (decidido)

- **Barra de ki.** Se carga manteniendo una tecla: el personaje se queda quieto y no ataca. El aura atrae a los enemigos, cada golpe recibido quita parte de lo cargado y matar enemigos da muy poco ki. Los jefes castigan al que carga delante de ellos.
- **Se sube forma a forma, cada una con sus tiempos (Josemi, 20 nov.).** «Cargas un tiempo razonable y después ya te transformas en Super Saiyan 1, en Super Saiyan 2, en Super Saiyan 3… cada transformación tiene sus respectivos tiempos, y en todos los personajes».
  - Se carga un tiempo razonable y el personaje se transforma en la primera forma (SSJ1). Ya transformado, vuelve a cargar para subir a la siguiente (SSJ2), y así hasta la última forma abierta, como en la serie.
  - Cada forma de cada personaje tiene **su tiempo de carga y su duración**. **(propuesta de Claude)** Las formas altas cargan más y duran menos. Valores de partida para ajustar jugando: SSJ1 carga 3 s y dura 25 s; cada forma siguiente carga 1,5 s más y dura 3 s menos. Al subir de forma, el tiempo vuelve a empezar con la duración de la nueva.
  - Josemi aprobó el diseño («el diseño está bien… muy bien, la verdad») y pide que lo visual salga de los sprites («tienes que cogerlo de los sprites»).
- **Transformación de unos 20 segundos**, con estallido de aura, temblor de pantalla y cambio al sprite de esa forma. Al acabar vuelve a la forma base y hay que volver a cargar.
- **Personajes de una sola forma: «poder máximo».** Cargan igual y durante unos 20 segundos ganan un aura blanca, más fuerza y su técnica estrella potenciada, sin cambiar de sprite.
- **Auras con PixelFX** (Josemi: «quedará mejor»). Las hojas de `05 - Sprites nuevos encontrados/…/03_Efectos_FX_y_Auras` sirven de modelo de cómo debe verse. Antes de darlas por buenas se manda un GIF a Josemi.
- **(propuesta de Claude)** Las formas se siguen desbloqueando para siempre con el deseo a Shenron del menú. En cada partida, el nivel decide hasta qué forma se puede subir: todas las formas se abren por niveles (decidido por Josemi). **(propuesta de Claude)** Se reparten entre el nivel 5 y el 40 según cuántas formas tenga el personaje (Goku: una cada 4 o 5 niveles; Piccolo: la naranja hacia el nivel 20). Se ajustará con el simulador de partidas.

## Prioridad: los personajes principales primero

Josemi: «primero lo que quiero tener son los personajes más icónicos de la serie, tenerlos bien animados y jugables. Y después ya seguiremos con los otros».

Personajes principales: Goku, Vegeta, Gohan, Piccolo, Krilin, Trunks, Goten, Freezer, Cell, Majin Buu y Broly.

**Orden de trabajo (Josemi, 20 nov.):** primero los principales, solo con lo que sale en la serie; después el resto de personajes de la serie; y al final los fanmade y similares («primero vamos a centrarnos con todos los de la serie y después ya fanmade y todos esos»).

### Formas y mejoras de los principales (propuesta de Claude)

Cada forma tendría una mejora propia sacada de la serie, en vez del +25 % igual para todas. Se ordenan como pasan en la serie.

| Personaje | Formas en orden de la serie | Mejora de cada forma |
|---|---|---|
| **Goku** | Base → Kaioken → SSJ → SSJ2 → SSJ3 → SSJ Dios → SSJ Blue → UI Señal → UI Dominado (aparte: SSJ4 GT) | Kaioken: mucho daño, pero pierde vida poco a poco. SSJ: equilibrada. SSJ2: los golpes sueltan rayos que saltan a otro enemigo. SSJ3: daño enorme, pero dura menos. Dios: se regenera y va más rápido. Blue: ki muy fuerte, pero gasta la barra deprisa. UI Señal: esquiva sola parte de los golpes. UI Dominado: esquiva casi todo y contraataca. SSJ4: fuerza bruta y aguante. |
| **Vegeta** | Base → SSJ → Super Vegeta → Majin Vegeta → SSJ Dios → SSJ Blue → Blue Evolution → Ultra Ego (aparte: SSJ4 GT) | Super Vegeta: más fuerza y algo más lento. Majin: más daño, pero recibe más daño. Ultra Ego: cuanto más daño recibe, más fuerte pega. |
| **Gohan** | Base → SSJ → SSJ2 → Definitivo → Bestia | SSJ2: rayos y furia. Definitivo: sube todo sin pegas. Bestia: más daño cuanto menos vida le queda. |
| **Piccolo** | Base → Naranja | Base: se regenera. Naranja: mucha más vida y fuerza bruta. |
| **Trunks** | Base → SSJ → SSJ2 (manga) | Hoy tiene «BASE MANGA» como si fuera otra forma; se quitaría de la cadena. |
| **Freezer** | 1ª → 3ª → Final → 100 % → Golden → Black | 100 %: muy fuerte, pero se cansa. Golden: enorme, pero gasta la barra muy rápido. Black: lo más alto. (No hay sprite de la 2ª forma). |
| **Cell** | Imperfecto → Semiperfecto → Perfecto | Imperfecto: se cura al matar (absorbe). Semiperfecto: más vida. Perfecto: se regenera y su Kamehameha es más fuerte. |
| **Majin Buu** | Gordo → Maligno → Super Buu → Buu Gohan → Kid Buu | Gordo: aguanta mucho. Super Buu y Buu Gohan: absorben (se curan al matar). Kid Buu: se regenera muy deprisa. |
| **Broly** | Contenido → SSJ → Legendario | Legendario: cuanto más dura el combate, más fuerte se hace. |
| **Krilin** | Una forma: poder máximo | Aura blanca y Kienzan potenciado. |
| **Goten** | Una forma (SSJ): poder máximo | Hoy no tiene forma base, solo SSJ. |

### Dudas para Josemi

1. ~~Lista de principales~~: resuelta, son los 11 de arriba.
2. ~~Formas inventadas por fans~~: resuelta. Cell Golden, Cell Majin y Broly SSJ4 salen de la cadena de los principales y se tratan más adelante, junto con los fanmade.
3. ~~Muchas formas~~: resuelta. Josemi: «todas por niveles». En cada partida se empieza con las primeras formas y cada pocos niveles se abre la siguiente, en el orden de la serie; solo se puede subir hasta la forma abierta.

Diseño aprobado por Josemi el 20 nov. 2026.

## Todos los personajes (118 en la pantalla de selección)

Con varias formas (los principales están en la tabla de arriba):
- Bardock: Base, SSJ, SSJ4 · Bardock Leyendas: Base, SSJ, Black, Evolución
- Vegetto: Base, Super Vegetto, Super Vegetto 2, Blue · Gogeta: Super Gogeta, SSJ4, Blue
- Goku Black: Base, SSJ, Rosé · Black Time Breaker: Dios, Rosé, Rosé 3
- Kefla: SSJ, Blue · Kale: Base, Berserker · Kyabe: Base, SSJ · Raditz: Base, SSJ · Bra: Base, SSJ · Turles: Base, SSJ maligno
- Frost: 1ª forma, final · Zamasu: Base, fusionado · Jiren: Base, máximo poder, Hakaishin
- Gohan DBS: Base, Místico, UI, MUI, Bestia · Goku saga Moro: Base, SSJ, Dios, Blue, UI · Goku película Broly: Base, SSJ, Dios, Blue perfecto · Vegeta Blue manga: Blue, Blue perfecto
- Goku Xeno: Base, Dios, SSJ4 · Vegeta Xeno: Base, SSJ4 · Goku Yardrat: Base, SSJ · Trunks niño: Base, SSJ
- Saiyans zombi: Gohan, Goku, Vegeta
- Fanmade: Goku fanmade (13 formas), Goku Black fanmade (7), Vegetto fanmade (4), Gogeta fanmade (3), Broly fanmade (2)

Con una sola forma (poder máximo): Krilin, Yamcha, Goten, Tenshinhan, Androides 13, 14, 16, 17, 18 y 21, Gotenks, Caulifla, Maestro Roshi, Saibaman, Cooler, Metal Cooler, Janemba, Bills, Hit, Toppo, Moro, Baby Vegeta, Gohan poseído, Gohan manga, Gohan del futuro, Cumber, DLRX, Nappa, Ginyu, Ginyu (cuerpo de Goku), Jeice, Guldo, Uub, Mr. Satán, Dyspo, Kibito, Kibitoshin, Supremo Kaioshin, Glorio, Hatchiyack, Trunks GT, Trunks armadura, Pan GT, Nuova Shenron, Omega Shenron, Super 17, Rey Gomah, Merus, Majin Kuu, Majin Duu, Bulma, Magetta, Gran Sacerdote, Paragus, Granola, Gas, Lord Slug, Tarble, Rey Cold, Cui, Videl, Goku niño, Tao Pai Pai, Tora, Vegeta Yardrat, Goku patrullero, Goku Black Kaioshin, Jiren (torneo) y las versiones sueltas de una forma (Goku SSJ4 Daima, Goku SSJ Kaioken, Goku UI verdadero, Goku SSJ chaqueta, Vegeta UI dominado, Vegeta Blue maligno, Vegeta SSJ3 Daima, Vegetto Blue, Vegetto SSJ falso, Bra Majin SSJ, Zamasu fusionado).
