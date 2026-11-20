// Transformaciones en partida (diseño aprobado por Josemi el 20 nov. 2026: 01 - Guía y documentación/TRANSFORMACIONES.md).
// Lógica pura, sin dibujo ni DOM, para poder probarla con Node (herramientas/comprobar_transformaciones.cjs).
// Expone window.TRANSF. Se carga antes que script.js (el juego sigue abriéndose con doble clic).
(function(){
  // Cadenas de los personajes principales: solo formas de la serie, en el orden en que salen.
  // Las que no estén aquí usan todas sus formas en el orden del juego.
  const CADENAS={
    goku:['BASE','KAIOKEN','SUPER SAIYAN','SUPER SAIYAN 2','SUPER SAIYAN 3','SSJ DIOS','SSJ BLUE','UI SEÑAL','UI DOMINADO'],
    vegeta:['BASE','SUPER SAIYAN','SUPER VEGETA','MAJIN VEGETA','SSJ DIOS','SSJ BLUE','BLUE EVOLUTION','ULTRA EGO'],
    gohan:['BASE','SUPER SAIYAN','SUPER SAIYAN 2','DEFINITIVO','BESTIA'],
    piccolo:['BASE','PICCOLO NARANJA'],
    krilin:['BASE'],
    trunks:['BASE','SUPER SAIYAN','SSJ2 MANGA'],
    goten:['SUPER SAIYAN'],
    freezer:['1ª FORMA','3ª FORMA','FORMA FINAL','100%','GOLDEN','BLACK'],
    cell:['IMPERFECTO','SEMIPERFECTO','PERFECTO'],
    buu:['GORDO','MALIGNO','SUPER BUU','BUU GOHAN','KID BUU'],
    broly:['CONTENIDO','SUPER SAIYAN','LEGENDARIO']
  };

  // Mejora de cada forma (multiplicadores) y su rasgo de la serie. duraK acorta la duración (formas que gastan mucho).
  const M=(dmg,spd,cd,hp,rasgo,duraK)=>duraK?{dmg,spd,cd,hp,rasgo:rasgo||null,duraK}:{dmg,spd,cd,hp,rasgo:rasgo||null};
  const MEJORAS={
    'SUPER SAIYAN':M(1.25,1.06,0.95,1.15),
    'KAIOKEN':M(1.35,1.10,0.95,1.0,'kaioken'),
    'SUPER SAIYAN 2':M(1.45,1.08,0.92,1.25,'rayos'),
    'SSJ2 MANGA':M(1.45,1.08,0.92,1.25,'rayos'),
    'SUPER SAIYAN 3':M(1.75,1.06,0.90,1.30,null,0.7),
    'SSJ DIOS':M(1.70,1.15,0.88,1.40,'regenera'),
    'SSJ BLUE':M(2.00,1.12,0.85,1.45,null,0.7),
    'UI SEÑAL':M(2.10,1.20,0.82,1.45,'esquiva'),
    'UI DOMINADO':M(2.40,1.25,0.80,1.50,'esquivaContra'),
    'SUPER VEGETA':M(1.45,0.95,0.95,1.30),
    'MAJIN VEGETA':M(1.60,1.06,0.90,1.30,'majin'),
    'BLUE EVOLUTION':M(2.20,1.12,0.84,1.50),
    'ULTRA EGO':M(2.20,1.10,0.85,1.60,'ultraEgo'),
    'DEFINITIVO':M(1.80,1.12,0.86,1.45),
    'BESTIA':M(2.20,1.15,0.84,1.45,'bestia'),
    'PICCOLO NARANJA':M(1.60,1.00,0.90,1.80),
    '3ª FORMA':M(1.20,1.00,0.95,1.35),
    'FORMA FINAL':M(1.40,1.12,0.92,1.30),
    '100%':M(1.75,1.10,0.88,1.40,'cansancio'),
    'GOLDEN':M(2.10,1.15,0.85,1.50,null,0.7),
    'BLACK':M(2.40,1.18,0.82,1.60),
    'SEMIPERFECTO':M(1.30,1.04,0.94,1.40),
    'PERFECTO':M(1.70,1.10,0.88,1.50,'regenera'),
    'MALIGNO':M(1.35,1.15,0.92,1.15),
    'SUPER BUU':M(1.60,1.10,0.90,1.35,'absorbe'),
    'BUU GOHAN':M(1.85,1.12,0.87,1.40,'absorbe'),
    'KID BUU':M(2.00,1.18,0.85,1.35,'regenera'),
    'LEGENDARIO':M(1.70,1.00,0.90,1.60,'legendario'),
    'PODER MÁXIMO':M(1.50,1.10,0.90,1.20)
  };
  const NEUTRA={dmg:1.25,spd:1.06,cd:0.95,hp:1.15,rasgo:null};

  function cadena(hid,forms){
    const L=CADENAS[hid];if(!L)return forms.map((_,i)=>i);
    const r=[];for(const n of L){const i=forms.indexOf(n);if(i>=0)r.push(i)}
    return r.length?r:[0];
  }
  function tiempos(paso){return{carga:3+1.5*(paso-1),dura:Math.max(8,25-3*(paso-1))}}
  function nivelPaso(paso,pasos){return pasos>1?Math.round(5+35*(paso-1)/(pasos-1)):20}
  function mejora(nombre){return MEJORAS[nombre]||NEUTRA}

  // Estado de la carga: carga (0-1 hacia la forma siguiente), paso (0 = base), t (segundos que quedan transformado)
  function nuevo(){return{carga:0,paso:0,t:0,cargando:false}}
  // e = {cargando, golpes, muertes, abiertos (pasos que se pueden alcanzar), nombre(paso) → nombre de la forma}
  // Devuelve 'sube', 'vuelve' o null.
  function avanzar(T,e,dt){
    T.cargando=!!e.cargando;
    if(T.paso>0){T.t-=dt;if(T.t<=0){T.paso=0;T.carga=0;T.t=0;return 'vuelve'}}
    if(T.paso<e.abiertos){
      if(e.cargando)T.carga+=dt/tiempos(T.paso+1).carga;
      T.carga+=0.02*(e.muertes||0);
    }
    T.carga=Math.max(0,T.carga-0.35*(e.golpes||0));
    if(T.paso<e.abiertos&&T.carga>=1-1e-9){
      T.paso++;T.carga=0;T.t=tiempos(T.paso).dura*(mejora(e.nombre(T.paso)).duraK||1);return 'sube';
    }
    if(T.paso>=e.abiertos)T.carga=Math.min(T.carga,0);
    return null;
  }

  window.TRANSF={CADENAS,MEJORAS,cadena,tiempos,nivelPaso,mejora,nuevo,avanzar};
})();
