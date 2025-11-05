from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.shaders import lit_with_shadows_shader, basic_lighting_shader, unlit_shader
from direct.filter.CommonFilters import CommonFilters
from panda3d.core import loadPrcFileData
from ursina import Entity
import random
import pygame
import threading
import time
loadPrcFileData('', 'sync-video False')         # отключает VSync       # ограничение FPS
loadPrcFileData('', 'clock-frame-rate 180')     # максимум FPS
loadPrcFileData('', 'show-frame-rate-meter True')

app=Ursina()
ui_front = Entity(parent=camera.ui)
walk=Audio('../walk.mp3', loop=True, autoplay=False,volume=0.4)
jump=Audio('../jump.mp3', loop=False, autoplay=False)
text_sound = Audio('soundtext1.m4a', loop=True, autoplay=False,volume=0.8)
hit_sound = Audio('2.mp3', loop=False, autoplay=False)
miss_sound = Audio('1.mp3', loop=False, autoplay=False)
battle_sound = Audio('battlesound.ogg', loop=True, autoplay=False)
battle_reaction_sound = Audio('battlereaction.ogg', loop=False, autoplay=False)
battle2_sound = Audio('battle2.ogg', loop=False, autoplay=False)
attack2_sound = Audio('attack2.ogg', loop=False, autoplay=False)
bg_music = Audio('BG.ogg', loop=True, autoplay=False)
bossa_sound=Audio('bossa_sound.mp3', loop=True, autoplay=False)
ground=Entity(model='cube',collider='mesh',texture='grass',scale=(500,1,100))


player=FirstPersonController(collider='box')


sun = DirectionalLight(shadows=True)
sun.look_at(Vec3(-1,-1,-1))
sun.shadow_map_resolution = (4096, 4096)
sun.color=color.rgb(1, 0.95, 0.9)
AmbientLight(color=color.rgb(100,100,75))
Sky=Sky()
Sky.texture='sky_default'
filters = CommonFilters(base.win, base.cam)
filters.setBloom(intensity=1)

# StartHome=Entity(model='StartHome.glb', scale=2, position=(1,0.2,0),collider='mesh')






humana=Entity(
    parent=scene,position=(10,1,3.8))
head=Entity(parent=humana,model='sphere',texture='face.jpg',scale=(0.7,0.7,0.7),position=(10,2.1,3.8),rotation=(0,90,0))
body= Entity(parent=humana,model='sphere',texture='body.png',scale=(1,2,1),rotation=(0,90,0),position=(10,1,3.8))
right=Entity(parent=humana,model='sphere',texture='body.png',scale=(0.5,2,0.5),rotation=(-30,120,0),position=(10.7,1,3.8))
human_collider=Entity(parent=humana,model='cube',position=(10,1,3.8),scale=(1,2,1),color=color.clear,collider='box')

humanb=Entity(
    parent=scene,position=(38,1,3.8))
heada=Entity(parent=humana,model='sphere',texture='face.jpg',scale=(0.7,0.7,0.7),position=(38,2.1,3.8),rotation=(0,90,0))
bodya= Entity(parent=humana,model='sphere',texture='body.png',scale=(1,2,1),rotation=(0,90,0),position=(38,1,3.8))
righta=Entity(parent=humana,model='sphere',texture='body.png',scale=(0.5,2,0.5),rotation=(-30,120,0),position=(38.7,1,3.8))
human_collidera=Entity(parent=humana,model='cube',position=(38,1,3.8),scale=(1,2,1),color=color.clear,collider='box')

humanc=Entity(
    parent=scene,position=(10,1,-11))
headb=Entity(parent=humana,model='sphere',texture='face.jpg',scale=(0.7,0.7,0.7),position=(10,2.1,-11),rotation=(0,-90,0))
bodyb= Entity(parent=humana,model='sphere',texture='body.png',scale=(1,2,1),rotation=(0,-90,0),position=(10,1,-11))
rightb=Entity(parent=humana,model='sphere',texture='body.png',scale=(0.5,2,0.5),rotation=(30,-120,0),position=(10.7,1,-11))
human_colliderb=Entity(parent=humana,model='cube',position=(10,1,-11),scale=(1,2,1),color=color.clear,collider='box')
bossa=Entity(parent=scene,position=(13.12,12.4,15.47),model='sphere',texture='face.jpg',scale=(2,2,2),rotation=(0,90,0))
bossa_collider=Entity(position=(13.12,10,15.47),model='cube',scale=(2,9,2),color=color.clear,collider='box')
all_npcs = [human_collider, human_collidera,human_colliderb,human_colliderb,bossa_collider]


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
# roadd=Entity(model='cube',texture='road1.jpg',scale=(40,1,5),position=(140,0.2,0),collider='box',shader=lit_with_shadows_shader)
# roade=Entity(model='cube',texture='road1.jpg',scale=(40,1,5),position=(180,0.2,0),collider='box',shader=lit_with_shadows_shader)
# roadf=Entity(model='cube',texture='road1.jpg',scale=(40,1,5),position=(220,0.2,0),collider='box',shader=lit_with_shadows_shader)
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
tree1 = Entity(model='bush01.fbx', texture='bush01.png', scale=(0.003,0.003,0.003), position=(8,0.2,10), shader=unlit_shader)
bigtree1 = Entity(model='tree03.fbx', texture='tree03.png', scale=(0.007,0.007,0.007), position=(7,0.2,12), shader=unlit_shader)
tree2 = Entity(model='bush02.fbx', texture='bush02.png', scale=(0.003,0.003,0.003), position=(10,0.2,8), shader=unlit_shader)
bigtree2 = Entity(model='tree18.fbx', texture='tree18.png', scale=(0.007,0.007,0.007), position=(9,0.2,14), shader=unlit_shader)
tree3 = Entity(model='bush04.fbx', texture='bush04.png', scale=(0.003,0.003,0.003), position=(6,0.2,11), shader=unlit_shader)
bigtree3 = Entity(model='tree19.fbx', texture='tree19.png', scale=(0.007,0.007,0.007), position=(4,0.2,9), shader=unlit_shader)
tree4 = Entity(model='bush01.fbx', texture='bush01.png', scale=(0.003,0.003,0.003), position=(13,0.2,13), shader=unlit_shader)
bigtree4 = Entity(model='tree21.fbx', texture='tree21.png', scale=(0.007,0.007,0.007), position=(6,0.2,15), shader=unlit_shader)
tree5 = Entity(model='bush02.fbx', texture='bush02.png', scale=(0.003,0.003,0.003), position=(11,0.2,7), shader=unlit_shader)
tree6 = Entity(model='bush04.fbx', texture='bush04.png', scale=(0.003,0.003,0.003), position=(14,0.2,9), shader=unlit_shader)
bigtree5 = Entity(model='tree03.fbx', texture='tree03.png', scale=(0.007,0.007,0.007), position=(5,0.2,11), shader=unlit_shader)
bigtree21=Entity(model='tree03.fbx', texture='tree03.png', scale=(0.007,0.007,0.007), position=(14,0.2,11), shader=unlit_shader)
bigtree22=Entity(model='tree18.fbx', texture='tree18.png', scale=(0.007,0.007,0.007), position=(11,0.2,11), shader=unlit_shader)
tree25=Entity(model='bush02.fbx', texture='bush02.png', scale=(0.003,0.003,0.003), position=(28,0.2,11), shader=unlit_shader)
tree26=Entity(model='bush04.fbx', texture='bush04.png', scale=(0.003,0.003,0.003), position=(29,0.2,11), shader=unlit_shader)
tree27=Entity(model='bush04.fbx', texture='bush04.png', scale=(0.003,0.003,0.003), position=(32,0.2,11), shader=unlit_shader)
tree28=Entity(model='bush02.fbx', texture='bush02.png', scale=(0.003,0.003,0.003), position=(38,0.2,11), shader=unlit_shader)

bigtree6 = Entity(model='tree18.fbx', texture='tree18.png', scale=(0.007,0.007,0.007), position=(31,0.2,9), shader=unlit_shader)
tree7 = Entity(model='bush01.fbx', texture='bush01.png', scale=(0.003,0.003,0.003), position=(35,0.2,11), shader=unlit_shader)
bigtree7 = Entity(model='tree19.fbx', texture='tree19.png', scale=(0.007,0.007,0.007), position=(38,0.2,14), shader=unlit_shader)
tree8 = Entity(model='bush02.fbx', texture='bush02.png', scale=(0.003,0.003,0.003), position=(40,0.2,8), shader=unlit_shader)
bigtree8 = Entity(model='tree21.fbx', texture='tree21.png', scale=(0.007,0.007,0.007), position=(29,0.2,12), shader=unlit_shader)
tree9 = Entity(model='bush04.fbx', texture='bush04.png', scale=(0.003,0.003,0.003), position=(38,0.2,10), shader=unlit_shader)
bigtree9 = Entity(model='tree03.fbx', texture='tree03.png', scale=(0.007,0.007,0.007), position=(27,0.2,15), shader=unlit_shader)
tree10 = Entity(model='bush01.fbx', texture='bush01.png', scale=(0.003,0.003,0.003), position=(42,0.2,7), shader=unlit_shader)
bigtree10 = Entity(model='tree18.fbx', texture='tree18.png', scale=(0.007,0.007,0.007), position=(40,0.2,13), shader=unlit_shader)
tree11 = Entity(model='bush02.fbx', texture='bush02.png', scale=(0.003,0.003,0.003), position=(27,0.2,10), shader=unlit_shader)
tree12 = Entity(model='bush04.fbx', texture='bush04.png', scale=(0.003,0.003,0.003), position=(26,0.2,12), shader=unlit_shader)
bigtree25=Entity(model='tree19.fbx', texture='tree19.png', scale=(0.007,0.007,0.007), position=(30,0.2,11), shader=unlit_shader)
bigtree26=Entity(model='tree03.fbx', texture='tree03.png', scale=(0.007,0.007,0.007), position=(43,0.2,11), shader=unlit_shader)
bigtree27=Entity(model='tree03.fbx', texture='tree03.png', scale=(0.007,0.007,0.007), position=(40,0.2,11), shader=unlit_shader)
bigtree28=Entity(model='tree03.fbx', texture='tree03.png', scale=(0.007,0.007,0.007), position=(36,0.2,11), shader=unlit_shader)
tree29=Entity(model='bush01.fbx', texture='bush01.png', scale=(0.003,0.003,0.003), position=(27,0.2,11), shader=unlit_shader)
tree30=Entity(model='bush02.fbx', texture='bush02.png', scale=(0.003,0.003,0.003), position=(30,0.2,11), shader=unlit_shader)
tree31=Entity(model='bush02.fbx', texture='bush02.png', scale=(0.003,0.003,0.003), position=(32,0.2,11), shader=unlit_shader)
tree32=Entity(model='bush04.fbx', texture='bush04.png', scale=(0.003,0.003,0.003), position=(36,0.2,11), shader=unlit_shader)
tree33=Entity(model='bush02.fbx', texture='bush02.png', scale=(0.003,0.003,0.003), position=(43,0.2,11), shader=unlit_shader)
tree34=Entity(model='bush04.fbx', texture='bush04.png', scale=(0.003,0.003,0.003), position=(45,0.2,11), shader=unlit_shader)

tree13 = Entity(model='bush01.fbx', texture='bush01.png', scale=(0.003,0.003,0.003), position=(58,0.2,10), shader=unlit_shader)
bigtree11 = Entity(model='tree19.fbx', texture='tree19.png', scale=(0.007,0.007,0.007), position=(72,0.2,12), shader=unlit_shader)
tree14 = Entity(model='bush02.fbx', texture='bush02.png', scale=(0.003,0.003,0.003), position=(62,0.2,8), shader=unlit_shader)
bigtree12 = Entity(model='tree21.fbx', texture='tree21.png', scale=(0.007,0.007,0.007), position=(65,0.2,14), shader=unlit_shader)
tree15 = Entity(model='bush04.fbx', texture='bush04.png', scale=(0.003,0.003,0.003), position=(55,0.2,11), shader=unlit_shader)
bigtree13 = Entity(model='tree03.fbx', texture='tree03.png', scale=(0.007,0.007,0.007), position=(63,0.2,9), shader=unlit_shader)
tree16 = Entity(model='bush01.fbx', texture='bush01.png', scale=(0.003,0.003,0.003), position=(60,0.2,13), shader=unlit_shader)
bigtree14 = Entity(model='tree18.fbx', texture='tree18.png', scale=(0.007,0.007,0.007), position=(67,0.2,15), shader=unlit_shader)
tree17 = Entity(model='bush02.fbx', texture='bush02.png', scale=(0.003,0.003,0.003), position=(75,0.2,7), shader=unlit_shader)
tree18 = Entity(model='bush04.fbx', texture='bush04.png', scale=(0.003,0.003,0.003), position=(68,0.2,8), shader=unlit_shader)
bigtree15 = Entity(model='tree19.fbx', texture='tree19.png', scale=(0.007,0.007,0.007), position=(70,0.2,11), shader=unlit_shader)
tree35=Entity(model='bush02.fbx', texture='bush02.png', scale=(0.003,0.003,0.003), position=(59,0.2,11), shader=unlit_shader)
tree36=Entity(model='bush04.fbx', texture='bush04.png', scale=(0.003,0.003,0.003), position=(61,0.2,11), shader=unlit_shader)
tree37=Entity(model='bush01.fbx', texture='bush01.png', scale=(0.003,0.003,0.003), position=(63,0.2,11), shader=unlit_shader)
tree38=Entity(model='bush02.fbx', texture='bush02.png', scale=(0.003,0.003,0.003), position=(67,0.2,11), shader=unlit_shader)
tree39=Entity(model='bush02.fbx', texture='bush02.png', scale=(0.003,0.003,0.003), position=(70,0.2,11), shader=unlit_shader)
tree40=Entity(model='bush01.fbx', texture='bush01.png', scale=(0.003,0.003,0.003), position=(72,0.2,11), shader=unlit_shader)
tree41=Entity(model='bush01.fbx', texture='bush01.png', scale=(0.003,0.003,0.003), position=(75,0.2,11), shader=unlit_shader)
bigtree29 = Entity(model='tree19.fbx', texture='tree19.png', scale=(0.007,0.007,0.007), position=(60,0.2,11), shader=unlit_shader)
bigtree30 = Entity(model='tree19.fbx', texture='tree19.png', scale=(0.007,0.007,0.007), position=(64,0.2,11), shader=unlit_shader)
bigtree32 = Entity(model='tree18.fbx', texture='tree18.png', scale=(0.007,0.007,0.007), position=(74,0.2,11), shader=unlit_shader)

tree42 = Entity(model='bush01.fbx', texture='bush01.png', scale=(0.003,0.003,0.003), position=(8,0.2,-9), shader=unlit_shader)
bigtree33 = Entity(model='tree03.fbx', texture='tree03.png', scale=(0.007,0.007,0.007), position=(7,0.2,-11), shader=unlit_shader)
tree43 = Entity(model='bush02.fbx', texture='bush02.png', scale=(0.003,0.003,0.003), position=(10,0.2,-8), shader=unlit_shader)
bigtree34 = Entity(model='tree18.fbx', texture='tree18.png', scale=(0.007,0.007,0.007), position=(9,0.2,-13), shader=unlit_shader)
tree44 = Entity(model='bush04.fbx', texture='bush04.png', scale=(0.003,0.003,0.003), position=(6,0.2,-10), shader=unlit_shader)
bigtree35 = Entity(model='tree19.fbx', texture='tree19.png', scale=(0.007,0.007,0.007), position=(4,0.2,-12), shader=unlit_shader)
tree45 = Entity(model='bush01.fbx', texture='bush01.png', scale=(0.003,0.003,0.003), position=(13,0.2,-7), shader=unlit_shader)
bigtree36 = Entity(model='tree21.fbx', texture='tree21.png', scale=(0.007,0.007,0.007), position=(6,0.2,-8), shader=unlit_shader)
tree46 = Entity(model='bush02.fbx', texture='bush02.png', scale=(0.003,0.003,0.003), position=(11,0.2,-13), shader=unlit_shader)

tree47 = Entity(model='bush04.fbx', texture='bush04.png', scale=(0.003,0.003,0.003), position=(26,0.2,-9), shader=unlit_shader)
bigtree37 = Entity(model='tree03.fbx', texture='tree03.png', scale=(0.007,0.007,0.007), position=(28,0.2,-11), shader=unlit_shader)
tree48 = Entity(model='bush01.fbx', texture='bush01.png', scale=(0.003,0.003,0.003), position=(30,0.2,-8), shader=unlit_shader)
bigtree38 = Entity(model='tree18.fbx', texture='tree18.png', scale=(0.007,0.007,0.007), position=(32,0.2,-13), shader=unlit_shader)
tree49 = Entity(model='bush02.fbx', texture='bush02.png', scale=(0.003,0.003,0.003), position=(35,0.2,-10), shader=unlit_shader)
bigtree39 = Entity(model='tree19.fbx', texture='tree19.png', scale=(0.007,0.007,0.007), position=(38,0.2,-12), shader=unlit_shader)
tree50 = Entity(model='bush04.fbx', texture='bush04.png', scale=(0.003,0.003,0.003), position=(40,0.2,-7), shader=unlit_shader)
bigtree40 = Entity(model='tree21.fbx', texture='tree21.png', scale=(0.007,0.007,0.007), position=(42,0.2,-8), shader=unlit_shader)
tree51 = Entity(model='bush01.fbx', texture='bush01.png', scale=(0.003,0.003,0.003), position=(45,0.2,-13), shader=unlit_shader)

tree52 = Entity(model='bush02.fbx', texture='bush02.png', scale=(0.003,0.003,0.003), position=(56,0.2,-9), shader=unlit_shader)
bigtree41 = Entity(model='tree03.fbx', texture='tree03.png', scale=(0.007,0.007,0.007), position=(58,0.2,-11), shader=unlit_shader)
tree53 = Entity(model='bush04.fbx', texture='bush04.png', scale=(0.003,0.003,0.003), position=(60,0.2,-8), shader=unlit_shader)
bigtree42 = Entity(model='tree18.fbx', texture='tree18.png', scale=(0.007,0.007,0.007), position=(62,0.2,-13), shader=unlit_shader)
tree54 = Entity(model='bush01.fbx', texture='bush01.png', scale=(0.003,0.003,0.003), position=(65,0.2,-10), shader=unlit_shader)
bigtree43 = Entity(model='tree19.fbx', texture='tree19.png', scale=(0.007,0.007,0.007), position=(68,0.2,-12), shader=unlit_shader)
tree55 = Entity(model='bush02.fbx', texture='bush02.png', scale=(0.003,0.003,0.003), position=(70,0.2,-7), shader=unlit_shader)
bigtree44 = Entity(model='tree21.fbx', texture='tree21.png', scale=(0.007,0.007,0.007), position=(72,0.2,-8), shader=unlit_shader)
tree56 = Entity(model='bush04.fbx', texture='bush04.png', scale=(0.003,0.003,0.003), position=(75,0.2,-13), shader=unlit_shader)

tree57 = Entity(model='bush01.fbx', texture='bush01.png', scale=(0.003,0.003,0.003), position=(86,0.2,-9), shader=unlit_shader)
bigtree45 = Entity(model='tree03.fbx', texture='tree03.png', scale=(0.007,0.007,0.007), position=(88,0.2,-11), shader=unlit_shader)
tree58 = Entity(model='bush02.fbx', texture='bush02.png', scale=(0.003,0.003,0.003), position=(90,0.2,-8), shader=unlit_shader)
bigtree46 = Entity(model='tree18.fbx', texture='tree18.png', scale=(0.007,0.007,0.007), position=(92,0.2,-13), shader=unlit_shader)
tree59 = Entity(model='bush04.fbx', texture='bush04.png', scale=(0.003,0.003,0.003), position=(95,0.2,-10), shader=unlit_shader)
bigtree47 = Entity(model='tree19.fbx', texture='tree19.png', scale=(0.007,0.007,0.007), position=(98,0.2,-12), shader=unlit_shader)
tree60 = Entity(model='bush01.fbx', texture='bush01.png', scale=(0.003,0.003,0.003), position=(100,0.2,-7), shader=unlit_shader)
bigtree48 = Entity(model='tree21.fbx', texture='tree21.png', scale=(0.007,0.007,0.007), position=(102,0.2,-8), shader=unlit_shader)
tree61 = Entity(model='bush02.fbx', texture='bush02.png', scale=(0.003,0.003,0.003), position=(105,0.2,-13), shader=unlit_shader)

tree62 = Entity(model='bush04.fbx', texture='bush04.png', scale=(0.003,0.003,0.003), position=(14,0.2,-10), shader=unlit_shader)
bigtree49 = Entity(model='tree03.fbx', texture='tree03.png', scale=(0.007,0.007,0.007), position=(12,0.2,-12), shader=unlit_shader)
tree63 = Entity(model='bush01.fbx', texture='bush01.png', scale=(0.003,0.003,0.003), position=(16,0.2,-11), shader=unlit_shader)
bigtree50 = Entity(model='tree18.fbx', texture='tree18.png', scale=(0.007,0.007,0.007), position=(15,0.2,-9), shader=unlit_shader)

bigtree16 = Entity(model='tree21.fbx', texture='tree21.png', scale=(0.007,0.007,0.007), position=(90,0.2,9), shader=unlit_shader)
tree19 = Entity(model='bush01.fbx', texture='bush01.png', scale=(0.003,0.003,0.003), position=(95,0.2,11), shader=unlit_shader)
bigtree17 = Entity(model='tree03.fbx', texture='tree03.png', scale=(0.007,0.007,0.007), position=(89,0.2,14), shader=unlit_shader)
tree20 = Entity(model='bush02.fbx', texture='bush02.png', scale=(0.003,0.003,0.003), position=(100,0.2,8), shader=unlit_shader)
bigtree18 = Entity(model='tree18.fbx', texture='tree18.png', scale=(0.007,0.007,0.007), position=(92,0.2,12), shader=unlit_shader)
tree21 = Entity(model='bush04.fbx', texture='bush04.png', scale=(0.003,0.003,0.003), position=(98,0.2,10), shader=unlit_shader)
bigtree19 = Entity(model='tree19.fbx', texture='tree19.png', scale=(0.007,0.007,0.007), position=(94,0.2,15), shader=unlit_shader)
tree22 = Entity(model='bush01.fbx', texture='bush01.png', scale=(0.003,0.003,0.003), position=(102,0.2,7), shader=unlit_shader)
bigtree20 = Entity(model='tree21.fbx', texture='tree21.png', scale=(0.007,0.007,0.007), position=(100,0.2,13), shader=unlit_shader)
tree23 = Entity(model='bush02.fbx', texture='bush02.png', scale=(0.003,0.003,0.003), position=(88,0.2,10), shader=unlit_shader)
tree24 = Entity(model='bush04.fbx', texture='bush04.png', scale=(0.003,0.003,0.003), position=(92,0.2,12), shader=unlit_shader)

tree64 = Entity(model='bush02.fbx', texture='bush02.png', scale=(0.003,0.003,0.003), position=(9,0.2,-10), shader=unlit_shader)
tree65 = Entity(model='bush04.fbx', texture='bush04.png', scale=(0.003,0.003,0.003), position=(11,0.2,-12), shader=unlit_shader)
bigtree51 = Entity(model='tree19.fbx', texture='tree19.png', scale=(0.007,0.007,0.007), position=(13,0.2,-8), shader=unlit_shader)
bigtree52 = Entity(model='tree21.fbx', texture='tree21.png', scale=(0.007,0.007,0.007), position=(15,0.2,-13), shader=unlit_shader)
tree66 = Entity(model='bush01.fbx', texture='bush01.png', scale=(0.003,0.003,0.003), position=(17,0.2,-9), shader=unlit_shader)

tree67 = Entity(model='bush02.fbx', texture='bush02.png', scale=(0.003,0.003,0.003), position=(27,0.2,-10), shader=unlit_shader)
tree68 = Entity(model='bush04.fbx', texture='bush04.png', scale=(0.003,0.003,0.003), position=(29,0.2,-12), shader=unlit_shader)
bigtree53 = Entity(model='tree03.fbx', texture='tree03.png', scale=(0.007,0.007,0.007), position=(31,0.2,-8), shader=unlit_shader)
tree69 = Entity(model='bush01.fbx', texture='bush01.png', scale=(0.003,0.003,0.003), position=(33,0.2,-13), shader=unlit_shader)
bigtree54 = Entity(model='tree18.fbx', texture='tree18.png', scale=(0.007,0.007,0.007), position=(35,0.2,-9), shader=unlit_shader)
tree70 = Entity(model='bush02.fbx', texture='bush02.png', scale=(0.003,0.003,0.003), position=(37,0.2,-11), shader=unlit_shader)
tree71 = Entity(model='bush04.fbx', texture='bush04.png', scale=(0.003,0.003,0.003), position=(39,0.2,-7), shader=unlit_shader)
bigtree55 = Entity(model='tree19.fbx', texture='tree19.png', scale=(0.007,0.007,0.007), position=(41,0.2,-10), shader=unlit_shader)
tree72 = Entity(model='bush01.fbx', texture='bush01.png', scale=(0.003,0.003,0.003), position=(43,0.2,-12), shader=unlit_shader)
bigtree56 = Entity(model='tree21.fbx', texture='tree21.png', scale=(0.007,0.007,0.007), position=(45,0.2,-8), shader=unlit_shader)

tree73 = Entity(model='bush02.fbx', texture='bush02.png', scale=(0.003,0.003,0.003), position=(57,0.2,-10), shader=unlit_shader)
tree74 = Entity(model='bush04.fbx', texture='bush04.png', scale=(0.003,0.003,0.003), position=(59,0.2,-12), shader=unlit_shader)
bigtree57 = Entity(model='tree03.fbx', texture='tree03.png', scale=(0.007,0.007,0.007), position=(61,0.2,-8), shader=unlit_shader)
tree75 = Entity(model='bush01.fbx', texture='bush01.png', scale=(0.003,0.003,0.003), position=(63,0.2,-13), shader=unlit_shader)
tree76 = Entity(model='bush02.fbx', texture='bush02.png', scale=(0.003,0.003,0.003), position=(65,0.2,-9), shader=unlit_shader)
bigtree58 = Entity(model='tree18.fbx', texture='tree18.png', scale=(0.007,0.007,0.007), position=(67,0.2,-11), shader=unlit_shader)
tree77 = Entity(model='bush04.fbx', texture='bush04.png', scale=(0.003,0.003,0.003), position=(69,0.2,-7), shader=unlit_shader)
tree78 = Entity(model='bush01.fbx', texture='bush01.png', scale=(0.003,0.003,0.003), position=(71,0.2,-10), shader=unlit_shader)
bigtree59 = Entity(model='tree19.fbx', texture='tree19.png', scale=(0.007,0.007,0.007), position=(73,0.2,-12), shader=unlit_shader)
tree79 = Entity(model='bush02.fbx', texture='bush02.png', scale=(0.003,0.003,0.003), position=(75,0.2,-8), shader=unlit_shader)

tree80 = Entity(model='bush04.fbx', texture='bush04.png', scale=(0.003,0.003,0.003), position=(87,0.2,-10), shader=unlit_shader)
tree81 = Entity(model='bush01.fbx', texture='bush01.png', scale=(0.003,0.003,0.003), position=(89,0.2,-12), shader=unlit_shader)
bigtree60 = Entity(model='tree21.fbx', texture='tree21.png', scale=(0.007,0.007,0.007), position=(91,0.2,-8), shader=unlit_shader)
tree82 = Entity(model='bush02.fbx', texture='bush02.png', scale=(0.003,0.003,0.003), position=(93,0.2,-13), shader=unlit_shader)
tree83 = Entity(model='bush04.fbx', texture='bush04.png', scale=(0.003,0.003,0.003), position=(95,0.2,-9), shader=unlit_shader)
bigtree61 = Entity(model='tree03.fbx', texture='tree03.png', scale=(0.007,0.007,0.007), position=(97,0.2,-11), shader=unlit_shader)
tree84 = Entity(model='bush01.fbx', texture='bush01.png', scale=(0.003,0.003,0.003), position=(99,0.2,-7), shader=unlit_shader)
tree85 = Entity(model='bush02.fbx', texture='bush02.png', scale=(0.003,0.003,0.003), position=(101,0.2,-10), shader=unlit_shader)
bigtree62 = Entity(model='tree18.fbx', texture='tree18.png', scale=(0.007,0.007,0.007), position=(103,0.2,-12), shader=unlit_shader)
tree86 = Entity(model='bush04.fbx', texture='bush04.png', scale=(0.003,0.003,0.003), position=(105,0.2,-8), shader=unlit_shader)

tree87 = Entity(model='bush01.fbx', texture='bush01.png', scale=(0.003,0.003,0.003), position=(10,0.2,-11), shader=unlit_shader)
tree88 = Entity(model='bush02.fbx', texture='bush02.png', scale=(0.003,0.003,0.003), position=(12,0.2,-7), shader=unlit_shader)
bigtree63 = Entity(model='tree19.fbx', texture='tree19.png', scale=(0.007,0.007,0.007), position=(14,0.2,-12), shader=unlit_shader)
tree89 = Entity(model='bush04.fbx', texture='bush04.png', scale=(0.003,0.003,0.003), position=(16,0.2,-8), shader=unlit_shader)

tree90 = Entity(model='bush01.fbx', texture='bush01.png', scale=(0.003,0.003,0.003), position=(28,0.2,-11), shader=unlit_shader)
bigtree64 = Entity(model='tree21.fbx', texture='tree21.png', scale=(0.007,0.007,0.007), position=(30,0.2,-7), shader=unlit_shader)
tree91 = Entity(model='bush02.fbx', texture='bush02.png', scale=(0.003,0.003,0.003), position=(32,0.2,-12), shader=unlit_shader)
tree92 = Entity(model='bush04.fbx', texture='bush04.png', scale=(0.003,0.003,0.003), position=(34,0.2,-8), shader=unlit_shader)

tree93 = Entity(model='bush01.fbx', texture='bush01.png', scale=(0.003,0.003,0.003), position=(58,0.2,-11), shader=unlit_shader)
bigtree65 = Entity(model='tree03.fbx', texture='tree03.png', scale=(0.007,0.007,0.007), position=(60,0.2,-7), shader=unlit_shader)
tree94 = Entity(model='bush02.fbx', texture='bush02.png', scale=(0.003,0.003,0.003), position=(62,0.2,-12), shader=unlit_shader)
tree95 = Entity(model='bush04.fbx', texture='bush04.png', scale=(0.003,0.003,0.003), position=(64,0.2,-8), shader=unlit_shader)
tree96 = Entity(model='bush01.fbx', texture='bush01.png', scale=(0.003,0.003,0.003), position=(88,0.2,-11), shader=unlit_shader)
tree97 = Entity(model='bush02.fbx', texture='bush02.png', scale=(0.003,0.003,0.003), position=(92,0.2,-12), shader=unlit_shader)
tree98 = Entity(model='bush04.fbx', texture='bush04.png', scale=(0.003,0.003,0.003), position=(94,0.2,-8), shader=unlit_shader)
tree99=Entity(model='bush04.fbx', texture='bush04.png', scale=(0.003,0.003,0.003), position=(0,0.2,-9), shader=unlit_shader)
tree100=Entity(model='bush01.fbx', texture='bush01.png', scale=(0.003,0.003,0.003), position=(-1,0.2,-7), shader=unlit_shader)
tree101=Entity(model='bush01.fbx', texture='bush01.png', scale=(0.003,0.003,0.003), position=(-2,0.2,-10), shader=unlit_shader)
tree102=Entity(model='bush04.fbx', texture='bush04.png', scale=(0.003,0.003,0.003), position=(-3,0.2,-9), shader=unlit_shader)
tree103=Entity(model='bush02.fbx', texture='bush02.png', scale=(0.003,0.003,0.003), position=(-5,0.2,-8), shader=unlit_shader)
tree104=Entity(model='bush04.fbx', texture='bush04.png', scale=(0.003,0.003,0.003), position=(3,0.2,-10), shader=unlit_shader)
tree105=Entity(model='bush02.fbx', texture='bush02.png', scale=(0.003,0.003,0.003), position=(1,0.2,-8), shader=unlit_shader)
bigtree66 = Entity(model='tree18.fbx', texture='tree18.png', scale=(0.007,0.007,0.007), position=(90,0.2,-7), shader=unlit_shader)
bigtree67=Entity(model='tree18.fbx', texture='tree18.png', scale=(0.007,0.007,0.007), position=(2,0.2,-8), shader=unlit_shader)
bigtree68=Entity(model='tree19.fbx', texture='tree19.png', scale=(0.007,0.007,0.007), position=(1,0.2,-9), shader=unlit_shader)
bigtree69=Entity(model='tree21.fbx', texture='tree21.png', scale=(0.007,0.007,0.007), position=(-2,0.2,-7), shader=unlit_shader)
bigtree70=Entity(model='tree03.fbx', texture='tree03.png', scale=(0.007,0.007,0.007), position=(-4,0.2,-10), shader=unlit_shader)

tree106=Entity(model='bush04.fbx', texture='bush04.png', scale=(0.003,0.003,0.003), position=(0,0.2,9), shader=unlit_shader)
tree107=Entity(model='bush01.fbx', texture='bush01.png', scale=(0.003,0.003,0.003), position=(-1,0.2,7), shader=unlit_shader)
tree108=Entity(model='bush01.fbx', texture='bush01.png', scale=(0.003,0.003,0.003), position=(-2,0.2,10), shader=unlit_shader)
tree109=Entity(model='bush04.fbx', texture='bush04.png', scale=(0.003,0.003,0.003), position=(-3,0.2,9), shader=unlit_shader)
tree110=Entity(model='bush02.fbx', texture='bush02.png', scale=(0.003,0.003,0.003), position=(-5,0.2,8), shader=unlit_shader)
tree111=Entity(model='bush04.fbx', texture='bush04.png', scale=(0.003,0.003,0.003), position=(3,0.2,10), shader=unlit_shader)
tree112=Entity(model='bush02.fbx', texture='bush02.png', scale=(0.003,0.003,0.003), position=(1,0.2,8), shader=unlit_shader)
bigtree71 = Entity(model='tree18.fbx', texture='tree18.png', scale=(0.007,0.007,0.007), position=(90,0.2,7), shader=unlit_shader)
bigtree72=Entity(model='tree18.fbx', texture='tree18.png', scale=(0.007,0.007,0.007), position=(2,0.2,8), shader=unlit_shader)
bigtree73=Entity(model='tree19.fbx', texture='tree19.png', scale=(0.007,0.007,0.007), position=(1,0.2,9), shader=unlit_shader)
bigtree74=Entity(model='tree21.fbx', texture='tree21.png', scale=(0.007,0.007,0.007), position=(-2,0.2,7), shader=unlit_shader)
bigtree75=Entity(model='tree03.fbx', texture='tree03.png', scale=(0.007,0.007,0.007), position=(-4,0.2,10), shader=unlit_shader)




back1=Entity(model='bush04.fbx', texture='bush04.png', scale=(0.1,0.031,0.030), position=(60,-0.4,30))
back2=Entity(model='bush04.fbx', texture='bush04.png', scale=(0.1,0.031,0.030), position=(0,-0.4,30))
back3=Entity(model='bush04.fbx', texture='bush04.png', scale=(0.1,0.031,0.030), position=(60,-0.4,-30))
back4=Entity(model='bush04.fbx', texture='bush04.png', scale=(0.1,0.031,0.030), position=(0,-0.4,-30))
back5=Entity(model='bush04.fbx', texture='bush04.png', scale=(0.1,0.031,0.030), position=(80,0,30))
back6=Entity(model='bush04.fbx', texture='bush04.png', scale=(0.1,0.031,0.030), position=(90,0,-30))
houseOWN=Entity(model='house2.glb',scale=1.3,position=(-6,0.6,0),collider='box')
window=Entity(model='cube',color=color.gray,collider='box',position=(-6.5,3,-3),scale=(1,3,2),shader=basic_lighting_shader)
zabor1=Entity(model='zabor2.glb', scale=(0.01,0.03,0.08), position=(-15,1,0.7),shader=basic_lighting_shader)
zabor2=Entity(model='zabor2.glb', scale=(0.01,0.03,0.08), position=(-15,1,-55),shader=basic_lighting_shader)
zabor3=Entity(model='zabor2.glb', scale=(0.01,0.05,0.08), position=(140,1,0),rotation=(0,180,0),shader=basic_lighting_shader)
zabor4=Entity(model='zabor2.glb', scale=(0.01,0.05,0.08), position=(140,1,55),rotation=(0,180,0),shader=basic_lighting_shader)
zabor5=Entity(model='zabor3.glb', scale=1, position=(116,0.5,10),rotation=(0,0,0),shader=basic_lighting_shader)
zabor6=Entity(model='zabor2.glb', scale=(0.01,0.05,0.08), position=(100,1,-5),rotation=(0,-270,0),shader=basic_lighting_shader)
zabor7=Entity(model='zabor2.glb', scale=(0.01,0.05,0.08), position=(100,1,50),rotation=(0,90,0),shader=basic_lighting_shader)
zabor8=Entity(model='zabor4.glb', scale=1.3, position=(120,0,30),rotation=(0,-30,0),shader=basic_lighting_shader)
questhouse=Entity(model='questhouse.glb',scale=1.5,position=(130,1.5,0),rotation=(0,180,0),shader=basic_lighting_shader)
collider_questhouse1=Entity(model='cube',position=(124,-1,2.5),scale=(2.5,100,2.5),rotation=(0,0,55),color=color.clear,collider='box')
collider_questhouse2=Entity(model='cube',position=(129,1,2.5),scale=(2,20,20),rotation=(0,0,0),color=color.clear,collider='box')
collider_door1=Entity(model='cube',position=(129,4,2.5),scale=(1,4,4),rotation=(0,0,0),color=color.clear,collider='box')
questhouseinside=Entity(model='questhouse_inside.glb',scale=0.06,position=(10,10,10),shader=basic_lighting_shader)
questhouseinside_collider1=Entity(model='cube',scale=(20,1,20),position=(10,9.5,10),color=color.clear,collider='box')
questhouseinside_collider2=Entity(model='cube',scale=(10,8,0.8),position=(10.34,10,10.1),color=color.clear,collider='box')
questhouseinside_collider3=Entity(model='cube',scale=(15,8,0.8),position=(16.04,10,10.11),rotation=(0,90,0),color=color.clear,collider='box')
questhouseinside_collider4=Entity(model='cube',scale=(2,2.1,1.7),position=(14.64,10,11.29),rotation=(0,90,0),color=color.clear,collider='box')
questhouseinside_collider5=Entity(model='cube',scale=(10,3,0.8),position=(16.04,10,10.11),rotation=(0,90,0),color=color.clear,collider='box')
questhouseinside_collider6=Entity(model='cube',scale=(20,8,0.8),position=(15.98,10,16.97),color=color.clear,collider='box')
questhouseinside_collider7=Entity(model='cube',scale=(20,8,0.9),position=(10.35,10,16.84),rotation=(0,270,0),color=color.clear,collider='box')
questhouseinside_collider8=Entity(model='cube',scale=(2.5,2.1,1.5),position=(12.48,10,14.38),color=color.clear,collider='box')
questhouseinside_collider9=Entity(model='cube',scale=(1.4,8,1.4),position=(11.02,10,13.64),rotation=(0,90,0),color=color.clear,collider='box')
questhouseinside_collider10=Entity(model='cube',scale=(1,8,1),position=(10,10,14.64),rotation=(0,90,0),color=color.black,collider='box')
collider_door2=Entity(model='cube',scale=(0.5,6,2),position=(7,11,11.4),color=color.clear,collider='box')
questhouseinside.enabled=False
questhouseinside_collider1.enabled=False
questhouseinside_collider2.enabled=False
questhouseinside_collider3.enabled=False
questhouseinside_collider4.enabled=False
questhouseinside_collider5.enabled=False
questhouseinside_collider6.enabled=False
questhouseinside_collider7.enabled=False
questhouseinside_collider8.enabled=False
questhouseinside_collider9.enabled=False
questhouseinside_collider10.enabled=False
bossa.enabled=False



# print("=== Дочерние узлы модели ===")
# for child in questhouseinside.model.get_children():
#     print(child)
houseOWN.shader=basic_lighting_shader
ground.shader = lit_with_shadows_shader
humana.shader=lit_with_shadows_shader
head.shader=lit_with_shadows_shader
body.shader=lit_with_shadows_shader
right.shader=lit_with_shadows_shader
house1.shader=lit_with_shadows_shader
human2.shader=basic_lighting_shader

moon = Entity(
    model='sphere',
    color=color.rgb(180, 180, 255),
    scale=10,
    position=(50, 100, 100),
    double_sided=True
)


door_text = Text(
    text='>> ВОЙТИ? <<',
    position=(0, 0.3),
    origin=(0, 0),
    scale=1.8,
    color=color.azure,
    background=True,
    background_color=color.rgba(0, 0, 0, 200),
    background_padding=(0.3, 0.2),
    border_color=color.cyan,
    border_width=2,
    enabled=False
)
door_text2 = Text(
    text='>> ВОЙТИ? <<',
    position=(0, 0.3),
    origin=(0, 0),
    scale=1.8,
    color=color.azure,
    background=True,
    background_color=color.rgba(0, 0, 0, 200),
    background_padding=(0.3, 0.2),
    border_color=color.cyan,
    border_width=2,
    enabled=False
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
character_portrait = Entity(parent=camera.ui, model='quad', texture='person1.png', scale=(0.8, 1.2),
                            x=-0.6, y=-0.2, z=0.1, enabled=False)
main_character_portrait = Entity(parent=camera.ui, model='quad', texture='MainPerson.png', scale=(0.8, 1.2), x=0.6,
                                 y=-0.3, z=0.1,
                                 enabled=False)
# Фон диалога
dialogue_bg = Entity(parent=camera.ui, model='quad', scale=(2, 1.1), y=-0.6, z=0,
                     color=color.rgba(0, 0, 0, 180))
dialogue_bg.enabled = False
# Имя NPC сверху слева

npc_name = Text("Человек", parent=camera.ui, x=-0.7, y=-0.15,
                origin=(-0.5, 0), scale=(2, 2), color=color.white, bold=True, font='4205.otf')
npc_name.enabled = False

# Основной текст диалога -
npc_line = Text(" ", parent=dialogue_bg, x=-0.4, y=0.35,
                origin=(-0.5, 0), scale=1.2, color=color.white, font='4205.otf')
npc_line.enabled = False
# Устанавливаем wordwrap после создания с текстом
npc_line.wordwrap = 30

# Кнопки боя
weak_attack_btn = Button(text='Слабая атака', color=color.dark_gray, scale=(0.25, 0.08),
                        position=(-0.3, -0.45), enabled=False, font='4205.otf')
weak_attack_btn.text_entity.font = '4205.otf'
strong_attack_btn = Button(text='Сильная атака', color=color.dark_gray, scale=(0.25, 0.08),
                          position=(0, -0.45), enabled=False, font='4205.otf')
strong_attack_btn.text_entity.font = '4205.otf'
surrender_btn = Button(text='Сдаться', color=color.red, scale=(0.25, 0.08),
                      position=(0.3, -0.45), enabled=False, font='4205.otf')
surrender_btn.text_entity.font = '4205.otf'

weak_attack_btn.enabled = False
strong_attack_btn.enabled = False
surrender_btn.enabled = False
weak_attack_btn.render_queue = 1
strong_attack_btn.render_queue = 1
surrender_btn.render_queue = 1

weak_attack_btn.z = -0.1
strong_attack_btn.z = -0.1
surrender_btn.z = -0.1
button1 = Button(text='Поговорить', color=color.green, scale=(0.2, 0.08),
                 position=(-0.3, -0.45), enabled=False, font='4205.otf')
button1.text_entity.font = '4205.otf'
button2 = Button(text='Напасть', color=color.red, scale=(0.2, 0.08),
                 position=(0, -0.45), enabled=False, font='4205.otf')
button2.text_entity.font = '4205.otf'
button3 = Button(text='Уйти', color=color.gray, scale=(0.2, 0.08),
                 position=(0.3, -0.45), enabled=False, font='4205.otf')
button3.text_entity.font = '4205.otf'
button1.enabled = False
button2.enabled = False
button3.enabled = False


talk_button = Button(text='Поболтать', color=color.green, scale=(0.2, 0.08),
                     position=(-0.15, -0.45), enabled=False, font='4205.otf')
talk_button.text_entity.font = '4205.otf'
dont_care_button = Button(text='Неважно', color=color.gray, scale=(0.2, 0.08),
                          position=(0.15, -0.45), enabled=False, font='4205.otf')
dont_care_button.text_entity.font = '4205.otf'
talk_button.enabled = False
dont_care_button.enabled = False

in_dialogue = False
current_text = ""
text_progress = 0
full_text = ""
text_speed = 10
dialogue_stage = 1
active_speaker = "npc"
dark_overlay = Entity(parent=camera.ui, model='quad', scale=(2, 2), color=color.black, alpha=0, enabled=False)
main_character_portrait.render_queue = 0
character_portrait.render_queue = 0
dialogue_bg.render_queue = 1
npc_name.render_queue = 2
npc_line.render_queue = 2
npc_name.z = -0.1
npc_line.z = -0.1
minigame_active = False
minigame_ui = None
zones = []
pointer = None
rotation_speed = 480  # градусов в секунду
hits = 0
attempts = 4

last_x_press_time = 0
x_cooldown = 0.2
enemy_portrait = None
player_battle_portrait = None
battle_background=None
enemy_hp_text = None
enemy_decorate=None
enemy_hp = 150
talk_button.render_queue = 2
dont_care_button.render_queue = 2
talk_button.z = -0.1
dont_care_button.z = -0.1
hit_text = None


class PygameSoundManager:
    def __init__(self):
        pygame.mixer.init()
        self.battle_active = False
        self.background_active = False
        self.bossa_active = False
        self.battle_sound_thread = None
        self.background_sound_thread = None
        self.bossa_sound_thread = None

        # Создаем отдельные каналы для разных звуков
        self.battle_channel = pygame.mixer.Channel(0)
        self.background_channel = pygame.mixer.Channel(1)
        self.bossa_channel = pygame.mixer.Channel(2)

        self.battle_sound = None
        self.background_sound = None
        self.bossa_sound = None

        # Текущие громкости
        self.battle_volume = 0.5
        self.background_volume = 0.7
        self.bossa_volume = 0.6

    def play_background_sound(self):
        """Запускает фоновый звук BG.ogg"""
        self.stop_background_sound()
        self.background_active = True

        def background_loop():
            try:
                self.background_sound = pygame.mixer.Sound('BG.ogg')
                self.background_channel.set_volume(self.background_volume)
                while self.background_active:
                    if not self.background_channel.get_busy():
                        self.background_channel.play(self.background_sound)
                    time.sleep(0.5)
            except Exception as e:
                print(f"Background sound error: {e}")

        self.background_sound_thread = threading.Thread(target=background_loop, daemon=True)
        self.background_sound_thread.start()
        print(f"🎵 Pygame background sound started (volume: {self.background_volume})")

    def play_battle_sound(self):
        """Запускает боевой звук battlesound.ogg"""
        self.stop_battle_sound()
        self.battle_active = True

        def battle_loop():
            try:
                self.battle_sound = pygame.mixer.Sound('battlesound.ogg')
                self.battle_channel.set_volume(self.battle_volume)
                while self.battle_active:
                    if not self.battle_channel.get_busy():
                        self.battle_channel.play(self.battle_sound)
                    time.sleep(0.5)
            except Exception as e:
                print(f"Battle sound error: {e}")

        self.battle_sound_thread = threading.Thread(target=battle_loop, daemon=True)
        self.battle_sound_thread.start()
        print(f"⚔️ Pygame battle sound started (volume: {self.battle_volume})")

    def play_bossa_sound(self):
        """Запускает босса-нову звук bossa_sound.mp3"""
        self.stop_bossa_sound()
        self.bossa_active = True

        def bossa_loop():
            try:
                self.bossa_sound = pygame.mixer.Sound('bossa_sound.mp3')
                self.bossa_channel.set_volume(self.bossa_volume)
                while self.bossa_active:
                    if not self.bossa_channel.get_busy():
                        self.bossa_channel.play(self.bossa_sound)
                    time.sleep(0.5)
            except Exception as e:
                print(f"Bossa sound error: {e}")

        self.bossa_sound_thread = threading.Thread(target=bossa_loop, daemon=True)
        self.bossa_sound_thread.start()
        print(f"🎷 Pygame bossa sound started (volume: {self.bossa_volume})")

    # Методы для управления громкостью фоновой музыки
    def set_background_volume(self, volume):
        """Устанавливает громкость фоновой музыки (0.0 - 1.0)"""
        if 0.0 <= volume <= 1.0:
            self.background_volume = volume
            self.background_channel.set_volume(volume)
            print(f"🔊 Background volume set to: {volume}")
        else:
            print("❌ Volume must be between 0.0 and 1.0")

    def get_background_volume(self):
        """Возвращает текущую громкость фоновой музыки"""
        return self.background_volume

    # Методы для управления громкостью боевого звука
    def set_battle_volume(self, volume):
        """Устанавливает громкость боевого звука (0.0 - 1.0)"""
        if 0.0 <= volume <= 1.0:
            self.battle_volume = volume
            self.battle_channel.set_volume(volume)
            print(f"🔊 Battle volume set to: {volume}")
        else:
            print("❌ Volume must be between 0.0 and 1.0")

    def get_battle_volume(self):
        """Возвращает текущую громкость боевого звука"""
        return self.battle_volume

    # Методы для управления громкостью босса-новы
    def set_bossa_volume(self, volume):
        """Устанавливает громкость босса-новы (0.0 - 1.0)"""
        if 0.0 <= volume <= 1.0:
            self.bossa_volume = volume
            self.bossa_channel.set_volume(volume)
            print(f"🔊 Bossa volume set to: {volume}")
        else:
            print("❌ Volume must be between 0.0 and 1.0")

    def get_bossa_volume(self):
        """Возвращает текущую громкость босса-новы"""
        return self.bossa_volume

    # Методы остановки
    def stop_background_sound(self):
        """Останавливает фоновый звук"""
        self.background_active = False
        self.background_channel.stop()
        print("🔇 Pygame background sound stopped")

    def stop_battle_sound(self):
        """Останавливает боевой звук"""
        self.battle_active = False
        self.battle_channel.stop()
        print("🔇 Pygame battle sound stopped")

    def stop_bossa_sound(self):
        """Останавливает босса-нову звук"""
        self.bossa_active = False
        self.bossa_channel.stop()
        print("🔇 Pygame bossa sound stopped")

    def stop_all_sounds(self):
        """Останавливает все звуки"""
        self.stop_background_sound()
        self.stop_battle_sound()
        self.stop_bossa_sound()
        print("🔇 All pygame sounds stopped")

    # Пресеты громкости для удобства
    def set_volume_preset(self, preset_name):
        """Устанавливает громкость по пресету для всех звуков"""
        presets = {
            'normal': {'background': 0.5, 'battle': 0.7, 'bossa': 0.6},
            'quiet': {'background': 0.3, 'battle': 0.4, 'bossa': 0.3},
            'loud': {'background': 0.8, 'battle': 0.9, 'bossa': 0.8},
            'menu': {'background': 0.2, 'battle': 0.0, 'bossa': 0.4},
            'battle_focus': {'background': 0.3, 'battle': 0.8, 'bossa': 0.0},
            'exploration': {'background': 0.6, 'battle': 0.0, 'bossa': 0.5},
            'bossa_only': {'background': 0.0, 'battle': 0.0, 'bossa': 0.7},
            'relaxed': {'background': 0.4, 'battle': 0.0, 'bossa': 0.6}
        }

        if preset_name in presets:
            bg_vol = presets[preset_name]['background']
            battle_vol = presets[preset_name]['battle']
            bossa_vol = presets[preset_name]['bossa']

            self.set_background_volume(bg_vol)
            self.set_battle_volume(battle_vol)
            self.set_bossa_volume(bossa_vol)
            print(f"🔊 Preset '{preset_name}' applied")

    # Дополнительные методы для удобства
    def play_sound_by_name(self, sound_name):
        """Запускает звук по имени"""
        if sound_name == 'background':
            self.play_background_sound()
        elif sound_name == 'battle':
            self.play_battle_sound()
        elif sound_name == 'bossa':
            self.play_bossa_sound()
        else:
            print(f"❌ Unknown sound: {sound_name}")

    def stop_sound_by_name(self, sound_name):
        """Останавливает звук по имени"""
        if sound_name == 'background':
            self.stop_background_sound()
        elif sound_name == 'battle':
            self.stop_battle_sound()
        elif sound_name == 'bossa':
            self.stop_bossa_sound()
        else:
            print(f"❌ Unknown sound: {sound_name}")

# Используйте этот менеджер вместо Ursina Audio
sound_manager = PygameSoundManager()
sound_manager.play_background_sound()



def start_dialogue(npc_name_text, npc_line_text):
    global in_dialogue, current_text, text_progress, full_text, dialogue_stage,active_speaker
    dialogue_stage = 1  # Сбрасываем на первый этап
    active_speaker = "npc"
    sound_manager.set_background_volume(0.3)

    in_dialogue = True
    press_e_text.enabled = False
    player.enabled = False

    npc_name.text = npc_name_text
    full_text = npc_line_text
    current_text = ""
    text_progress = 0

    dark_overlay.enabled = True
    character_portrait.enabled = True
    main_character_portrait.enabled = True

    dialogue_bg.scale_x = 0.1
    dialogue_bg.scale_y = 0.1
    dialogue_bg.enabled = True
    dialogue_bg.color = color.black66
    character_portrait.enabled = True
    main_character_portrait.enabled = True
    character_portrait.y = -0.3
    main_character_portrait.y = -0.3
    character_portrait.color = color.rgba(255, 255, 255, 0)
    main_character_portrait.color = color.rgba(255, 255, 255, 0)

    npc_name.enabled = False
    npc_line.enabled = False
    npc_line.text = " "


    button1.enabled = False
    button2.enabled = False
    button3.enabled = False
    talk_button.enabled = False
    dont_care_button.enabled = False

    walk.stop()

    def animate_dialogue():
        # Анимация фона
        dialogue_bg.animate_scale((1.6, 1.1, 1), duration=1.3, curve=curve.out_quad)

        dark_overlay.animate_color(color.rgba(0, 0, 0, 0.7), duration=0.8)

        character_portrait.animate_color(color.white, duration=1.5, delay=0.8, curve=curve.in_out_quad)
        main_character_portrait.animate_color(color.white, duration=1.5, delay=0.8, curve=curve.in_out_quad)

        # NPC говорит, игрок ниже
        character_portrait.animate_y(-0.1, duration=1.3, delay=0.3, curve=curve.out_cubic)
        main_character_portrait.animate_y(-0.3, duration=1.3, delay=0.3, curve=curve.out_cubic)

        invoke(setattr, npc_name, 'enabled', True, delay=1.5)

        invoke(setattr, npc_line, 'enabled', True, delay=1.8)
        invoke(lambda: setattr(scene, 'text_printing_active', True), delay=2)
    animate_dialogue()


def start_text_printing():
    global text_progress, current_text
    text_progress = 0
    current_text = ""
    scene.text_printing_active = True


def update_text_printing():
    global text_progress, current_text

    if hasattr(scene, 'text_printing_active') and scene.text_printing_active:
        if text_progress < len(full_text):
            text_progress = min(text_progress + text_speed * time.dt, len(full_text))
            current_text = full_text[:int(text_progress)]
            npc_line.text = current_text

            if not text_sound.playing:
                text_sound.play()
        else:
            scene.text_printing_active = False
            text_sound.stop()

            if battle_active:
                # В режиме боя кнопки не показываем - они появятся через invoke
                pass
            elif dialogue_stage == 1:
                button1.enabled = True
                button2.enabled = True
                button3.enabled = True
            elif dialogue_stage == 2:
                talk_button.enabled = True
                dont_care_button.enabled = True


def setup_conversation_buttons():
    global full_text, current_text, text_progress, dialogue_stage, active_speaker
    dialogue_stage = 2
    active_speaker = "equal"

    button1.enabled = False
    button2.enabled = False
    button3.enabled = False
    talk_button.enabled = False
    dont_care_button.enabled = False


    full_text = "Ну давай поговорим."
    current_text = ""
    text_progress = 0
    npc_line.text = ""


    character_portrait.animate_y(-0.2, duration=0.8, curve=curve.out_cubic)
    main_character_portrait.animate_y(-0.2, duration=0.8, curve=curve.out_cubic)


    scene.text_printing_active = True


def talk_action():

    global full_text, current_text, text_progress, active_speaker

    active_speaker = "player"  # Теперь говорит игрок


    talk_button.enabled = False
    dont_care_button.enabled = False

    #игрок поднимается выше, NPC слегка опускается
    main_character_portrait.animate_y(-0.13, duration=1.0, curve=curve.out_cubic)
    character_portrait.animate_y(-0.25, duration=1.0, curve=curve.out_cubic)  # Легкое опускание


    full_text = "Привет! Как дела? Что нового?"
    current_text = ""
    text_progress = 0


    scene.text_printing_active = True


def dont_care_action():

    global full_text, current_text, text_progress, dialogue_stage, active_speaker

    dialogue_stage = 1
    active_speaker = "npc"  # NPC снова говорит


    talk_button.enabled = False
    dont_care_button.enabled = False

    # NPC выше, игрок ниже
    character_portrait.animate_y(-0.1, duration=0.8, curve=curve.out_cubic)
    main_character_portrait.animate_y(-0.3, duration=0.8, curve=curve.out_cubic)


    full_text = "Привет! Рад тебя видеть. Что скажешь?"
    current_text = ""
    text_progress = 0
    npc_line.text = ""


    button1.enabled = True
    button2.enabled = True
    button3.enabled = True


    scene.text_printing_active = True


def close_dialogue():
    global in_dialogue, dialogue_stage, battle_active
    global enemy_portrait, player_battle_portrait, enemy_hp_text, enemy_hp,battle_background,enemy_decorate

    def finish_close():
        global in_dialogue, battle_active, enemy_hp
        global enemy_portrait, player_battle_portrait, enemy_hp_text,battle_background,enemy_decorate
        sound_manager.stop_battle_sound()
        if battle2_sound.playing:
            battle2_sound.stop()
        if battle_reaction_sound.playing:
            battle_reaction_sound.stop()
        sound_manager.set_background_volume(1)
        dialogue_bg.enabled = False
        npc_name.enabled = False
        npc_line.enabled = False
        player.enabled = True
        dark_overlay.enabled = False
        character_portrait.enabled = False
        main_character_portrait.enabled = False
        enemy_decorate=False
        battle_background=False
        in_dialogue = False
        battle_active = False

        # Скрываем все кнопки
        button1.enabled = False
        button2.enabled = False
        button3.enabled = False
        talk_button.enabled = False
        dont_care_button.enabled = False
        weak_attack_btn.enabled = False
        strong_attack_btn.enabled = False
        surrender_btn.enabled = False

        # Удаляем боевые элементы
        if enemy_portrait:
            destroy(enemy_portrait)
            enemy_portrait = None
        if player_battle_portrait:
            destroy(player_battle_portrait)
            player_battle_portrait = None
        if enemy_hp_text:
            destroy(enemy_hp_text)
            enemy_hp_text = None
        if battle_background:
            destroy(battle_background)
            battle_background = None
        if enemy_decorate:
            destroy(enemy_decorate)
            enemy_decorate=None

        # Сбрасываем HP врага
        enemy_hp = 150

        if hasattr(scene, 'text_printing_active'):
            scene.text_printing_active = False

    def animate_close():
        dialogue_bg.animate_scale((0.1, 0.1, 1), duration=0.9, curve=curve.in_quad)
        dark_overlay.animate_color(color.rgba(0, 0, 0, 0), duration=0.7)
        character_portrait.animate_color(color.rgba(1, 1, 1, 0), duration=0.7)
        main_character_portrait.animate_color(color.rgba(1, 1, 1, 0), duration=0.7)
        if 'battle_background' in globals() and battle_background:
            battle_background.animate_color(color.rgba(1, 1, 1, 0), duration=0.7)
        else:
            print("[DEBUG] battle_background отсутствует (обычный диалог) — пропускаю анимацию закрытия.")

        # 🔹 Проверяем наличие enemy_decorate
        if 'enemy_decorate' in globals() and enemy_decorate:
            enemy_decorate.animate_color(color.rgba(1, 1, 1, 0), duration=0.7)
        else:
            print("[DEBUG] enemy_decorate отсутствует (обычный диалог) — пропускаю анимацию закрытия.")


        npc_name.enabled = False
        npc_line.enabled = False
        button1.enabled = False
        button2.enabled = False
        button3.enabled = False
        talk_button.enabled = False
        dont_care_button.enabled = False

        invoke(finish_close, delay=0.9)

    animate_close()

battle_active = False



def start_battle():
    global battle_active, full_text, current_text, text_progress, enemy_portrait, player_battle_portrait, enemy_hp_text,battle_background,\
        enemy_decorate

    battle_active = True
    sound_manager.stop_background_sound()
    if not battle_reaction_sound.playing:
        battle_reaction_sound.play()
    button1.enabled = False
    button2.enabled = False
    button3.enabled = False

    full_text = "..............................."
    current_text = ""
    text_progress = 0
    npc_line.text = ""

    scene.text_printing_active = True

    # После печати текста запускаем анимацию перехода к бою
    def transition_to_battle():
        if battle_reaction_sound.playing:
            battle_reaction_sound.stop()
        if not battle2_sound.playing:
            battle2_sound.play()
        def animate_close_old():
            dialogue_bg.animate_scale((0.1, 0.1, 1), duration=0.9, curve=curve.in_quad)
            dark_overlay.animate_color(color.rgba(0, 0, 0, 0), duration=0.7)
            character_portrait.animate_color(color.rgba(1, 1, 1, 0), duration=0.7)
            main_character_portrait.animate_color(color.rgba(1, 1, 1, 0), duration=0.7)

            # Скрываем элементы
            npc_name.enabled = False
            npc_line.enabled = False

            invoke(create_battle_interface, delay=0.9)

        animate_close_old()

    invoke(transition_to_battle, delay=3.0)


def create_battle_interface():
    global enemy_portrait, player_battle_portrait, enemy_hp_text,battle_background,enemy_decorate

    # -----------------------------
    # Фон диалога
    # -----------------------------
    dialogue_bg.y = -0.6
    dialogue_bg.color = color.black66
    dialogue_bg.scale = (1.6, 0.8)
    dialogue_bg.enabled = True
    dialogue_bg.animate_scale((1.6, 0.8, 1), duration=1.3, curve=curve.out_quad)
    dark_overlay.animate_color(color.rgba(0, 0, 0, 0.7), duration=0.8)

    # -----------------------------
    # Портрет игрока
    # -----------------------------
    player_battle_portrait = Entity(
        parent=camera.ui,
        model='quad',
        texture='personenemy.png',
        scale=(0.30, 0.30),
        x=-0.61,
        y=-0.38
    )
    player_battle_portrait.color = color.rgba(1, 1, 1, 0)
    player_battle_portrait.animate_color(color.white, duration=1.0, delay=0.5)

    # -----------------------------
    # Портрет врага
    # -----------------------------
    enemy_portrait = Entity(
        parent=camera.ui,
        model='quad',
        texture='enemy1.png',
        scale=(0.3, 0.3),
        x=0.61,
        y=-0.38
    )
    enemy_portrait.color = color.rgba(1, 1, 1, 0)
    enemy_portrait.animate_color(color.white, duration=1.0, delay=0.5)

    # -----------------------------
    # Текст HP врага
    # -----------------------------
    enemy_hp_text = Text(
        parent=camera.ui,
        text="HP: 150",
        position=(0.6, -1),
        scale=1.3,
        color=color.red,
        font='4205.otf'
    )
    enemy_hp_text.enabled = True
    # Анимация подъема текста на нужную позицию
    enemy_hp_text.animate_position((0.3, -0.3), duration=1.0, delay=0.5, curve=curve.out_quad)
    # Враг на фоне
    enemy_decorate = Entity(
        parent=camera.ui,
        model='quad',
        texture='enemy_decorate1.png',
        scale=(0.6, 0.6),
        x=0,
        y=0.1,
        z=0
    )
    enemy_decorate.color = color.rgba(1, 1, 1, 0)
    enemy_decorate.animate_color(color.white, duration=1.0, delay=0.5)
    # Задний фон
    battle_background=Entity(
        parent=camera.ui,
        model='quad',
        texture='battleback1.png',
        scale=(2,1),
        x=0,
        y=0,
        z=1
    )



    # -----------------------------
    # Кнопки боя
    # -----------------------------
    def show_battle_buttons():
        if battle2_sound.playing:
            battle2_sound.stop()
            # ВКЛЮЧАЕМ ГЛОБАЛЬНЫЙ ЗВУК БИТВЫ
        sound_manager.play_battle_sound()
        weak_attack_btn.enabled = True
        strong_attack_btn.enabled = True
        surrender_btn.enabled = True

        weak_attack_btn.x = -0.25
        strong_attack_btn.x = -0.25
        surrender_btn.x = -0.25

        weak_attack_btn.y = -0.25
        strong_attack_btn.y = -0.35
        surrender_btn.y = -0.45

    invoke(show_battle_buttons, delay=1.0)


def weak_attack_action():
    """Слабая атака - запускаем мини-игру с прямоугольником"""
    global battle_active

    weak_attack_btn.enabled = False
    strong_attack_btn.enabled = False
    surrender_btn.enabled = False

    def animate_dialogue_down():
        dialogue_bg.animate_y(-1.0, duration=0.8, curve=curve.in_quad)

        if player_battle_portrait:
            player_battle_portrait.animate_y(-1.0, duration=0.8, curve=curve.in_quad)

        if enemy_portrait:
            enemy_portrait.animate_y(-1.0, duration=0.8, curve=curve.in_quad)

        if enemy_hp_text:
            enemy_hp_text.animate_position((0.6, -1.5), duration=0.8, curve=curve.in_quad)

        invoke(start_weak_attack_minigame, delay=0.9)

    animate_dialogue_down()
    print("⚔️ Слабая атака!")

def strong_attack_action():
    #Сильная атака - запускаем мини-игру с анимацией
    global battle_active, dialogue_bg, player_battle_portrait, enemy_portrait, enemy_hp_text,battle_background

    weak_attack_btn.enabled = False
    strong_attack_btn.enabled = False
    surrender_btn.enabled = False


    def animate_dialogue_down():
        dialogue_bg.animate_y(-1.0, duration=0.8, curve=curve.in_quad)
        if player_battle_portrait:
            player_battle_portrait.animate_y(-1.0, duration=0.8, curve=curve.in_quad)
        if enemy_portrait:
            enemy_portrait.animate_y(-1.0, duration=0.8, curve=curve.in_quad)
        if enemy_hp_text:
            enemy_hp_text.animate_position((0.6, -1.5), duration=0.8, curve=curve.in_quad)  # Опускаем текст

        invoke(start_minigame, delay=0.9)

    animate_dialogue_down()


def surrender_action():
    """Сдаться - закрываем диалог"""
    global battle_active

    battle_active = False
    sound_manager.stop_battle_sound()
    sound_manager.play_background_sound()
    if battle2_sound.playing:
        battle2_sound.stop()
    if battle_reaction_sound.playing:
        battle_reaction_sound.stop()

    weak_attack_btn.enabled = False
    strong_attack_btn.enabled = False
    surrender_btn.enabled = False

    close_dialogue()
    print("🏳️ Сдался!")

def attack_action():
    """Обработчик для кнопки Напасть в основном диалоге"""
    start_battle()

# В функции input обновляем обработку клавиш для боя

def start_minigame():
    global minigame_active, minigame_ui, pointer, zones, hits, attempts

    if minigame_active:
        return

    minigame_active = True
    hits = 0
    attempts = 3

    # Тёмный полупрозрачный фон
    minigame_ui = Entity(parent=camera.ui, model='quad', scale=(1.5, 1.5), color=color.rgba(0, 0, 0, 0.6), z=-1)

    # Центральный круг
    circle = Entity(parent=minigame_ui, model=Circle(resolution=128), scale=0.45, color=color.rgba(0.16, 0.16, 0.16, 0.8),
                    z=-0.9)

    # Внешний ободок
    Entity(parent=circle, model=Circle(resolution=128, mode='line'), scale=1.05, color=color.rgba(1, 1, 1, 0.3),
           thickness=4, z=-0.88)

    # Центральная точка
    Entity(parent=circle, model='circle', scale=0.03, color=color.white, z=-0.7)

    # Основная палка
    pointer = Entity(parent=circle, model='quad', color=color.yellow, scale=(0.015, 0.70), y=0, origin_y=-0.5,
                     z=-0.6)

    # Создаём 8 красных палок
    divider_angles = [0, 45, 90, 135, 180, 225, 270, 315]
    dividers = []

    for angle in divider_angles:
        divider = Entity(
            parent=circle,
            model='quad',
            color=color.rgba(1, 0, 0, 0.5),
            scale=(0.01, 0.8),
            rotation_z=angle,
            y=0,
            origin_y=-0.5,
            z=-0.8
        )
        dividers.append(divider)

    # Создаём 8 зон между палками
    zones = []
    zone_angles = [22.5, 67.5, 112.5, 157.5, 202.5, 247.5, 292.5, 337.5]

    # Выбираем 3 случайные зоны которые будут активными (красными)
    active_zones = random.sample(zone_angles, 3)

    for angle in zone_angles:
        zone = Entity(
            parent=circle,
            model='quad',
            color=color.rgba(1, 0, 0, 0.4) if angle in active_zones else color.rgba(0.3, 0.3, 0.3, 0.1),  # Более прозрачные
            scale=(0.08, 0.25),
            rotation_z=angle,
            y=0,
            origin=(0, -2),
            z=-0.85
        )
        # Сохраняем только активные зоны
        if angle in active_zones:
            zones.append({'entity': zone, 'angle': angle, 'active': True})


    Text("Нажимай X", parent=minigame_ui, y=-0.2,z=-4,x=0.4, scale=1.1, color=color.rgba(1, 1, 1, 0.8))
    Text(f"Целей: {len(zones)}", parent=minigame_ui, y=0.30, scale=0.8, color=color.rgba(1, 1, 0, 0.8))


def stop_minigame_hand():
    global minigame_active, pointer, zones, hits, attempts, last_x_press_time, hit_text, minigame_ui

    if not minigame_active or attempts <= 0:
        return

    current_time = time.time()
    if current_time - last_x_press_time < x_cooldown:
        return

    last_x_press_time = current_time
    attempts -= 1
    pointer_angle = pointer.rotation_z % 360
    hit = False

    for zone in zones:
        if not zone['active']:
            continue

        if abs(pointer_angle - zone['angle']) <= 10 or abs(pointer_angle - zone['angle'] - 360) <= 10:
            zone['entity'].color = color.gray
            zone['active'] = False
            hit = True
            hits += 1

            if hit_sound:
                hit_sound.play()

            if hits == 1:
                rating_text = "Kill"
                text_color = color.red

            elif hits == 2:
                rating_text = "Kill"
                text_color = color.red

            elif hits == 3:
                rating_text = "Kill"
                text_color = color.red

            else:
                rating_text = ""
                text_color = color.white

            if hit_text:
                destroy(hit_text)

            # Создаём текст внутри мини-игры
            hit_text = Text(
                parent=minigame_ui,   # теперь часть мини-игры!
                text=rating_text,
                position=(0, 0.2),
                scale=0.1,
                color=text_color,
                background=True,
                font='4205.otf',
                background_color=color.rgba(0, 0, 0, 150)
            )
            hit_text.z = -3

            # Лёгкая анимация
            hit_text.animate_scale(3.0, duration=0.5, curve=curve.out_elastic)
            hit_text.animate_position((0, 0.3), duration=0.8, curve=curve.out_quad)
            invoke(lambda: destroy(hit_text) if hit_text else None, delay=1.5)

            print(f"✅ {rating_text}! Попал! Осталось зон: {3 - hits}")

            if hits >= 3:
                print("🎉 Все зоны сбиты! Задержка перед завершением...")
                invoke(end_minigame, delay=2.0)  # Задержка 2 секунды
            break

    if not hit:
        if miss_sound:
            miss_sound.play()
        print("❌ Мимо!")

    if hits >= 3:
        print("🎉 Все зоны сбиты!")
        end_minigame()
    elif attempts == 0 and hits < 3:
        print("💀 Попытки закончились!")
        end_minigame()

def end_minigame():
    global minigame_active, minigame_ui, pointer, zones, enemy_hp, enemy_hp_text, hits, hit_text

    if not minigame_active:
        return

    if hit_text:
        destroy(hit_text)
        hit_text = None


    if minigame_ui:
        destroy(minigame_ui)
    minigame_ui = None
    pointer = None
    zones = []
    minigame_active = False

    print("🎯 Мини-игра завершена!")

    def enemy_hit_animation():
        if enemy_decorate:
            original_x = enemy_decorate.x
            for i in range(6):
                invoke(setattr, enemy_decorate, 'x', original_x + (0.02 if i % 2 == 0 else -0.02), delay=i * 0.05)
            invoke(setattr, enemy_decorate, 'x', original_x, delay=0.3)
            # Мелькание
            enemy_decorate.animate_color(color.rgb(1, 0.2, 0.2), duration=0.1)
            invoke(enemy_decorate.animate_color, color.white, 0.2, delay=0.1)
        if not attack2_sound.playing:
            attack2_sound.play()


    def animate_dialogue_up():

        dialogue_bg.animate_y(-0.6, duration=0.8, curve=curve.out_quad)

        if player_battle_portrait:
            player_battle_portrait.animate_y(-0.38, duration=0.8, curve=curve.out_quad)
            player_battle_portrait.animate_x(-0.61, duration=0.8, curve=curve.out_quad)
        if enemy_portrait:
            enemy_portrait.animate_y(-0.38, duration=0.8, curve=curve.out_quad)
            enemy_portrait.animate_x(0.61, duration=0.8, curve=curve.out_quad)
        if enemy_hp_text:
            enemy_hp_text.animate_position((0.3, -0.3), duration=0.8, curve=curve.out_quad)
        if enemy_decorate:
            enemy_decorate.animate_y(0.1,duration=0.8, curve=curve.out_quad)


        def show_buttons_again():
            global enemy_hp

            weak_attack_btn.enabled = True
            strong_attack_btn.enabled = True
            surrender_btn.enabled = True

            weak_attack_btn.x = -0.25
            strong_attack_btn.x = -0.25
            surrender_btn.x = -0.25

            weak_attack_btn.y = -0.25
            strong_attack_btn.y = -0.35
            surrender_btn.y = -0.45

            if hits >= 3:
                damage = 30
            elif hits == 2:
                damage = 20
            elif hits == 1:
                damage = 10
            else:
                damage = 0

            if damage > 0:
                enemy_hp -= damage
                if enemy_hp < 0:
                    enemy_hp = 0

                if enemy_hp_text:
                    enemy_hp_text.text = f"HP: {enemy_hp}"

                enemy_hit_animation()

            # сообщение в консоль
            print(f"🔸 Мини-игра: попал {hits} раз(а), урон {damage}, HP врага теперь {enemy_hp}")

        invoke(show_buttons_again, delay=0.9)

    animate_dialogue_up()



base_walk_speed = 8
base_run_speed = 12
speed_multiplier = 1.0
# ===== ГЛОБАЛЬНЫЕ ПЕРЕМЕННЫЕ ДЛЯ СЛАБОЙ АТАКИ =====
weak_zones = []
weak_hit = False
weak_attempts = 0
last_x_press_time = 0
x_cooldown = 0.2


def enemy_hit_animation():
    """Анимация попадания по врагу"""
    if 'enemy_decorate' in globals() and enemy_decorate:
        original_x = enemy_decorate.x
        for i in range(6):
            invoke(setattr, enemy_decorate, 'x', original_x + (0.02 if i % 2 == 0 else -0.02), delay=i * 0.05)
        invoke(setattr, enemy_decorate, 'x', original_x, delay=0.3)

        # Мелькание
        enemy_decorate.animate_color(color.rgb(1, 0.2, 0.2), duration=0.1)
        invoke(enemy_decorate.animate_color, color.white, 0.2, delay=0.1)

    if not attack2_sound.playing:
        attack2_sound.play()


def start_weak_attack_minigame():
    global minigame_active, minigame_ui, pointer, weak_zones, weak_hit, weak_attempts

    if minigame_active:
        return

    minigame_active = True
    weak_hit = False
    weak_attempts = 1

    # Тёмный полупрозрачный фон
    minigame_ui = Entity(parent=camera.ui, model='quad', scale=(1.5, 1.5), color=color.rgba(0, 0, 0, 0.6), z=-1)

    # Основной прямоугольник
    Entity(
        parent=minigame_ui,
        model='quad',
        color=color.gray,
        scale=(0.8, 0.2),
        position=(0, 0),
        z=1
    )

    # Обводка прямоугольника
    Entity(
        parent=minigame_ui,
        model=Quad(mode='line'),
        color=color.white,
        scale=(0.81, 0.21),
        position=(0, 0),
        thickness=3,
        z=-0.88
    )

    # Создаем симметричные зоны вокруг центра
    weak_zones = []

    # Ширина зон (симметрично от центра):
    # Центр: 20% (по 10% с каждой стороны от центра)
    # Середина: 30% (по 15% с каждой стороны от центральной зоны)
    # Край: 50% (по 25% с каждой стороны)
    zone_widths = [0.16, 0.24, 0.4]  # Центр, Середина, Край
    zone_damage = [15, 10, 5]  # Урон: Центр-15, Середина-10, Край-5

    
    zone_colors_with_alpha = [
        color.green.tint(0.3),  # Зеленый - центр (самый сложный)
        color.yellow.tint(0.3),  # Желтый - середина
        color.red.tint(0.3)  # Красный - край (самый легкий)
    ]

    
    zone_full_colors = [color.green, color.yellow, color.red]

    # Начинаем с центра и двигаемся наружу
    total_width = 0.8
    center_width = zone_widths[0]  # 0.16 (20%)
    middle_width = zone_widths[1]  # 0.24 (30%)
    edge_width = zone_widths[2]  # 0.4 (50%)

    # Центральная зона 
    center_zone = Entity(
        parent=minigame_ui,
        model='quad',
        color=zone_colors_with_alpha[0],
        scale=(center_width, 0.18),
        position=(0, 0),  # Прямо в центре
        z=-0.85
    )

    weak_zones.append({
        'entity': center_zone,
        'x_start': -center_width / 2,
        'x_end': center_width / 2,
        'damage': zone_damage[0],
        'color': zone_full_colors[0],
        'zone_name': 'Центр'
    })

    # Средние зоны (по бокам от центра)
    middle_left_zone = Entity(
        parent=minigame_ui,
        model='quad',
        color=zone_colors_with_alpha[1],
        scale=(middle_width / 2, 0.18),
        position=(-center_width / 2 - middle_width / 4, 0),  # Слева от центра
        z=-0.85
    )

    middle_right_zone = Entity(
        parent=minigame_ui,
        model='quad',
        color=zone_colors_with_alpha[1],
        scale=(middle_width / 2, 0.18),
        position=(center_width / 2 + middle_width / 4, 0),  # Справа от центра
        z=-0.85
    )

    weak_zones.append({
        'entity': middle_left_zone,
        'x_start': -center_width / 2 - middle_width / 2,
        'x_end': -center_width / 2,
        'damage': zone_damage[1],
        'color': zone_full_colors[1],
        'zone_name': 'Середина'
    })

    weak_zones.append({
        'entity': middle_right_zone,
        'x_start': center_width / 2,
        'x_end': center_width / 2 + middle_width / 2,
        'damage': zone_damage[1],
        'color': zone_full_colors[1],
        'zone_name': 'Середина'
    })

    
    edge_left_zone = Entity(
        parent=minigame_ui,
        model='quad',
        color=zone_colors_with_alpha[2],
        scale=(edge_width / 2, 0.18),
        position=(-total_width / 2 + edge_width / 4, 0),  # Левый край
        z=-0.85
    )

    edge_right_zone = Entity(
        parent=minigame_ui,
        model='quad',
        color=zone_colors_with_alpha[2],
        scale=(edge_width / 2, 0.18),
        position=(total_width / 2 - edge_width / 4, 0),  # Правый край
        z=-0.85
    )

    weak_zones.append({
        'entity': edge_left_zone,
        'x_start': -total_width / 2,
        'x_end': -center_width / 2 - middle_width / 2,
        'damage': zone_damage[2],
        'color': zone_full_colors[2],
        'zone_name': 'Край'
    })

    weak_zones.append({
        'entity': edge_right_zone,
        'x_start': center_width / 2 + middle_width / 2,
        'x_end': total_width / 2,
        'damage': zone_damage[2],
        'color': zone_full_colors[2],
        'zone_name': 'Край'
    })

    # Движущаяся палка
    pointer = Entity(
        parent=minigame_ui,
        model='quad',
        color=color.cyan,
        scale=(0.01, 0.22),
        position=(-0.4, 0),
        z=-0.96
    )

    # Направление движения 1вправо, -1влево
    pointer.direction = 1
    pointer.speed = 2.4

    # Текст инструкции
    Text(
        "Нажимай X чтобы атаковать",
        parent=minigame_ui,
        y=-0.3,
        scale=1.1,
        color=color.white,
        font='4205.otf'
    )

    # Текст с уроном
    Text(
        "Центр: -15HP | Середина: -10HP | Край: -5HP",
        parent=minigame_ui,
        y=-0.4,
        scale=10,
        color=color.white,
        font='4205.otf'
    )


    # Между краем и серединой слева
    Entity(
        parent=minigame_ui,
        model='quad',
        color=color.white,
        scale=(0.005, 0.22),
        position=(-center_width / 2 - middle_width / 2, 0),
        z=-0.9
    )

    # Между серединой и центром слева
    Entity(
        parent=minigame_ui,
        model='quad',
        color=color.white,
        scale=(0.005, 0.22),
        position=(-center_width / 2, 0),
        z=-0.9
    )

    # Между центром и серединой справа
    Entity(
        parent=minigame_ui,
        model='quad',
        color=color.white,
        scale=(0.005, 0.22),
        position=(center_width / 2, 0),
        z=-0.9
    )

    # Между серединой и краем справа
    Entity(
        parent=minigame_ui,
        model='quad',
        color=color.white,
        scale=(0.005, 0.22),
        position=(center_width / 2 + middle_width / 2, 0),
        z=-0.9
    )

def update_weak_minigame():
    global minigame_active, pointer, weak_zones, weak_hit

    if not minigame_active or weak_hit:
        return

    # Двигаем палку
    pointer.x += pointer.direction * pointer.speed * time.dt

    if pointer.x >= 0.4:
        pointer.x = 0.4
        pointer.direction = -1
    elif pointer.x <= -0.4:
        pointer.x = -0.4
        pointer.direction = 1


def stop_weak_minigame():
    global minigame_active, minigame_ui, pointer, weak_zones, weak_hit, weak_attempts, enemy_hp, last_x_press_time

    if not minigame_active or weak_hit or weak_attempts <= 0:
        return

    current_time = time.time()
    if current_time - last_x_press_time < x_cooldown:
        return

    last_x_press_time = current_time
    weak_attempts -= 1
    weak_hit = True

    # Определяем в какую зону попали
    damage = 0
    hit_zone = None

    for zone in weak_zones:
        if zone['x_start'] <= pointer.x <= zone['x_end']:
            damage = zone['damage']
            hit_zone = zone
            break

    
    if hit_zone:
        # Подсвечиваем зону
        hit_zone['entity'].color = color.white

        
        damage_text = Text(
            parent=minigame_ui,
            text=f"-{damage} HP",
            position=(0, 0.2),
            scale=1,
            color=hit_zone['color'],
            background=True,
            font='4205.otf',
            background_color=color.rgba(0, 0, 0, 150)
        )

        
        damage_text.animate_scale(1, duration=0.5, curve=curve.out_elastic)
        damage_text.animate_position((0, 0.3), duration=0.8, curve=curve.out_quad)

    
        if hit_sound:
            hit_sound.play()

        print(f"✅ Слабая атака! Попал в зону с уроном {damage}")
    else:
        damage = 0
        if miss_sound:
            miss_sound.play()
        print("❌ Слабая атака! Промах!")

    
    if damage > 0:
        enemy_hp -= damage
        if enemy_hp < 0:
            enemy_hp = 0
        if enemy_hp_text:
            enemy_hp_text.text = f"HP: {enemy_hp}"

        # Анимация попадания по врагу
        enemy_hit_animation()

    # Завершаем мини-игру через секунду
    invoke(end_weak_minigame, delay=1.0)


def end_weak_minigame():
    
    global minigame_active, minigame_ui, pointer, weak_zones

    if not minigame_active:
        return

    
    if minigame_ui:
        destroy(minigame_ui)
    minigame_ui = None
    pointer = None
    weak_zones = []
    minigame_active = False

    print("🎯 Мини-игра слабой атаки завершена!")

    # Возвращаемся к бою
    animate_dialogue_up_after_weak_attack()


def animate_dialogue_up_after_weak_attack():
    dialogue_bg.animate_y(-0.6, duration=0.8, curve=curve.out_quad)

    if player_battle_portrait:
        player_battle_portrait.animate_y(-0.38, duration=0.8, curve=curve.out_quad)
        player_battle_portrait.animate_x(-0.61, duration=0.8, curve=curve.out_quad)

    if enemy_portrait:
        enemy_portrait.animate_y(-0.38, duration=0.8, curve=curve.out_quad)
        enemy_portrait.animate_x(0.61, duration=0.8, curve=curve.out_quad)

    if enemy_hp_text:
        enemy_hp_text.animate_position((0.3, -0.3), duration=0.8, curve=curve.out_quad)

    if enemy_decorate:
        enemy_decorate.animate_y(0.1, duration=0.8, curve=curve.out_quad)

    def show_buttons_again():
        weak_attack_btn.enabled = True
        strong_attack_btn.enabled = True
        surrender_btn.enabled = True

        weak_attack_btn.x = -0.25
        strong_attack_btn.x = -0.25
        surrender_btn.x = -0.25

        weak_attack_btn.y = -0.25
        strong_attack_btn.y = -0.35
        surrender_btn.y = -0.45

    invoke(show_buttons_again, delay=0.9)

def update():
    global in_dialogue, pointer, minigame_active, speed_multiplier

    if minigame_active:
        if walk.playing:
            walk.stop()
        press_e_text.enabled = False

        # Определяем тип активной мини-игры
        if hasattr(pointer, 'direction'): 
            update_weak_minigame() 
        elif pointer: 
            pointer.rotation_z += rotation_speed * time.dt
        return

    if minigame_active:
        if walk.playing:
            walk.stop()
        press_e_text.enabled = False
        if pointer:
            pointer.rotation_z += rotation_speed * time.dt
        return


    if in_dialogue:
        press_e_text.enabled = False
        update_text_printing()
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
    in_zone4 =(11 <= player_pos.x <= 15.18 and
              8 <= player_pos.y <= 20 and
              12 <= player_pos.z <= 18)
    in_door_zone = (125 <= player.position.x <= 131 and
                    -2 <= player.position.y <= 5 and
                    0 <= player.position.z <= 5)
    in_door_zone2=(10 <= player.position.x <= 11.9 and
                   8 <= player.position.y <= 17 and
                   11 <= player.position.z <= 12)
    press_e_text.enabled = ((human_collider.hovered and in_zone1) or
                            (human_collidera.hovered and in_zone2) or
                            (human_colliderb.hovered and in_zone3) or
                            bossa_collider.hovered and in_zone4)
    from ursina import distance
    look_at_door = False

    if hasattr(player, 'forward'):
        look_point = player.position + player.forward * 2
        if distance(look_point, collider_door1.position) < 3:
            look_at_door = True
    door_text.enabled = (in_door_zone and look_at_door)
    if hasattr(player, 'forward'):
        look_point = player.position + player.forward * 2
        if distance(look_point, collider_door2.position) < 3:
            look_at_door = True

    # --- Появление подсказки "ВОЙТИ?" ---
    door_text2.enabled = (in_door_zone2 and look_at_door)


    # --- Отладочный ---
    print(f"x={player_pos.x:.2f}  y={player_pos.y:.2f}  z={player_pos.z:.2f}  "
          f"in_door_zone={in_door_zone2}  смотрю_на_дверь={look_at_door}")

    walking = held_keys['a'] or held_keys['w'] or held_keys['d'] or held_keys['s']
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
        sun.color = color.rgb(0.16, 0.16, 0.24)
        AmbientLight(color=color.rgb(0.06, 0.06, 0.1))
        camera.background_color = color.rgb(0.01, 0.01, 0.04)
        Sky.texture = 'sky3.jpg'
        player.position = (0, 2, 0)

        apply_shaders_to_all_objects()
        lvl = 2
        print("Переключено на ночь (уровень 2) - шейдеры включены")
    else:
        sun.color = color.rgb(1.0, 0.95, 0.9)
        AmbientLight(color=color.rgb(0.6, 0.6, 0.6))
        camera.background_color = color.rgb(0.5, 0.7, 1.0)
        Sky.texture = 'sky_default'
        player.position = player.position

        remove_shaders_from_all_objects()
        lvl = 1
        print("Переключено на день (уровень 1) - шейдеры выключены")


def apply_shaders_to_all_objects():
    all_objects = []

    for i in range(1, 113):
        obj_name = f'tree{i}'
        if obj_name in globals():
            all_objects.append(globals()[obj_name])
    for i in range(1, 76):
        obj_name = f'bigtree{i}'
        if obj_name in globals():
            all_objects.append(globals()[obj_name])
    for i in range(1, 8):
        obj_name = f'back{i}'
        if obj_name in globals():
            all_objects.append(globals()[obj_name])
    for i in range(1, 8):
        obj_name = f'house{i}'
        if obj_name in globals():
            all_objects.append(globals()[obj_name])
    for i in range(1, 10):
        obj_name = f'zabor{i}'
        if obj_name in globals():
            all_objects.append(globals()[obj_name])
    for i in range(1, 3):
        obj_name = houseOWN
        if obj_name in globals():
            all_objects.append(globals()[obj_name])
    for i in range(1,3):
        obj_name = questhouse
        if obj_name in globals():
            all_objects.append(globals()[obj_name])

    for obj in all_objects:
        obj.shader = lit_with_shadows_shader
        houseOWN.shader = lit_with_shadows_shader
        human2.shader = lit_with_shadows_shader
        questhouse.shader=lit_with_shadows_shader

    print(f"Шейдеры применены к {len(all_objects)} объектам")


def remove_shaders_from_all_objects():
    all_objects = []

    for i in range(1, 113):
        obj_name = f'tree{i}'
        if obj_name in globals():
            all_objects.append(globals()[obj_name])
    for i in range(1, 76):
        obj_name = f'bigtree{i}'
        if obj_name in globals():
            all_objects.append(globals()[obj_name])
    for i in range(1, 9):
        obj_name = f'back{i}'
        if obj_name in globals():
            all_objects.append(globals()[obj_name])
    for i in range(1, 8):
        obj_name = f'house{i}'
        if obj_name in globals():
            all_objects.append(globals()[obj_name])
    for i in range(1, 10):
        obj_name = f'zabor{i}'
        if obj_name in globals():
            all_objects.append(globals()[obj_name])
    for i in range(1,3):
        obj_name = questhouse
        if obj_name in globals():
            all_objects.append(globals()[obj_name])

    for obj in all_objects:
        obj.shader = unlit_shader
        houseOWN.shader = basic_lighting_shader
        zabor1.shader = basic_lighting_shader
        zabor2.shader = basic_lighting_shader
        human2.shader = basic_lighting_shader
        questhouse.shader=basic_lighting_shader

    print(f"Шейдеры убраны с {len(all_objects)} объектов")


def test_battle_interface():
    global battle_active

    print("🔧 Тестирование боевого интерфейса...")

    player.enabled = False
    battle_active = True

    create_battle_interface()


def ultra_safe_hide():
    """Сверхбезопасное скрытие объектов с проверкой на использование в коде"""
    objects_to_hide = [
        # Дома
        'house1', 'house2', 'house3', 'house4', 'house5', 'house6', 'house7', 'house8',
        'roada', 'roadb', 'roadc',
        'trotuara', 'trotuarb', 'trotuarc', 'trotuard', 'trotuare', 'trotuarf',
        'trotuarg', 'trotuarh', 'trotuark', 'trotuar1', 'trotuar2', 'trotuar3',
        'ogranich1', 'ogranich2',
        'back1', 'back2', 'back3', 'back4', 'back5','back6',
        'houseOWN', 'window', 'zabor1', 'zabor2','zabor3','zabor4','zabor5','zabor6','zabor7','zabor8',
        'questhouse', 'collider_questhouse1', 'collider_questhouse2'
        
    ]

    trees_to_hide = []

    
    for i in range(1, 113):
        trees_to_hide.append(f'tree{i}')

    
    for i in range(1, 76):
        trees_to_hide.append(f'bigtree{i}')

    # Объединяем все объекты для скрытия
    all_objects_to_hide = objects_to_hide + trees_to_hide

    hidden_count = 0

    for obj_name in all_objects_to_hide:
        if obj_name in globals():
            obj = globals()[obj_name]
            if obj and hasattr(obj, 'enabled'):  
                try:
                    obj.enabled = False  
                    hidden_count += 1
                    print(f"👻 Скрыт: {obj_name}")
                except Exception as e:
                    print(f"❌ Ошибка при скрытии {obj_name}: {e}")

    print(f"🎯 Всего скрыто объектов: {hidden_count}")


def hide_npcs():
    
    npc_objects = [
        # Первый NPC
        'humana', 'head', 'body', 'right', 'human_collider',
        # Второй NPC
        'humanb', 'heada', 'bodya', 'righta', 'human_collidera',
        # Третий NPC
        'humanc', 'headb', 'bodyb', 'rightb', 'human_colliderb'
    ]

    hidden_count = 0

    for obj_name in npc_objects:
        if obj_name in globals():
            obj = globals()[obj_name]
            if obj and hasattr(obj, 'enabled'):
                try:
                    obj.enabled = False  # Скрываем объект
                    hidden_count += 1
                    print(f"👻 Скрыт NPC: {obj_name}")
                except Exception as e:
                    print(f"❌ Ошибка при скрытии {obj_name}: {e}")

    print(f"🎯 Всего скрыто NPC объектов: {hidden_count}")


def show_npcs():
    
    npc_objects = [
        'humana', 'head', 'body', 'right', 'human_collider',
        'humanb', 'heada', 'bodya', 'righta', 'human_collidera',
        'humanc', 'headb', 'bodyb', 'rightb', 'human_colliderb'
    ]

    shown_count = 0

    for obj_name in npc_objects:
        if obj_name in globals():
            obj = globals()[obj_name]
            if obj and hasattr(obj, 'enabled'):
                try:
                    obj.enabled = True 
                    shown_count += 1
                    print(f"👀 Показан NPC: {obj_name}")
                except Exception as e:
                    print(f"❌ Ошибка при показе {obj_name}: {e}")

    print(f"🎯 Всего показано NPC объектов: {shown_count}")
def ultra_safe_show():
    
    objects_to_show = [
        # Дома
        'house1', 'house2', 'house3', 'house4', 'house5', 'house6', 'house7', 'house8',
        'roada', 'roadb', 'roadc',
        'trotuara', 'trotuarb', 'trotuarc', 'trotuard', 'trotuare', 'trotuarf',
        'trotuarg', 'trotuarh', 'trotuark', 'trotuar1', 'trotuar2', 'trotuar3',
        'ogranich1', 'ogranich2',
        'back1', 'back2', 'back3', 'back4', 'back5','back6',
        'houseOWN', 'window', 'zabor1', 'zabor2','zabor3','zabor4','zabor5','zabor6','zabor7','zabor8',
        'questhouse', 'collider_questhouse1', 'collider_questhouse2'
    ]

    # Добавляем все деревья
    trees_to_show = []
    for i in range(1, 113):
        trees_to_show.append(f'tree{i}')
    for i in range(1, 76):
        trees_to_show.append(f'bigtree{i}')

    # Объединяем все объекты для показа
    all_objects_to_show = objects_to_show + trees_to_show

    shown_count = 0

    for obj_name in all_objects_to_show:
        if obj_name in globals():
            obj = globals()[obj_name]
            if obj and hasattr(obj, 'enabled'):
                try:
                    obj.enabled = True  # Показываем объект
                    shown_count += 1
                    print(f"👀 Показан: {obj_name}")
                except Exception as e:
                    print(f"❌ Ошибка при показе {obj_name}: {e}")

    print(f"🎯 Всего показано объектов: {shown_count}")

def teleport_player(x, y, z):
    
    player.position = (x, y, z)
    print(f"🎮 Игрок телепортирован в ({x}, {y}, {z})")


def teleport_with_fade(target_position, fade_duration=2):


    # Создаем черный экран для затемнения
    fade_overlay = Entity(
        parent=camera.ui,
        model='quad',
        scale=(2, 2),
        color=color.black,
        alpha=0,
        z=-10
    )

    def fade_sequence():
        # 1. Затемнение экрана
        fade_overlay.animate('alpha', 1, duration=fade_duration / 2, curve=curve.linear)

        # 2. Телепортация в середине затемнения
        def do_teleport():
            player.position = target_position

        invoke(do_teleport, delay=fade_duration / 2)

        # 3. Осветление экрана
        invoke(lambda: fade_overlay.animate('alpha', 0, duration=fade_duration / 2, curve=curve.linear),
               delay=fade_duration / 2)

        # 4. Удаление overlay после анимации
        invoke(lambda: destroy(fade_overlay), delay=fade_duration)

    fade_sequence()
def input(key):
    global in_dialogue, minigame_active, pointer, zones, hits, attempts, battle_active

    if minigame_active:
        if key == 'x':
            # Определяем тип активной мини-игры
            if hasattr(pointer, 'direction'):  # Мини-игра слабой атаки
                stop_weak_minigame()
            else:  # Мини-игра сильной атаки
                stop_minigame_hand()
            return
        return

    # --- Мини-игра ---
    if minigame_active:
        if key == 'x' and attempts > 0:
            stop_minigame_hand()
            return
        return

    # --- Запуск мини-игры ---
    if key == '0' and not minigame_active:
        start_minigame()
        return

    if key == 'z':
        ultra_safe_hide()
        hide_npcs()
        print("💥 Нажата J - уничтожаем указанные объекты!")
        return

    # --- Тест боя ---
    if key == 'u' and not in_dialogue and not battle_active and not minigame_active:
        test_battle_interface()
        return

    # --- Взаимодействие с NPC ---
    if key == 'e' and not in_dialogue and press_e_text.enabled:
        player_pos = player.position
        in_zone1 = (18 <= player_pos.x <= 23 and 0.4 <= player_pos.y <= 0.7 and 3 <= player_pos.z <= 9)
        in_zone2 = (45 <= player_pos.x <= 52 and 0.4 <= player_pos.y <= 0.7 and 4 <= player_pos.z <= 7.5)
        in_zone3 = (17.5 <= player_pos.x <= 22.8 and 0.4 <= player_pos.y <= 0.7 and -6.5 <= player_pos.z <= -4)
        in_zone4 = (11 <= player_pos.x <= 15.18 and 8 <= player_pos.y <= 20 and 12 <= player_pos.z <= 18)

        if human_collider.hovered and in_zone1:
            start_dialogue("Человек 1", "Привет! Рад тебя видеть. Что скажешь?")
        elif human_collidera.hovered and in_zone2:
            start_dialogue("Человек 2", "Привет! Я второй NPC.")
        elif human_colliderb.hovered and in_zone3:
            start_dialogue("Человек 3", "Здравствуй! Я третий NPC.")
        elif bossa_collider.hovered and in_zone4:
            start_dialogue("Босс","Вот тебе задание.")

    # --- Взаимодействие с дверями ---
    if key == 'e':
        print("[DEBUG] Нажата клавиша E")

        player_pos = player.position

        
        in_door_zone1 = (125 <= player_pos.x <= 131 and
                         -2 <= player_pos.y <= 5 and
                         0 <= player_pos.z <= 5)

        
        in_door_zone2 = (10 <= player_pos.x <= 11.9 and
                         8 <= player_pos.y <= 17 and
                         11 <= player_pos.z <= 12)

        print(f"[DEBUG] Позиция игрока: x={player_pos.x:.2f}, y={player_pos.y:.2f}, z={player_pos.z:.2f}")
        print(f"[DEBUG] Дверь1: in_zone={in_door_zone1}")
        print(f"[DEBUG] Дверь2: in_zone={in_door_zone2}")

        # Проверяем расстояние до объектов дверей
        if 'collider_door1' in globals() and collider_door1:
            dist_to_door1 = distance(player_pos, collider_door1.position)
            print(f"[DEBUG] Расстояние до двери1: {dist_to_door1}")
        else:
            dist_to_door1 = 1000
            print("[DEBUG] Дверь1 не найдена")

        if 'collider_door2' in globals() and collider_door2:
            dist_to_door2 = distance(player_pos, collider_door2.position)
            print(f"[DEBUG] Расстояние до двери2: {dist_to_door2}")
        else:
            dist_to_door2 = 1000
            print("[DEBUG] Дверь2 не найдена")

        # Если находимся в зоне первой двери и близко к ней
        if in_door_zone1 and dist_to_door1 < 5:
            print("[DEBUG] ВХОД В ДОМ — запуск анимации телепортации")

            def enter_house():
                ultra_safe_hide()
                hide_npcs()
                questhouseinside.enabled = True
                questhouseinside_collider1.enabled = True
                questhouseinside_collider2.enabled = True
                questhouseinside_collider3.enabled = True
                questhouseinside_collider4.enabled = True
                questhouseinside_collider5.enabled = True
                questhouseinside_collider6.enabled = True
                questhouseinside_collider7.enabled = True
                questhouseinside_collider8.enabled = True
                questhouseinside_collider9.enabled = True
                questhouseinside_collider10.enabled = True
                bossa.enabled= True
                sound_manager.stop_background_sound()
                sound_manager.play_bossa_sound()



            
            teleport_with_fade((10.9, 10, 11.03), fade_duration=3)
            invoke(enter_house, delay=1.5)  

        # Если находимся в зоне второй двери и близко к ней
        elif in_door_zone2 and dist_to_door2 < 5:
            print("[DEBUG] ВЫХОД ИЗ ДОМА — запуск анимации телепортации")

            def exit_house():
                ultra_safe_show()
                show_npcs()
                questhouseinside.enabled = False
                questhouseinside_collider1.enabled = False
                questhouseinside_collider2.enabled = False
                questhouseinside_collider3.enabled = False
                questhouseinside_collider4.enabled = False
                questhouseinside_collider5.enabled = False
                questhouseinside_collider6.enabled = False
                questhouseinside_collider7.enabled = False
                questhouseinside_collider8.enabled = False
                questhouseinside_collider9.enabled = False
                questhouseinside_collider10.enabled = False
                bossa.enabled= False
                sun.look_at(Vec3(-1, -1, -1))
                sun.color = color.rgb(1.0, 0.7, 0.4)
                Sky.texture = 'Sunrise.jpg'

                AmbientLight(color=color.rgb(0.8, 0.6, 0.3))

                camera.background_color = color.rgb(0.9, 0.5, 0.2)
                hide_npcs()
                sound_manager.stop_bossa_sound()
                sound_manager.play_background_sound()


            
            teleport_with_fade((126, 2.24, 2.64), fade_duration=3)
            invoke(exit_house, delay=1.5) 

        else:
            print("[DEBUG] Неукакойs двери или слишком далеко")

    # --- Закрытие диалогов ---
    if key in ('1', '2', '3') and in_dialogue and not battle_active:
        close_dialogue()

    # --- Быстрая смена уровня ---
    if key == 'p':
        print("[DEBUG] Ручной вызов switch_level() через P")
        switch_level()

    # --- Прыжок ---
    if key == 'space' and not jump.playing:
        jump.play()

    # --- Выход ---
    if key == 'q':
        quit()
    if key=='v':
        ultra_safe_show()
        show_npcs()
    if key=='b':
        teleport_player(10.9, 10, 11.03)
        questhouseinside.enabled = True
        questhouseinside_collider1.enabled = True
        questhouseinside_collider2.enabled = True
        questhouseinside_collider3.enabled = True
        questhouseinside_collider4.enabled = True
        questhouseinside_collider5.enabled = True
        questhouseinside_collider6.enabled = True
        questhouseinside_collider7.enabled = True
        questhouseinside_collider8.enabled = True
        questhouseinside_collider9.enabled = True
        questhouseinside_collider10.enabled = True

button1.on_click = setup_conversation_buttons  # "Поговорить"
button2.on_click = attack_action  # "Напасть"
button3.on_click = close_dialogue  # "Уйти"
talk_button.on_click = talk_action
dont_care_button.on_click = dont_care_action
weak_attack_btn.on_click = weak_attack_action
strong_attack_btn.on_click = strong_attack_action
surrender_btn.on_click = surrender_action

app.run()







