> **Referencia de diseño, solo inspiración.** Análisis del 27 nov. 2026 de las mecánicas de PokéSurvivor (pokesurvivor.com), sacado de sus guías públicas y de partidas como invitado. Se pueden reutilizar las ideas de mecánica, nunca su código, nombres ni recursos. Las cifras pueden haber cambiado desde entonces.

# PokéSurvivor: informe de mecánicas para inspirar tu propio juego

*Análisis de diseño · 27-11-2026 · fuentes: guías públicas de pokesurvivor.com y una sesión de juego observada como invitado*

**Cómo leer las etiquetas.** Cada dato lleva su origen:

- **[G]**: lo dicen las guías oficiales de la web (/guia, /movimientos, /tipos, /objetos, /jefes, /legendarios, /eventos, /poderes, /shinies, /mejoras, /maestria, /logros, /pokedex).
- **[N]**: lo dice la página de Novedades, el registro de cambios fechado. Es más reciente que algunas guías y a veces las contradice.
- **[P]**: lo vi en la partida de prueba (4 partidas cortas como invitado, la más larga de 2:06).
- **[I]**: es inferencia o cálculo mío. No lo dice ninguna fuente tal cual.

Cuando una guía y Novedades no coinciden, lo indico y doy por vigente la versión más reciente, si la partida observada la respalda.

---

## 1. Resumen

PokéSurvivor es un juego de fans gratuito, de navegador (PC, tablet y móvil, instalable como PWA), del género *survivors* (Vampire Survivors, Survivor.io), con la estética de Pokémon Mundo Misterioso [G]. Eliges un Pokémon compañero y aguantas en un mapa infinito mientras te rodean hordas que no paran de crecer. El ataque es automático [G].

Su rasgo distintivo es que **solo dispara el movimiento activo**: llevas hasta 4 y eliges cuál con 1-4 o Q/E [G][P]. Eso convierte el género, que suele jugarse sin manos, en uno de posicionamiento más una decisión táctica continua: qué tipo de ataque usar contra quién y con qué clima.

El resto del bucle sigue la fórmula conocida. Recoges experiencia del suelo y en cada nivel eliges 1 de 4 cartas: un movimiento nuevo, una mejora de un movimiento, una stat o una evolución [G][P]. La partida sigue un **calendario fijo** [N]:

- jefes en los minutos 2, 6, 10, 14 y 18;
- grietas legendarias opcionales en los minutos 4, 8, 12, 16 y 25;
- Eternatus en el minuto 20, que hace de "examen": si lo vences eliges un poder de transformación;
- la Sentencia de Arceus en el minuto 30, un jefe imbatible que sirve de puntuación.

Fuera de la partida hay de todo:

- Pokémonedas para mejoras permanentes de cada Pokémon, con un techo bajo (unas 1,3 veces más poder) [G];
- tickets para un gacha que no se paga con dinero real [G];
- maestría cosmética por Pokémon, misiones, 149 logros y rankings;
- cooperativo de hasta 4 jugadores.

---

## 2. Bucle de partida

### 2.1 Segundo a segundo (microbucle)

1. **Moverte y esquivar.** La guía aconseja no pararse y moverse en círculos amplios para que la horda te siga en fila [G].
2. **El ataque activo dispara solo**: por defecto al enemigo más cercano, o a mano si lo activas en Accesibilidad [N][P].
3. **Los enemigos caen y sueltan cosas**: cristales azules de experiencia, monedas, a veces tickets, bayas, esferas o un imán [P].
4. **Hay que ir a recoger.** El radio de recogida inicial es pequeño: en la partida 1, quieto, seguía en nivel 1 a los 0:40 [P].
5. **La barra de experiencia se llena** y el juego se pausa con 4 cartas [P].
6. **Eliges** y sigues.

Mientras tanto vas tomando decisiones de fondo [G][P]:

- si cambias de ataque (por la tabla de tipos, por el clima o para cargar un movimiento de mejora);
- si usas una esfera (teclas 5-8);
- si sales de las zonas marcadas en el suelo antes de que se llenen;
- si te desvías hacia un cofre, un altar o un manantial.

**Ritmo observado [P].** En la partida 4:

- subidas de nivel en 0:17, 0:18, 0:25, 0:27, 0:29, 0:34, 0:37, 0:48, 0:57, 1:28 y 1:46 (nivel 12);
- 173 derrotados en 2:06, unos 1,4 por segundo [I];
- mareas de Pokémon hacia 0:32 y 1:27.

Las mejores partidas del ranking pasan de 12 derrotados por segundo [N].

### 2.2 Minuto a minuto (0 a 30 y más)

| Minuto | Qué pasa | Fuente |
|---|---|---|
| 0:00 | Empiezas con 1 movimiento (2 con la mejora Repertorio) y 1 hueco de objeto. Las hordas entran sin parar por los bordes. | [G][P] |
| Cada <1 min | Mareas de Pokémon: oleadas extra sobre el flujo normal. En las partidas observadas, la primera llegó entre 0:32 y 1:15. | [G][P] |
| 2:00 | Primer jefe del calendario. En la partida observada fue Inteleon, con barra propia y furia a media vida. | [G][N][P] |
| 2-4 | Puede aparecer el primer ladrón de monedas (Meowth o Gholdengo). Como mucho salen 2 por partida. | [G] |
| 3:00+ | Puede activarse un clima natural de 55-75 s. | [G] |
| 4:00 | Primera grieta legendaria (opcional). | [N] |
| 4-5 | Primer evento de la rotación (horda de un tipo, hora dorada, Pokémon perdido o Munchlax). Los siguientes llegan 4-5 min después de que acabe el anterior. | [G] |
| 6 / 10 / 14 / 18 | Jefes del calendario 2 a 5, cada uno más duro que el anterior. | [G][N] |
| 8 / 12 / 16 | Grietas 2 a 4. Tras la 3.ª (minuto 12), los Pokémon con formas alternativas pueden elegir una. | [N][G] |
| Nivel 20 | Primera evolución opcional del Pokémon. La guía general dice nivel 12, pero ha cambiado. Ver 3.5. | [N][P] |
| 20:00 | **Eternatus Eternamax.** Viajas a su arena y lo que quede en el suelo se pierde. Tiene 3 fases y un golpe final. En solitario, perder es el fin de la partida. Ganar da ticket ×10, 600 Pokémonedas, botín y un poder; además desbloquea la dificultad siguiente. | [G][N] |
| 20-30 | Vuelves al mapa con el poder (tecla F) y la presión sigue subiendo. | [G] |
| 25:00 | Grieta "de recuperación": solo da vínculo si perdiste alguna de las anteriores. | [N] |
| Nivel 40 | Segunda evolución opcional (antes nivel 24). | [N] |
| 30:00 | **Sentencia de Arceus** (en Halloween la sustituye un gran Gengar bruja). No se puede ganar: termina cuando caes. | [G] |
| 30-40+ | Arceus suma un ataque cada 30 s hasta tenerlos todos a los 2:30 de Sentencia. Rompe un objeto a los 2, 4 y 6 min (y a los 8, si llevas un cuarto). Añade carriles de aspas a los 5 y 7 min. Desde el minuto 10 de Sentencia (≈40:00 de partida), su contacto deja KO. La guía llama a ese punto "cosa de leyendas". | [G][N] |

**[I] El pulso de la partida.** Entre el minuto 2 y el 18 hay siempre un pico cada 2 minutos, alternando jefe (2, 6, 10, 14, 18) y grieta (4, 8, 12, 16). Encima van una marea por minuto, un evento cada 4-5 minutos y climas de algo más de un minuto. El jugador nunca pasa mucho tiempo sin un objetivo nuevo a la vista.

---

## 3. Sistemas

### 3.1 Controles, movimiento y cámara

**Cómo funciona**

- **PC.** WASD o flechas para moverte; 1-4 eligen ataque; Q y E (o Tab) pasan al anterior o al siguiente; F usa el poder; 5-8, las esferas; P o Esc pausan [G][P].
  - En la pantalla de cartas: 1-9 eligen, R cambia las opciones y Espacio salta la animación [P].
  - Todas las teclas se pueden reasignar, con dos por acción [N][P].
- **Mando** (Xbox, PlayStation, Switch, USB o Bluetooth), con vibración al recibir daño. Según Novedades del 14-11, el poder va en B y X queda para la esfera elegida. La guía de poderes todavía dice X; parece desactualizada [N][G].
- **Móvil.** Se juega en horizontal. El joystick es flotante (aparece donde tocas), anclado o fijo, y los botones se pueden recolocar. Para activar un ataque tocas su icono [G][N].
- **Apuntado.** Por defecto es automático al enemigo más cercano. En Accesibilidad hay "Apuntar a mano": con ratón o stick derecho, y en el móvil con un segundo joystick en la mitad derecha [N][P].
- **No hay esquiva básica confirmada.** La movilidad sale de movimientos de embestida y desplazamiento (Ataque Rápido, Nitrocarga, Velocidad Extrema, Agilidad) y de stats de velocidad (mejora Zancada, carta Carrera, Pañuelo Elección, Rapidosfera) [G][I].
- **Cámara.** Se aleja con la Luminosfera, con el Dinamax y en las arenas de grieta [N][G].

**Por qué funciona.** Con un solo eje de movimiento y una decisión discreta (qué ataque está activo), se juega igual de bien con teclado, mando o pantalla táctil. El apuntado automático por defecto mantiene la accesibilidad del género, y el manual da techo de habilidad a quien lo quiera.

### 3.2 Ataque automático con un único movimiento activo

**Cómo funciona**

- **Solo ataca el movimiento seleccionado** [G]. Lo confirmé en la partida 1: aprendí Fuego Fatuo, Lanzallamas y Llamarada sin activarlos, y la pantalla final les puso 0 de daño a los tres [P].
- **Hay 4 huecos** de movimiento (teclas 1-4) [P]. Al aprender un ataque nuevo no se cambia a él solo; sigues con el que tenías [N].
- **Atajos.** Desde el menú de Mejoras se puede fijar qué movimiento ocupa cada hueco [P].
- **Cosas que solo tienen sentido con un único ataque activo:**
  - *Movimientos de mejora* (Danza Espada, Maquinación, Agilidad, Fortaleza, Acua Aro…). No hacen daño; acumulan una stat mientras están activos. Invitan a cargar y luego cambiar al ataque [G][P].
  - *Climas lanzados* (Día Soleado, Danza Lluvia). Duran un rato "aunque cambies de ataque". Lo comprobé con Día Soleado y volviendo después a Ascuas [G][P].
  - *Cinta Elección*: +40 % de daño, pero no puedes cambiar de movimiento [G].
  - *Metrónomo*: +6 % de daño por cada 3 s seguidos con el mismo ataque, hasta +48 % (unos 24 s). Se pierde al cambiar [G].
  - *Espray Bucal*: al cambiar de ataque, +25 % de Ataque Especial durante 8 s, como mucho cada 12 s [G].
  - *Acróbata*: ×1,5 de daño si no llevas ningún objeto [G].
- **Vínculos.** Cada legendario que vences en una grieta te da un vínculo. Un vínculo une dos movimientos en un solo hueco y los lanza a la vez; se pueden tener hasta 4 [N]. La carta Quitamovimientos avisa: "si estaba Fusionado, el nuevo ocupa su sitio" [P].

**Por qué funciona.** Recupera una decisión activa en un género que suele ser pasivo, y es lo que hace que la tabla de tipos importe de verdad: si todo disparase a la vez, el tipo daría igual. Los objetos crean dos estilos de build enfrentados: el especialista (Cinta Elección, Metrónomo) y el que rota (Espray Bucal, mejoras que se cargan). Los vínculos devuelven poco a poco el caos de "todo dispara a la vez", pero como premio a medio plazo por los desafíos opcionales.

### 3.3 Fórmula de daño: stats, físico y especial, monotipo, críticos

**Cómo funciona**

- **Stats al estilo Pokémon**: Vida, Ataque, Ataque Especial, Defensa, Defensa Especial y Velocidad [N].
  - En la ficha de Charmander [P]: Vida 88, Ataque ×0,89, At. Esp. ×1,03, Defensa 47, Def. Esp. 50, Velocidad 105.
  - Su naturaleza era Osada (+Defensa, −Ataque) [P]; que sea aleatoria es suposición mía [I].
  - Su habilidad, Mar Llamas: +35 % de daño de Fuego con menos de 1/3 de la vida [P].
- **Físico y especial.** Los físicos escalan con Ataque y los especiales con Ataque Especial [G]. El movimiento que usa tu stat ofensiva más alta pega al 100 %; el otro, en proporción [G]. Se puede escribir así: multiplicador = stat que usa ÷ máx(Ataque, At. Esp.) [I].
  - **Comprobado [P+I]**: la carta de un movimiento físico decía "Con Charmander rinde un 87 %", y 0,89 ÷ 1,03 = 0,864.
- **Sesgo de cartas.** Los ataques de tu categoría fuerte salen el doble de a menudo, y cada carta indica cuánto rinden con tu Pokémon [N][P].
- **Defensas enemigas.** Reducen tus golpes físicos con su Defensa y los especiales con su Defensa Especial, con un efecto pequeño. Cada enemigo te ataca con su lado fuerte y tú te defiendes con tu Defensa o tu Defensa Especial [G][N].
- **Monotipo.** Los Pokémon de un solo tipo hacen +20 % de daño con los ataques de su tipo [N][P]. No se menciona un bonus general por mismo tipo (STAB).
- **Críticos.** El daño base del crítico es ×1,5 [G].
  - Cartas en partida: Ojo Crítico da +2 % de probabilidad y Golpe Brutal +5 % de daño crítico [P][N].
  - Topes: 60 % de probabilidad y ×3,5 de daño [N].
  - Mejoras permanentes: Golpe Crítico +1 % y Crítico Potente +5 % por nivel [G].
- **Reducción de daño.** Tope del 80 % [N]. Contra Arceus solo cuenta hasta un 30 % (ver 3.14).
- **Transparencia.**
  - La pausa muestra cada ataque con su categoría, daño total y daño por segundo, y todas tus stats: vida, ataque, defensa con su % de reducción, crítico, recarga y regeneración [P].
  - La pantalla final repite la tabla de daño de cada ataque [P].
- **Muchas capas de multiplicadores sin regla publicada** [I]. Proporción de stat, tipo (con tope de ×2,4), clima, monotipo, Tera, objetos, cartas, Triturar o Acróbata. La web no dice si se suman o se multiplican.

**Por qué funciona.** Ningún movimiento queda inútil, pero los que encajan con el Pokémon salen ganando. El "% de rendimiento" en la carta enseña la regla sin tutorial. Las tablas de daño por segundo en la pausa y al final convierten cada partida en un experimento que el jugador puede leer.

### 3.4 Experiencia, niveles y cartas

**Cómo funciona**

- **La experiencia hay que recogerla** del suelo [G][P]. El radio de recogida mejora con:
  - la carta Imán (+25 % de radio) [P];
  - la mejora permanente Imán (+12 % de recogida por nivel) [G];
  - el altar de imán (×4) [G];
  - los imanes que caen al suelo [P].
- **Curva de experiencia.** El 14-11 cada nivel pasó a pedir un tercio de lo que pedía, y el 16-11 bajó otro 25 %. En total, ≈1/4 del coste original [N].
- **4 cartas por nivel** (antes 3) [N][P]. Las cartas no se pueden pulsar durante un instante al aparecer, para evitar clics por error [N].
- **Tipos de carta que vi** [P]:
  - *Nuevo*: muestra tipo, Físico o Especial y el % de rendimiento.
  - *Nv. A > B*: mejora concreta del movimiento.
  - *Mejora*: una stat.
  - *EVOLUCIÓN*: dorada.
  - *Quitamovimientos*: cambias un movimiento por otro de tu Pokémon (empieza en nivel 1) o dejas el hueco libre.
- **Cartas especiales según las guías:**
  - *Cuarto objeto*: carta muy rara que solo sale si ya llevas 3 objetos [G][N].
  - *Sabiduría*: rara, +15 % de experiencia, una vez por partida [N].
  - *Ataques exclusivos* del Pokémon: carta especial desde el nivel 10. Hay 39 [N].
  - *Poder rápido*: reduce la recarga del poder [N].
- **Valores de las cartas de stat vistas** [P]:

| Carta | Efecto por copia | Tope |
|---|---|---|
| Potencia | +8 % de daño | sin tope [N] |
| Reflejos | −5 % de recarga | sin tope, rinde menos con cada copia [N] |
| Vigor | +20 de vida máxima (y la recupera) | sin tope [N] |
| Síntesis | +0,6 de vida por segundo | sin tope [N] |
| Carrera | +5 % de velocidad de movimiento | sin tope [N] |
| Imán | +25 % de radio de recogida | sin tope [N] |
| Ojo Crítico | +2 % de probabilidad de crítico | sin tope de copias; crítico total máx. 60 % [N] |
| Golpe Brutal | +5 % de daño crítico | sin tope de copias; daño crítico máx. ×3,5 [N] |
| Cazador | +6 % de daño a jefes, legendarios y Eternatus | sin tope [N] |
| Aprendizaje | +8 % de experiencia | hasta 15 copias [N] |
| Esquiva | +3 % de probabilidad de esquivar golpes y disparos | con tope [N] |
| Coraza | (defensa; no vi la cifra) | sin tope; reducción total máx. 80 % [N] |
| Racha de suerte | más monedas (sin cifra) | con tope [N] |
| Baya Zidra (carta) | recupera el 45 % de la vida al momento | — |

- **Subidas de movimiento: el máximo es el nivel 5** [G]. Cada nivel trae una mejora concreta, no un "+10 %" genérico [P]:
  - Ascuas: 1 > 2 da +1 proyectil; 2 > 3, +45 % de daño; 3 > 4, −25 % de recarga; 4 > 5, +1 proyectil y +1 de perforación.
  - Fuego Fatuo, 1 > 2: +50 % de daño. Día Soleado, 1 > 2: +35 % de duración.
- **Control del azar.**
  - *Cambiar opciones*: 1 por partida sin mejoras ("Cambiar opciones (1) · R"), que desaparece al gastarlo [P]. La mejora permanente Cambio de cartas suma +1 por nivel, hasta +5 [G].
  - *Veto*: bloquea movimientos para que no salgan en las cartas, hasta 5 (antes 3) [G][N].
- **Fuentes de nivel instantáneo.** El cofre con candado da justo la experiencia de un nivel [G] (en grupo se reparte: 1/2, 1/3 o 1/4 [N]). El Caramelo Exp. da +1 nivel [G].

**Por qué funciona.** Cuatro cartas, más los cambios y los vetos que compras con la meta, hacen que el control sobre el azar crezca a medida que inviertes. Las mejoras concretas por nivel ("+1 proyectil", "−25 % recarga") se entienden en un segundo y hacen que cada nivel se note. Las cartas sin tope y con rendimiento decreciente evitan los callejones sin salida de las partidas largas.

### 3.5 Evolución del Pokémon en plena partida

**Cómo funciona**

- **Niveles.** La guía general [G] dice que al llegar a los niveles 12 y 24 decides si tu Pokémon evoluciona. Novedades del 13-11 [N] cambió esos puntos a los **niveles 20 y 40**, porque con la nueva curva de experiencia llegan "más o menos al mismo minuto".
  - **La partida lo apoya [P]**: llegué al nivel 12 a 1:46 y solo me salieron cartas normales. Doy por vigentes los niveles 20 y 40.
- **Si no evolucionas**, solo te suben las stats. Los Pokémon sin evolución también se refuerzan en esos niveles [G][N].
- **Cartas.** Si hay más de cuatro evoluciones posibles (Eevee), salen más cartas. Las cartas de evolución y de forma muestran la diferencia de stats ("±0" en lo que no cambia) [N].
- **Nivelado entre Pokémon** [N]:
  - los que ya están evolucionados empiezan con la fuerza de su primera fase y alcanzan la suya en el nivel 40;
  - los que no evolucionan empiezan con el 65 % de sus stats.
- **Efectos colaterales.** La maestría va al Pokémon que elegiste al empezar [G]. El poder se adapta a la nueva especie [N]. El Quitamovimientos sirve para rehacer la build si al evolucionar cambias de tipo [N].

**Por qué funciona.** Es un subidón de poder con carga emocional a mitad de partida. Nivela el roster: un Pokémon "fuerte" y uno "débil" empiezan parecidos, así que elegir compañero es cuestión de gusto. Y deja una salida estética a quien quiera conservar la forma que le gusta.

### 3.6 Evolución de movimientos

**Cómo funciona**

- **Receta: movimiento al nivel 5 más una carta de stat concreta** [G]. Cuando tienes las dos cosas, aparece una carta dorada de EVOLUCIÓN.
  - En la partida 4 [P], la carta Potencia salió antes con la etiqueta "Evoluciona Ascuas". Con Ascuas al nivel 5 y Potencia, a los 1:28 salió "Ascuas → Ascuas+": ×1,8 de daño, +2 proyectiles, +2 de perforación y proyectiles más grandes.
- **Resultado.** El movimiento conserva el nombre con un "+" y un borde dorado [N][P]. La guía general dice que "Ascuas se convierte en Llamarada"; está desactualizada (según la tabla de /movimientos, Llamarada tiene su propia evolución, "Llamarada +") [G].
- **Cartas que piden las evoluciones**: 7 cartas para los 149 movimientos que evolucionan [G].

| Carta | Nº de evoluciones que la piden |
|---|---|
| Potencia | 53 |
| Reflejos | 29 |
| Carrera | 24 |
| Síntesis | 17 |
| Coraza | 12 |
| Vigor | 10 |
| Imán | 4 |

  - [I] El reparto sigue más al tipo y a la clase del ataque que al "tema" de la carta. Potencia la piden 12 de 13 cuerpo a cuerpo. Carrera, 7 de los 9 de Volador. Síntesis, 5 de los 7 de Veneno que evolucionan. Reflejos, 5 de 8 teledirigidos y 3 de 5 de carga.
- **Recuento.** De 176 movimientos evolucionan 149; no lo hacen 27: los 15 de estado y 12 de daño [G]. Los ataques característicos de legendarios (Aerochorro, Fuego Sagrado, Distorsión…) evolucionan desde el 19-11 [N].
- **Plantillas por clase.** El bonus de evolución depende del arquetipo, no del movimiento en concreto, con multiplicadores de ×1,6 a ×1,9 [G/I]. Detalle en 3.7.
- **Logros** por evolucionar 1, 25 y los 149 movimientos [G].

**Por qué funciona.** Es la receta arma + pasiva de Vampire Survivors, pero **legible**: la carta de stat te avisa de qué evoluciona. El jugador no necesita una wiki para descubrir combinaciones; las va viendo en la propia oferta de cartas. Que haya 149 evoluciones da un objetivo de colección dentro del combate.

### 3.7 Catálogo de movimientos y arquetipos

**Cómo funciona**

- **176 movimientos** en 18 tipos: 73 físicos, 88 especiales y 15 sin daño [G]. Todos los tipos tienen al menos 5 [N].
  - Por número total, Normal tiene más (17) y Hada menos (7).
  - Contando solo los que hacen daño, va primero Fuego (13) y último Hada (6) [I].
- **Cada Pokémon tiene su repertorio.** El de Charmander tiene 26 movimientos [P].
- **MT.** La Tienda Kecleon vende 8 al día, iguales para todos, a 400-870 Pokémonedas. Enseñan para siempre ataques de fuera del tipo, pero solo si el Pokémon puede aprenderlos en los juegos oficiales [N][P].

**Arquetipos (clases) y su evolución [G]:**

| Clase | Qué hace | Nº | Al evolucionar |
|---|---|---|---|
| Cuerpo a cuerpo | Arco frente al Pokémon (algunos empujan, paralizan o debilitan) | 13 | ×1,9, más alcance, golpea en 360° |
| Proyectil | Disparo al enemigo más cercano; a menudo perfora o aplica estado | 18 | ×1,8, +2 proyectiles, +2 perforación, más grandes |
| Ráfaga | Proyectiles en todas direcciones | 11 | ×1,6, +6 proyectiles, +1 perforación |
| Teledirigido | Proyectiles que persiguen | 10 | ×1,8, +2 proyectiles, más grandes |
| Embestida | Te lanzas y dañas todo el trayecto (también sirve para moverte) | 9 | ×1,9, más distancia, menos recarga |
| Meteoros | Caen del cielo sobre los enemigos cercanos | 8 | ×1,7, +2 meteoros, más radio |
| Rayo | Rayo en línea recta | 8 | ×1,8, +50 % de grosor, más largo |
| Carga | Se carga un momento y suelta un rayo enorme que lo atraviesa todo | 5 | ×1,8, +50 % de grosor, carga más rápida |
| Giro | Giras golpeando todo lo que te rodea | 7 | ×1,8, +1 vuelta, más radio |
| Aura | Campo de daño permanente a tu alrededor | 7 | ×1,8, +35 % de radio |
| Órbita | Orbes que giran a tu alrededor | 4 | ×1,7, +2 orbes, más radio |
| Rebote | Proyectil que rebota de enemigo en enemigo | 7 | ×1,8, +2 rebotes, +1 proyectil |
| Cadena | Rayo o maldición que salta entre enemigos | 3 | ×1,7, +3 saltos |
| Saltos en cadena | El propio Pokémon salta de enemigo en enemigo sin que lo toquen | 1 | ×1,7, +3 saltos |
| Empujón | Onda que daña y aparta a los cercanos | 6 | ×1,8, más radio, empuja más |
| Aturdir | Golpe de área que aturde, paraliza, congela o atrapa (casi todos marcan antes la zona) | 6 | ×1,8, más radio, aturde más rato |
| Abanico | Cono corto de disparos | 5 | ×1,7, +4 disparos, +1 perforación |
| Puñetazo | Combo de 3 directos; el último con efecto | 5 | ×1,8, +2 directos |
| Bumerán | Va y vuelve cortando | 4 | ×1,8, +1 bumerán, más alcance |
| Remolino | Vórtice que atrae hacia su centro | 3 | ×1,8, más radio, atrae más |
| Minas | Trampas que estallan o atrapan al pisarlas | 3 | ×1,8, +2 minas, explosión mayor |
| Torreta | Invocación fija que dispara sola | 2 | ×1,8, +1 a la vez, dispara más rápido |
| Tormenta | Rayos sobre muchos enemigos de la pantalla | 2 | ×1,7, +3 rayos, más radio |
| Rastro | Deja charcos dañinos al moverte | 2 | ×1,8, charcos más grandes y duraderos |
| Cruz | Explosión en cruz sobre un enemigo | 2 | ×1,8, brazos más largos |
| Temblor | Anillo que se expande desde ti | 2 | ×1,8, +30 % de radio |
| Terremoto | Ondas en línea, una tras otra | 2 | ×1,8, +3 ondas |
| Salto | Saltas sobre el enemigo y haces una onda al caer | 2 | ×1,8, onda mayor |
| Tijera | Dos tajos en X; el centro recibe ambos | 2 | ×1,8 (solo Tijera X) |
| Onda dirigida (Surf) | Ola hacia donde apuntas que arrastra enemigos | 1 | ×1,8, ola más ancha |
| Explosión | Gran explosión que cuesta el 25 % de tu vida actual (nunca KO) | 1 | ×1,8, +30 % de radio |
| De estado | Mejora acumulativa (7), Protección, Doble Equipo, Descanso, Reflejo, Pantalla Luz y 3 de clima | 15 | no evolucionan |

- **Detalles de los movimientos de estado** [G]:
  - Protección: 1,5 s de invulnerabilidad, recarga de 7 s, que nunca baja de 5 s.
  - Reflejo y Pantalla Luz: −35 % al daño físico o al especial.
  - Doble Equipo: deja un señuelo.
  - Descanso: cura mucho, pero te deja dormido.
- **Estados alterados** [G][N]:
  - *Daño y control*: quemadura; veneno (quita un % de la vida, menos contra enemigos de muchísima vida); varios grados de ralentización.
  - *Inmovilización*: aturdir, paralizar, congelar, atrapar y sueño.
  - *Vulnerabilidad*: Triturar hace que el enemigo reciba +25 % de daño durante 4 s.
  - *Desplazamiento*: empuje y atracción.
  - *Otros*: drenaje de vida y charcos persistentes.
  - *Sinergia*: Infortunio pega más a quemados, envenenados o frenados.
- **Nerfs del registro** [N]. Dejan ver qué rompe el género:
  - *Ataques que persiguen*: giran con la mitad de fuerza, empiezan a buscar más cerca y solo van a por lo que tienen delante.
  - *Surf*: −28 % de daño y luego −60 %, y su alcance bajó de 560 a 360.
  - *Puño Meteoro*: daño base de 34 a 24.

**Por qué funciona.** Con un único ataque activo, cada clase es un **verbo** que cambia cómo te mueves: el rastro premia correr, el aura premia meterse en la horda, la carga premia pararse un instante y la embestida es también movilidad. Las evoluciones por plantilla abaratan el contenido: 31 fórmulas cubren 149 evoluciones.

### 3.8 Tipos y clima

**Tabla de tipos [G]**

- Son los 18 tipos de los juegos, pero con los multiplicadores **comprimidos** para que tu único ataque nunca quede inútil:

| Relación | En los juegos | En PokéSurvivor |
|---|---|---|
| Súper eficaz | ×2 | ×1,6 |
| Poco eficaz | ×0,5 | ×0,6 |
| Inmune | ×0 | ×0,3 |

- **Doble tipo.** Se multiplican los dos factores, con tope de ×2,4 (1,6 × 1,6 = 2,56 se queda en 2,4).
  - [I] Salen combinaciones curiosas: súper eficaz más resistido da ×0,96 (en los juegos sería neutro); inmune más débil da ×0,48; el mínimo posible es ×0,18.
- **Vale en los dos sentidos**: para tus ataques contra ellos y para los suyos contra ti.
- Con la guía en la mano, la tabla coincide con la moderna de los juegos (con Hada) traducida a estos multiplicadores.

**Clima [G][N][P]**

| Clima | Potencia | Penaliza |
|---|---|---|
| Sol abrasador | Fuego ×1,5 | Agua ×0,5 |
| Lluvia | Agua ×1,5 y Eléctrico ×1,2 | Fuego ×0,5 |
| Tormenta de arena | Roca, Tierra y Acero ×1,3 | daño progresivo a los demás tipos |
| Nevada | Hielo ×1,5 | desgasta y ralentiza a los que no son de Hielo |
| Niebla | Fantasma, Hada y Psíquico ×1,3 | reduce tu campo de visión |

- **Cómo se activa:**
  - de forma natural, desde el minuto 3, durante 55-75 s [G];
  - con movimientos (Día Soleado, Danza Lluvia, Tormenta Arena), y el clima sigue aunque cambies de ataque [G][P];
  - con habilidades (Sequía, Llovizna, Chorro Arena, Nevada), también en cooperativo [N];
  - con algunas Megas y formas primigenias [G];
  - por la arena de cada grieta [G];
  - por la condición del desafío semanal. Esta semana era "Siempre llueve" [P].
- **Afecta a los dos bandos.** La Gafa Protectora te quita las penalizaciones del clima y conserva los bonus [G].
- **[P]** Con Día Soleado, los números de daño de Ascuas subieron a 92-134 por golpe.
- **Más sistemas que juegan con el tipo:**
  - la Tabla aleatoria de Arceus [G];
  - el evento Horda de un tipo [G];
  - las 18 arenas de grieta [G];
  - el Teracristal [G].

**Por qué funciona.** Comprimir la tabla mantiene la decisión ("cambia al ataque eficaz") sin castigar con un 0 a quien no tiene opción. El clima cambia las prioridades más o menos cada minuto y da una razón para llevar ataques de varios tipos. Si además puedes provocarlo tú, se convierte en una combinación que el jugador planifica.

### 3.9 Objetos: equipables, consumibles y esferas

**Huecos y fuentes**

- **Huecos** [G]:
  - empiezas con 1;
  - el 2.º se compra con la mejora permanente Segundo objeto (10.000);
  - el 3.º con Tercer objeto (30.000, la mejora "legendaria");
  - el 4.º solo con la carta muy rara, que exige llevar ya 3.
- **Si encuentras uno con los huecos llenos**, eliges cuál cambias o te quedas con los tuyos [G]. En el juego sale como "¡Un objeto! Puedes llevarlo o dejarlo" [P].
- **Duran la partida** [G].
- **De dónde salen:**
  - jefes y legendarios sueltan siempre uno [G];
  - cofres [G][P]: un cofre de madera me dio Guante de Boxeo a los 0:24;
  - el evento de Munchlax [G].
- **Objeto inicial.** Es una mejora permanente (400) que te deja empezar con un objeto comprado en la Tienda Kecleon a 500 Pokémonedas. Gasta una unidad por partida [G][P].
  - En la tienda vi 22 a la venta [P]. Faltan los dos de experiencia (Huevo Suerte y Amuleto Exp.), que la tienda no vende [N][I].

**Los 24 equipables [G]**

| Objeto | Efecto |
|---|---|
| Restos | +1,5 % de vida por segundo |
| Cinta Elección | +40 % de daño; no puedes cambiar de movimiento |
| Garra Rápida | −20 % de recarga (respeta el mínimo de Protección) |
| Banda Focus | Un golpe que te dejaría KO te deja con 1 de vida; recarga de 60 s |
| Cascabel Concha | Robo de vida (sin cifra) |
| Moneda Amuleto | +50 % de Pokémonedas |
| Huevo Suerte | +30 % de experiencia |
| Vidasfera | +30 % de daño; cada ataque cuesta algo de vida |
| Pañuelo Elección | +35 % de velocidad, sin bloqueo |
| Casco Dentado | Daña a quien te golpea cuerpo a cuerpo |
| Chaleco Asalto | 20 % menos de daño recibido |
| Botas Gruesas | Inmunidad a trampas, lava y agua |
| Metrónomo | +6 % cada 3 s con el mismo ataque, hasta +48 % |
| Hierba Copia | Los poderes de los altares duran el doble |
| Capa Furtiva | Anula a los curanderos y escuderos cercanos |
| Guante de Boxeo | +30 % al daño físico cuerpo a cuerpo |
| Supertapones | −30 % de daño de los ataques con aviso en el suelo |
| Espray Bucal | Al cambiar de ataque, +25 % de At. Esp. durante 8 s (como mucho cada 12 s) |
| Dado Trucado | +1 proyectil o golpe en los ataques múltiples |
| Gafa Protectora | El clima no te debilita ni te frena, pero sigue potenciándote |
| Amuleto Exp. | +20 % de experiencia y +10 % de Pokémonedas |
| Incienso Suerte | +60 % de Pokémonedas y −15 % de daño |
| Incienso Raro | Shinies salvajes el doble de frecuentes (en grupo, solo si lo lleva el anfitrión) |
| Gafas Radar | Minimapa con jefes, shinies, cofres, altares, manantiales, objetos y la grieta |

**Consumibles de un solo uso [G]**

- No ocupan hueco.
- **Caramelo Exp.**: +1 nivel.
- **Bayas.** Se guarda como mucho una de cada clase y se activan solas:
  - Zidra: con menos del 25 % de vida, cura un 30 %;
  - Atania: con menos del 25 % de vida, +30 % de daño durante 10 s;
  - Meloc: si algo te frena, te limpia y te hace inmune a los frenazos 5 s.
- **Mochis**, que se aplican al recogerlos y duran toda la partida: +5 % de vida, +5 % de daño, +5 % de velocidad o −5 % de daño recibido.

**Esferas (estilo Mundo Misterioso) [G][N][P]**

- Se llevan hasta 4 distintas, con 3 unidades de cada una [N], y se usan con las teclas 5-8.
- Salen de cofres, de jefes y a veces de enemigos derrotados. Las vi como un orbe verde en el suelo [P].
- A los jefes les afectan menos.

| Esfera | Efecto | A quién |
|---|---|---|
| Soporesfera | Duerme 4 s a los enemigos de la pantalla (jefes, 1 s) | enemigos |
| Ralentosfera | −50 % de velocidad durante 8 s (jefes, −20 %) | enemigos |
| Rafagaesfera | Lanza lejos a los cercanos (jefes, la mitad) | enemigos |
| Focosfera | +25 % de crítico durante 15 s | tú y los compañeros cercanos |
| Luminosfera | Aleja la cámara durante 15 s | tú y los compañeros cercanos |
| Rapidosfera | +40 % de velocidad durante 10 s | tú y los compañeros cercanos |

**En el final.** Arceus rompe un objeto a los 2, 4 y 6 minutos de Sentencia (y el cuarto a los 8). Los objetos de monedas siguen pagando aunque se rompan [G].

**Por qué funciona.** Muchos objetos **cambian las reglas** en vez de sumar stats: bloquear el cambio de ataque, premiarlo, premiar no llevar objeto, quitarte las penalizaciones del clima. Además tienen contrapartidas claras (Vidasfera, Incienso Suerte, Cinta Elección). Las esferas dan "botones de pánico" activos, distintos del equipo pasivo. La escalera de huecos es el gran sumidero de monedas de la meta: 40.400 de los 93.470 de llevar un Pokémon al máximo [I].

### 3.10 Mapa y elementos del escenario

**Cómo funciona**

- **Mapa.** Es infinito [G] y cada partida generó uno distinto [P]. El HUD lo llamaba siempre "Bosque Umbrío" [P]. Según Novedades, el mapa principal repite en ciclo los biomas Bosque, Cueva y Volcán [N].
- **Terreno** [P][G]:
  - hierba, caminos, hierba alta, árboles, rocas y estanques;
  - mesetas y acantilados que cortan el paso;
  - agua que frena y lava que quema (lo que anulan las Botas Gruesas).
- **Altar de poder.** De un solo uso por zona. Al tocarlo te da durante 25 s una de cuatro mejoras: daño ×2, +45 % de velocidad, imán ×4 o −40 % de recarga [G][N].
- **Manantial.** Te cura un 14 % de la vida por segundo mientras estás encima, hasta agotarse; se recarga si estás cerca [G].
- **Cofres:**
  - *de madera*: se abren al tocarlos [P];
  - *con candado*: hay que quedarse 3,5 s junto a ellos; dan monedas, tickets, esferas, objetos y un nivel [G].
- **Trampas.** De veneno, pegajosas y explosivas. Se activan al pisarlas, también con los enemigos, así que puedes llevarlos hacia ellas [G]. Pisé una (una casilla morada con calavera) que soltó cristales y me quitó 9 de vida [P].
- **Dinamax** rompe árboles, rocas, muros y cofres [G][N].

**Por qué funciona.** Los puntos de interés te sacan de tu círculo seguro: hay que elegir entre el kiteo cómodo y desviarte por un cofre, un altar o un manantial, que es riesgo y recompensa en el espacio. Que las trampas afecten a los enemigos convierte el mapa en una herramienta.

### 3.11 Enemigos y sus comportamientos

**Cómo funciona**

- **Llegada.** Entran sin parar por los bordes, en grupos, y encima llegan las mareas [G][P].
- **Especies.** Identifiqué Bulbasaur, Dratini, Pineco, Gastly, Nidoran, Geodude, Cyndaquil, Totodile, Farfetch'd y Larvitar [P/S].
  - [I] El logro de derrotar 600 especies distintas implica que salen como enemigos al menos 600.
- **Roles** [G][N]:
  - curanderos (vi un icono de corazón sobre Clefairy) [P];
  - escuderos (vi un icono de escudo con aura ovalada) [P];
  - invocadores, kamikazes y tiradores, con ataques avisados en el suelo [G];
  - élites grandes con anillo (uno soltó un imán) [P];
  - enemigos que disparan proyectiles [P].
- **Límites a los roles de apoyo.** Como mucho hay 3 curanderos, 3 escuderos y 3 invocadores a la vez. Su curación y su escudo escalan con el daño que haces, con tope. Un jefe solo recibe un escudo cada 6 s [N]. La guía aconseja matar primero a los de apoyo [G], y la Capa Furtiva los anula [G].
- **Tienen tipo y stats.** Atacan con su lado fuerte y se defienden con Defensa o Defensa Especial [N]. Los de tipo Agua nadan sin frenarse [N].
- **Tendencia.** Varias actualizaciones dejaron menos enemigos, pero más duros [N].
- **Shinies salvajes.** Salen con probabilidad 1/4096, brillan y salta un aviso; si lo derrotas, pasa a tu colección en shiny [G]. El Incienso Raro duplica la probabilidad [G].
- **Registro.** El juego cuenta las especies vistas y derrotadas, como una Pokédex, con logros de 400 vistas y 600 derrotadas [G][N].
- **Cooperativo.** Cada jugador activo hace que salgan más enemigos [N].

**Por qué funciona.** Los roles de apoyo dan **prioridades de objetivo** en un género donde normalmente basta con moverse, y combinan con la puntería manual y con los ataques teledirigidos. Los topes por rol evitan muros de curación frustrantes. El shiny salvaje es un premio por sorpresa que mantiene los ojos en la pantalla.

### 3.12 Jefes del calendario

**Cómo funciona**

- **Cuándo.** En los minutos 2, 6, 10, 14 y 18 sale un Pokémon fuerte que no es legendario, cada uno más duro que el anterior [G].
- **Patrón.** Tienen 4 ataques avisados, se acercan o pelean de lejos y se enfurecen a media vida [G][N]. Cuando no están en pantalla, una flecha en el borde marca dónde están y a qué distancia ("JEFE · 12 m") [N][P].
- **Botín.** Siempre un objeto y, una de cada tres veces, un ticket ×10 [G].
- **Topes** [N]:
  - no caen de un golpe ni se saltan fases;
  - ningún golpe te quita más del 30 % de tu vida (25 % en Normal); Arceus va aparte.
- **En la partida [P].** A los 2:00 apareció Inteleon ("¡Inteleon salvaje apareció!"). Lanzaba una columna azul translúcida avisada en el suelo y un rayo en espiral. Hacia la mitad de su vida salió "¡Inteleon se ha enfurecido!", y me mató a los 2:06.

**Por qué funciona.** Hitos cada 4 minutos que se pueden prever son metas cortas y claras ("llego al jefe del 10"), y las misiones diarias se apoyan en ellos ("Derrota a 2 jefes"). El tope de daño recibido evita muertes injustas de un solo golpe, y la furia a media vida le da al combate su propio clímax.

### 3.13 Eternatus Eternamax (minuto 20)

**Cómo funciona [G][N]**

- **Arena y reglas.**
  - Se pelea en la Cima de la Torre, y lo que quede en el suelo del mapa se pierde.
  - No hay tiempo límite, pero tras 5 minutos de pelea entra en furia total.
  - Ningún golpe tuyo le quita más del 10 % de su vida y no se pueden saltar fases.
  - Sus ataques quitan un porcentaje de tu vida, nunca más del 30 %.
  - Contra él sí funcionan Protección, Robustez y Banda Focus.
- **Fases:**

| Fase | Vida | Qué hace |
|---|---|---|
| 1 · Despertar | 100 → 66 % | Barrido de Rayo Infinito, charcos que envenenan, coronas de orbes y Pulso Dragón si estás cerca |
| 2 · Escudo Dinamax | 66 → 33 % | 4 núcleos que lo hacen inmune hasta que los rompes (cada uno deja una cura), láseres intermitentes entre ellos y nubes rojas que van cerrando la arena |
| 3 · Furioso | 33 → 10 % | Espiral Infinita, Noche Oscura (hay que meterse en uno de 3 círculos seguros), Rayo Infinito doble y un Remolino que te arrastra (corre en contra) |
| 4 · Rayo Eternamax | 10 % | Carga durante 8 s. Si rompes el Núcleo Eterno a tiempo, queda aturdido 6 s y recibe +50 % de daño. Si no, refúgiate en uno de los 2 círculos seguros |

- **Resultado.**
  - *Perder*: en solitario se acaba la partida; en grupo os podéis levantar.
  - *Ganar*: ticket ×10, +600 Pokémonedas, su botín y elegir un poder (3.17).
  - *Dificultad*: ganarlo en Normal desbloquea Difícil, y en Difícil, Pesadilla.
  - *Cooperativo*: mete a todo el grupo en su arena.

**Por qué funciona.** Es el **examen** de la build: el tope del 10 % por golpe convierte la pelea en una coreografía de fases, en lugar de borrarlo de un golpe con mucho daño. La fase de escudo cambia el objetivo (los núcleos), y la fase 4 premia leer la situación con una ventana de castigo. Ponerlo como llave de las dificultades le da sentido de "título".

### 3.14 Sentencia de Arceus (minuto 30)

**Cómo funciona [G][N]**

- **Planteamiento.**
  - Te lleva a la Sala del Origen, una plataforma flotante.
  - Arceus es invencible: la partida acaba cuando caes (en grupo, cuando caéis todos).
  - Hay ranking por tiempo aguantado y por daño total hecho a Arceus.
- **Tabla al azar.** En cada partida lleva una que le da su tipo, y se avisa al entrar. Así ningún tipo de ataque es siempre el mejor.
- **Defensa de Arceus.**
  - Solo recibe una fracción del daño, y esa fracción va bajando con el tiempo.
  - Pegarle no cura: ni robo de vida ni Cascabel Concha.
- **Su daño.**
  - Es puro: no mira tipos ni defensas, y no valen Protección, Robustez ni Banda Focus.
  - La reducción de daño solo te protege hasta un 30 %, y solo si la llevas al máximo (80 %). Escala en proporción, y el daño por tocarle no se reduce [N 16-11].
- **Persecución.**
  - Al minuto 1 iguala tu velocidad, a los 3 te supera y a los 10 va al 140 % de la tuya.
  - Tocarle te quita el 45 % de la vida, y desde el minuto 10 te deja KO.
- **Ataques que va sumando:**

| Tiempo de Sentencia | Novedad |
|---|---|
| 0:00 | Sentencia (pilares de luz sobre cada jugador), Cruz Sagrada (rayos en cruz hasta el borde) y Onda Divina (solo si estás pegado a él) |
| 0:30 | Velocidad Extrema (marca una franja y la cruza); la Cruz Sagrada pasa a 8 rayos |
| 1:00 | Premonición (explosiones retardadas por donde acabas de pasar) |
| 1:30 | Gravedad: 4 s al 60 % de velocidad y sin poder embestir; mientras, Arceus se queda quieto |
| 2:00 | Hiperrayo: abanico de 16 rayos que barre 1/4 de la arena |
| 2:30 | Sentencia de las Tablas: 17 Tablas orbitan y disparan proyectiles de todos los tipos |
| 2:00 / 4:00 / 6:00 | Rompe uno de tus objetos (y el cuarto a los 8:00) |
| 5:00 / 7:00 | Aspas Doradas: un carril de ruedas junto al borde, y a los 7 un segundo carril más interior que gira al revés. Cada impacto quita el 35 % y te echa del carril |
| Todo el rato | Cada 4 s se derrumba una parte del suelo, hasta perder el 30 % |
| 10:00 | Su contacto deja KO. La guía dice que llegar aquí es "cosa de leyendas" (≈40:00 de partida) |

- **No se puede huir.**
  - Si te alejas, reaparece delante de ti avisando con un sello dorado, y además lo hace cada ~20 s.
  - Si salta a por ti 3 veces en 45 s, rompe el ataque con el que huyes (Ataque Rápido, embestidas, Agilidad…).
- **En grupo.** La primera vez que caes te pueden levantar; la segunda, Arceus te juzga y quedas fuera. En cooperativo llega en el minuto 30 aunque la pelea con Eternatus no haya terminado [N].
- **Variantes.** En Halloween lo sustituye un gran Gengar bruja [G]. En 1 de cada 3 partidas que llegan a la Sentencia (solo en solitario) el Team Rocket secuestra a tu Pokémon (3.16). La guía no dice en qué momento exacto.
- **Historial.** Antes, durante la Sentencia acudían legendarios cada vez más fuertes; se quitaron el 13-11. También se reiniciaron los rankings, porque las marcas conseguidas huyendo de Arceus ya no se podían alcanzar [N].

**Por qué funciona.** Un final sin victoria convierte el cierre de la partida en una **puntuación comparable** entre builds y jugadores, y alimenta los rankings. El desarrollador cerró uno a uno los trucos del género: kiteo infinito, envenenar y huir, robo de vida, inmunidades. Así la Sentencia mide lo que quiere medir. Que te quite objetos y suelo poco a poco da una tensión creciente y un final garantizado.

### 3.15 Grietas legendarias y arenas

**Cómo funciona**

- **Cuándo.** En los minutos 4, 8, 12, 16 y 25 [N]. La guía general habla de "muy de vez en cuando", una redacción más antigua [G]. Entrar es opcional, y la grieta nunca sale en un sitio cerrado [N].
- **Arenas.** Hay 18, una por tipo [G]: Pradera Eterna (Normal), Volcán Ígneo (Fuego), Gruta Marina (Agua), Selva Esmeralda (Planta), Central Voltio (Eléctrico), Glaciar Eterno (Hielo), Dojo Ancestral (Lucha), Ciénaga Tóxica (Veneno), Desierto Rojo (Tierra), Pico Celeste (Volador), Templo Mental (Psíquico), Bosque Colmena (Bicho), Cantera Antigua (Roca), Cementerio Sombrío (Fantasma), Santuario Dragón (Dragón), Callejón Oscuro (Siniestro), Fortaleza de Acero (Acero) y Bosque Encantado (Hada).
  - Cada una tiene terreno (lava que quema, hielo que resbala, agua que frena) y clima propios [G].
  - Si el legendario tiene dos tipos, la arena se sortea entre ellos [G].
- **Rivales.** Son 97 legendarios, del n.º 144 (Articuno) al 1025 (Pecharunt), incluidos singulares, las aves de Galar y formas previas como Cosmog o Kubfu [G]. Los que todavía no tienes salen más a menudo [N].
  - [I] Ponderando a medias los de doble tipo, la arena de Psíquico saldría unas 17 veces de cada 97 y la de Bicho solo 0,5 (si el legendario se eligiera al azar uniforme).
- **Pelea.** Tiene tres fases, cinco ataques móviles por tipo y un ataque definitivo, que se esquiva escondiéndose tras columnas, árboles o rocas [N].
- **Premio:**
  - ticket ×10 [G];
  - un objeto, que sueltan siempre [G];
  - un **vínculo** de movimientos [N];
  - a veces un huevo [P, en la Mochila].
- **Perder** solo te devuelve al mapa sin premio [G].
- **En grupo** entráis todos juntos. El reloj del Pokémon perdido se para dentro [G][N].
- **Logros.** Hay 100 de legendarios (uno por cada uno de los 97 más 3 de recuento) y 3 de grietas, incluido ganar en las 18 arenas [G].

**Por qué funciona.** Es un **desafío opcional sin game over**: riesgo bajo y recompensa alta, así que el jugador entra con ganas en vez de con miedo. Que salgan más los que te faltan guía la colección sin depender del azar puro. Las arenas por tipo obligan a llevar variedad de ataques, y la grieta del 25 da una segunda oportunidad de completar los vínculos antes de la Sentencia.

### 3.16 Eventos de partida, casino y temporada

**Rotación [G]**

- Hay **4 eventos en rotación**. El primero llega en el minuto 4-5 y los siguientes, 4-5 min después de que acabe el anterior. **Nunca se repite el mismo dos veces seguidas.** En grupo los veis todos y la recompensa es para todos.

| Evento | Qué hay que hacer | Números |
|---|---|---|
| Horda de un tipo | Durante un rato, todos los enemigos que aparecen son de un mismo tipo | 30 s |
| Hora dorada | Los enemigos se vuelven dorados | 30 s; experiencia ×2; a veces sueltan monedas |
| Pokémon perdido | Lo tocas, te sigue y hay que llevarlo a una marca verde sin que le peguen | 2 min de límite. Premio: cura el 50 %, 60 monedas, 1 ticket y, 1 de cada 5 veces, se une a tu colección |
| Munchlax hambriento | Sacudes arbustos (enseñan qué bayas tienen) y le llevas 3 de la clase que pide | 2 arbustos trampa con enjambre de Combee. Premio: un objeto por jugador y un Caramelo Exp.; las bayas que no quiere son para ti [N] |

**Fuera de la rotación**

- **Ladrones de monedas** [G]. Un Pokémon cargado de botín huye en zigzag y no ataca; tienes 15 s para atraparlo.
  - Como mucho 2 por partida; el primero, entre el minuto 2 y el 4.
  - Suele ser un Meowth con 100 monedas; 1 de cada 4 veces, un Gholdengo con un ticket ×10.
- **Team Rocket y Casino** [G][N]. En 1 de cada 3 partidas que llegan a la Sentencia, y solo en solitario.
  - El reloj se para y puedes salir enseguida o gastar Pokémonedas.
  - Hay 4 minijuegos: tragaperras, Voltorb escondido, Carrera Rocket y ¡Atrapa a Pikachu! (de habilidad, en 3 fases).
  - A la larga la casa gana. Premios exclusivos: la estela Team Rocket (no se puede vender) y la skin Mewtwo Obsidiana.
- **Temporada** [N][G]. Hubo evento de Halloween del 30 de octubre al 2 de noviembre, con cuenta atrás desde dos semanas antes y el Gengar bruja como jefe del minuto 30.

**Por qué funciona.** Los eventos meten **objetivos distintos** (escoltar, recoger, perseguir, aprovechar una ventana) usando los mismos controles. La cadencia está garantizada y no repetirse evita la fatiga. El casino es un sumidero de monedas con sabor propio y premios cosméticos exclusivos. Las trampas de Munchlax evitan que el evento se juegue en piloto automático.

### 3.17 Poderes tras vencer a Eternatus

**Cómo funciona [G][N]**

- **La elección.** Tras ganar salen **3 o 4 cartas**.
  - Siempre salen Dinamax (o Gigamax si el Pokémon tiene esa forma), Pulsera Z y Teracristal.
  - La Megaevolución, o la Fusión o Cambio de forma equivalente, solo sale si tu Pokémon la tiene.
- **Reglas.**
  - Es un poder por partida: no se puede cambiar ni pasa a la siguiente.
  - En grupo, cada uno elige el suyo.
  - Se activa a mano (F en PC, B en mando, botón redondo en móvil). Dura unos segundos y se recarga solo; una barra bajo la vida te avisa.

| Poder | Activo / recarga | Qué hace |
|---|---|---|
| Megaevolución | 40 s / 90 s | Tomas los tipos, stats y habilidad de tu Mega y conservas tu vida. Los stats se escalan con lo que llevas (nivel, naturaleza, mejoras). La tienen 85 Pokémon. Si hay dos Megas (X/Y), eliges una al coger el poder. Algunas ponen clima (Mega Charizard Y pone sol; Kyogre y Groudon primigenios, lluvia o sol) |
| Dinamax / Gigamax | 12 s / 80 s | Te haces gigante, con vida ×2 y +40 % de daño. Cada golpe salpica alrededor, la cámara se aleja y rompes el escenario aplastando a los enemigos normales. Los 32 con Gigamax sueltan además una onda G-Max cada 3 s con un efecto propio (curar, quemar, aturdir, escudo…). En la Sentencia no cura |
| Pulsera Z | 15 s + mov. Z / 60 s | Eliges un tipo o el Z exclusivo de tu Pokémon. Durante 15 s sale una gran Z cada 0,8 s que rueda y atraviesa a todos (unas 18-19 por activación [I]). Al final, el movimiento Z golpea a todos los enemigos de la pantalla |
| Teracristal | 30 s / 75 s | Eliges uno de los 18 tipos: pasas a ser solo de ese tipo y tus ataques de ese tipo hacen ×1,5, o ×1,8 si ya era uno de tus tipos. Con Astral conservas tus tipos y todos tus ataques hacen ×1,3 |

- **Matices.**
  - La guía avisa de que duraciones y recargas son valores iniciales que se ajustarán con datos de partidas.
  - Desde el 18-11, Dinamax, Gigamax y Tera también potencian los proyectiles [N].
  - La carta **Poder rápido** reduce la recarga sin límite de copias, pero cada una rinde menos y nunca llega a cero [N].
- **[I] Tiempo activo por ciclo.** Depende de si la recarga cuenta desde que activas o desde que termina:

| Poder | Si cuenta desde que termina | Si cuenta desde que activas |
|---|---|---|
| Mega | 31 % | 44 % |
| Dinamax | 13 % | 15 % |
| Z | 20 % | 25 % |
| Tera | 29 % | 40 % |

**Por qué funciona.** Abre un **segundo acto** después del clímax del minuto 20, con un botón activo que contrasta con el ataque automático. Que la oferta dependa del Pokémon da identidad a cada compañero, y las cuatro opciones genéricas aseguran que todos tengan algo. Los tiempos se ajustan por separado para equilibrar estilos muy distintos: una ráfaga corta y enorme frente a un modo largo.

### 3.18 Formas

**Cómo funciona [G][N]**

- **Formas regionales.** Son 57 y cuentan como Pokémon aparte, con tipos y stats propios. Salen en el gacha y tienen sus propios huevos. Por eso la Pokédex tiene 1082 entradas (1025 especies más las 57 formas).
  - [I] Contándolas: 18 de Alola, 19 de Galar, 16 de Hisui y 4 de Paldea.
- **Formas elegibles** (Deoxys, Rotom, Shaymin, Hoopa, Oricorio…). Se eligen una sola vez, después de la 3.ª grieta (minuto 12).
- **Formas de combate** (Aegislash, Wishiwashi, Darmanitan, Mimikyu, Eiscue, Morpeko, Palafin…). Cambian solas según lo que pase en la partida.
- **Formas estéticas** (letras de Unown, motivos de Vivillon, Alcremie, versiones hembra). Son gratis en el Vestidor.
- **Volumen.** La "Gran Actualización" del 13-11 añadió 388 formas [N].

**Por qué funciona.** Reaprovecha contenido que ya existe para multiplicar el número de coleccionables y crea hitos dentro de la partida ("en la grieta 3 elijo forma").

### 3.19 Dificultades

**Cómo funciona [G][N][P]**

| Dificultad | Cómo se desbloquea | Cambios | Recompensas |
|---|---|---|---|
| Normal | Disponible de inicio | Enemigos y jefes con algo menos de vida y daño. Ningún golpe quita más de 1/4 de tu vida. La Sentencia no cambia | ×1 |
| Difícil | Vencer a Eternatus en Normal | — | ×1,5 de monedas y tickets |
| Pesadilla | Vencer a Eternatus en Difícil | Más vida y daño, golpes más duros y más enemigos a la vez | ×2 de monedas y tickets |

- Ganar en un modo superior desbloquea también los anteriores.

**Por qué funciona.** Da una escalera de maestría clara con el mismo contenido. Que el multiplicador de recompensas caiga en la meta, y no en el poder dentro de la partida, empuja a subir de dificultad sin obligar.

### 3.20 Meta-progresión

#### a) Economía: Pokémonedas y tickets

- **Pokémonedas.** Como invitado empiezas con 600 [P].
  - *Se ganan con*: tiempo, derrotados y lo recogido (la pantalla final lo desglosa) [P]; Eternatus (600) [G]; misiones y logros [G][P]; repetidos del gacha (un shiny repetido da el triple) [G][P]; objetos de monedas [G]; la mejora Fortuna (+8 % por nivel) [G]; la dificultad (×1,5 o ×2) [N].
  - **Las "monedas" que recoges en la partida son las mismas Pokémonedas [P+I]**: tras 4 partidas el menú marcaba 787 = 600 + 44 + 33 + 22 + 88.
  - **[P+I] Ritmo medido:** unas 0,2 monedas por segundo de tiempo (~12/min) y 1 por cada 4 derrotados aproximadamente. Datos: 17 en 86 s, 25 en 126 s, 27 por 111 derrotados, 43 por 173.
  - **[I] Extrapolación muy gruesa** (supone que esas tasas no cambian): una partida completa de ~30 min daría unas 2.000-2.500, así que llevar un Pokémon al máximo (93.470) costaría del orden de 40 partidas completas. No está verificado.
- **Tickets.** Hay dos clases: tickets normales (amarillos) y tickets ×10 (morados) [P]. Un ticket ×10 equivale a 10 tickets: paga una tirada ×10 [P].
  - *Fuentes de tickets normales*: enemigos normales de vez en cuando [G]; misiones diarias (2-3) [P]; cofres; el Pokémon perdido.
  - *Fuentes de ticket ×10*: jefes (1/3), Eternatus, grietas, Gholdengo, misiones semanales y aguantar 3 min en el desafío semanal [G][N][P].
  - Los tickets no se venden por dinero real [G].
- **Sumideros:**
  - mejoras permanentes (hasta 93.470 por Pokémon);
  - Tienda Kecleon [P]: objetos a 500, MT a 400-870, Menta y Cápsula Habilidad a 1.500, Cápsula Habilidad Oculta a 5.000, MT vacía a 500, fotos a 2.500 o 5.000 (variocolor), marcos a 17.500 o 25.000, estelas a 15.000-20.000 y skins a 30.000-35.000;
  - el casino.

#### b) Mejoras permanentes (por Pokémon) [G]

- Las mejoras son de cada Pokémon y solo cuentan cuando juegas con él. En grupo, cada uno lleva las suyas; no se aplican en el desafío semanal.
- Son 19 mejoras, y llevar un Pokémon al máximo cuesta **93.470**.
- Con todo comprado, un Pokémon solo "pega y aguanta unas 1,3 veces más". La guía lo resume así: ayudan, pero lo que más cuenta es jugar bien.

| Mejora | Efecto por nivel | Niveles | Coste (1.º → último) | Total |
|---|---|---|---|---|
| Vitalidad | +3 de vida | 10 | 60 → 890 | 3.270 |
| Fuerza | +1,5 % de daño | 10 | 80 → 1.450 | 5.050 |
| Zancada | +1,5 % de velocidad | 8 | 70 → 740 | 2.420 |
| Reflejos | −1 % de recarga | 8 | 90 → 1.050 | 3.340 |
| Coraza | +0,75 % de defensa | 8 | 80 → 840 | 2.750 |
| Síntesis | +0,1 de vida por segundo | 5 | 120 → 610 | 1.590 |
| Imán | +12 % de recogida | 6 | 50 → 270 | 820 |
| Sabiduría | +2 % de experiencia | 8 | 100 → 1.160 | 3.700 |
| Fortuna | +8 % de Pokémonedas | 8 | 120 → 1.620 | 4.950 |
| Golpe Crítico | +1 % de probabilidad de crítico | 10 | 90 → 1.860 | 6.300 |
| Crítico Potente | +5 % de daño crítico | 10 | 90 → 1.860 | 6.300 |
| Cambio de cartas | +1 cambio de cartas por partida | 5 | 150 → 980 | 2.360 |
| Veto | 1 movimiento bloqueado más | 5 | 300 → 3.910 | 7.920 |
| Repertorio | Empiezas con 2 movimientos | 1 | 1.500 | 1.500 |
| Movimiento inicial | Eliges el ataque con el que empiezas | 1 | 400 | 400 |
| Segundo movimiento inicial | Eliges también el 2.º (requiere Repertorio) | 1 | 400 | 400 |
| Segundo objeto | 2 huecos de objeto | 1 | 10.000 | 10.000 |
| Tercer objeto | 3 huecos (requiere el 2.º) | 1 | 30.000 | 30.000 |
| Objeto inicial | Empiezas con un objeto de la Mochila | 1 | 400 | 400 |

- **[I] Forma de la curva.** Los precios suben de forma geométrica: entre ×1,35 y ×1,45 por nivel en las stats, ×1,6 en Cambio de cartas y ×1,9 en Veto.
- **[I] Reparto.** El 43 % del total se va en objetos (40.400), el 54 % en las 13 mejoras de varios niveles y el 2,5 % en movimientos iniciales.
- **Recomendación de la guía**: Repertorio y Veto "cambian mucho las partidas", y llevar 3 objetos "es muy fuerte".
- **Calibración de la partida observada [P].** El primer nivel de cada mejora cuesta lo que dice la tabla.

#### c) Personalización permanente de cada Pokémon [N][P]

- **Naturaleza**: ±10 % a dos stats. Se cambia con una Menta (1.500).
- **Habilidad** con efecto en partida (por ejemplo, Mar Llamas). Se cambia con una Cápsula Habilidad (1.500) o una Cápsula Habilidad Oculta (5.000).
- **MT** para siempre; la MT vacía borra una y también quita su veto.
- **Movimientos iniciales**: comprados una vez por Pokémon.

#### d) Maestría [G]

- **Puntos.** 1 por cada 6 enemigos derrotados y 25 por minuto aguantado. De cada partida cuentan como mucho 40 minutos. Una partida entera da unos 1.600 puntos, algo más de la mitad por derrotas.
  - **Comprobado [P+I]**: la fórmula cuadra con las 4 partidas. P4: 173/6 + 2,1 × 25 = 28,8 + 52,5 ≈ 81, igual que el resumen (+81). P1: 18,5 + 35,8 ≈ 54 (+54). P2: 7 + 17,9 ≈ 24 (+24). P3: 9,7 + 18,3 ≈ 28 (+28).
- **Premios**, contados por partidas completas y, con la estimación de unos 30 minutos por partida [I], en horas de juego:

| Puntos | Premio | Partidas (aprox.) | Horas (aprox.) [I] |
|---|---|---|---|
| 10.000 | Foto de maestro | ~6 | ~3 h |
| 25.000 | Título "Maestro de…" | ~16 | ~8 h |
| 50.000 | Marco dorado con gemas de su tipo | ~32 | ~16 h |
| 100.000 | Aura dorada con chispas, visible también para el grupo | ~63 | ~31 h |

  - Pasados los 100.000 se sigue sumando sin tope.
- **A quién cuenta.** Al Pokémon con el que empezaste, aunque evolucione, y tanto en solitario como en grupo. No cuenta en el desafío semanal.
- **Validación.** El servidor confirma los puntos al acabar y las partidas con trampas no cuentan.
- **Ficha del Pokémon.** Guarda 8 estadísticas: partidas, tiempo, derrotados, llegadas a Arceus, mejor tiempo, jefes, grietas y Eternatus vencidos.

#### e) Cosmética: Vestidor, tienda y perfil [G][N][P]

- **Vestidor.** Por Pokémon eliges versión normal o shiny, aspecto, skin, efectos visuales y estela.
  - Hay 56 estelas: se compran una vez y valen para todos tus Pokémon.
  - Hay 27 skins de la comunidad: salen 3 a la semana en la tienda, iguales para todos. Algunas tienen versión shiny o Mega.
  - Exclusivas: Mewtwo Obsidiana (casino) y Deoxys Xenomorfo (rango del foro).
- **Rotaciones de la tienda.** Fotos cada pocas horas y distintas para cada jugador; marcos, skins y estelas cada semana [P][N].
- **Perfil.** Foto (la cara de un Pokémon con la expresión que elijas), marco, 3 favoritos, título y horas jugadas. Se publica si juegas con cuenta [P].

#### f) Gacha, huevos y shinies

- **Banners.** Hay 9, uno por región ("Gen 1-9") [P]. El de Kanto lleva los 151 [P].
- **Probabilidades publicadas [P]:**

| Rareza | Probabilidad | Pokémon en el banner de Kanto |
|---|---|---|
| Legendaria | 1,5 % | 6 |
| Épica | 6,5 % | 31 |
| Rara | 17 % | 38 |
| Poco común | 30 % | 41 |
| Común | 45 % | 35 |
| Shiny | 1 % por tirada | — |

- **Reglas [P][N].**
  - Una tirada ×10 asegura al menos una Épica.
  - Pity: tras 70 tiradas sin Legendaria en un banner, la siguiente lo es.
  - Los repetidos dan Pokémonedas, y los shinies no se repiten.
  - La tirada ×1 se quitó. Quedan ×10 (10 tickets o 1 ticket ×10) y ×100 (100 tickets o 10 tickets ×10), que enseña lo mejor de cada ×10 y acaba con un resumen.
  - Hay botón para saltar la animación, y con cuenta hace falta conexión.
- **Huevos [P][N].**
  - Salen del gacha (uno cada 10 tiradas ×10 en un banner), de las misiones semanales y a veces de legendarios.
  - La incubadora de la Mochila tiene 3 huecos, y los huevos se abren derrotando enemigos.
  - Pueden salir shiny.
- **Amuletos Iris** (9, uno por región) [N][P]. Completar la Pokédex de una región, legendarios incluidos, duplica la probabilidad shiny en su banner: del 1 % al 2 %.
- **Shinies.**
  - Casi todos los Pokémon tienen sprite shiny [G], y desde el 13-11 ya no queda ninguno sin él [N].
  - En el mapa salen con probabilidad 1/4096; en el gacha, 1/100 [G].
  - Un shiny repetido da el triple de Pokémonedas [G]. En la pantalla de inicio hay un interruptor para jugar en shiny [P].

#### g) Misiones, logros, desafío semanal, ranking y comunidad

- **Misiones diarias** [P]. Hay 3 y cada una tiene un botón "Cambiar". Ejemplos:
  - "Aguanta 7 min": 3 tickets y 200 monedas;
  - "Encuentra un objeto equipable": 2 y 150;
  - "Derrota a 2 jefes": 3 y 250.

  Los premios se recogen a mano en el menú.
- **Misiones semanales** [P]: "Derrota a 6000 Pokémon" (1 ticket ×10 y 800) o "Derrota a 6 jefes" (1 ×10 y 900).
- **Logros [G]**: 149, en 6 categorías. 27 dan título para el perfil; todos dan medalla, tickets y monedas.
  - Novedades hablaba de 127 el 08-10; la cifra ha crecido desde entonces [N].

| Categoría | Nº | Qué piden (ejemplos) |
|---|---|---|
| Colección | 16 | Tener 1 / 10 / 50 / 100 / 250 / 500 / 1082 Pokémon; 1 / 5 / 20 shinies; 100 tiradas; ver 100 / 400 especies; derrotar 100 / 300 / 600 distintas |
| Supervivencia | 13 | Aguantar 5 / 10 / 15 / 20 min; nivel 15 / 30; llegar a Eternatus, vencerlo y vencerlo 10 veces; llegar a Arceus y aguantar 1 / 5 min; jugar 50 partidas |
| Combate | 12 | 25 usos del poder; 1.000 / 10.000 / 100.000 derrotados; 1 / 25 / 100 jefes; evolucionar 1 / 25 / 149 movimientos; encontrar 5 / 24 objetos |
| Grietas | 3 | Ganar 1 / 10 grietas; ganar en las 18 arenas |
| Legendarios | 100 | Uno por cada uno de los 97, más 3 de recuento (10 / 30 / 97) |
| Misiones y más | 5 | Completar 10 / 50 / 200 misiones; jugar 1 / 10 partidas en grupo |

- **Desafío semanal [P][N].**
  - Mismo mapa, mismo Pokémon prestado (sin tus mejoras) y misma condición para todos. Condiciones posibles: climas, "Todos de tipo…", "Sin curaciones", "Noche cerrada".
  - Solo en solitario y con un intento por semana, que se gasta al empezar.
  - Aguantar 3 minutos da un ticket ×10, y tiene ranking propio.
  - Esta semana: Conkeldurr con "Siempre llueve".
- **Rankings [N].**
  - Diario, semanal, mensual, anual e histórico, por daño a Arceus y por tiempo aguantado.
  - Por Pokémon solo cuentan las partidas de 10 minutos o más; el resto, desde 2 minutos.
  - Muestran la build y hay filtro de "Solo amigos" (top 50).
- **Comunidad [N].** Participar en el foro da Puntos de Exploración y rangos que se canjean por tickets; el rango Maestro da una skin exclusiva.

**Por qué funciona (toda la meta).** Hay dos fuerzas en tensión:

- *Profundidad*: las mejoras y la maestría van por Pokémon, así que conviene especializarse en un favorito.
- *Amplitud*: el gacha, la Pokédex, los logros de "ver o derrotar distintos" y los legendarios que te faltan empujan a probar muchos.

El techo de ×1,3 evita que la meta sustituya a la habilidad. Hay metas a todos los plazos:

- diarias: misiones, fotos de la tienda;
- semanales: desafío, skins, misiones;
- de temporada: eventos;
- de largo plazo: maestría de 100.000, 97 legendarios, Amuletos Iris.

### 3.21 Cooperativo

**Cómo funciona [G][N][P]**

- **Acceso.** Hasta 4 jugadores. Necesitas cuenta: añades amigos por apodo y los invitas a una sala; la invitación caduca a los 3 min.
- **Durante la partida:**
  - la experiencia se comparte;
  - revives a un compañero quedándote a su lado un rato, y al levantarse tiene 2 s de invulnerabilidad;
  - la partida sigue mientras quede alguien en pie;
  - mientras estás caído puedes mirar a un compañero (Q/E o LB/RB).
- **Lo que lleva cada uno.** Sus mejoras, su poder y su maestría.
- **Lo que se comparte.**
  - Eventos y recompensas.
  - Munchlax hace un regalo a cada jugador.
  - El nivel del cofre con candado se reparte (1/2, 1/3 o 1/4).
  - Algunas esferas afectan a los compañeros cercanos.
  - El Incienso Raro solo cuenta si lo lleva el anfitrión.
- **Elecciones.** Cuando alguien elige carta, objeto, evolución, vínculo o regalo, aparece "X está eligiendo…" y la partida espera.
- **Escalado.** Cada jugador de más solo añade lo que aporta, y cada jugador activo hace salir más enemigos.
- **Jefes.** Contra Eternatus os podéis levantar. En la Sentencia, la segunda caída te elimina.
- **Red.**
  - Si el anfitrión se va, otro ocupa su lugar, pero esa partida ya no cuenta para el ranking.
  - Al anfitrión se le espera 1 minuto, y si deja la pestaña la partida sigue a los 30 s.
  - Un invitado tiene 45 s para reconectar.
  - A los 3 s sin noticias de un jugador, los enemigos van a por los demás.
  - Hay medidas contra abusos: bloquear el móvil ya no te libra de los enemigos, ni se pueden coger dos veces los mismos objetos.

**Por qué funciona.** Revivir por cercanía y compartir la experiencia hace el juego cooperativo de verdad y no cuatro partidas en paralelo. Que la partida espere a quien elige evita que el pausado del género rompa la experiencia en grupo. La regla de la segunda caída en el jefe final evita que se reviva sin fin en una pelea que es, al fin y al cabo, una puntuación.

### 3.22 Onboarding, interfaz, plataforma y accesibilidad

**Onboarding [P]**

- Al pulsar "Jugar como invitado" sale un **test de personalidad de 8 preguntas** de 4 respuestas, al estilo Mundo Misterioso. Algunos ejemplos: una pelea en el pueblo, una cartera en el suelo, un examen mañana, un camino oscuro y corto o largo y soleado.
- El resultado da una personalidad y un compañero. En mi caso: Valiente, Charmander.
- Con "Elegir otro" se ven 29 iniciales: los 27 de las 9 generaciones más Psyduck y Slowpoke. De cada uno se muestra el tipo, el ataque inicial y dos rasgos.
- La partida empieza sin más pantallas, en Normal.

**Interfaz de partida [P]**

- *Arriba a la izquierda*: nombre, nivel y barra de vida ("88 / 88").
- *Borde superior*: barra fina de experiencia.
- *Arriba en el centro*: el reloj y la línea "BIOMA · N DERROTADOS · N MONEDAS".
- *Arriba a la derecha*: el clima con su cuenta atrás.
- *Jefes*: barra de vida con nombre y flecha con distancia cuando están fuera de pantalla.
- *Abajo*: los 4 movimientos con su número y puntos de nivel (el activo resaltado y el evolucionado con marco dorado), el hueco del objeto, 4 huecos de esfera y los buffs temporales con sus segundos.
- *Textos y avisos*: números de daño, avisos ("¡Marea de Pokémon!", "¡Inteleon se ha enfurecido!", el clima), logros y misiones completadas.

**Pausa y final [P]**

- La **pausa** enseña tus ataques con su daño total y por segundo, tus stats completas, los objetos y cartas cogidos con su contador, y tus esferas.
- La **pantalla final** ("Has caído…") enseña:
  - tiempo, nivel y derrotados;
  - Pokémonedas con su desglose (tiempo, derrotados y recogidas);
  - tickets y maestría;
  - la tabla de daño de cada ataque;
  - "¡Nuevo récord de tiempo!" si lo hay.

**Plataforma [G][N]**

- Navegador, sin descarga, instalable como app y en 7 idiomas.
- Con cuenta (usuario y contraseña, o Google) se guarda en la nube; como invitado se juega al momento, pero no se guarda nada.
- Abandonar conserva lo ganado, y si el juego falla en el móvil también guarda.
- Las partidas no tienen límite de tiempo: se arregló un fallo que aparecía pasados los 84 minutos.

**Accesibilidad [N][P]**

- Tres barras de opacidad: tus ataques, los de tus compañeros y los de enemigos (estos, nunca por debajo del 25 %).
- Apuntar a mano, teclas reasignables y botones móviles recolocables.
- Límite de FPS y opciones de efectos y estelas.

**Por qué funciona.** El test convierte la elección de personaje en un pequeño ritual con identidad y quita parálisis de elección al empezar. El juego da mucha información (rendimiento en la carta, daño por segundo, desglose de monedas), así que su densidad de sistemas no resulta opaca.

### 3.23 Modelo del proyecto, monetización y desarrollo en directo

- **Monetización [G][N][P].** Juego de fans gratuito, sin anuncios ni compras, con donaciones voluntarias (vi un aviso de Ko-fi al acabar una partida). Sin afiliación con Nintendo, Creatures, GAME FREAK ni The Pokémon Company. No vende tickets ni tiene criptomoneda.
- **Licencia y código [N][G].** El código fue MIT hasta el 14-10-2026. Desde ese día está bajo **PolyForm Noncommercial 1.0.0**; el registro de cambios lo vincula a la aparición de copias que cobraban. Según la comprobación hecha en este trabajo, el repositorio público que enlaza el pie ya no existe.
- **Recursos.** Sprites de PMD SpriteCollab (CC BY-NC 4.0), datos de PokéAPI, música y sonidos originales [G].
- **Desarrollo en directo [N].** Novedades tiene entradas casi diarias del 08-10 al 25-11-2026. Incluye una "Gran Actualización" (13-11) que rehízo el calendario, las dificultades, las cartas, las formas y Eternatus, y nerfs frecuentes con cifras.
- **Antitrampas [G][N].** El servidor valida la maestría y se cerró un agujero de seguridad en los perfiles del ranking.

---

## 4. Tabla de números clave

| Valor | Sistema | Qué es | Fuente |
|---|---|---|---|
| 1 de 4 | Combate | Solo dispara el ataque activo; hay 4 huecos | [G][P] |
| máx(Atk, AtEsp) | Daño | El lado fuerte pega al 100 %; el otro, en proporción (87 % visto con Charmander) | [G][P] |
| ×2 | Cartas | Probabilidad de que salgan ataques de tu lado fuerte | [N] |
| +20 % | Daño | Monotipo con ataques de su tipo | [N][P] |
| ×1,6 / ×0,6 / ×0,3 | Tipos | Súper eficaz, poco eficaz e inmune | [G] |
| ×2,4 | Tipos | Tope de doble debilidad | [G] |
| ×1,5 / ×1,2 / ×1,3 / ×0,5 | Clima | Bonus y penalizaciones por tipo | [G] |
| 55-75 s, desde el min 3 | Clima | Clima natural | [G] |
| 4 | Niveles | Cartas por nivel | [N][P] |
| ≈1/4 | Niveles | Coste actual de un nivel frente al original | [N] |
| 1 (+5) | Niveles | Cambios de cartas por partida (base + mejora) | [P][G] |
| 5 | Niveles | Movimientos que se pueden vetar | [G][N] |
| 60 % / ×3,5 | Críticos | Topes de probabilidad y de daño crítico | [N] |
| ×1,5 | Críticos | Daño crítico base | [G] |
| 80 % | Defensa | Tope de reducción de daño | [N] |
| 5 | Movimientos | Nivel máximo antes de evolucionar | [G] |
| 149 / 176 | Movimientos | Movimientos que evolucionan / total | [G] |
| ×1,6-×1,9 | Movimientos | Multiplicador de daño al evolucionar, según la clase | [G] |
| 7 | Movimientos | Cartas que activan evoluciones (Potencia 53 … Imán 4) | [G] |
| Niv. 20 y 40 | Evolución | Evolución del Pokémon (antes 12 y 24) | [N][P] |
| 65 % | Evolución | Stats iniciales de los Pokémon que no evolucionan | [N] |
| 1 → 4 | Objetos | Huecos: 1 base, 2.º 10.000, 3.º 30.000, 4.º con carta rara | [G] |
| 24 / 22 | Objetos | Equipables / los que vende la tienda a 500 | [G][P] |
| 4 × 3 | Esferas | Esferas distintas × unidades de cada una | [N] |
| 25 s | Mapa | Duración de un altar (daño ×2, +45 % vel., imán ×4 o −40 % recarga) | [G] |
| 14 %/s | Mapa | Curación del manantial | [G] |
| 3,5 s | Mapa | Tiempo para abrir un cofre con candado | [G] |
| máx. 3 | Enemigos | Curanderos, escuderos e invocadores a la vez | [N] |
| 1/4096 | Shiny | Shiny salvaje (×2 con Incienso Raro) | [G] |
| min 2, 6, 10, 14, 18 | Jefes | Jefes del calendario | [G][N] |
| 1/3 | Jefes | Probabilidad de ticket ×10 por jefe del calendario | [G] |
| 30 % (25 % en Normal) | Jefes | Lo máximo que te quita un golpe de jefe | [N] |
| min 4, 8, 12, 16, 25 | Grietas | Calendario de grietas | [N] |
| 18 / 97 | Grietas | Arenas / legendarios | [G] |
| 4 | Vínculos | Pares de movimientos fusionados como máximo | [N] |
| min 20 | Eternatus | Llegada del jefe | [G] |
| 10 % | Eternatus | Lo máximo que le quita un golpe tuyo | [G] |
| 8 s / 6 s / +50 % | Eternatus | Carga del Rayo Eternamax / aturdimiento / daño extra que recibe | [G] |
| 600 + ticket ×10 | Eternatus | Recompensa por vencerlo | [G] |
| min 30 | Arceus | Inicio de la Sentencia | [G] |
| 45 % / KO desde min 10 | Arceus | Daño por tocarle | [G] |
| 140 % | Arceus | Su velocidad respecto a la tuya en el min 10 | [G] |
| 2, 4, 6 (8) min | Arceus | Roturas de objetos | [G] |
| 30 % | Arceus | Suelo que se derrumba como máximo; también la reducción de daño máxima que vale contra él | [G][N] |
| 4-5 min | Eventos | Cadencia de eventos sin repetición | [G] |
| 1/5 | Eventos | El Pokémon perdido se une a tu colección | [G] |
| 1/4 | Eventos | El ladrón es Gholdengo (ticket ×10) | [G] |
| 1/3 | Eventos | Secuestro del Team Rocket en partidas que llegan a la Sentencia | [G] |
| 40/90 · 12/80 · 15/60 · 30/75 s | Poderes | Duración y recarga de Mega, Dinamax, Z y Tera | [G] |
| ×1,5 / ×1,8 / ×1,3 | Poderes | Teracristal: tipo nuevo / tipo propio / Astral | [G] |
| ×1,5 / ×2 | Dificultad | Monedas y tickets en Difícil y en Pesadilla | [N] |
| 93.470 | Meta | Coste de llevar un Pokémon al máximo | [G] |
| ~×1,3 | Meta | Techo de poder con todas las mejoras | [G] |
| 1 por 6 derrotados + 25/min | Maestría | Puntos de maestría (comprobado en 4 partidas) | [G][P] |
| 40 min | Maestría | Lo máximo que cuenta de una partida | [G] |
| 10k / 25k / 50k / 100k | Maestría | Foto / título / marco / aura | [G] |
| ~0,2/s y ~1 por cada 4 derrotados | Economía | Ritmo de Pokémonedas observado al principio de la partida | [P][I] |
| 1,5 / 6,5 / 17 / 30 / 45 % | Gacha | Legendaria / Épica / Rara / Poco común / Común | [P] |
| 70 | Gacha | Tiradas para el pity de Legendaria | [P] |
| 1 % (2 % con Iris) | Gacha | Shiny por tirada | [G][N][P] |
| 149 | Logros | Total de logros, 27 con título | [G] |
| 1082 | Colección | 1025 especies + 57 formas regionales | [G] |
| 4 | Coop | Jugadores máximos | [G] |

---

## 5. Qué hace bien como diseño

**Decisiones del jugador**

- **Un ataque activo.** Convierte el auto-ataque en una decisión continua y legible, y da sentido a los tipos, al clima y a los objetos que premian o castigan cambiar de ataque.
- **Control del azar con la meta.** Cuatro cartas, cambios, vetos, movimientos iniciales y Repertorio dan más control a medida que inviertes, sin dar más poder bruto.
- **Elecciones con coste.** Evolucionar o no, entrar en la grieta o no, Cinta Elección frente a Espray Bucal, Incienso Suerte (monedas a cambio de daño), qué poder coger.

**Ritmo**

- **Calendario fijo con picos cada 2 minutos** entre el minuto 2 y el 18, sobre mareas, eventos y climas. Siempre hay un "próximo objetivo".
- **Tres actos claros**: supervivencia y construcción de la build (0-20), el examen de Eternatus con el poder como recompensa (20-30) y la Sentencia como puntuación (30+).
- **Riesgo sin castigo en lo opcional.** Las grietas y los eventos no te matan la partida si fallas.

**Retención**

- **Metas a todos los plazos**: misiones diarias y semanales, desafío semanal de un intento, rotaciones de la tienda, eventos de temporada, maestría de 100.000 puntos, 97 legendarios y 9 Amuletos Iris.
- **Especialización frente a colección**: las mejoras y la maestría por Pokémon frente al gacha y las Pokédex por región. Cada jugador encuentra su motivación.
- **Meta acotada (×1,3)**: los récords dependen de la habilidad, lo que hace creíbles los rankings.
- **Comunidad**: rankings con la build visible, perfil público, skins de la comunidad, foro con rangos.

**Claridad y justicia**

- **Información a la vista**: % de rendimiento en la carta, etiqueta "Evoluciona X", daño por segundo en la pausa y al final, desglose de monedas y probabilidades del gacha publicadas.
- **Topes contra la frustración**: ningún golpe de jefe quita más del 30 % (25 % en Normal), máximo 3 enemigos de apoyo por rol, bloqueo anti-clic en las cartas, aviso en el suelo de los ataques peligrosos.
- **Topes contra los exploits**: tope de daño a Eternatus, anti-kiteo en Arceus, veneno limitado contra los legendarios, tope de minutos que cuentan para la maestría y servidor que valida.

**Puntos débiles que conviene no copiar [I]**

- **Mucha densidad de sistemas** y guías que se contradicen con el registro de cambios: niveles de evolución, "Ascuas → Llamarada", el botón del mando, el número de logros.
- **Reglas de apilamiento sin publicar** (cómo se combinan los multiplicadores) y muchas cifras "sin número" en objetos y estados.
- **La colección depende de la marca.** Mil Pokémon son atractivos porque ya los conoces; un juego original necesita otro motor para que coleccionar enganche.
- **Equilibrio muy cambiante** (Surf, teledirigidos, curva de experiencia). Funciona en un proyecto de fans, pero en un juego comercial obligaría a una comunicación muy cuidada.

---

## 6. Ideas para tu propio juego

> **Aviso legal.** Lo que puedes reutilizar son **las mecánicas como ideas**: un arma activa, recetas de evolución, un calendario de jefes, un jefe final imbatible… En general las ideas de juego no están protegidas por derechos de autor. Lo que **no** puedes usar:
>
> - **Nombres y marca**: Pokémon, Eternatus, Arceus, Megaevolución, Dinamax, Teracristal, Tienda Kecleon, Pokémonedas, los nombres de movimientos y objetos, el estilo Mundo Misterioso, y la marca Pokémon en general (propiedad de Nintendo, Creatures, GAME FREAK y The Pokémon Company).
> - **Personajes, sprites y sonidos**: los sprites del juego son de PMD SpriteCollab bajo CC BY-NC 4.0 (no comercial y, además, arte derivado de Pokémon).
> - **Los datos de PokéAPI** (stats, movimientos por especie), que también son material de Pokémon.
> - **Su código**: MIT hasta el 14-10-2026, PolyForm Noncommercial desde entonces, y el repositorio ya no es público.
>
> La tabla de 18 tipos también es muy reconocible: diseña tus propias afinidades. Si vas a vender el juego, consulta con un abogado.

1. **Un arma activa y vínculos que se ganan.**
   - *Patrón*: solo dispara el ataque seleccionado; los vínculos de las grietas fusionan pares.
   - *Giro*: el jugador lleva 4 instrumentos de una banda y solo suena el que está activo. Cada guardián opcional derrotado da un "acorde" que une dos instrumentos y los hace sonar a la vez, hasta 3 acordes.
   - *Resultado*: la partida pasa de "una decisión táctica" a "caos controlado" como recompensa visible.

2. **Posturas que se cargan.**
   - *Patrón*: movimientos que acumulan una stat mientras están activos.
   - *Giro*: posturas de canalización (Concentración, Furia, Guardia). Cargan mientras están seleccionadas y se gastan poco a poco al cambiar a un ataque.
   - *Detalle*: un indicador de cargas en el icono crea un ritmo de cargar y soltar que el jugador aprende.

3. **Rendimiento visible y dos vías de stat.**
   - *Patrón*: multiplicador = stat usada ÷ stat dominante, y la carta dice "rinde un 87 %".
   - *Giro*: personajes con dos vías (por ejemplo, Músculo e Ingenio, o Materia y Espíritu). Las cartas de tu vía fuerte salen el doble y todas enseñan su %.
   - *Resultado*: ninguna carta es basura y el jugador entiende la regla sin tutorial.

4. **Afinidades suavizadas y mareas elementales.**
   - *Patrón*: tabla comprimida (×1,6 / ×0,6 / ×0,3, tope ×2,4) y climas que cambian los multiplicadores y que también puede provocar el jugador.
   - *Giro*: 6-8 afinidades propias (por ejemplo, Marea, Brasa, Raíz, Chispa, Ceniza, Eco), con "inmunidad blanda" al ×0,3 y "mareas" de 60 s que invierten un par.
   - *Detalle*: un objeto que anula solo la parte negativa de la marea.

5. **Calendario con un pico cada 2 minutos.**
   - *Patrón*: jefes en 2, 6, 10, 14, 18 y grietas en 4, 8, 12, 16, 25.
   - *Giro*: alterna "jefe obligatorio" (premio: objeto) y "portal opcional" (premio: vínculo o colección), y publica el calendario en la interfaz para que el jugador planifique.
   - *Detalle*: añade una ventana de recuperación hacia el final para quien falló un portal.

6. **Un jefe "examen" a mitad de partida.**
   - *Patrón*: Eternatus en el minuto 20, con tope del 10 % de su vida por golpe, fases obligatorias, una ventana de castigo y el desbloqueo de la dificultad siguiente.
   - *Giro*: un examen que cambia según cómo hayas construido la build (por ejemplo, si llevas mucha área, fase de núcleos dispersos; si llevas mucho daño a un objetivo, fase de escudos). Vencerlo abre la dificultad siguiente y un "acto 2".

7. **Un final imbatible que puntúa.**
   - *Patrón*: la Sentencia de Arceus, con ataques que se van sumando, objetos rotos, suelo que cae y anti-kiteo.
   - *Giro*: "El Juicio". Cada 2 minutos **el jugador elige** qué objeto sacrificar a cambio de una bendición temporal, en vez de perderlo al azar.
   - *Detalle*: ranking doble, por tiempo y por daño, con la build visible.

8. **Portales opcionales sin game over.**
   - *Patrón*: las grietas. Perder solo te devuelve al mapa, y los rivales que aún no tienes salen más a menudo.
   - *Giro*: arenas temáticas con terreno propio y un rival que, si lo vences, se convierte en un **personaje jugable o en un vínculo**.
   - *Resultado*: la colección se gana jugando y no comprando.

9. **Eventos en rotación que no se repiten.**
   - *Patrón*: 4 eventos cada 4-5 minutos, nunca el mismo dos veces seguidas; ladrones aparte.
   - *Giro*: una baraja de 6 minieventos de 30-120 s con un "verbo" distinto cada uno: escoltar, recoger con trampas, perseguir a un ladrón, defender un punto, una ventana dorada y una horda temática.
   - *Detalle*: el evento elegido se avisa con 10 s de antelación.

10. **Objetos que cambian las reglas del arma activa.**
    - *Patrón*: Cinta Elección (bloquea el cambio de ataque), Metrónomo (premia no cambiar), Espray Bucal (premia cambiar), Acróbata (premia ir sin objetos).
    - *Giro*: una familia de "juramentos" que se equipan como objetos y definen el estilo: el Fiel no puede cambiar de arma pero pega +40 %; el Malabarista gana velocidad al cambiar; el Asceta es más fuerte con los huecos vacíos.
    - *Resultado*: las builds se definen por cómo juegas, no solo por los números.

11. **Una transformación elegida tras el jefe.**
    - *Patrón*: 3-4 cartas de poder según el personaje, con duración y recarga, una por partida.
    - *Giro*: cada personaje tiene una transformación propia más tres genéricas (gigante, ráfaga rodante, cambio de afinidad). Una barra bajo la vida y un solo botón.
    - *Detalle*: una carta "Poder rápido" con rendimiento decreciente para quien quiera construir alrededor de la transformación.

12. **Meta acotada y maestría cosmética.**
    - *Patrón*: mejoras por personaje con techo de ×1,3 y maestría de 10k, 25k, 50k y 100k puntos.
    - *Giro*: invierte la proporción. Que el 40 % del coste sea **flexibilidad** (huecos, movimientos iniciales, vetos) y no poder bruto.
    - *Detalle*: que el último hito de maestría sea visible para los compañeros de grupo (como el aura).

13. **Colección que se gana en la partida.**
    - *Patrón*: el Pokémon perdido se une 1 de cada 5 veces, los shinies salvajes, las Pokédex de vistos y derrotados, los Amuletos Iris.
    - *Giro*: sin la marca de por medio, cada criatura o personaje se desbloquea rescatándolo en eventos, venciéndolo en un portal o completando su "ficha" tras verlo y derrotarlo X veces. Completar un bioma da un amuleto que mejora los encuentros raros de ese bioma.
    - *Gacha*: si pones uno, que sea solo con moneda del juego, con probabilidades publicadas, una garantía en la tirada ×10 y pity.

14. **Un test de personalidad como onboarding.**
    - *Patrón*: 8 preguntas que asignan compañero y rasgos.
    - *Giro*: preguntas que además **enseñan** el juego ("¿huyes o te plantas?" lleva a recomendar un arquetipo de cuerpo a cuerpo o de rastro). Al final, una frase de identidad y la opción de elegir otro.

15. **Cooperativo amable.**
    - *Patrón*: experiencia compartida, revivir por cercanía, 2 s de invulnerabilidad al levantarse, la partida espera a quien elige, escalado por jugador activo y segunda caída eliminatoria en el jefe final.
    - *Giro*: los vínculos o acordes se pueden hacer **entre jugadores** (dos jugadores cerca combinan sus armas activas durante unos segundos). Así hay una razón para no separarse.

---

## 7. Preguntas abiertas

**Combate y cartas**

1. ¿Daño base, recarga, alcance y área de cada movimiento? Solo se publican los multiplicadores de evolución.
2. ¿Siguen actuando las torretas, minas, charcos y cargas de mejora al cambiar de ataque? ¿Las cargas tienen tope o se pierden?
3. ¿Cómo se combinan los multiplicadores de daño y las reducciones (¿se suman o se multiplican?)? ¿El tope de ×2,4 incluye el clima o el Tera?
4. ¿Qué hace por sí sola la carta Coraza? ¿Cuánto dan Racha de suerte y Esquiva, y qué tope tienen? ¿Qué es exactamente Aprendizaje con tope 15?
5. ¿Hay un bonus general por mismo tipo además del +20 % de los monotipo?
6. Duración y daño de quemadura y veneno, porcentaje de frenado, duración de aturdimiento y congelación, y si se acumulan.

**Partida**

7. ¿Cómo escalan con el tiempo la vida, el daño y la densidad de enemigos, y cuánto cambian en Difícil y Pesadilla?
8. ¿Cuánta vida tienen los jefes del calendario y Eternatus, y cómo escala esa vida con la dificultad y con el número de jugadores?
9. ¿Qué fracción del daño recibe Arceus y a qué ritmo baja?
10. Los ataques de Arceus no miran tipos: ¿su Tabla cambia en algo la eficacia de tus ataques?
11. ¿La recarga de un poder cuenta desde que lo activas o desde que termina? ¿El poder está listo nada más elegirlo?
12. ¿En qué momento exacto ocurre el secuestro del Team Rocket? ¿Qué probabilidades y pagos tiene cada minijuego del casino?
13. ¿El clima natural se elige al azar, depende del bioma o del tiempo? ¿Un clima nuevo sustituye al anterior?
14. ¿Qué patrones de ataque tiene cada legendario de grieta, y hay límite de tiempo en la arena?
15. ¿Qué cambia exactamente cada bioma (Bosque, Cueva, Volcán)? En las 4 partidas solo vi "Bosque Umbrío".

**Meta y economía**

16. ¿Cuántas Pokémonedas da de verdad una partida completa? (Mi cifra de 2.000-2.500 es una extrapolación.) ¿Cuántas da un repetido normal del gacha?
17. ¿Las mejoras permanentes son por especie o por línea evolutiva? Al evolucionar en partida, ¿cuáles se aplican?
18. ¿De dónde salieron los 3 tickets que no aparecían en los resúmenes de mis partidas (el contador marcaba 6 y solo vi "+3")?
19. ¿Qué dan exactamente los logros (cuántos tickets y monedas) y qué son los "caramelos" que aparecen como tercera divisa?
20. ¿La grieta del minuto 25 da algo si ya ganaste las cuatro anteriores?

**Cooperativo**

21. ¿Cómo se reparte la experiencia, cuánto tarda en revivirse a un compañero y quién recibe los objetos de jefes y grietas?
22. Si caes ante Eternatus pero tu grupo gana, ¿recibes poder?

**Contradicciones entre fuentes**

23. Niveles de evolución del Pokémon: 12 y 24 [G] frente a 20 y 40 [N]. La partida apoya 20 y 40, pero no lo vi pasar.
24. Botón del poder con mando: X [G] frente a B [N].
25. Número de logros: 127 [N, 08-10] frente a 149 [G][P].

---

## 8. Limitaciones y fuentes

**Fuentes**

- **Guías públicas de pokesurvivor.com**, descargadas como texto: guía general, guías, movimientos, tipos, objetos, jefes, legendarios, eventos, poderes, shinies, mejoras, maestría, logros, Pokédex y Novedades. Un verificador las revisó por grupos de sistemas (núcleo, combate, enemigos y meta) y corrigió las afirmaciones que iban más allá del texto. Todos los grupos dieron resultado; ninguno falló.
- **Una sesión observada como invitado**: 4 partidas de 0:43, 0:44, 1:26 y 2:06, con Charmander en Normal. Además, una revisión solo de lectura de los menús (tienda, gacha, mejoras, misiones, logros, Pokédex, Vestidor, ajustes y desafío semanal). No se creó cuenta, no se gastó nada y no se jugó el desafío semanal.

**Limitaciones**

- **Partida corta.** Lo observado solo llega al minuto 2:06. No vi grietas, eventos de la rotación, climas naturales, Eternatus, la Sentencia de Arceus, los poderes, la evolución del Pokémon, la carta del cuarto objeto ni un shiny salvaje. Todo eso sale solo de las guías.
- **Movimiento simulado.** Moví al personaje con eventos de teclado lanzados por JavaScript, porque las pulsaciones de la herramienta eran demasiado cortas, y el panel del navegador estaba oculto. Eso puede haber afectado al ritmo y a las muertes tempranas. La única intervención en la página fueron esos eventos de teclado.
- **Sin cuenta ni gasto.** No se probó el cooperativo, el ranking, los amigos, el guardado en la nube, tiradas de gacha, compras, mejoras, Difícil ni Pesadilla.
- **Código no analizado.** El código del juego en la web está ofuscado y no se analizó; no se hizo ingeniería inversa. El repositorio público que enlazaba el pie ya no existe. El informe sale solo de documentación pública y de la observación.
- **Página de mejoras.** La primera descarga de /mejoras devolvió un error temporal del servidor. Después se volvió a descargar y la tabla de 3.20 b) se cotejó línea a línea con ella: coinciden los niveles, los precios y los totales (93.470 en total, con "unas 1,3 veces más"). Los costes del primer nivel también coinciden con lo visto en el menú.
- **Fuentes que se contradicen.** Varias guías no coinciden con Novedades: niveles de evolución, "Ascuas → Llamarada", el botón del mando, el número de logros, la frecuencia de las grietas. He priorizado lo más reciente cuando la partida lo apoyaba, y he señalado cada caso.
- **Números provisionales.** El juego cambia casi a diario (registro del 08-10 al 25-11-2026), y la propia guía de poderes avisa de que sus valores son iniciales. Cualquier cifra puede estar ya ajustada.
- **Inferencias.** Todo lo marcado [I] es cálculo o deducción mía: tasas de monedas, horas de maestría, reparto de arenas, tiempo activo de los poderes, número de formas por región, pulso del calendario. No lo afirma ninguna fuente.
- **Identificación de especies.** Los enemigos que nombro en las partidas los reconocí por el sprite y pueden tener errores.
