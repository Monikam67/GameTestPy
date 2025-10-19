from ursina import *
from ursina import load_texture
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.shaders import lit_with_shadows_shader, basic_lighting_shader, unlit_shader
from direct.filter.CommonFilters import CommonFilters
from panda3d.core import loadPrcFileData
from ursina import Entity

loadPrcFileData('', 'sync-video False')         # отключает VSync       # ограничение FPS
loadPrcFileData('', 'clock-frame-rate 180')     # максимум FPS
loadPrcFileData('', 'show-frame-rate-meter True')

app=Ursina()

walk=Audio('walk.mp3',loop=True,autoplay=False)
jump=Audio('jump.mp3',loop=False,autoplay=False)

ground=Entity(model='cube',collider='mesh',texture='grass',scale=(500,1,100))
player=FirstPersonController(collider='box')
brick=load_texture('Test1.jpg')
box_Y=10
box_X=2
box_Z=1
box1=Entity(model='cube',color=color.red,collider='box',position=(1,1,1))
box2=Entity(model='cube',color=color.green,collider='box',position=(4,1,1))
box3=Entity(model='cube',color=color.blue,collider='box',position=(1,4,1))
box4=Entity(model='cube',color=color.gray,collider='box',position=(1,1,4))
box5=Entity(model='cube',color=color.red,collider='box',position=(box_Y,box_X,box_Z))
#wall=Entity(model='cube',collider='box',texture='brick.jpg',scale=(20,10,2),position=(20,1,20))

sun = DirectionalLight(shadows=True)
sun.look_at(Vec3(-1,-1,-1))
sun.shadow_map_resolution = (4096, 4096)
sun.color=color.rgb(1, 0.95, 0.9)
AmbientLight(color=color.rgb(100,100,75))
Sky=Sky()
Sky.texture='sky_default'
filters = CommonFilters(base.win, base.cam)
filters.setBloom(intensity=1.5)


humana=Entity(
    parent=scene,position=(10,1,3.8))
head=Entity(parent=humana,model='Sphere',texture='face.jpg',scale=(0.7,0.7,0.7),position=(10,2.1,3.8),rotation=(0,90,0))
body= Entity(parent=humana,model='Sphere',texture='body.png',scale=(1,2,1),rotation=(0,90,0),position=(10,1,3.8))
right=Entity(parent=humana,model='Sphere',texture='body.png',scale=(0.5,2,0.5),rotation=(-30,120,0),position=(10.7,1,3.8))
human_collider=Entity(parent=humana,model='cube',position=(10,1,3.8),scale=(1,2,1),color=color.clear,collider='box')

humanb=Entity(
    parent=scene,position=(38,1,3.8))
heada=Entity(parent=humana,model='Sphere',texture='face.jpg',scale=(0.7,0.7,0.7),position=(38,2.1,3.8),rotation=(0,90,0))
bodya= Entity(parent=humana,model='Sphere',texture='body.png',scale=(1,2,1),rotation=(0,90,0),position=(38,1,3.8))
righta=Entity(parent=humana,model='Sphere',texture='body.png',scale=(0.5,2,0.5),rotation=(-30,120,0),position=(38.7,1,3.8))
human_collidera=Entity(parent=humana,model='cube',position=(38,1,3.8),scale=(1,2,1),color=color.clear,collider='box')

humanc=Entity(
    parent=scene,position=(10,1,-11))
headb=Entity(parent=humana,model='Sphere',texture='face.jpg',scale=(0.7,0.7,0.7),position=(10,2.1,-11),rotation=(0,-90,0))
bodyb= Entity(parent=humana,model='Sphere',texture='body.png',scale=(1,2,1),rotation=(0,-90,0),position=(10,1,-11))
rightb=Entity(parent=humana,model='Sphere',texture='body.png',scale=(0.5,2,0.5),rotation=(30,-120,0),position=(10.7,1,-11))
human_colliderb=Entity(parent=humana,model='cube',position=(10,1,-11),scale=(1,2,1),color=color.clear,collider='box')
all_npcs = [human_collider, human_collidera,human_colliderb,human_colliderb]


human2 = Entity(parent=scene,model='human.fbx',scale=0.1,position=(5, 1, 1),rotation_y=180,texture='human1.png',collider='sphere')
human2_collider=Entity(scale=1,position=(5, 1, 1),rotation_y=90,collider='sphere')

house1=Entity(model='house.glb',scale=1.0,position=(20,0.6,20))
house2=Entity(model='house.glb',scale=1.0,position=(50,0.6,20))
house3=Entity(model='house.glb',scale=1.0,position=(80,0.6,20))
house4=Entity(model='house.glb',scale=1.0,position=(110,0.6,20))
house5=Entity(model='house.glb',scale=1.0,position=(20,0.6,-20),rotation=(0,180,0))
house6=Entity(model='house.glb',scale=1.0,position=(50,0.6,-20),rotation=(0,180,0))
house7=Entity(model='house.glb',scale=1.0,position=(80,0.6,-20),rotation=(0,180,0))
house8=Entity(model='house.glb',scale=1.0,position=(110,0.6,-20),rotation=(0,180,0))
roada=Entity(model='cube',texture='road1.jpg',scale=(40,1,5),position=(20,0.2,0),collider='box',shader=lit_with_shadows_shader)
roadb=Entity(model='cube',texture='road1.jpg',scale=(40,1,5),position=(60,0.2,0),collider='box',shader=lit_with_shadows_shader)
roadc=Entity(model='cube',texture='road1.jpg',scale=(40,1,5),position=(100,0.2,0),collider='box',shader=lit_with_shadows_shader)
roadd=Entity(model='cube',texture='road1.jpg',scale=(40,1,5),position=(140,0.2,0),collider='box',shader=lit_with_shadows_shader)
roade=Entity(model='cube',texture='road1.jpg',scale=(40,1,5),position=(180,0.2,0),collider='box',shader=lit_with_shadows_shader)
roadf=Entity(model='cube',texture='road1.jpg',scale=(40,1,5),position=(220,0.2,0),collider='box',shader=lit_with_shadows_shader)
trotuara=Entity(model='cube',texture='trotuar.jpg',scale=(20,1,2),position=(10,0.1,5),collider='box',shader=lit_with_shadows_shader)
trotuarb=Entity(model='cube',texture='trotuar.jpg',scale=(20,1,2),position=(30,0.1,5),collider='box',shader=lit_with_shadows_shader)
trotuarc=Entity(model='cube',texture='trotuar.jpg',scale=(20,1,2),position=(50,0.1,5),collider='box',shader=lit_with_shadows_shader)
trotuard=Entity(model='cube',texture='trotuar.jpg',scale=(20,1,2),position=(70,0.1,5),collider='box',shader=lit_with_shadows_shader)
trotuare=Entity(model='cube',texture='trotuar.jpg',scale=(20,1,2),position=(90,0.1,5),collider='box',shader=lit_with_shadows_shader)
trotuarf=Entity(model='cube',texture='trotuar.jpg',scale=(20,1,2),position=(110,0.1,5),collider='box',shader=lit_with_shadows_shader)
trotuarg=Entity(model='cube',texture='trotuar.jpg',scale=(20,1,2),position=(10,0.1,-5),collider='box',shader=lit_with_shadows_shader)
trotuarh=Entity(model='cube',texture='trotuar.jpg',scale=(20,1,2),position=(30,0.1,-5),collider='box',shader=lit_with_shadows_shader)
trotuark=Entity(model='cube',texture='trotuar.jpg',scale=(20,1,2),position=(50,0.1,-5),collider='box',shader=lit_with_shadows_shader)
trotuar1=Entity(model='cube',texture='trotuar.jpg',scale=(20,1,2),position=(70,0.1,-5),collider='box',shader=lit_with_shadows_shader)
trotuar2=Entity(model='cube',texture='trotuar.jpg',scale=(20,1,2),position=(90,0.1,-5),collider='box',shader=lit_with_shadows_shader)
trotuar3=Entity(model='cube',texture='trotuar.jpg',scale=(20,1,2),position=(110,0.1,-5),collider='box',shader=lit_with_shadows_shader)
ogranich1=Entity(model='cube',scale=(500,20,0.1),position=(10,1,8),collider='box',color=color.clear)
ogranich2=Entity(model='cube',scale=(500,20,0.1),position=(10,1,-7),collider='box',color=color.clear)
# Диапазон 6-15 (для bigtree: 1-10)
tree1 = Entity(model='bush01.fbx', texture='bush01.png', scale=(0.003,0.003,0.003), position=(8,0.2,10))
bigtree1 = Entity(model='tree03.fbx', texture='tree03.png', scale=(0.007,0.007,0.007), position=(7,0.2,12))  # 12-5=7
tree2 = Entity(model='bush02.fbx', texture='bush02.png', scale=(0.003,0.003,0.003), position=(10,0.2,8))
bigtree2 = Entity(model='tree18.fbx', texture='tree18.png', scale=(0.007,0.007,0.007), position=(9,0.2,14))  # 14-5=9
tree3 = Entity(model='bush04.fbx', texture='bush04.png', scale=(0.003,0.003,0.003), position=(6,0.2,11))
bigtree3 = Entity(model='tree19.fbx', texture='tree19.png', scale=(0.007,0.007,0.007), position=(4,0.2,9))   # 9-5=4
tree4 = Entity(model='bush01.fbx', texture='bush01.png', scale=(0.003,0.003,0.003), position=(13,0.2,13))
bigtree4 = Entity(model='tree21.fbx', texture='tree21.png', scale=(0.007,0.007,0.007), position=(6,0.2,15))  # 11-5=6
tree5 = Entity(model='bush02.fbx', texture='bush02.png', scale=(0.003,0.003,0.003), position=(11,0.2,7))
tree6 = Entity(model='bush04.fbx', texture='bush04.png', scale=(0.003,0.003,0.003), position=(14,0.2,9))
bigtree5 = Entity(model='tree03.fbx', texture='tree03.png', scale=(0.007,0.007,0.007), position=(5,0.2,11))
bigtree21=Entity(model='tree03.fbx', texture='tree03.png', scale=(0.007,0.007,0.007), position=(14,0.2,11))
bigtree22=Entity(model='tree18.fbx', texture='tree18.png', scale=(0.007,0.007,0.007), position=(11,0.2,11))
tree25=Entity(model='bush02.fbx', texture='bush02.png', scale=(0.003,0.003,0.003), position=(28,0.2,11))
tree26=Entity(model='bush04.fbx', texture='bush04.png', scale=(0.003,0.003,0.003), position=(29,0.2,11))
tree27=Entity(model='bush04.fbx', texture='bush04.png', scale=(0.003,0.003,0.003), position=(32,0.2,11))
tree28=Entity(model='bush02.fbx', texture='bush02.png', scale=(0.003,0.003,0.003), position=(38,0.2,11))

# Диапазон 25-45 (для bigtree: 20-40)
bigtree6 = Entity(model='tree18.fbx', texture='tree18.png', scale=(0.007,0.007,0.007), position=(31,0.2,9))  # 28-5=23
tree7 = Entity(model='bush01.fbx', texture='bush01.png', scale=(0.003,0.003,0.003), position=(35,0.2,11))
bigtree7 = Entity(model='tree19.fbx', texture='tree19.png', scale=(0.007,0.007,0.007), position=(38,0.2,14)) # 32-5=27
tree8 = Entity(model='bush02.fbx', texture='bush02.png', scale=(0.003,0.003,0.003), position=(40,0.2,8))
bigtree8 = Entity(model='tree21.fbx', texture='tree21.png', scale=(0.007,0.007,0.007), position=(29,0.2,12)) # 25-5=20
tree9 = Entity(model='bush04.fbx', texture='bush04.png', scale=(0.003,0.003,0.003), position=(38,0.2,10))
bigtree9 = Entity(model='tree03.fbx', texture='tree03.png', scale=(0.007,0.007,0.007), position=(27,0.2,15)) # 30-5=25
tree10 = Entity(model='bush01.fbx', texture='bush01.png', scale=(0.003,0.003,0.003), position=(42,0.2,7))
bigtree10 = Entity(model='tree18.fbx', texture='tree18.png', scale=(0.007,0.007,0.007), position=(40,0.2,13)) # 45-5=40
tree11 = Entity(model='bush02.fbx', texture='bush02.png', scale=(0.003,0.003,0.003), position=(27,0.2,10))
tree12 = Entity(model='bush04.fbx', texture='bush04.png', scale=(0.003,0.003,0.003), position=(26,0.2,12))
bigtree25=Entity(model='tree19.fbx', texture='tree19.png', scale=(0.007,0.007,0.007), position=(30,0.2,11))
bigtree26=Entity(model='tree03.fbx', texture='tree03.png', scale=(0.007,0.007,0.007), position=(43,0.2,11))
bigtree27=Entity(model='tree03.fbx', texture='tree03.png', scale=(0.007,0.007,0.007), position=(40,0.2,11))
bigtree28=Entity(model='tree03.fbx', texture='tree03.png', scale=(0.007,0.007,0.007), position=(36,0.2,11))
tree29=Entity(model='bush01.fbx', texture='bush01.png', scale=(0.003,0.003,0.003), position=(27,0.2,11))
tree30=Entity(model='bush02.fbx', texture='bush02.png', scale=(0.003,0.003,0.003), position=(30,0.2,11))
tree31=Entity(model='bush02.fbx', texture='bush02.png', scale=(0.003,0.003,0.003), position=(32,0.2,11))
tree32=Entity(model='bush04.fbx', texture='bush04.png', scale=(0.003,0.003,0.003), position=(36,0.2,11))
tree33=Entity(model='bush02.fbx', texture='bush02.png', scale=(0.003,0.003,0.003), position=(43,0.2,11))
tree34=Entity(model='bush04.fbx', texture='bush04.png', scale=(0.003,0.003,0.003), position=(45,0.2,11))

# Диапазон 55-75 (для bigtree: 50-70)
tree13 = Entity(model='bush01.fbx', texture='bush01.png', scale=(0.003,0.003,0.003), position=(58,0.2,10))
bigtree11 = Entity(model='tree19.fbx', texture='tree19.png', scale=(0.007,0.007,0.007), position=(70,0.2,12)) # 65-5=60
tree14 = Entity(model='bush02.fbx', texture='bush02.png', scale=(0.003,0.003,0.003), position=(62,0.2,8))
bigtree12 = Entity(model='tree21.fbx', texture='tree21.png', scale=(0.007,0.007,0.007), position=(65,0.2,14)) # 70-5=65
tree15 = Entity(model='bush04.fbx', texture='bush04.png', scale=(0.003,0.003,0.003), position=(55,0.2,11))
bigtree13 = Entity(model='tree03.fbx', texture='tree03.png', scale=(0.007,0.007,0.007), position=(63,0.2,9))  # 68-5=63
tree16 = Entity(model='bush01.fbx', texture='bush01.png', scale=(0.003,0.003,0.003), position=(60,0.2,13))
bigtree14 = Entity(model='tree18.fbx', texture='tree18.png', scale=(0.007,0.007,0.007), position=(67,0.2,15)) # 72-5=67
tree17 = Entity(model='bush02.fbx', texture='bush02.png', scale=(0.003,0.003,0.003), position=(75,0.2,7))
tree18 = Entity(model='bush04.fbx', texture='bush04.png', scale=(0.003,0.003,0.003), position=(68,0.2,8))
bigtree15 = Entity(model='tree19.fbx', texture='tree19.png', scale=(0.007,0.007,0.007), position=(70,0.2,11)) # 75-5=70
tree35=Entity(model='bush02.fbx', texture='bush02.png', scale=(0.003,0.003,0.003), position=(59,0.2,11))
tree36=Entity(model='bush04.fbx', texture='bush04.png', scale=(0.003,0.003,0.003), position=(61,0.2,11))
tree37=Entity(model='bush01.fbx', texture='bush01.png', scale=(0.003,0.003,0.003), position=(63,0.2,11))
tree38=Entity(model='bush02.fbx', texture='bush02.png', scale=(0.003,0.003,0.003), position=(67,0.2,11))
tree39=Entity(model='bush02.fbx', texture='bush02.png', scale=(0.003,0.003,0.003), position=(70,0.2,11))
tree40=Entity(model='bush01.fbx', texture='bush01.png', scale=(0.003,0.003,0.003), position=(72,0.2,11))
tree41=Entity(model='bush01.fbx', texture='bush01.png', scale=(0.003,0.003,0.003), position=(75,0.2,11))
bigtree29 = Entity(model='tree19.fbx', texture='tree19.png', scale=(0.007,0.007,0.007), position=(60,0.2,11))
bigtree30 = Entity(model='tree19.fbx', texture='tree19.png', scale=(0.007,0.007,0.007), position=(64,0.2,11))
bigtree31 = Entity(model='tree21.fbx', texture='tree21.png', scale=(0.007,0.007,0.007), position=(62,0.2,11))
bigtree32 = Entity(model='tree18.fbx', texture='tree18.png', scale=(0.007,0.007,0.007), position=(74,0.2,11))
# Диапазон 6-15 (дом на 20, так что безопасно)
tree42 = Entity(model='bush01.fbx', texture='bush01.png', scale=(0.003,0.003,0.003), position=(8,0.2,-9))
bigtree33 = Entity(model='tree03.fbx', texture='tree03.png', scale=(0.007,0.007,0.007), position=(7,0.2,-11))
tree43 = Entity(model='bush02.fbx', texture='bush02.png', scale=(0.003,0.003,0.003), position=(10,0.2,-8))
bigtree34 = Entity(model='tree18.fbx', texture='tree18.png', scale=(0.007,0.007,0.007), position=(9,0.2,-13))
tree44 = Entity(model='bush04.fbx', texture='bush04.png', scale=(0.003,0.003,0.003), position=(6,0.2,-10))
bigtree35 = Entity(model='tree19.fbx', texture='tree19.png', scale=(0.007,0.007,0.007), position=(4,0.2,-12))
tree45 = Entity(model='bush01.fbx', texture='bush01.png', scale=(0.003,0.003,0.003), position=(13,0.2,-7))
bigtree36 = Entity(model='tree21.fbx', texture='tree21.png', scale=(0.007,0.007,0.007), position=(6,0.2,-8))
tree46 = Entity(model='bush02.fbx', texture='bush02.png', scale=(0.003,0.003,0.003), position=(11,0.2,-13))

# Диапазон 25-45 (избегаем дом на 20±5, начинаем от 26)
tree47 = Entity(model='bush04.fbx', texture='bush04.png', scale=(0.003,0.003,0.003), position=(26,0.2,-9))
bigtree37 = Entity(model='tree03.fbx', texture='tree03.png', scale=(0.007,0.007,0.007), position=(28,0.2,-11))
tree48 = Entity(model='bush01.fbx', texture='bush01.png', scale=(0.003,0.003,0.003), position=(30,0.2,-8))
bigtree38 = Entity(model='tree18.fbx', texture='tree18.png', scale=(0.007,0.007,0.007), position=(32,0.2,-13))
tree49 = Entity(model='bush02.fbx', texture='bush02.png', scale=(0.003,0.003,0.003), position=(35,0.2,-10))
bigtree39 = Entity(model='tree19.fbx', texture='tree19.png', scale=(0.007,0.007,0.007), position=(38,0.2,-12))
tree50 = Entity(model='bush04.fbx', texture='bush04.png', scale=(0.003,0.003,0.003), position=(40,0.2,-7))
bigtree40 = Entity(model='tree21.fbx', texture='tree21.png', scale=(0.007,0.007,0.007), position=(42,0.2,-8))
tree51 = Entity(model='bush01.fbx', texture='bush01.png', scale=(0.003,0.003,0.003), position=(45,0.2,-13))

# Диапазон 55-75 (избегаем дом на 50±5, начинаем от 56)
tree52 = Entity(model='bush02.fbx', texture='bush02.png', scale=(0.003,0.003,0.003), position=(56,0.2,-9))
bigtree41 = Entity(model='tree03.fbx', texture='tree03.png', scale=(0.007,0.007,0.007), position=(58,0.2,-11))
tree53 = Entity(model='bush04.fbx', texture='bush04.png', scale=(0.003,0.003,0.003), position=(60,0.2,-8))
bigtree42 = Entity(model='tree18.fbx', texture='tree18.png', scale=(0.007,0.007,0.007), position=(62,0.2,-13))
tree54 = Entity(model='bush01.fbx', texture='bush01.png', scale=(0.003,0.003,0.003), position=(65,0.2,-10))
bigtree43 = Entity(model='tree19.fbx', texture='tree19.png', scale=(0.007,0.007,0.007), position=(68,0.2,-12))
tree55 = Entity(model='bush02.fbx', texture='bush02.png', scale=(0.003,0.003,0.003), position=(70,0.2,-7))
bigtree44 = Entity(model='tree21.fbx', texture='tree21.png', scale=(0.007,0.007,0.007), position=(72,0.2,-8))
tree56 = Entity(model='bush04.fbx', texture='bush04.png', scale=(0.003,0.003,0.003), position=(75,0.2,-13))

# Диапазон 85-105 (избегаем дом на 80±5, начинаем от 86)
tree57 = Entity(model='bush01.fbx', texture='bush01.png', scale=(0.003,0.003,0.003), position=(86,0.2,-9))
bigtree45 = Entity(model='tree03.fbx', texture='tree03.png', scale=(0.007,0.007,0.007), position=(88,0.2,-11))
tree58 = Entity(model='bush02.fbx', texture='bush02.png', scale=(0.003,0.003,0.003), position=(90,0.2,-8))
bigtree46 = Entity(model='tree18.fbx', texture='tree18.png', scale=(0.007,0.007,0.007), position=(92,0.2,-13))
tree59 = Entity(model='bush04.fbx', texture='bush04.png', scale=(0.003,0.003,0.003), position=(95,0.2,-10))
bigtree47 = Entity(model='tree19.fbx', texture='tree19.png', scale=(0.007,0.007,0.007), position=(98,0.2,-12))
tree60 = Entity(model='bush01.fbx', texture='bush01.png', scale=(0.003,0.003,0.003), position=(100,0.2,-7))
bigtree48 = Entity(model='tree21.fbx', texture='tree21.png', scale=(0.007,0.007,0.007), position=(102,0.2,-8))
tree61 = Entity(model='bush02.fbx', texture='bush02.png', scale=(0.003,0.003,0.003), position=(105,0.2,-13))

# Дополнительные густые посадки между домами
tree62 = Entity(model='bush04.fbx', texture='bush04.png', scale=(0.003,0.003,0.003), position=(14,0.2,-10))
bigtree49 = Entity(model='tree03.fbx', texture='tree03.png', scale=(0.007,0.007,0.007), position=(12,0.2,-12))
tree63 = Entity(model='bush01.fbx', texture='bush01.png', scale=(0.003,0.003,0.003), position=(16,0.2,-11))
bigtree50 = Entity(model='tree18.fbx', texture='tree18.png', scale=(0.007,0.007,0.007), position=(15,0.2,-9))

# Диапазон 85-105 (для bigtree: 80-100)
bigtree16 = Entity(model='tree21.fbx', texture='tree21.png', scale=(0.007,0.007,0.007), position=(90,0.2,9))  # 88-5=83
tree19 = Entity(model='bush01.fbx', texture='bush01.png', scale=(0.003,0.003,0.003), position=(95,0.2,11))
bigtree17 = Entity(model='tree03.fbx', texture='tree03.png', scale=(0.007,0.007,0.007), position=(89,0.2,14)) # 92-5=87
tree20 = Entity(model='bush02.fbx', texture='bush02.png', scale=(0.003,0.003,0.003), position=(100,0.2,8))
bigtree18 = Entity(model='tree18.fbx', texture='tree18.png', scale=(0.007,0.007,0.007), position=(92,0.2,12)) # 85-5=80
tree21 = Entity(model='bush04.fbx', texture='bush04.png', scale=(0.003,0.003,0.003), position=(98,0.2,10))
bigtree19 = Entity(model='tree19.fbx', texture='tree19.png', scale=(0.007,0.007,0.007), position=(94,0.2,15)) # 90-5=85
tree22 = Entity(model='bush01.fbx', texture='bush01.png', scale=(0.003,0.003,0.003), position=(102,0.2,7))
bigtree20 = Entity(model='tree21.fbx', texture='tree21.png', scale=(0.007,0.007,0.007), position=(100,0.2,13)) # 105-5=100
tree23 = Entity(model='bush02.fbx', texture='bush02.png', scale=(0.003,0.003,0.003), position=(88,0.2,10))
tree24 = Entity(model='bush04.fbx', texture='bush04.png', scale=(0.003,0.003,0.003), position=(92,0.2,12))
# Дополнительные густые посадки между домами (продолжение)
tree64 = Entity(model='bush02.fbx', texture='bush02.png', scale=(0.003,0.003,0.003), position=(9,0.2,-10))
tree65 = Entity(model='bush04.fbx', texture='bush04.png', scale=(0.003,0.003,0.003), position=(11,0.2,-12))
bigtree51 = Entity(model='tree19.fbx', texture='tree19.png', scale=(0.007,0.007,0.007), position=(13,0.2,-8))
bigtree52 = Entity(model='tree21.fbx', texture='tree21.png', scale=(0.007,0.007,0.007), position=(15,0.2,-13))
tree66 = Entity(model='bush01.fbx', texture='bush01.png', scale=(0.003,0.003,0.003), position=(17,0.2,-9))

# Густая посадка в диапазоне 25-45
tree67 = Entity(model='bush02.fbx', texture='bush02.png', scale=(0.003,0.003,0.003), position=(27,0.2,-10))
tree68 = Entity(model='bush04.fbx', texture='bush04.png', scale=(0.003,0.003,0.003), position=(29,0.2,-12))
bigtree53 = Entity(model='tree03.fbx', texture='tree03.png', scale=(0.007,0.007,0.007), position=(31,0.2,-8))
tree69 = Entity(model='bush01.fbx', texture='bush01.png', scale=(0.003,0.003,0.003), position=(33,0.2,-13))
bigtree54 = Entity(model='tree18.fbx', texture='tree18.png', scale=(0.007,0.007,0.007), position=(35,0.2,-9))
tree70 = Entity(model='bush02.fbx', texture='bush02.png', scale=(0.003,0.003,0.003), position=(37,0.2,-11))
tree71 = Entity(model='bush04.fbx', texture='bush04.png', scale=(0.003,0.003,0.003), position=(39,0.2,-7))
bigtree55 = Entity(model='tree19.fbx', texture='tree19.png', scale=(0.007,0.007,0.007), position=(41,0.2,-10))
tree72 = Entity(model='bush01.fbx', texture='bush01.png', scale=(0.003,0.003,0.003), position=(43,0.2,-12))
bigtree56 = Entity(model='tree21.fbx', texture='tree21.png', scale=(0.007,0.007,0.007), position=(45,0.2,-8))

# Очень густая посадка в диапазоне 55-75
tree73 = Entity(model='bush02.fbx', texture='bush02.png', scale=(0.003,0.003,0.003), position=(57,0.2,-10))
tree74 = Entity(model='bush04.fbx', texture='bush04.png', scale=(0.003,0.003,0.003), position=(59,0.2,-12))
bigtree57 = Entity(model='tree03.fbx', texture='tree03.png', scale=(0.007,0.007,0.007), position=(61,0.2,-8))
tree75 = Entity(model='bush01.fbx', texture='bush01.png', scale=(0.003,0.003,0.003), position=(63,0.2,-13))
tree76 = Entity(model='bush02.fbx', texture='bush02.png', scale=(0.003,0.003,0.003), position=(65,0.2,-9))
bigtree58 = Entity(model='tree18.fbx', texture='tree18.png', scale=(0.007,0.007,0.007), position=(67,0.2,-11))
tree77 = Entity(model='bush04.fbx', texture='bush04.png', scale=(0.003,0.003,0.003), position=(69,0.2,-7))
tree78 = Entity(model='bush01.fbx', texture='bush01.png', scale=(0.003,0.003,0.003), position=(71,0.2,-10))
bigtree59 = Entity(model='tree19.fbx', texture='tree19.png', scale=(0.007,0.007,0.007), position=(73,0.2,-12))
tree79 = Entity(model='bush02.fbx', texture='bush02.png', scale=(0.003,0.003,0.003), position=(75,0.2,-8))

# Сверхгустая посадка в диапазоне 85-105
tree80 = Entity(model='bush04.fbx', texture='bush04.png', scale=(0.003,0.003,0.003), position=(87,0.2,-10))
tree81 = Entity(model='bush01.fbx', texture='bush01.png', scale=(0.003,0.003,0.003), position=(89,0.2,-12))
bigtree60 = Entity(model='tree21.fbx', texture='tree21.png', scale=(0.007,0.007,0.007), position=(91,0.2,-8))
tree82 = Entity(model='bush02.fbx', texture='bush02.png', scale=(0.003,0.003,0.003), position=(93,0.2,-13))
tree83 = Entity(model='bush04.fbx', texture='bush04.png', scale=(0.003,0.003,0.003), position=(95,0.2,-9))
bigtree61 = Entity(model='tree03.fbx', texture='tree03.png', scale=(0.007,0.007,0.007), position=(97,0.2,-11))
tree84 = Entity(model='bush01.fbx', texture='bush01.png', scale=(0.003,0.003,0.003), position=(99,0.2,-7))
tree85 = Entity(model='bush02.fbx', texture='bush02.png', scale=(0.003,0.003,0.003), position=(101,0.2,-10))
bigtree62 = Entity(model='tree18.fbx', texture='tree18.png', scale=(0.007,0.007,0.007), position=(103,0.2,-12))
tree86 = Entity(model='bush04.fbx', texture='bush04.png', scale=(0.003,0.003,0.003), position=(105,0.2,-8))

# Еще более густая посадка - заполняем все промежутки
tree87 = Entity(model='bush01.fbx', texture='bush01.png', scale=(0.003,0.003,0.003), position=(10,0.2,-11))
tree88 = Entity(model='bush02.fbx', texture='bush02.png', scale=(0.003,0.003,0.003), position=(12,0.2,-7))
bigtree63 = Entity(model='tree19.fbx', texture='tree19.png', scale=(0.007,0.007,0.007), position=(14,0.2,-12))
tree89 = Entity(model='bush04.fbx', texture='bush04.png', scale=(0.003,0.003,0.003), position=(16,0.2,-8))

tree90 = Entity(model='bush01.fbx', texture='bush01.png', scale=(0.003,0.003,0.003), position=(28,0.2,-11))
bigtree64 = Entity(model='tree21.fbx', texture='tree21.png', scale=(0.007,0.007,0.007), position=(30,0.2,-7))
tree91 = Entity(model='bush02.fbx', texture='bush02.png', scale=(0.003,0.003,0.003), position=(32,0.2,-12))
tree92 = Entity(model='bush04.fbx', texture='bush04.png', scale=(0.003,0.003,0.003), position=(34,0.2,-8))

tree93 = Entity(model='bush01.fbx', texture='bush01.png', scale=(0.003,0.003,0.003), position=(58,0.2,-11))
bigtree65 = Entity(model='tree03.fbx', texture='tree03.png', scale=(0.007,0.007,0.007), position=(60,0.2,-7))
tree94 = Entity(model='bush02.fbx', texture='bush02.png', scale=(0.003,0.003,0.003), position=(62,0.2,-12))
tree95 = Entity(model='bush04.fbx', texture='bush04.png', scale=(0.003,0.003,0.003), position=(64,0.2,-8))

tree96 = Entity(model='bush01.fbx', texture='bush01.png', scale=(0.003,0.003,0.003), position=(88,0.2,-11))
bigtree66 = Entity(model='tree18.fbx', texture='tree18.png', scale=(0.007,0.007,0.007), position=(90,0.2,-7))
tree97 = Entity(model='bush02.fbx', texture='bush02.png', scale=(0.003,0.003,0.003), position=(92,0.2,-12))
tree98 = Entity(model='bush04.fbx', texture='bush04.png', scale=(0.003,0.003,0.003), position=(94,0.2,-8))
back1=Entity(model='bush04.fbx', texture='bush04.png', scale=(0.1,0.031,0.030), position=(60,-0.4,30))
back2=Entity(model='bush04.fbx', texture='bush04.png', scale=(0.1,0.031,0.030), position=(0,-0.4,30))
back3=Entity(model='bush04.fbx', texture='bush04.png', scale=(0.1,0.031,0.030), position=(60,-0.4,-30))
back4=Entity(model='bush04.fbx', texture='bush04.png', scale=(0.1,0.031,0.030), position=(0,-0.4,-30))
back5=Entity(model='bush04.fbx', texture='bush04.png', scale=(0.1,0.031,0.030), position=(-30,0,0),rotation=(0,90,0))
back6=Entity(model='bush04.fbx', texture='bush04.png', scale=(0.1,0.031,0.030), position=(140,0,0),rotation=(0,90,0))
houseOWN=Entity(model='house2.glb',scale=1.3,position=(-6,0.6,0),collider='box')

# print("=== Дочерние узлы модели ===")
# for child in Trailer.model.get_children():
#     print(child)
houseOWN.shader=lit_with_shadows_shader
ground.shader = lit_with_shadows_shader
box1.shader = lit_with_shadows_shader
#wall.shader=lit_with_shadows_shader
human2.shader=lit_with_shadows_shader
box2.shader=lit_with_shadows_shader
box3.shader=lit_with_shadows_shader
box4.shader=lit_with_shadows_shader
box5.shader=lit_with_shadows_shader
box1.shader=lit_with_shadows_shader
humana.shader=lit_with_shadows_shader
head.shader=lit_with_shadows_shader
body.shader=lit_with_shadows_shader
right.shader=lit_with_shadows_shader
house1.shader=lit_with_shadows_shader

moon = Entity(
    model='sphere',
    color=color.rgb(180, 180, 255),
    scale=10,
    position=(50, 100, 100),
    double_sided=True
)







press_e_text = Text(
    text='>> НАЖМИТЕ E <<',
    position=(0, 0.3),
    origin=(0, 0),
    scale=1.8,
    color=color.green,
    background=True,
    background_color=color.rgba(0, 0, 0, 200),
    background_padding=(0.3, 0.2),
    border_color=color.cyan,
    border_width=2,
    enabled=False
)

press_e_text.enabled = False


dialogue_bg = Entity(parent=camera.ui, model='quad', scale=(1.6,1), y=-0.6,
                     color=color.black66)

dialogue_bg.enabled = False


npc_name = Text("Человек", parent=dialogue_bg, y=0.45,
                origin=(0, 0), scale=(2,2),color=color.white,bold=True)

npc_line = Text("...", parent=dialogue_bg, y=0.4,
                origin=(0, 0), scale=1.1, wordwrap=500)


button1 = Button(text='Привет и пока', color=color.green, scale=(0.2, 0.08),
                 position=(-0.15, -0.45), enabled=False)
button2 = Button(text='Пока', color=color.red, scale=(0.2, 0.08),
                 position=(0.15, -0.45), enabled=False)
button1.enabled = False
button2.enabled = False

in_dialogue = False


def update():
    global in_dialogue

    if in_dialogue:
        press_e_text.enabled = False
        return

    player_pos = player.position

    # Зоны для всех NPC
    in_zone1 = (18 <= player_pos.x <= 23 and
                0.4 <= player_pos.y <= 0.7 and
                3 <= player_pos.z <= 9)

    in_zone2 = (45 <= player_pos.x <= 52 and
                0.4 <= player_pos.y <= 0.7 and
                4 <= player_pos.z <= 7.5)

    in_zone3 = (17.5 <= player_pos.x <= 22.8 and
                    0.4 <= player_pos.y <= 0.7 and
                    -6.5 <= player_pos.z <= -4)

    # Отладка
    print(f"NPC1 - Hovered: {human_collider.hovered}, In zone: {in_zone1}")
    print(f"NPC2 - Hovered: {human_collidera.hovered}, In zone: {in_zone2}")
    print(f"NPC3 - Hovered: {human_colliderb.hovered}, In zone: {in_zone3}")
    print(f"Player: ({player_pos.x:.1f}, {player_pos.y:.1f}, {player_pos.z:.1f})")

    press_e_text.enabled = ((human_collider.hovered and in_zone1) or
                            (human_collidera.hovered and in_zone2) or
                            (human_colliderb.hovered and in_zone3))
    walking=held_keys['a']or held_keys['w'] or held_keys['d']or held_keys['s']
    if walking and player.grounded:
        if not walk.playing:
            walk.play()
    else:
        if walk.playing:
            walk.stop()


lvl = 1

def switch_level():
    global lvl
    if lvl == 1:
        # === ПЕРЕХОД НА НОЧЬ ===
        sun.color = color.rgb(0.16, 0.16, 0.24)
        AmbientLight(color=color.rgb(0.06, 0.06, 0.1))
        camera.background_color = color.rgb(0.01, 0.01, 0.04)
        Sky.texture = 'sky3.jpg'
        player.position = (0, 2, 0)

        # Добавляем шейдеры ко всем объектам
        apply_shaders_to_all_objects()


        lvl = 2
        print("Переключено на ночь (уровень 2) - шейдеры включены")
    else:
        # === ПЕРЕХОД НА ДЕНЬ ===
        sun.color = color.rgb(1.0, 0.95, 0.9)
        AmbientLight(color=color.rgb(0.6, 0.6, 0.6))
        camera.background_color = color.rgb(0.5, 0.7, 1.0)
        Sky.texture = 'sky_default'
        player.position = player.position

        # Убираем шейдеры со всех объектов
        remove_shaders_from_all_objects()

        lvl = 1
        print("Переключено на день (уровень 1) - шейдеры выключены")


def apply_shaders_to_all_objects():
    """Добавляет шейдер lit_with_shadows_shader ко всем объектам"""
    all_objects = []

    # Добавляем все tree объекты
    for i in range(1, 108):
        obj_name = f'tree{i}'
        if obj_name in globals():
            all_objects.append(globals()[obj_name])

    # Добавляем все bigtree объекты
    for i in range(1, 67):
        obj_name = f'bigtree{i}'
        if obj_name in globals():
            all_objects.append(globals()[obj_name])

    # Добавляем back объекты
    for i in range(1, 7):
        obj_name = f'back{i}'
        if obj_name in globals():
            all_objects.append(globals()[obj_name])
    for i in range(1,8):
        obj_name = f'house{i}'
        if obj_name in globals():
            all_objects.append(globals()[obj_name])
    for obj in all_objects:
        obj.shader = lit_with_shadows_shader

    print(f"Шейдеры применены к {len(all_objects)} объектам")


def remove_shaders_from_all_objects():
    """Убирает шейдеры со всех объектов"""
    all_objects = []

    # Добавляем все tree объекты
    for i in range(1, 108):
        obj_name = f'tree{i}'
        if obj_name in globals():
            all_objects.append(globals()[obj_name])

    # Добавляем все bigtree объекты
    for i in range(1, 67):
        obj_name = f'bigtree{i}'
        if obj_name in globals():
            all_objects.append(globals()[obj_name])

    # Добавляем back объекты
    for i in range(1, 7):
        obj_name = f'back{i}'
        if obj_name in globals():
            all_objects.append(globals()[obj_name])
    for i in range(1,8):
        obj_name = f'house{i}'
        if obj_name in globals():
            all_objects.append(globals()[obj_name])


    # Убираем шейдеры со всех объектов
    for obj in all_objects:
        obj.shader = unlit_shader

    print(f"Шейдеры убраны с {len(all_objects)} объектов")
def input(key):
    global in_dialogue

    if key == 'e' and not in_dialogue and press_e_text.enabled:
        player_pos = player.position

        # Проверяем зоны для всех NPC
        in_zone1 = (18 <= player_pos.x <= 23 and
                    0.4 <= player_pos.y <= 0.7 and
                    3 <= player_pos.z <= 9)

        in_zone2 = (45 <= player_pos.x <= 52 and
                    0.4 <= player_pos.y <= 0.7 and
                    4 <= player_pos.z <= 7.5)

        in_zone3 = (17.5 <= player_pos.x <= 22.8 and
                    0.4 <= player_pos.y <= 0.7 and
                    -6.5 <= player_pos.z <= -4)

        if human_collider.hovered and in_zone1:
            # Диалог с первым NPC
            in_dialogue = True
            dialogue_bg.enabled = True
            npc_name.text = "Человек 1"
            npc_line.text = "Привет! Рад тебя видеть. Что скажешь?"
            button1.enabled = True
            button2.enabled = True
            press_e_text.enabled = False
            player.enabled = False

        elif human_collidera.hovered and in_zone2:
            # Диалог со вторым NPC
            in_dialogue = True
            dialogue_bg.enabled = True
            npc_name.text = "Человек 2"
            npc_line.text = "Привет! Я второй NPC."
            button1.enabled = True
            button2.enabled = True
            press_e_text.enabled = False
            player.enabled = False

        elif human_colliderb.hovered and in_zone3:
            # Диалог с третьим NPC
            in_dialogue = True
            dialogue_bg.enabled = True
            npc_name.text = "Человек 3"
            npc_line.text = "Здравствуй! Я третий NPC."
            button1.enabled = True
            button2.enabled = True
            press_e_text.enabled = False
            player.enabled = False

    if key == '1' and in_dialogue:
        close_dialogue()
    if key == '2' and in_dialogue:
        close_dialogue()
    global lvl
    if key == 'p':
        switch_level()
    if key == 'space':
        if not jump.playing:
            jump.play()
    if key == 'q':
        quit()
def close_dialogue():
    global in_dialogue
    dialogue_bg.enabled = False
    button1.enabled = False
    button2.enabled = False
    in_dialogue = False
    press_e_text.enabled = False
    player.enabled = True
button1.on_click = close_dialogue
button2.on_click = close_dialogue
app.run()




