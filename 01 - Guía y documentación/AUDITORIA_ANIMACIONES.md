# Auditoría de animaciones (2026-11-11)

Generada con `python herramientas/auditar_animaciones.py`. Compara `sprites/` con las selecciones montadas en el juego. Un fotograma sin usar puede ser un efecto o un duplicado: la cifra indica material sin aprovechar, no ataques exactos.

## Resumen

- Carpetas con imágenes: **405** (37468 imágenes). En el juego: **302**. Sin usar: **103**.
- De las 103 sin usar, 10 son escenarios, referencias o Shenron; quedan **93** con personajes (6655 imágenes).
- En los packs usados hay 30590 imágenes y el juego usa **6273** (20 %).
- Formas de personajes jugables: 225. Con los 5 ataques extra completos: **76**. Sin ninguno: **36**.
- Formas de personajes ocultos que no se ven en el juego: 48. Formas solo de enemigo u otras: 40.

Ataques extra contados: `attack2`, `attack3`, `kick2`, `beam` y `up`. `dash` no cuenta porque reutiliza el cuerpo del vuelo.

## Personajes jugables, de menos a más completos

| Personaje | Formas | Fotogramas en sus packs | Usados | Ataques extra que faltan |
|---|---:|---:|---:|---:|
| blackfan | 4 | 522 | 74 | 20 |
| gokumoro | 5 | 445 | 80 | 19 |
| blacktime | 3 | 514 | 55 | 15 |
| gokubroly | 4 | 286 | 86 | 10 |
| kyabe | 2 | 162 | 30 | 10 |
| trunksnino | 2 | 346 | 29 | 10 |
| vegetamanga | 2 | 250 | 36 | 10 |
| gokualt | 3 | 302 | 67 | 7 |
| broly | 4 | 234 | 80 | 6 |
| bulma | 1 | 16 | 12 | 5 |
| freezer | 6 | 443 | 127 | 5 |
| gomah | 1 | 38 | 18 | 5 |
| kibitoshin | 1 | 22 | 15 | 5 |
| merus | 1 | 48 | 15 | 5 |
| nuova | 1 | 14 | 13 | 5 |
| tarble | 1 | 31 | 15 | 5 |
| trunksgt | 1 | 39 | 14 | 5 |
| vegetabroly | 1 | 101 | 18 | 5 |
| vegitoblue254 | 1 | 546 | 14 | 5 |
| cell | 5 | 461 | 107 | 4 |
| gogeta | 3 | 565 | 65 | 4 |
| gohan | 4 | 278 | 90 | 4 |
| goku | 5 | 393 | 114 | 4 |
| black | 3 | 359 | 68 | 3 |
| buu | 5 | 379 | 102 | 3 |
| gohanfut | 1 | 123 | 22 | 3 |
| janemba | 1 | 72 | 20 | 3 |
| jiren | 3 | 295 | 61 | 3 |
| kale | 2 | 100 | 45 | 3 |
| metalcooler | 1 | 56 | 17 | 3 |
| moro | 1 | 52 | 20 | 3 |
| reycold | 1 | 59 | 17 | 3 |
| shin | 1 | 51 | 19 | 3 |
| taopaipai | 1 | 78 | 18 | 3 |
| vegeta | 5 | 421 | 127 | 3 |
| a17 | 1 | 41 | 20 | 2 |
| bardock | 3 | 271 | 70 | 2 |
| blackkaioshin | 1 | 45 | 20 | 2 |
| cumber | 1 | 26 | 15 | 2 |
| daishinkan | 1 | 86 | 21 | 2 |
| gohanmanga | 1 | 87 | 21 | 2 |
| gokupatrulla | 1 | 53 | 21 | 2 |
| gokussj4daima | 1 | 281 | 21 | 2 |
| pangt | 1 | 99 | 21 | 2 |
| paragus | 1 | 99 | 22 | 2 |
| piccolo | 2 | 179 | 46 | 2 |
| raditz | 2 | 92 | 48 | 2 |
| roshi | 1 | 82 | 19 | 2 |
| super17 | 1 | 51 | 20 | 2 |
| trunks | 3 | 312 | 69 | 2 |
| trunksarmor | 1 | 74 | 17 | 2 |
| vegetaxeno | 1 | 185 | 21 | 2 |
| vegetto | 4 | 446 | 97 | 2 |
| a13 | 1 | 142 | 22 | 1 |
| a14 | 1 | 57 | 21 | 1 |
| a16 | 1 | 64 | 23 | 1 |
| a18 | 1 | 47 | 21 | 1 |
| bra | 2 | 217 | 50 | 1 |
| bramajin | 1 | 315 | 23 | 1 |
| cui | 1 | 46 | 21 | 1 |
| dlrx | 1 | 86 | 25 | 1 |
| dyspo | 1 | 128 | 25 | 1 |
| gokunino | 1 | 133 | 23 | 1 |
| gokussjchaqueta | 1 | 76 | 23 | 1 |
| gokussjkaioken | 1 | 76 | 22 | 1 |
| gokuuiverdadero | 1 | 140 | 22 | 1 |
| gokuxeno | 3 | 355 | 70 | 1 |
| gokuyardrat | 1 | 113 | 23 | 1 |
| goten | 1 | 89 | 20 | 1 |
| granola | 1 | 137 | 23 | 1 |
| hatchiyack | 1 | 56 | 22 | 1 |
| hit | 1 | 98 | 26 | 1 |
| jirengray | 1 | 73 | 22 | 1 |
| kibito | 1 | 85 | 25 | 1 |
| krilin | 1 | 81 | 22 | 1 |
| majinduu | 1 | 79 | 20 | 1 |
| majinkuu | 1 | 50 | 22 | 1 |
| nappa | 1 | 104 | 27 | 1 |
| omega | 1 | 56 | 19 | 1 |
| saibaman | 1 | 46 | 22 | 1 |
| vegetayardrat | 1 | 90 | 19 | 1 |
| vegettofalso | 1 | 124 | 22 | 1 |
| zamasu | 2 | 168 | 47 | 1 |
| zamasufusion | 1 | 136 | 18 | 1 |
| a21 | 1 | 195 | 29 | 0 |
| babyvegeta | 1 | 57 | 22 | 0 |
| bardockalt | 4 | 329 | 97 | 0 |
| bills | 1 | 78 | 27 | 0 |
| brolyfan | 2 | 241 | 50 | 0 |
| caulifla | 1 | 103 | 25 | 0 |
| cooler | 1 | 81 | 27 | 0 |
| frost | 2 | 106 | 48 | 0 |
| gas | 1 | 44 | 24 | 0 |
| ginyu | 1 | 111 | 26 | 0 |
| glorio | 1 | 90 | 23 | 0 |
| gogetafan | 3 | 573 | 79 | 0 |
| gohandbs | 5 | 603 | 128 | 0 |
| gohanposeido | 1 | 68 | 25 | 0 |
| gotenks | 1 | 108 | 26 | 0 |
| guldo | 1 | 103 | 28 | 0 |
| jeice | 1 | 79 | 26 | 0 |
| kefla | 2 | 253 | 52 | 0 |
| magetta | 1 | 84 | 22 | 0 |
| mrsatan | 1 | 371 | 31 | 0 |
| slug | 1 | 46 | 25 | 0 |
| tenshinhan | 1 | 77 | 25 | 0 |
| toppo | 1 | 77 | 26 | 0 |
| turles | 2 | 166 | 51 | 0 |
| uub | 1 | 93 | 28 | 0 |
| vegetabluemal | 1 | 89 | 22 | 0 |
| vegetamui | 1 | 115 | 23 | 0 |
| vegettofan | 4 | 691 | 98 | 0 |
| videl | 1 | 83 | 24 | 0 |
| yamcha | 1 | 79 | 22 | 0 |
| zombies | 3 | 396 | 74 | 0 |

## Packs de personajes sin usar

| Imágenes | Pack |
|---:|---|
| 1 | `00_Dragon_Ball_Z/00_Saiyans/DeviantArt` |
| 4 | `00_Dragon_Ball_Z/01_Namek_y_Freezer/DeviantArt` |
| 72 | `00_Dragon_Ball_Z/01_Namek_y_Freezer/DeviantArt/421_FREEZER FORMAS (qsab101)` |
| 80 | `00_Dragon_Ball_Z/01_Namek_y_Freezer/Goku/060_Goku Ssj (Saga Freeza)` |
| 1 | `00_Dragon_Ball_Z/02_Androides_Cell_y_Trunks/DeviantArt` |
| 41 | `00_Dragon_Ball_Z/02_Androides_Cell_y_Trunks/DeviantArt/407_ANDROIDE 19 (ChrisReinerVV)` |
| 2 | `00_Dragon_Ball_Z/03_Majin_Buu/DeviantArt` |
| 55 | `00_Dragon_Ball_Z/03_Majin_Buu/Goku/056_Goku SSJ 3` |
| 130 | `00_Dragon_Ball_Z/03_Majin_Buu/Goku/278_GOKU SSJ3 ULSW DBZ` |
| 17 | `00_Dragon_Ball_Z/03_Majin_Buu/Vegeta/300_Vegeta ssj3` |
| 30 | `00_Dragon_Ball_Z/04_Peliculas_y_especiales/Broly/008_Broly ssj restringido,remake, Andrés Gamen` |
| 21 | `00_Dragon_Ball_Z/04_Peliculas_y_especiales/DeviantArt/447_BUJIN (Morai)` |
| 181 | `00_Dragon_Ball_Z/04_Peliculas_y_especiales/Goku/001_(Goku Genkidama absorbida) Andrés` |
| 106 | `00_Dragon_Ball_Z/04_Peliculas_y_especiales/Goku/061_Goku Ssj Falso` |
| 90 | `00_Dragon_Ball_Z/04_Peliculas_y_especiales/Goku/145_GOKU SSJ FALSO,DBZ,BY ANDRÉS GAMEN ANIMATIONS` |
| 54 | `01_Dragon_Ball_Super/00_Dioses_y_Super_Saiyan_God/Vegeta/098_Vegeta Ssj God` |
| 86 | `01_Dragon_Ball_Super/02_Universo_6/Hit/067_Hitto 2` |
| 95 | `01_Dragon_Ball_Super/03_Trunks_del_futuro/Goku Black/039_Goku Black` |
| 94 | `01_Dragon_Ball_Super/03_Trunks_del_futuro/Goku Black/268_GOKU BLACK (ZAMASU) ULSW` |
| 50 | `01_Dragon_Ball_Super/03_Trunks_del_futuro/Goku Black/269_GOKU BLACK PITIKOS` |
| 10 | `01_Dragon_Ball_Super/03_Trunks_del_futuro/Zamasu/107_Zamasu e Black Fusão Desmanchando - Damage` |
| 143 | `01_Dragon_Ball_Super/03_Trunks_del_futuro/Zamasu/108_Zamasu e Black fusion Robotica` |
| 59 | `01_Dragon_Ball_Super/04_Torneo_del_Poder/Goku/052_Goku Instinto Superior Completo` |
| 24 | `01_Dragon_Ball_Super/04_Torneo_del_Poder/Goku/152_GOKU,MUI,EXTRA ,ANDRES GAMEN ANIMATIONS` |
| 24 | `01_Dragon_Ball_Super/05_Broly/Goku/217_GOKU, TRAJE DE INVIERNO,DBS BROLY ,ANDRÉS GAMEN ANIMATIONS` |
| 56 | `01_Dragon_Ball_Super/05_Broly/Goku/222_GOKU,SSJ BLUE,DBS BROLY, ANDRÉS GAMEN ANIMATIONS` |
| 21 | `01_Dragon_Ball_Super/05_Broly/Vegeta/225_VEGETA,BASE,DBS, BROLY,DAMAGED, ANDRÉS GAMEN ANIMATIONS` |
| 26 | `01_Dragon_Ball_Super/05_Broly/Vegeta/304_Vegeta com capote HD` |
| 85 | `01_Dragon_Ball_Super/06_Moro/Vegeta/250_Vegeta ssj Dios patrullero galáctico.Andres Gamen` |
| 81 | `01_Dragon_Ball_Super/08_Super_Hero/Piccolo/227_PICCOLO ORANGE (FORMA GIGANTE)` |
| 10 | `01_Dragon_Ball_Super/08_Super_Hero/Piccolo/228_PICCOLO ORANGE DAMAGED` |
| 53 | `01_Dragon_Ball_Super/09_Generales_y_manga/Bardock/224_BARDOCK,BASE,DBS` |
| 14 | `01_Dragon_Ball_Super/09_Generales_y_manga/Gohan/110_GOHAN SSJ 1 DBS ANDRÉS GAMEN ANIMATIONS` |
| 12 | `01_Dragon_Ball_Super/09_Generales_y_manga/Gohan/111_GOHAN SSJ 2 DBS ANDRÉS GAMEN ANIMATIONS` |
| 1 | `01_Dragon_Ball_Super/09_Generales_y_manga/Gohan/157_Gohan (Manga)` |
| 17 | `01_Dragon_Ball_Super/09_Generales_y_manga/Gohan/158_Gohan (Manga) - Ataque` |
| 3 | `01_Dragon_Ball_Super/09_Generales_y_manga/Gohan/159_Gohan (Manga) - Daño` |
| 7 | `01_Dragon_Ball_Super/09_Generales_y_manga/Gohan/160_Extra - Cabeza` |
| 4 | `01_Dragon_Ball_Super/09_Generales_y_manga/Gohan/161_Extra - Ki` |
| 11 | `01_Dragon_Ball_Super/09_Generales_y_manga/Gohan/162_Aros de Ki` |
| 3 | `01_Dragon_Ball_Super/09_Generales_y_manga/Gohan/163_Escudo de Ki` |
| 5 | `01_Dragon_Ball_Super/09_Generales_y_manga/Gohan/164_Kamehameha` |
| 7 | `01_Dragon_Ball_Super/09_Generales_y_manga/Gohan/165_Efectos Kamehameha` |
| 8 | `01_Dragon_Ball_Super/09_Generales_y_manga/Gohan/166_Masenko` |
| 7 | `01_Dragon_Ball_Super/09_Generales_y_manga/Gohan/167_Efectos Masenko` |
| 4 | `01_Dragon_Ball_Super/09_Generales_y_manga/Gohan/168_Gohan (Manga) - Ki` |
| 3 | `01_Dragon_Ball_Super/09_Generales_y_manga/Gohan/169_Ki - si ki` |
| 3 | `01_Dragon_Ball_Super/09_Generales_y_manga/Gohan/170_Gohan (Manga) - Pose` |
| 2 | `01_Dragon_Ball_Super/09_Generales_y_manga/Gohan/171_Gohan (Manga) - Volador` |
| 2 | `01_Dragon_Ball_Super/09_Generales_y_manga/Gohan/172_Volador - Dash` |
| 4 | `01_Dragon_Ball_Super/09_Generales_y_manga/Gohan/173_Volador - Dash 2` |
| 115 | `01_Dragon_Ball_Super/09_Generales_y_manga/Goku Black/042_Goku Black SSJ` |
| 124 | `01_Dragon_Ball_Super/09_Generales_y_manga/Goku/046_Goku Blue` |
| 120 | `01_Dragon_Ball_Super/09_Generales_y_manga/Goku/047_Goku Blue 2` |
| 121 | `01_Dragon_Ball_Super/09_Generales_y_manga/Goku/143_GOKU SSJ BLUE PERFECTO,MEJORADO , ANDRÉS GAMEN ANIMATIONS` |
| 65 | `02_GT/Vegeta/308_VEGETA SSJ4 HD` |
| 433 | `03_Daima/Goku/279_GOKU SSJ4 ULSW DBZ DAIMA` |
| 1 | `04_Heroes_y_videojuegos/DeviantArt` |
| 46 | `04_Heroes_y_videojuegos/Vegetto/294_veggeto xeno.ssj2.ssj3.ssj5.mini pack.andres Gamen` |
| 32 | `05_Fanmade_y_alternativos/Broly/007_BROLY SSJ DIOS,DBZ,BY ANDRÉS GAMEN ANIMATIONS` |
| 27 | `05_Fanmade_y_alternativos/Broly/194_Broly ssj legendario, perfecto, Andrés Gamen` |
| 52 | `05_Fanmade_y_alternativos/Gogeta/155_Gogeta black.Andres Gamen` |
| 25 | `05_Fanmade_y_alternativos/Gohan/195_Gohan del futuro,ssj3, Andrés Gamen` |
| 42 | `05_Fanmade_y_alternativos/Goku Black/005_BLACKKU SSJ ROSE,BLUE, EVOLUTION,BY ANDRÉS GAMEN ANIMATIONS` |
| 54 | `05_Fanmade_y_alternativos/Goku Black/175_Goku black Ultra instito dominado.Andres Gamen` |
| 49 | `05_Fanmade_y_alternativos/Goku Black/183_Majin Goku black Ultra instito.Andres Gamen` |
| 53 | `05_Fanmade_y_alternativos/Goku Black/185_Majin Goku black ssj Rosen.Andres Gamen` |
| 41 | `05_Fanmade_y_alternativos/Goku Black/186_Majin Goku black ssj blue.Andres Gamen` |
| 58 | `05_Fanmade_y_alternativos/Goku Black/187_Majin Goku black ssj1.Andres Gamen` |
| 58 | `05_Fanmade_y_alternativos/Goku/137_GOKU MUI TRAJE WHISS BY ANDRÉS GAMEN ANIMATIONS` |
| 28 | `05_Fanmade_y_alternativos/Goku/139_GOKU SSJ 100, ANDRÉS GAMEN ANIMATIONS, SPRITE HD` |
| 62 | `05_Fanmade_y_alternativos/Goku/142_GOKU SSJ BLUE 3 ( traje wis ) ANDRÉS GAMEN ANIMATIONS` |
| 48 | `05_Fanmade_y_alternativos/Goku/146_GOKU SSJ PRIMARIO, ANDRÉS GAMEN ANIMATIONS` |
| 229 | `05_Fanmade_y_alternativos/Goku/179_Goku ultra ego` |
| 464 | `05_Fanmade_y_alternativos/Goku/272_GOKU SSJ BLUE UNIVERSAL ULSW` |
| 35 | `05_Fanmade_y_alternativos/Goku/318_GOKU .EXE ,ANDRÉS GAMEN ANIMATIONS` |
| 55 | `05_Fanmade_y_alternativos/Varios/316_ANDRÉS GAMEN ANIMATIONS(.EXE) 🎃 SPRITE HD 🎃` |
| 58 | `05_Fanmade_y_alternativos/Varios/317_EXTRA PACK DE SPRITES DE HELLOWEEN BY ANDRÉS GAMEN ANIMATIONS 🎃` |
| 39 | `05_Fanmade_y_alternativos/Vegeta/197_Majin Vegeta ssj blue evolution, Damaged, Andrés Gamen` |
| 31 | `05_Fanmade_y_alternativos/Vegeta/198_Vegeta ssj Blue1,Ultra ssjb, Damaged, Andrés Gamen` |
| 50 | `05_Fanmade_y_alternativos/Vegeta/249_Vegeta Omni God,Damaged.Andres Gamen` |
| 60 | `05_Fanmade_y_alternativos/Vegeta/310_vegeta ssj3 Blu` |
| 112 | `07_Personajes_sin_saga_concreta/Goku/054_Goku SSJ 1(versión 2)` |
| 15 | `07_Personajes_sin_saga_concreta/Goku/287_GOKU` |
| 22 | `07_Personajes_sin_saga_concreta/Trunks/288_TRUNKS DEL FUTURO` |
| 55 | `07_Personajes_sin_saga_concreta/Vegeta/091_Vegeta` |
| 14 | `07_Personajes_sin_saga_concreta/Vegeta/289_VEGETA` |
| 212 | `09_Packs_mixtos_por_revisar/Varios/109_EXTRA PACK DE SPRITES #3 ESPECIAL 5K ANDRÉS GAMEN ANIMATIONS` |
| 260 | `09_Packs_mixtos_por_revisar/Varios/116_EXTRA PACK DE SPRITES PARTE 2 , BY ANDRÉS GAMEN ANIMATIONS ✓` |
| 39 | `09_Packs_mixtos_por_revisar/Varios/203_MINI EXTRA PACK DE SPRITES, ANDRÉS GAMEN ANIMATIONS` |
| 359 | `09_Packs_mixtos_por_revisar/Varios/229_SUPER EXTRA PACK DE SPRITES #2 (POR LOS 33KSUBS) DE ANDRÉS GAMEN ANIMATIONS 👍` |
| 273 | `09_Packs_mixtos_por_revisar/Varios/230_SUPER EXTRA PACK DE SPRITES (ESPECIAL DE 24K DE SUBS) ANDRÉS GAMEN ANIMATIONS` |
| 700 | `09_Packs_mixtos_por_revisar/Varios/291_SUPER EXTRA PACK DE SPRITES #3 (ESPECIAL 38K) ANDRÉS GAMEN ANIMATIONS 👍` |
