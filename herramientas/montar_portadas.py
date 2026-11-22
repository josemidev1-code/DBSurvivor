# Genera portadas_mapas.js: una portada por mapa, incrustada (sin fetch).
# Dos modos:
#   python herramientas/montar_portadas.py                 -> dibujos de sprites/06_Escenarios (las portadas antiguas)
#   python herramientas/montar_portadas.py --juego CARPETA -> CARPETA/<mapa>.png. Hoy: ui/portadas_mapas/serie, hechas con
#                                                            herramientas/montar_portadas_serie.py (23 nov. 2026)
import glob,io,base64,json,os,sys
from PIL import Image
os.chdir(os.path.join(os.path.dirname(__file__),'..'))
ELEGIDAS={'namek':85,'tierra':20,'arena':16,'time':121,'vegetasei':83,'futuro':82,'kame':47,'paoz':30,'kaio':23,'lookout':11,
 'budokai':56,'redribbon':67,'musculo':71,'capsule':36,'yardrat':87,'kaioshin':41,'infierno':128,'bills':49,'poder':112,
 'pradera':7,'bosque':15,'desierto':32,'gizard':69,'volcan':24}
out={};fuentes={}
if '--juego' in sys.argv:
  carpeta=sys.argv[sys.argv.index('--juego')+1]
  for k in ELEGIDAS:
    im=Image.open(os.path.join(carpeta,k+'.png')).convert('RGB')
    # pixel art: paleta de 128 colores sin tramado, en PNG (nítido y ligero)
    im=im.resize((352,220),Image.LANCZOS)  # en el menú se ven a 176×110: el doble para pantallas nítidas
    b=io.BytesIO();im.save(b,'JPEG',quality=86)  # JPEG: los fondos de la serie tienen demasiados colores para una paleta
    out[k]='data:image/jpeg;base64,'+base64.b64encode(b.getvalue()).decode();fuentes[k]=carpeta+'/'+k+'.png'
else:
  fs=[f for f in sorted(glob.glob('sprites/06_Escenarios/**/*',recursive=True)) if f.lower().endswith(('.png','.jpg','.jpeg','.webp','.gif'))]
  W,H=264,165  # índice de la hoja de miniaturas (orden alfabético de rutas) -> mapa
  for k,i in ELEGIDAS.items():
    im=Image.open(fs[i]).convert('RGB');r=max(W/im.width,H/im.height)
    im=im.resize((round(im.width*r),round(im.height*r)),Image.LANCZOS);x=(im.width-W)//2;y=(im.height-H)//2;im=im.crop((x,y,x+W,y+H))
    b=io.BytesIO();im.save(b,'JPEG',quality=82);out[k]='data:image/jpeg;base64,'+base64.b64encode(b.getvalue()).decode()
    fuentes[k]=fs[i].replace(chr(92),'/')
open('02 - Código del juego/portadas_mapas.js','w',encoding='utf-8').write('// Generado por herramientas/montar_portadas.py\nwindow.MAP_COVER='+json.dumps(out)+';\nwindow.MAP_COVER_SRC='+json.dumps(fuentes,ensure_ascii=False,indent=0)+';\n')
print(len(out),os.path.getsize('02 - Código del juego/portadas_mapas.js'))
