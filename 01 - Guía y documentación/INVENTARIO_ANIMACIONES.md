# Inventario de animaciones (2026-11-14)

Generado con `python herramientas/inventario_animaciones.py`. Para cada forma se miran las 14 animaciones del juego: ✅ animada (2 fotogramas o más; moverse, daño, muerte y retrato valen con 1), 🟡 quieta (un solo fotograma), ❌ falta (el juego usa otra).

## Resumen

El retrato se enseña pero no cuenta para «completa» (no es una animación; sin él se usa el de otra forma).

- Formas jugables: **225**. Completas: **13** · casi (1-2 pendientes): **156** · a medias (3-6): **56** · poco animadas (7 o más): **0**.
- Formas de enemigos: **40**. Formas ocultas (no se ven en el juego): **48**.
- Carpetas de `sprites/` con personajes que el juego no usa: **88** (6646 imágenes).

**Lo que más se repite en las formas jugables:**

- Brazos arriba con un solo fotograma: 100 formas
- Guardia con un solo fotograma: 13 formas
- Poder/aura con un solo fotograma: 12 formas
- Retrato sin animación propia: 144 formas
- Brazos arriba sin animación propia: 97 formas
- Combo 3 sin animación propia: 67 formas
- Rayo sin animación propia: 46 formas
- Patada 2 sin animación propia: 40 formas
- Muerte sin animación propia: 36 formas
- Combo 2 sin animación propia: 23 formas

## Formas jugables (de menos a más animadas)

| Personaje · forma | Estado | Guardia | Moverse | Puñetazos | Patadas | Ki | Poder/aura | Daño | Muerte | Retrato | Combo 2 | Combo 3 | Patada 2 | Rayo | Brazos arriba |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Vegetto Blue (`vegitoblue254/0`) | A MEDIAS | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Tarble (`tarble/0`) | A MEDIAS | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Nuova Shenron (`nuova/0`) | A MEDIAS | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Kibitoshin (`kibitoshin/0`) | A MEDIAS | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Goku Saga Moro · Ultra Instinto (`gokumoro/4`) | A MEDIAS | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Goku Saga Moro · Super Saiyan (`gokumoro/1`) | A MEDIAS | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Goku Saga Moro · Ssj Dios (`gokumoro/2`) | A MEDIAS | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Goku Saga Moro · Ssj Blue (`gokumoro/3`) | A MEDIAS | ✅ | ✅ | ✅ | ✅ | ✅ | 🟡 | ✅ | ❌ | ✅ | ❌ | ❌ | ❌ | ✅ | ❌ |
| Goku Saga Moro · Base (`gokumoro/0`) | A MEDIAS | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Goku Black Ssj Falso (`blackfalso/0`) | A MEDIAS | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Bulma (`bulma/0`) | A MEDIAS | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Majin Black Dios (`blackmajin/0`) | A MEDIAS | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ |
| Black Time Breaker · Ssj Rosé (`blacktime/1`) | A MEDIAS | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Black Rosé Evolution (`blackrosen/0`) | A MEDIAS | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ |
| Tao Pai Pai (`taopaipai/0`) | A MEDIAS | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ✅ | ❌ | ✅ | ❌ | ❌ |
| Supremo Kaioshin (`shin/0`) | A MEDIAS | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ |
| Rey Gomah (`gomah/0`) | A MEDIAS | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ |
| Rey Cold (`reycold/0`) | A MEDIAS | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ |
| Maestro Roshi (`roshi/0`) | A MEDIAS | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ✅ | ❌ | ✅ | ❌ | 🟡 |
| Goku Ui · Ultra Instinto (`gokuui/3`) | A MEDIAS | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ❌ | ✅ | ✅ | ❌ | ❌ |
| Goku Ui · Ui Dominado (`gokuui/4`) | A MEDIAS | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ❌ | ✅ | ❌ | ✅ | 🟡 |
| Goku Ui Blue (`gokumuiblue/0`) | A MEDIAS | ✅ | ✅ | ✅ | ✅ | ✅ | 🟡 | ✅ | ❌ | ❌ | ✅ | ✅ | ✅ | ❌ | 🟡 |
| Goku Rey Mono (`gokureymono/0`) | A MEDIAS | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ |
| Cumber (`cumber/0`) | A MEDIAS | ✅ | ✅ | ✅ | ✅ | ✅ | 🟡 | ✅ | ✅ | ❌ | ✅ | ❌ | ❌ | ✅ | 🟡 |
| Vegeta Yardrat (`vegetayardrat/0`) | A MEDIAS | 🟡 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ❌ | 🟡 |
| Vegeta Dios · Broly (`vegetabroly/0`) | A MEDIAS | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ❌ | 🟡 |
| Vegeta Blue Manga · Ssj Blue Perfecto (`vegetamanga/1`) | A MEDIAS | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ❌ | 🟡 |
| Trunks · Base (`trunks/0`) | A MEDIAS | ✅ | ✅ | ✅ | ✅ | ✅ | 🟡 | ✅ | ✅ | ❌ | ✅ | ❌ | ✅ | ✅ | 🟡 |
| Trunks Niño · Super Saiyan (`trunksnino/1`) | A MEDIAS | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ✅ | ✅ | ✅ | ❌ | ❌ |
| Trunks Niño · Base (`trunksnino/0`) | A MEDIAS | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ✅ | ❌ | ✅ |
| Trunks Gt (`trunksgt/0`) | A MEDIAS | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ❌ | ✅ | ❌ | ❌ |
| Trunks Armadura (`trunksarmor/0`) | A MEDIAS | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ❌ | ✅ | ❌ | 🟡 |
| Super 17 (`super17/0`) | A MEDIAS | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ❌ | ❌ | ✅ | 🟡 |
| Omega Shenron (`omega/0`) | A MEDIAS | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ✅ | ✅ | ❌ | ✅ | 🟡 |
| Moro (`moro/0`) | A MEDIAS | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ✅ | ❌ |
| Metal Cooler (`metalcooler/0`) | A MEDIAS | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ❌ | ❌ | ✅ | ❌ |
| Merus (`merus/0`) | A MEDIAS | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ❌ | ❌ | ✅ | ❌ |
| Jiren · Máximo Poder (`jiren/1`) | A MEDIAS | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ✅ | ✅ | 🟡 |
| Janemba (`janemba/0`) | A MEDIAS | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ✅ | ✅ | ❌ |
| Hatchiyack (`hatchiyack/0`) | A MEDIAS | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ✅ | ✅ | ❌ | ✅ | 🟡 |
| Goku Xeno · Super Saiyan 4 (`gokuxeno/2`) | A MEDIAS | ✅ | ✅ | ✅ | ✅ | ✅ | 🟡 | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | 🟡 |
| Goku Ui Blue Evolution (`gokumuiblueevo/0`) | A MEDIAS | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ❌ | ✅ | ❌ | ❌ |
| Goku Super · Kaioken (`gokusuper/1`) | A MEDIAS | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ✅ | ✅ | ❌ | ✅ | 🟡 |
| Goku Película Broly · Ssj Dios (`gokubroly/2`) | A MEDIAS | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | 🟡 |
| Goku Dios Berserker (`gokudiosberserk/0`) | A MEDIAS | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ❌ | ❌ | ✅ | ❌ |
| Goku Black Kaioshin (`blackkaioshin/0`) | A MEDIAS | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ✅ | ✅ | ❌ | ✅ | ❌ |
| Goku Black Fanmade · Rosé Ultra Instinto (`blackfan/2`) | A MEDIAS | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ❌ | 🟡 |
| Gohan · Definitivo (`gohan/3`) | A MEDIAS | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ✅ | ✅ | 🟡 |
| Gohan Manga (`gohanmanga/0`) | A MEDIAS | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ✅ | 🟡 |
| Gohan Del Futuro (`gohanfut/0`) | A MEDIAS | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ✅ | ✅ | ❌ |
| Gohan Adulto · Místico (`gohanadult/1`) | A MEDIAS | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ✅ | ✅ | 🟡 |
| Gohan Adulto · Bestia (`gohanadult/2`) | A MEDIAS | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ✅ |
| Freezer · 3ª Forma (`freezer/1`) | A MEDIAS | 🟡 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ❌ | ✅ | ✅ | ❌ |
| Broly · Super Saiyan (`broly/1`) | A MEDIAS | ✅ | ✅ | ✅ | ✅ | ✅ | 🟡 | ✅ | ✅ | ❌ | ✅ | ❌ | ✅ | ✅ | ❌ |
| Androide 17 (`a17/0`) | A MEDIAS | 🟡 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ❌ | ✅ | ✅ | ❌ |
| Androide 14 (`a14/0`) | A MEDIAS | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ✅ | ✅ | ✅ | ❌ | 🟡 |
| Zamasu · Base (`zamasu/0`) | CASI | 🟡 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ❌ |
| Zamasu Fusionado (Deshaciéndose) (`zamasufusion/0`) | CASI | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ❌ | ✅ | ✅ | 🟡 |
| Vegetto · Base (`vegetto/0`) | CASI | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ❌ | ✅ | ✅ | 🟡 |
| Vegeta · Majin Vegeta (`vegeta/3`) | CASI | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ❌ | ✅ | ✅ | 🟡 |
| Vegeta Xeno · Base (`vegetaxeno/0`) | CASI | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ❌ | ✅ | ✅ | ❌ |
| Vegeta Super · Blue Full Power (`vegetasuper/4`) | CASI | 🟡 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 🟡 |
| Vegeta Blue Manga · Ssj Blue (`vegetamanga/0`) | CASI | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | 🟡 |
| Vegeta Blue Maligno (`vegetabluemal/0`) | CASI | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ | 🟡 |
| Trunks · Base Manga (`trunks/2`) | CASI | ✅ | ✅ | ✅ | ✅ | ✅ | 🟡 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ |
| Saibaman (`saibaman/0`) | CASI | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ❌ | ✅ | 🟡 |
| Paragus (`paragus/0`) | CASI | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ❌ | ✅ | ❌ |
| Pan Gt (`pangt/0`) | CASI | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ❌ | ✅ | ✅ | ❌ |
| Nappa (`nappa/0`) | CASI | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | 🟡 |
| Majin Kuu (`majinkuu/0`) | CASI | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ | ❌ |
| Majin Duu (`majinduu/0`) | CASI | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ❌ | 🟡 |
| Majin Buu · Super Buu (`buu/2`) | CASI | 🟡 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | 🟡 |
| Majin Buu · Gordo (`buu/0`) | CASI | 🟡 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ❌ |
| Majin Buu · Buu Gohan (`buu/3`) | CASI | 🟡 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | 🟡 |
| Magetta (`magetta/0`) | CASI | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ | 🟡 |
| Kyabe · Base (`kyabe/0`) | CASI | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ❌ | ❌ |
| Kefla · Ssj Blue (`kefla/1`) | CASI | 🟡 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 🟡 |
| Kale · Base (`kale/0`) | CASI | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ❌ | ✅ | ✅ | ❌ |
| Jiren · Hakaishin (`jiren/2`) | CASI | ✅ | ✅ | ✅ | ✅ | ✅ | 🟡 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 🟡 |
| Jiren · Base (`jiren/0`) | CASI | 🟡 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ |
| Jiren (Torneo) (`jirengray/0`) | CASI | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ❌ | 🟡 |
| Gran Sacerdote (`daishinkan/0`) | CASI | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ❌ | ✅ | ✅ | ❌ |
| Goten (`goten/0`) | CASI | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ❌ | ✅ | ✅ | 🟡 |
| Goku · Super Saiyan 2 (`goku/2`) | CASI | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ❌ | ✅ | ✅ | 🟡 |
| Goku · Super Saiyan (`goku/1`) | CASI | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ❌ |
| Goku · Ssj Blue (`goku/4`) | CASI | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | 🟡 |
| Goku Yardrat Ssj (`gokuyardratssj/0`) | CASI | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ | ❌ |
| Goku Xeno · Ssj Dios (`gokuxeno/1`) | CASI | ✅ | ✅ | ✅ | ✅ | ✅ | 🟡 | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | 🟡 |
| Goku Ultra Ssj Dios (`gokuultradios/0`) | CASI | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ | 🟡 |
| Goku Ui Verdadero (`gokuuiverdadero/0`) | CASI | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ❌ | ✅ | ✅ | 🟡 |
| Goku Ui Dios (`gokumuidios/0`) | CASI | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ | ❌ |
| Goku Ssj4 (Daima) (`gokussj4daima/0`) | CASI | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ❌ | ❌ |
| Goku Ssj Supremo (`gokussjsupremo/0`) | CASI | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ❌ | ❌ |
| Goku Ssj Legendario (`gokussjlegend/0`) | CASI | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ❌ | 🟡 |
| Goku Ssj Kaioken (`gokussjkaioken/0`) | CASI | ✅ | ✅ | ✅ | ✅ | ✅ | 🟡 | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ❌ |
| Goku Ssj Chaqueta (`gokussjchaqueta/0`) | CASI | ✅ | ✅ | ✅ | ✅ | ✅ | 🟡 | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ❌ |
| Goku Película Broly · Super Saiyan (`gokubroly/1`) | CASI | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ❌ |
| Goku Patrullero (`gokupatrulla/0`) | CASI | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ❌ | ✅ | ❌ |
| Goku Maligno Ssj2 (`gokuevilssj2/0`) | CASI | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ❌ | ❌ |
| Goku Gt · Super Saiyan 4 (`gokugt/3`) | CASI | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ |
| Goku Fanmade · Ikari (`gokualt/1`) | CASI | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | 🟡 |
| Goku Fanmade · Bestia (`gokualt/2`) | CASI | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ |
| Goku Black · Super Saiyan (`black/1`) | CASI | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ❌ | ✅ | ✅ | 🟡 |
| Goku Black Fanmade · Ssj Rage (`blackfan/0`) | CASI | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ |
| Goku Black Fanmade · Rosé Kaioken (`blackfan/1`) | CASI | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | 🟡 |
| Goku Black Fanmade · Mui (`blackfan/3`) | CASI | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | 🟡 |
| Gohan · Base (`gohan/0`) | CASI | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ❌ | ✅ | ✅ | 🟡 |
| Gogeta · Super Gogeta (`gogeta/0`) | CASI | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ❌ | ✅ | ✅ | ❌ |
| Dyspo (`dyspo/0`) | CASI | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ❌ | 🟡 |
| Cui (`cui/0`) | CASI | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ❌ | ✅ | ✅ | 🟡 |
| Cell · Perfecto (`cell/2`) | CASI | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ❌ | ✅ | ✅ | ❌ |
| Cell · Imperfecto (`cell/0`) | CASI | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ | 🟡 |
| Broly · Super Saiyan 4 (`broly/3`) | CASI | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ❌ | ✅ | ✅ | 🟡 |
| Broly · Legendario (`broly/2`) | CASI | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ❌ | ✅ | ✅ | ❌ |
| Black Time Breaker · Ssj Dios (`blacktime/0`) | CASI | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ❌ |
| Androide 16 (`a16/0`) | CASI | 🟡 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ❌ |
| Androide 13 (`a13/0`) | CASI | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ | ❌ |
| Zamasu · Fusionado (`zamasu/1`) | CASI | 🟡 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Yamcha (`yamcha/0`) | CASI | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | 🟡 |
| Videl (`videl/0`) | CASI | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | 🟡 |
| Vegetto · Super Vegetto 2 (`vegetto/2`) | CASI | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | 🟡 |
| Vegetto · Super Vegetto (`vegetto/1`) | CASI | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ❌ |
| Vegetto · Ssj Blue (`vegetto/3`) | CASI | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | 🟡 |
| Vegetto Ssj Falso (`vegettofalso/0`) | CASI | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ❌ |
| Vegetto Fanmade · Super Saiyan 4 (`vegettofan/2`) | CASI | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 🟡 |
| Vegetto Fanmade · Ssj Dios (`vegettofan/0`) | CASI | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 🟡 |
| Vegetto Fanmade · Mui (`vegettofan/3`) | CASI | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 🟡 |
| Vegetto Fanmade · Dios Kaioken (`vegettofan/1`) | CASI | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 🟡 |
| Vegeta · Super Vegeta (`vegeta/2`) | CASI | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ❌ |
| Vegeta · Super Saiyan (`vegeta/1`) | CASI | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 🟡 |
| Vegeta · Ssj Blue (`vegeta/4`) | CASI | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ |
| Vegeta · Base (`vegeta/0`) | CASI | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | 🟡 |
| Vegeta Ui Dominado (`vegetamui/0`) | CASI | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | 🟡 |
| Vegeta Super · Ssj God (`vegetasuper/2`) | CASI | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 🟡 |
| Vegeta Gt · Super Saiyan 4 (`vegetagt/2`) | CASI | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | 🟡 |
| Vegeta Ego · Ultra Ego (`vegetaue/3`) | CASI | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 🟡 |
| Uub (`uub/0`) | CASI | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 🟡 |
| Turles · Ssj Maligno (`turles/1`) | CASI | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 🟡 |
| Turles · Base (`turles/0`) | CASI | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | 🟡 |
| Trunks · Super Saiyan (`trunks/1`) | CASI | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | 🟡 |
| Trunks (Cell) · Ultra Ssj (`trunkscell/2`) | CASI | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 🟡 |
| Trunks (Cell) · Base (`trunkscell/0`) | CASI | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 🟡 |
| Toppo (`toppo/0`) | CASI | 🟡 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Saiyans Zombi · Vegeta (`zombies/2`) | CASI | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | 🟡 |
| Saiyans Zombi · Goku (`zombies/1`) | CASI | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 🟡 |
| Saiyans Zombi · Gohan (`zombies/0`) | CASI | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 🟡 |
| Raditz · Super Saiyan (`raditz/1`) | CASI | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ❌ |
| Raditz · Base (`raditz/0`) | CASI | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ❌ |
| Piccolo · Piccolo Naranja (`piccolo/1`) | CASI | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ |
| Piccolo · Base (`piccolo/0`) | CASI | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ❌ |
| Majin Buu · Maligno (`buu/1`) | CASI | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ❌ |
| Majin Buu · Kid Buu (`buu/4`) | CASI | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ❌ |
| Kyabe · Super Saiyan (`kyabe/1`) | CASI | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ❌ | ✅ |
| Krilin (`krilin/0`) | CASI | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ |
| Kibito (`kibito/0`) | CASI | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ❌ |
| Kefla · Super Saiyan (`kefla/0`) | CASI | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | 🟡 |
| Kale · Berserker (`kale/1`) | CASI | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ❌ |
| Hit (`hit/0`) | CASI | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ❌ |
| Guldo (`guldo/0`) | CASI | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 🟡 |
| Granola (`granola/0`) | CASI | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ❌ |
| Gotenks (`gotenks/0`) | CASI | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | 🟡 |
| Goku · Super Saiyan 3 (`goku/3`) | CASI | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 🟡 |
| Goku · Base (`goku/0`) | CASI | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ |
| Goku Yardrat · Base (`gokuyardrat/0`) | CASI | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ❌ |
| Goku Xeno · Base (`gokuxeno/0`) | CASI | ✅ | ✅ | ✅ | ✅ | ✅ | 🟡 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Goku Ui Señal (`gokuuisign/0`) | CASI | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | 🟡 |
| Goku Super · Ssj God (`gokusuper/3`) | CASI | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ❌ |
| Goku Ssj4 Dios (`gokussj4dios/0`) | CASI | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ❌ |
| Goku Película Broly · Ssj Blue Perfecto (`gokubroly/3`) | CASI | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ |
| Goku Película Broly · Base (`gokubroly/0`) | CASI | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ |
| Goku Niño (`gokunino/0`) | CASI | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ❌ |
| Goku Fanmade · Místico (`gokualt/0`) | CASI | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ |
| Goku Black · Super Saiyan Rosé (`black/2`) | CASI | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ❌ |
| Goku Black · Base (`black/0`) | CASI | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ❌ |
| Gohan · Super Saiyan (`gohan/1`) | CASI | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ❌ |
| Gohan Poseído (`gohanposeido/0`) | CASI | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | 🟡 |
| Gohan Dbs · Ultra Instinto (`gohandbs/2`) | CASI | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Gohan Dbs · Místico (`gohandbs/1`) | CASI | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 🟡 |
| Gohan Dbs · Mui (`gohandbs/3`) | CASI | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Gogeta · Super Saiyan 4 (`gogeta/1`) | CASI | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ |
| Gogeta · Ssj Blue (`gogeta/2`) | CASI | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ |
| Gogeta Fanmade · Ssj4 Blue (`gogetafan/1`) | CASI | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 🟡 |
| Glorio (`glorio/0`) | CASI | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | 🟡 |
| Gas (`gas/0`) | CASI | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | 🟡 |
| Frost · Forma Final (`frost/1`) | CASI | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | 🟡 |
| Frost · 1ª Forma (`frost/0`) | CASI | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | 🟡 |
| Freezer · Golden (`freezer/4`) | CASI | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ❌ |
| Freezer · Forma Final (`freezer/2`) | CASI | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ❌ |
| Freezer · Black (`freezer/5`) | CASI | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ |
| Freezer · 1ª Forma (`freezer/0`) | CASI | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | 🟡 |
| Freezer · 100% (`freezer/3`) | CASI | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | 🟡 |
| Dlrx (`dlrx/0`) | CASI | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ |
| Cell · Semiperfecto (`cell/1`) | CASI | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ❌ |
| Cell · Majin (`cell/4`) | CASI | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 🟡 |
| Cell · Golden (`cell/3`) | CASI | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ |
| Caulifla (`caulifla/0`) | CASI | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | 🟡 |
| Capitán Ginyu (`ginyu/0`) | CASI | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 🟡 |
| Broly · Contenido (`broly/0`) | CASI | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ❌ |
| Broly Fanmade · Super Saiyan 3 (`brolyfan/1`) | CASI | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 🟡 |
| Broly Fanmade · Ssj Falso (`brolyfan/0`) | CASI | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 🟡 |
| Bra · Super Saiyan (`bra/1`) | CASI | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ |
| Bra Majin Ssj (`bramajin/0`) | CASI | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ❌ |
| Black Time Breaker · Ssj Rosé 3 (`blacktime/2`) | CASI | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ❌ | ✅ |
| Bills (`bills/0`) | CASI | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | 🟡 |
| Bardock · Super Saiyan (`bardock/1`) | CASI | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ❌ |
| Bardock · Forma 3 (`bardock/3`) | CASI | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ❌ |
| Bardock · Base (`bardock/0`) | CASI | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 🟡 |
| Bardock Leyendas · Evolución (`bardockalt/3`) | CASI | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 🟡 |
| Bardock Leyendas · Base (`bardockalt/0`) | CASI | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | 🟡 |
| Baby Vegeta (`babyvegeta/0`) | CASI | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 🟡 |
| Androide 21 (`a21/0`) | CASI | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 🟡 |
| Androide 18 (`a18/0`) | CASI | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ❌ |
| Tenshinhan (`tenshinhan/0`) | COMPLETA | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Mr. Satán (`mrsatan/0`) | COMPLETA | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Lord Slug (`slug/0`) | COMPLETA | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Jeice (`jeice/0`) | COMPLETA | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Gohan · Super Saiyan 2 (`gohan/2`) | COMPLETA | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Gohan Dbs · Bestia (`gohandbs/4`) | COMPLETA | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Gohan Dbs · Base (`gohandbs/0`) | COMPLETA | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Gogeta Fanmade · Mui (`gogetafan/2`) | COMPLETA | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Gogeta Fanmade · Blue Evolution (`gogetafan/0`) | COMPLETA | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Cooler (`cooler/0`) | COMPLETA | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Bra · Base (`bra/0`) | COMPLETA | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Bardock Leyendas · Super Saiyan (`bardockalt/1`) | COMPLETA | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Bardock Leyendas · Black (`bardockalt/2`) | COMPLETA | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

## Enemigos

| Enemigo | Estado | Guardia | Moverse | Puñetazos | Patadas | Ki | Poder/aura | Daño | Muerte | Retrato | Combo 2 | Combo 3 | Patada 2 | Rayo | Brazos arriba |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ginyu (Cuerpo De Goku) (`ginyucuerpogoku/0`) | A MEDIAS | 🟡 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ✅ | ❌ |
| Goku Black (Lsw) (`blacklsw/0`) | A MEDIAS | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Goku Ui Granola (V2) (`gokumuigranolav2/0`) | A MEDIAS | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Goku Ui Torneo (Anime) (`gokumuitorneoanime/0`) | A MEDIAS | 🟡 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Kyabe (Clásico) (`kyabeclasico/0`) | A MEDIAS | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Tora (`tora/0`) | A MEDIAS | 🟡 | ✅ | ✅ | ✅ | ✅ | 🟡 | ✅ | ✅ | ❌ | ✅ | ❌ | ✅ | ✅ | ✅ |
| Vegeta Explorador (Hd) (`vegetaexploradorhd/0`) | A MEDIAS | 🟡 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | 🟡 |
| Vegeta Sin Armadura (`vegetasinarmadura/0`) | A MEDIAS | 🟡 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Vegeta Ssj3 (Daima) (`vegetassj3daima/0`) | A MEDIAS | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Vegeta Super Saiyan 2 (Hd) (`vegetassj2hd/0`) | A MEDIAS | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Vegeta Xeno Ssj4 (`vegetaxenossj4/0`) | CASI | 🟡 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 🟡 |
| e_a19 (`e_a19/0`) | A MEDIAS | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| e_appule (`e_appule/0`) | A MEDIAS | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| e_blue (`e_blue/0`) | A MEDIAS | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| e_burter (`e_burter/0`) | A MEDIAS | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| e_dabura (`e_dabura/0`) | A MEDIAS | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| e_dodoria (`e_dodoria/0`) | A MEDIAS | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| e_drum (`e_drum/0`) | A MEDIAS | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| e_fasha (`e_fasha/0`) | A MEDIAS | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| e_freeza2 (`e_freeza2/0`) | A MEDIAS | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| e_garlic (`e_garlic/0`) | A MEDIAS | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| e_gero (`e_gero/0`) | A MEDIAS | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| e_ginyu (`e_ginyu/0`) | A MEDIAS | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| e_jeice (`e_jeice/0`) | A MEDIAS | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| e_kingveg (`e_kingveg/0`) | A MEDIAS | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| e_mecha (`e_mecha/0`) | A MEDIAS | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| e_murasaki (`e_murasaki/0`) | A MEDIAS | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| e_myuu (`e_myuu/0`) | A MEDIAS | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| e_nam (`e_nam/0`) | A MEDIAS | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| e_ozaru (`e_ozaru/0`) | A MEDIAS | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| e_puipui (`e_puipui/0`) | A MEDIAS | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| e_recoome (`e_recoome/0`) | A MEDIAS | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| e_rrsoldier (`e_rrsoldier/0`) | A MEDIAS | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| e_silver (`e_silver/0`) | A MEDIAS | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| e_soldado (`e_soldado/0`) | A MEDIAS | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| e_tambourine (`e_tambourine/0`) | A MEDIAS | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| e_whis (`e_whis/0`) | A MEDIAS | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| e_yamu (`e_yamu/0`) | A MEDIAS | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| e_zangya (`e_zangya/0`) | A MEDIAS | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| e_zarbon (`e_zarbon/0`) | A MEDIAS | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |

## Carpetas de personajes sin montar en el juego

No tienen ninguna animación en el juego todavía.

- `00_Dragon_Ball_Z/01_Namek_y_Freezer/DeviantArt/421_FREEZER FORMAS (qsab101)` (72 imágenes)
- `00_Dragon_Ball_Z/01_Namek_y_Freezer/Goku/060_Goku Ssj (Saga Freeza)` (80 imágenes)
- `00_Dragon_Ball_Z/02_Androides_Cell_y_Trunks/DeviantArt/407_ANDROIDE 19 (ChrisReinerVV)` (41 imágenes)
- `00_Dragon_Ball_Z/03_Majin_Buu/Goku/056_Goku SSJ 3` (55 imágenes)
- `00_Dragon_Ball_Z/03_Majin_Buu/Goku/278_GOKU SSJ3 ULSW DBZ` (130 imágenes)
- `00_Dragon_Ball_Z/03_Majin_Buu/Vegeta/300_Vegeta ssj3` (17 imágenes)
- `00_Dragon_Ball_Z/04_Peliculas_y_especiales/Broly/008_Broly ssj restringido,remake, Andrés Gamen` (30 imágenes)
- `00_Dragon_Ball_Z/04_Peliculas_y_especiales/DeviantArt/447_BUJIN (Morai)` (21 imágenes)
- `00_Dragon_Ball_Z/04_Peliculas_y_especiales/Goku/001_(Goku Genkidama absorbida) Andrés` (181 imágenes)
- `00_Dragon_Ball_Z/04_Peliculas_y_especiales/Goku/061_Goku Ssj Falso` (106 imágenes)
- `00_Dragon_Ball_Z/04_Peliculas_y_especiales/Goku/145_GOKU SSJ FALSO,DBZ,BY ANDRÉS GAMEN ANIMATIONS` (90 imágenes)
- `01_Dragon_Ball_Super/00_Dioses_y_Super_Saiyan_God/Vegeta/098_Vegeta Ssj God` (54 imágenes)
- `01_Dragon_Ball_Super/02_Universo_6/Hit/067_Hitto 2` (86 imágenes)
- `01_Dragon_Ball_Super/03_Trunks_del_futuro/Goku Black/039_Goku Black` (95 imágenes)
- `01_Dragon_Ball_Super/03_Trunks_del_futuro/Goku Black/268_GOKU BLACK (ZAMASU) ULSW` (94 imágenes)
- `01_Dragon_Ball_Super/03_Trunks_del_futuro/Goku Black/269_GOKU BLACK PITIKOS` (50 imágenes)
- `01_Dragon_Ball_Super/03_Trunks_del_futuro/Zamasu/107_Zamasu e Black Fusão Desmanchando - Damage` (10 imágenes)
- `01_Dragon_Ball_Super/03_Trunks_del_futuro/Zamasu/108_Zamasu e Black fusion Robotica` (143 imágenes)
- `01_Dragon_Ball_Super/04_Torneo_del_Poder/Goku/052_Goku Instinto Superior Completo` (59 imágenes)
- `01_Dragon_Ball_Super/04_Torneo_del_Poder/Goku/152_GOKU,MUI,EXTRA ,ANDRES GAMEN ANIMATIONS` (24 imágenes)
- `01_Dragon_Ball_Super/05_Broly/Goku/217_GOKU, TRAJE DE INVIERNO,DBS BROLY ,ANDRÉS GAMEN ANIMATIONS` (24 imágenes)
- `01_Dragon_Ball_Super/05_Broly/Goku/222_GOKU,SSJ BLUE,DBS BROLY, ANDRÉS GAMEN ANIMATIONS` (56 imágenes)
- `01_Dragon_Ball_Super/05_Broly/Vegeta/225_VEGETA,BASE,DBS, BROLY,DAMAGED, ANDRÉS GAMEN ANIMATIONS` (21 imágenes)
- `01_Dragon_Ball_Super/05_Broly/Vegeta/304_Vegeta com capote HD` (26 imágenes)
- `01_Dragon_Ball_Super/06_Moro/Vegeta/250_Vegeta ssj Dios patrullero galáctico.Andres Gamen` (85 imágenes)
- `01_Dragon_Ball_Super/08_Super_Hero/Piccolo/227_PICCOLO ORANGE (FORMA GIGANTE)` (81 imágenes)
- `01_Dragon_Ball_Super/08_Super_Hero/Piccolo/228_PICCOLO ORANGE DAMAGED` (10 imágenes)
- `01_Dragon_Ball_Super/09_Generales_y_manga/Bardock/224_BARDOCK,BASE,DBS` (53 imágenes)
- `01_Dragon_Ball_Super/09_Generales_y_manga/Gohan/110_GOHAN SSJ 1 DBS ANDRÉS GAMEN ANIMATIONS` (14 imágenes)
- `01_Dragon_Ball_Super/09_Generales_y_manga/Gohan/111_GOHAN SSJ 2 DBS ANDRÉS GAMEN ANIMATIONS` (12 imágenes)
- `01_Dragon_Ball_Super/09_Generales_y_manga/Gohan/157_Gohan (Manga)` (1 imágenes)
- `01_Dragon_Ball_Super/09_Generales_y_manga/Gohan/158_Gohan (Manga) - Ataque` (17 imágenes)
- `01_Dragon_Ball_Super/09_Generales_y_manga/Gohan/159_Gohan (Manga) - Daño` (3 imágenes)
- `01_Dragon_Ball_Super/09_Generales_y_manga/Gohan/160_Extra - Cabeza` (7 imágenes)
- `01_Dragon_Ball_Super/09_Generales_y_manga/Gohan/161_Extra - Ki` (4 imágenes)
- `01_Dragon_Ball_Super/09_Generales_y_manga/Gohan/162_Aros de Ki` (11 imágenes)
- `01_Dragon_Ball_Super/09_Generales_y_manga/Gohan/163_Escudo de Ki` (3 imágenes)
- `01_Dragon_Ball_Super/09_Generales_y_manga/Gohan/164_Kamehameha` (5 imágenes)
- `01_Dragon_Ball_Super/09_Generales_y_manga/Gohan/165_Efectos Kamehameha` (7 imágenes)
- `01_Dragon_Ball_Super/09_Generales_y_manga/Gohan/166_Masenko` (8 imágenes)
- `01_Dragon_Ball_Super/09_Generales_y_manga/Gohan/167_Efectos Masenko` (7 imágenes)
- `01_Dragon_Ball_Super/09_Generales_y_manga/Gohan/168_Gohan (Manga) - Ki` (4 imágenes)
- `01_Dragon_Ball_Super/09_Generales_y_manga/Gohan/169_Ki - si ki` (3 imágenes)
- `01_Dragon_Ball_Super/09_Generales_y_manga/Gohan/170_Gohan (Manga) - Pose` (3 imágenes)
- `01_Dragon_Ball_Super/09_Generales_y_manga/Gohan/171_Gohan (Manga) - Volador` (2 imágenes)
- `01_Dragon_Ball_Super/09_Generales_y_manga/Gohan/172_Volador - Dash` (2 imágenes)
- `01_Dragon_Ball_Super/09_Generales_y_manga/Gohan/173_Volador - Dash 2` (4 imágenes)
- `01_Dragon_Ball_Super/09_Generales_y_manga/Goku Black/042_Goku Black SSJ` (115 imágenes)
- `01_Dragon_Ball_Super/09_Generales_y_manga/Goku/046_Goku Blue` (124 imágenes)
- `01_Dragon_Ball_Super/09_Generales_y_manga/Goku/047_Goku Blue 2` (120 imágenes)
- `01_Dragon_Ball_Super/09_Generales_y_manga/Goku/143_GOKU SSJ BLUE PERFECTO,MEJORADO , ANDRÉS GAMEN ANIMATIONS` (121 imágenes)
- `02_GT/Vegeta/308_VEGETA SSJ4 HD` (65 imágenes)
- `03_Daima/Goku/279_GOKU SSJ4 ULSW DBZ DAIMA` (433 imágenes)
- `04_Heroes_y_videojuegos/Vegetto/294_veggeto xeno.ssj2.ssj3.ssj5.mini pack.andres Gamen` (46 imágenes)
- `05_Fanmade_y_alternativos/Broly/007_BROLY SSJ DIOS,DBZ,BY ANDRÉS GAMEN ANIMATIONS` (32 imágenes)
- `05_Fanmade_y_alternativos/Broly/194_Broly ssj legendario, perfecto, Andrés Gamen` (27 imágenes)
- `05_Fanmade_y_alternativos/Gogeta/155_Gogeta black.Andres Gamen` (52 imágenes)
- `05_Fanmade_y_alternativos/Gohan/195_Gohan del futuro,ssj3, Andrés Gamen` (25 imágenes)
- `05_Fanmade_y_alternativos/Goku Black/005_BLACKKU SSJ ROSE,BLUE, EVOLUTION,BY ANDRÉS GAMEN ANIMATIONS` (42 imágenes)
- `05_Fanmade_y_alternativos/Goku Black/175_Goku black Ultra instito dominado.Andres Gamen` (54 imágenes)
- `05_Fanmade_y_alternativos/Goku Black/183_Majin Goku black Ultra instito.Andres Gamen` (49 imágenes)
- `05_Fanmade_y_alternativos/Goku Black/185_Majin Goku black ssj Rosen.Andres Gamen` (53 imágenes)
- `05_Fanmade_y_alternativos/Goku Black/186_Majin Goku black ssj blue.Andres Gamen` (41 imágenes)
- `05_Fanmade_y_alternativos/Goku Black/187_Majin Goku black ssj1.Andres Gamen` (58 imágenes)
- `05_Fanmade_y_alternativos/Goku/137_GOKU MUI TRAJE WHISS BY ANDRÉS GAMEN ANIMATIONS` (58 imágenes)
- `05_Fanmade_y_alternativos/Goku/139_GOKU SSJ 100, ANDRÉS GAMEN ANIMATIONS, SPRITE HD` (28 imágenes)
- `05_Fanmade_y_alternativos/Goku/142_GOKU SSJ BLUE 3 ( traje wis ) ANDRÉS GAMEN ANIMATIONS` (62 imágenes)
- `05_Fanmade_y_alternativos/Goku/146_GOKU SSJ PRIMARIO, ANDRÉS GAMEN ANIMATIONS` (48 imágenes)
- `05_Fanmade_y_alternativos/Goku/179_Goku ultra ego` (229 imágenes)
- `05_Fanmade_y_alternativos/Goku/272_GOKU SSJ BLUE UNIVERSAL ULSW` (464 imágenes)
- `05_Fanmade_y_alternativos/Goku/318_GOKU .EXE ,ANDRÉS GAMEN ANIMATIONS` (35 imágenes)
- `05_Fanmade_y_alternativos/Varios/316_ANDRÉS GAMEN ANIMATIONS(.EXE) 🎃 SPRITE HD 🎃` (55 imágenes)
- `05_Fanmade_y_alternativos/Varios/317_EXTRA PACK DE SPRITES DE HELLOWEEN BY ANDRÉS GAMEN ANIMATIONS 🎃` (58 imágenes)
- `05_Fanmade_y_alternativos/Vegeta/197_Majin Vegeta ssj blue evolution, Damaged, Andrés Gamen` (39 imágenes)
- `05_Fanmade_y_alternativos/Vegeta/198_Vegeta ssj Blue1,Ultra ssjb, Damaged, Andrés Gamen` (31 imágenes)
- `05_Fanmade_y_alternativos/Vegeta/249_Vegeta Omni God,Damaged.Andres Gamen` (50 imágenes)
- `05_Fanmade_y_alternativos/Vegeta/310_vegeta ssj3 Blu` (60 imágenes)
- `07_Personajes_sin_saga_concreta/Goku/054_Goku SSJ 1(versión 2)` (112 imágenes)
- `07_Personajes_sin_saga_concreta/Goku/287_GOKU` (15 imágenes)
- `07_Personajes_sin_saga_concreta/Trunks/288_TRUNKS DEL FUTURO` (22 imágenes)
- `07_Personajes_sin_saga_concreta/Vegeta/091_Vegeta` (55 imágenes)
- `07_Personajes_sin_saga_concreta/Vegeta/289_VEGETA` (14 imágenes)
- `09_Packs_mixtos_por_revisar/Varios/109_EXTRA PACK DE SPRITES #3 ESPECIAL 5K ANDRÉS GAMEN ANIMATIONS` (212 imágenes)
- `09_Packs_mixtos_por_revisar/Varios/116_EXTRA PACK DE SPRITES PARTE 2 , BY ANDRÉS GAMEN ANIMATIONS ✓` (260 imágenes)
- `09_Packs_mixtos_por_revisar/Varios/203_MINI EXTRA PACK DE SPRITES, ANDRÉS GAMEN ANIMATIONS` (39 imágenes)
- `09_Packs_mixtos_por_revisar/Varios/229_SUPER EXTRA PACK DE SPRITES #2 (POR LOS 33KSUBS) DE ANDRÉS GAMEN ANIMATIONS 👍` (359 imágenes)
- `09_Packs_mixtos_por_revisar/Varios/230_SUPER EXTRA PACK DE SPRITES (ESPECIAL DE 24K DE SUBS) ANDRÉS GAMEN ANIMATIONS` (273 imágenes)
- `09_Packs_mixtos_por_revisar/Varios/291_SUPER EXTRA PACK DE SPRITES #3 (ESPECIAL 38K) ANDRÉS GAMEN ANIMATIONS 👍` (700 imágenes)

## Cómo animar con Piskel

1. `python herramientas/exportar_piskel_lote.py` deja en `piskel_animaciones/<personaje>_<forma>/` un `.piskel` por animación.
2. Abre el `.piskel` en https://www.piskelapp.com (Abrir → archivo), edita o añade fotogramas y guarda el `.piskel`.
3. `python herramientas/importar_piskel.py` lo devuelve al juego (lee `piskel_animaciones/LEEME.md` antes).
