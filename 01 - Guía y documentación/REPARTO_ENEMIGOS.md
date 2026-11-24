# Reparto de enemigos por mapa (24 nov. 2026, sesión 25)

Pedido de Josemi: cada mapa con los enemigos que le tocan según el lore (nada de Majin Buu en Kame House) y bastantes enemigos distintos para que no sea repetitivo.

**Dónde está en el código:** `const ZONAS=` en `02 - Código del juego/script.js` (justo después de `depurarEnemigos`). Sustituye a los parches anteriores que metían los mismos enemigos en todos los mapas (saibamen, zombis, Turles, Cooler…). Para cambiar un mapa, solo hay que tocar su línea de `ZONAS`: `c` = comunes `[segundo, id, peso]`, `e` = élites (entran de uno en uno desde el minuto 2:30), `b` = jefes en orden, `ring` = anillo que te rodea, `squad` = escuadrón del minuto 10, `w` = oleadas.

**Enemigos nuevos (15 + 1 jefe):** usan el sprite de su grupo de la serie, pero cada uno con otro papel (pegador, embestidor, tirador) y otro color:
Soldado de la raza de Appule, Soldado de Frost, Asaltante y Artillero Red Ribbon, Hermano de Murasaki (en la serie son cuatro hermanos), Cell Jr. veloz y de ki, Trozo de Majin Buu, Saiyan zombi de ki, Clon de Zamasu con espada, Tropa del Orgullo y, como élites, Tao Pai Pai, Jackie Chun, Tenshinhan y Paragus. El jefe nuevo es Cell Superperfecto (mismo sprite que el Perfecto, como en la serie).

## Mapas

| Mapa | Saga / idea | Comunes | Élites | Jefes |
|---|---|---|---|---|
| Planeta Namek | Saga de Freezer | soldados de Freezer (raso, tirador, raza de Appule, élite) | Appule, Cui, Fuerzas Especiales, Vegeta, Freezer 2.ª | Dodoria → Zarbon → Ginyu → Freezer 1.ª, 2.ª, 3.ª → 100 % |
| Tierra volcánica | Namek se desmorona | soldados de Freezer | Cui, Vegeta, Freezer 2.ª, Cooler | Freezer (todas las formas) → Cooler |
| Planeta Yardrat | Cooler viene a por Goku | soldados de Freezer | Appule, Cui, Cooler, Freezer 2.ª | Cui → Rey Cold → Meca Freezer → Cooler → Metal Cooler |
| Planeta Vegeta | Saga de Bardock | soldados de Freezer, Fasha | Vegeta, Raditz, Nappa, Rey Vegeta | Dodoria → Zarbon → Rey Vegeta → Ozaru → Freezer |
| Yermo de Gizard | Llegada de los Saiyans | los cuatro saibamen | Raditz, Nappa, Vegeta, Turles | Raditz → Nappa → Turles → Vegeta → Ozaru Vegeta |
| Praderas | Raditz y películas en la Tierra | saibamen | Raditz, Garlic Jr., Turles, Zangya, Paragus | Raditz → Garlic → Turles → Slug → Broly (3 formas) |
| Kame House | Red Ribbon (General Blue) y Raditz | soldados Red Ribbon | Blue, Raditz, 17, 18 | Blue → Raditz → 17 → Cell imperfecto → semiperfecto |
| Monte Paoz | Garlic Jr. y androides en casa de Goku | saibamen (provisional) | Garlic, Raditz, 16, 17, 18 | Raditz → Garlic → 18 → 17 → 16 |
| Bosque profundo | Bosque de Karin | soldados Red Ribbon | Silver, Tao Pai Pai, Blue, Garlic | Silver → Blue → Tao → Garlic → Piccolo Daimaku |
| Torre Músculo | Red Ribbon | soldados RR, hermanos de Murasaki | Murasaki, Silver, Tao, Blue | Silver → Murasaki → Blue → Tao → Dr. Gero |
| Base Red Ribbon | Red Ribbon y laboratorio de Gero | soldados RR | Silver, Murasaki, Blue, Tao, 13, 14 | Blue → Tao → Gero → 19 → 16 → 13 → 21 |
| Desierto | Androides del Dr. Gero | soldados RR | Gero, 13, 14, 17, 18, 21 | Gero → 19 → 13 → 16 → 21 → 21 Majin |
| Tierra · Yermo | Llegan Freezer y los androides | soldados de Freezer (de Rey Cold) | Gero, 16, 17, 18, Cell imperfecto | Meca Freezer → Rey Cold → 19 → Gero → Cell (3 formas) |
| Juegos de Cell | Saga de Cell | Cell Jr. (normal, veloz, de ki) | 16, 17, 18, Cell Perfecto, Cell Jr. | Cell imp. → semi → 16 → Perfecto → Superperfecto |
| Ciudad del Oeste | Freezer resucita; Bills en la fiesta | soldados de Freezer | Gero, Freezer 2.ª, Cooler | 19 → Gero → Freezer → Golden Freezer → Bills |
| Tenkaichi Budokai | Torneos 21-25 | Pui Pui, Yamu, fragmentos de Buu | Nam, Jackie Chun, Tenshinhan, Tao, Tambourine, Majin Vegeta | Nam → Jackie Chun → Tao → Piccolo Daimaku → Majin Vegeta |
| Templo de Kami | Garlic Jr. y Buu en la Atalaya | fragmentos de Buu, Pui Pui | Garlic, Buu maligno, Super Buu, Gohan poseído | Piccolo → Garlic → Buu maligno → Super Buu → Buu con Gohan |
| Mundo Kaioshin | Saga de Majin Buu | fragmentos de Buu, Pui Pui, Yamu | Majin Vegeta, las formas de Buu | Dabura → Majin Vegeta → Buu (todas) → Kid Buu |
| Infierno | La fusión de los muertos (Janemba) | Saiyans zombi | Fuerzas Especiales, Cooler, Cell, Hatchiyack | Cooler → Freezer → Cell → Kid Buu → Janemba |
| Planeta de Kaio | El Más Allá | Saiyans zombi | Fuerzas Especiales, Cell | Jeice → Recoome → Ginyu → Freezer → Cell |
| Futuro de Trunks | Saga de Goku Black | clones de Zamasu | 17, 18, Black, Zamasu | 17 → 18 → Black → Black SSJ → Zamasu → Rosé → Zamasu fusionado |
| Planeta de Bills | Torneo de Champa | soldados de Frost | Frost, Magetta, Hit, Vegeta | Frost → Magetta → Hit → Vegeta → Whis → Bills |
| Torneo del Poder | Torneo del Poder | Tropas del Orgullo, soldados de Frost | Dyspo, Magetta, Frost, Hit, Kale | Dyspo → Frost → Kale → Hit → Toppo → Jiren |
| Sala del Tiempo | Entrenamiento: rivales de todas las épocas | mezcla de todas las sagas | mezcla | Myuu → Baby → Super 17 → Gomah → Gas → Moro → Omega |

La Sala del Tiempo hace de mapa mezcla porque en la serie no hay enemigos dentro; ahí van también los de GT, Daima y Granola, que aún no tienen mapa propio.

Fuera de los mapas a propósito: Goku SSJ, Vegeta SSJ y Trunks SSJ como jefes (son héroes) y Broly SSJ4 (es de fans).

## Sprites que hacen falta (para pedírselos a Josemi)

Con los packs de ahora, varios mapas solo tienen 2-3 tipos de comunes. Lo que más falta, por orden:

1. **Ejército Red Ribbon:** General White, Sargento Metallic, Androide 8, Comandante Red, Black con la armadura de combate → Base Red Ribbon, Torre Músculo, Bosque, Kame House.
2. **Esbirros de las películas:** los de Garlic Jr. (Sansho, Nicky, Ginger) → Monte Paoz y Templo de Kami; los de Slug (Medamatcha, Angila, Wings) y la banda de Turles (Amond, Cacao, Daiz, Rasin, Lakasei) → Praderas y Gizard; el escuadrón de Cooler (Salza, Neiz, Dore) → Yardrat; Bojack y su banda (Bujin, Bido, Gokua) → Juegos de Cell.
3. **Saiyans de clase baja** (Tora, Shugesh, Borgos) → Planeta Vegeta (Tora ya tiene pack jugable; se puede usar).
4. **Torneo de Artes Marciales:** Bacterian, Giran, Spopovich; y Babidi → Budokai y Mundo Kaioshin.
5. **Dragon Ball Super:** Tropas del Orgullo de verdad (Kahseral, Tupper, Zoiray…), Botamo, Sorbet y Tagoma, Gamma 1 y 2 → Torneo del Poder, Bills, Ciudad del Oeste.
6. **Más Allá:** luchadores del torneo del Más Allá (Pikkon, Olibu…) → Planeta de Kaio.
7. **Ambiente de Dragon Ball clásico:** robots de Pilaf, animales salvajes, dinosaurios → Monte Paoz y Desierto (hoy Monte Paoz usa saibamen de forma provisional).
