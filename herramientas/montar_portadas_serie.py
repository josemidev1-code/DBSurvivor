# Portadas de los mapas al estilo de la serie (23 nov. 2026, Josemi: «todas las portadas tienen que ser de la serie,
# tiene que ser un buen fanmade»). Cada portada: escenario de la serie + protagonista (con su aura) frente al jefe del mapa.
#   python herramientas/montar_portadas_serie.py          -> ui/portadas_mapas/serie/<mapa>.png
#   python herramientas/montar_portadas.py --juego ui/portadas_mapas/serie   -> las mete en el juego
# Fondos: sprites/06_Escenarios (por nombre de archivo). Sala del Tiempo, Torneo y Red Ribbon no tienen fondo de la
# serie: usan una foto del propio juego (ui/portadas_mapas/fondos_juego/). Personajes: ui/portadas_mapas/personajes/
# (fotogramas del juego exportados con scHero: <id>_<forma>_idle.png y _pow.png).
import glob,os
from PIL import Image,ImageDraw,ImageFilter,ImageOps
os.chdir(os.path.join(os.path.dirname(__file__),'..'))
ESC='sprites/06_Escenarios/'
def f(nombre):
  r=[p for p in glob.glob(ESC+'**/*',recursive=True) if os.path.basename(p)==nombre];assert r,nombre;return r[0]
W,H=528,330
# mapa: (fondo, centro x del recorte 0-1 para panorámicas, protagonista (id, forma), jefe (id, forma))
PORTADAS={
 'namek':(f('Namek_1.jpg'),.5,('goku',1),('freezer',2)),
 'tierra':(f('DywTiyzXcAcDbjg.jpg'),.5,('goku',0),('vegeta',0)),
 'arena':(f('Dual-monitor-Dragon-Ball-Z-DBZ-wallpapers-HD-backgrounds.jpg'),.5,('gohan',2),('cell',2)),
 'time':('ui/portadas_mapas/fondos_juego/time.png',.5,('goku',1),('vegeta',2)),
 'vegetasei':(f('Planeta_Vegeta_en_Dragon_Ball_Super_Broly.png'),.5,('bardock',1),('freezer',0)),
 'futuro':(f('77caf420861431.562f257cd7b35.jpg'),.5,('trunks',1),('black',2)),
 'kame':(f('InShot_20221107_204740494.jpg'),.47,('goku',0),('roshi',0)),
 'paoz':(f('017.png'),.5,('gohan',0),('turles',0)),
 'kaio':(f('InShot_20221107_205118653.jpg'),.5,('goku',8),('vegeta',0)),
 'lookout':(f('88ba20e75056b4db5b91e8d0f57cb045.jpg'),.5,('piccolo',0),('buu',2)),
 'budokai':('ui/portadas_mapas/fondos_juego/budokai.png',.5,('goku',0),('piccolo',0)),
 'redribbon':('ui/portadas_mapas/fondos_juego/redribbon.png',.5,('krilin',0),('a17',0)),
 'musculo':(f('Escenario.jpg'),.5,('gokunino',0),('a16',0)),
 'capsule':(f('InShot_20221107_205032161.jpg'),.42,('bulma',0),('vegeta',0)),
 'yardrat':(f('sddefault.jpg'),.5,('gokuyardrat',0),('ginyu',0)),
 'kaioshin':(f('HxwyoWxopnQ7-HjG3oIw9Vcq1E8.png'),.5,('goku',3),('buu',4)),
 'infierno':(f('031.png'),.5,('gogeta',1),('janemba',0)),
 'bills':(f('20-Dbz-Planet-Namek-Background-Pictures-and-Ideas-on-Weric.jpg'),.5,('goku',9),('bills',0)),
 'poder':(f('universo-1-e1568576142428.jpg'),.5,('goku',6),('jiren',1)),
 'pradera':(f('dbz_sprite_backgrounds_by_sonicmechaomega999_d93msrb_-_selection.png'),.5,('piccolo',0),('raditz',0)),
 'bosque':(f('96f3bdce1866ec2a45711bfddbc7433c.gif'),.5,('krilin',0),('cell',0)),
 'desierto':(f('Paprika_Wasteland.jpg'),.5,('gokunino',0),('yamcha',0)),
 'gizard':(f('HTR001_Desierto.png'),.5,('piccolo',0),('nappa',0)),
 'volcan':(f('MH4_U_Ingle_Isle_Screenshot_001.png'),.5,('goku',1),('freezer',3)),
}
# su pose de aura (pow) no queda bien en portada: van en guardia
SIN_AURA={'piccolo'}
def fondo(ruta,cx):
  im=Image.open(ruta).convert('RGB');pixel=im.width<700 or ruta.endswith(('.png','.gif'))
  if im.width/im.height>2.2:  # panorámica muy ancha: recorte de proporción 1,6 sin encoger tanto
    h=im.height;w=int(h*1.6);x=int(max(0,min(im.width-w,im.width*cx-w/2)));im=im.crop((x,0,x+w,h))
  r=max(W/im.width,H/im.height);im=im.resize((round(im.width*r),round(im.height*r)),Image.NEAREST if pixel and r>1 else Image.LANCZOS)
  x=(im.width-W)//2;y=(im.height-H)//2;return im.crop((x,y,x+W,y+H)).convert('RGBA')
def personaje(hid,forma,pose,alto,voltear):
  ruta=f'ui/portadas_mapas/personajes/{hid}_{forma}_{pose}.png'
  if not os.path.exists(ruta):ruta=f'ui/portadas_mapas/personajes/{hid}_{forma}_idle.png'
  im=Image.open(ruta).convert('RGBA');im=im.crop(im.getbbox())
  if voltear:im=ImageOps.mirror(im)
  esc=max(2,round(alto/im.height));im=im.resize((im.width*esc,im.height*esc),Image.NEAREST)
  al=im.split()[3];borde=al.filter(ImageFilter.MaxFilter(5));out=Image.new('RGBA',(im.width+8,im.height+8))
  out.paste(Image.new('RGBA',im.size,(10,6,20,255)),(4,4),borde);out.alpha_composite(im,(4,4));return out
def capa(color,mascara):c=Image.new('RGBA',(W,H),color);c.putalpha(mascara);return c
def montar(k):
  ruta,cx,heroe,jefe=PORTADAS[k];im=fondo(ruta,cx)
  # viñeta y suelo oscuro para que destaquen los personajes
  m=Image.new('L',(W,H),0);ImageDraw.Draw(m).ellipse((-W*.2,-H*.25,W*1.2,H*1.15),fill=255);m=ImageOps.invert(m.filter(ImageFilter.GaussianBlur(55))).point(lambda v:v*120//255)
  im=Image.alpha_composite(im,capa((8,4,24,255),m))
  g=Image.new('L',(1,H));[g.putpixel((0,y),int(175*max(0,(y-H*.5)/(H*.5))**1.5)) for y in range(H)];im=Image.alpha_composite(im,capa((8,4,24,255),g.resize((W,H))))
  j=personaje(*jefe,'idle',H*.58,True);h=personaje(*heroe,'idle' if heroe[0] in SIN_AURA else 'pow',H*.5,False)
  # resplandor detrás de cada uno: dorado el protagonista, rojo el jefe
  for (px,py,pw,ph,col) in [(W-j.width//2-26,H-j.height//2-8,j.width,j.height,(255,70,50,95)),(34+h.width//2,H-h.height//2-12,h.width,h.height,(255,215,90,95))]:
    gl=Image.new('RGBA',(W,H));ImageDraw.Draw(gl).ellipse((px-pw*.75,py-ph*.62,px+pw*.75,py+ph*.62),fill=col);im=Image.alpha_composite(im,gl.filter(ImageFilter.GaussianBlur(28)))
  im.alpha_composite(j,(W-j.width-22,H-j.height-4));im.alpha_composite(h,(34,H-h.height-8))
  return im.convert('RGB')
os.makedirs('ui/portadas_mapas/serie',exist_ok=True)
for k in PORTADAS:montar(k).save(f'ui/portadas_mapas/serie/{k}.png')
print(len(PORTADAS),'portadas en ui/portadas_mapas/serie/')
