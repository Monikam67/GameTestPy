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
ground2=Entity(model='cube',collider='mesh',texture='grass',scale=(500,1,100))
ground2.enabled=False


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

# StartHome=Entity(model='StartHome.glb', scale=2, position=(1,0.8,0))






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


Tonight_girl=Entity(parent=scene,position=(109.88,2,7.46),model='sphere',texture='face.jpg',scale=(2,2,2),rotation=(0,90,0))
Tonight_girl_collider=Entity(position=(109.88,2,7.46),model='cube',scale=(3,3,3),color=color.clear,collider='box')

Tonight_man=Entity(parent=scene,position=(80.06,2,7.49),model='sphere',texture='face.jpg',scale=(2,2,2),rotation=(0,90,0))
Tonight_man_collider=Entity(position=(80.06,2,7.49),model='cube',scale=(3,3,3),color=color.clear,collider='box')

Tonight_QuestMan=Entity(parent=scene,position=(109.94,2,-6.48),model='sphere',texture='face.jpg',scale=(2,2,2),rotation=(0,90,0))
Tonight_QuestMan_collider=Entity(position=(109.94,2,-6.48),model='cube',scale=(3,3,3),color=color.clear,collider='box')

all_npcs = [human_collider, human_collidera,human_colliderb,human_colliderb,bossa_collider,Tonight_girl,Tonight_girl_collider,Tonight_man_collider,Tonight_QuestMan_collider]


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
collider_door3=Entity(model='cube',scale=(0.5,6,2),position=(109.95,2,-9),color=color.clear,collider='box',rotation=(0,90,0))
collider_door4=Entity(model='cube',scale=(0.5,6,2),position=(50.07,2,-9),color=color.clear,collider='box',rotation=(0,90,0))

#---- Dream объекты ----
moon3 = Entity(
    model='sphere',
    color=color.rgb(180, 180, 255),
    scale=10,
    position=(-100,20,0),
    double_sided=True
)
moon3.enabled=False
Dream_collider1=Entity(model='cube',scale=(1,20,80),position=(70,0,0),rotation=(0,0,0),color=color.clear,collider='box')
Dream_collider2=Entity(model='cube',scale=(1,20,200),position=(0,0,30),rotation=(0,90,0),color=color.clear,collider='box')
Dream_collider3=Entity(model='cube',scale=(1,20,200),position=(0,0,-30),rotation=(0,90,0),color=color.clear,collider='box')
Dream_collider4=Entity(model='cube',scale=(10,500,400),position=(0,-40,30),rotation=(0,0,90),color=color.clear,collider='box')
Dream_collider5=Entity(model='cube',scale=(10,1,300),position=(-250,0.1,0),rotation=(0,90,0),color=color.white66,collider='box')
Dream_collider1.enabled=False
Dream_collider2.enabled=False
Dream_collider3.enabled=False
Dream_collider5.enabled=False
Dream_house=Entity(model='house.glb',scale=1.0,position=(-140,5,-20),rotation=(-15,180,15),shader=lit_with_shadows_shader)
Dream_house2=Entity(model='Dream_office.glb',scale=2.0,position=(-188,3,20),rotation=(0,180,15),shader=lit_with_shadows_shader)
Dream_house3=Entity(model='Dream_playground.glb',scale=5,position=(-235,3,-20),rotation=(0,90,-5),shader=lit_with_shadows_shader)
Dream_house4=Entity(model='Dream_exit1.glb',scale=5,position=(-370,5,0),rotation=(0,90,0),shader=lit_with_shadows_shader)
Dream_house5=Entity(model='Dream_exit2.glb',scale=5,position=(-370,10,0),rotation=(0,90,0)   )
#-----------------




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
collider_door2.position=(40,40,40)
collider_door3.position=(40,40,40)
collider_door4.position=(50.07,2,-9)


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
blood_frame = Entity(
        parent=camera.ui,
        model='quad',
        texture='blood_frame.png',
        scale=(2.1, 2.1),
        color=color.rgb(0.3, 0, 0),
        alpha=0,
        z=-10
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
    text='>> ВЫЙТИ? <<',
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
door_text3 = Text(
    text='>> ЗАЙТИ? <<',
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
door_text4 = Text(
    text='>> Дом,милый Дом <<',
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

npc_name = Text("Человек", parent=camera.ui, x=-0.7, y=-0.1,
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





# "Взять задание"
take_quest_btn = Button(text='Взять задание', color=color.orange, scale=(0.25, 0.08),
                       position=(0.3, -0.45), enabled=False, font='4205.otf')
take_quest_btn.text_entity.font = '4205.otf'
take_quest_btn.enabled = False
take_quest_btn.render_queue = 1
take_quest_btn.z = -0.1


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
take_quest_btn.enabled=False


talk_button = Button(text='Поболтать', color=color.green, scale=(0.2, 0.08),
                     position=(10, -0.45), enabled=False, font='4205.otf')
talk_button.text_entity.font = '4205.otf'
dont_care_button = Button(text='Неважно', color=color.gray, scale=(0.2, 0.08),
                          position=(0.15, -0.45), enabled=False, font='4205.otf')
dont_care_button.text_entity.font = '4205.otf'



talk_button.enabled = False
dont_care_button.enabled = False


# 9 кнопок вопросов для обычных NPC
question_btn1 = Button(text='Сколько сейчас времени?', color=color.gray, scale=(0.3, 0.07),
                      position=(-0.4, 0.2), enabled=False, font='4205.otf')
question_btn1.text_entity.font = '4205.otf'
question_btn1.enabled = False
question_btn1.render_queue = 2
question_btn1.z = -0.1

question_btn2 = Button(text='Что ты делаешь весь день?', color=color.gray, scale=(0.3, 0.07),
                      position=(-0.4, 0.1), enabled=False, font='4205.otf')
question_btn2.text_entity.font = '4205.otf'
question_btn2.enabled = False
question_btn2.render_queue = 2
question_btn2.z = -0.1

question_btn3 = Button(text='Что это за место?', color=color.gray, scale=(0.3, 0.07),
                      position=(-0.4, 0.0), enabled=False, font='4205.otf')
question_btn3.text_entity.font = '4205.otf'
question_btn3.enabled = False
question_btn3.render_queue = 2
question_btn3.z = -0.1

question_btn4 = Button(text='Ты никогда не хотел сбежать отсюда?', color=color.gray, scale=(0.3, 0.07),
                      position=(0.1, 0.0), enabled=False, font='4205.otf')
question_btn4.text_entity.font = '4205.otf'
question_btn4.enabled = False
question_btn4.render_queue = 2
question_btn4.z = -0.1

question_btn5 = Button(text='Расскажи о себе', color=color.gray, scale=(0.3, 0.07),
                      position=(0.1, 0.2), enabled=False, font='4205.otf')
question_btn5.text_entity.font = '4205.otf'
question_btn5.enabled = False
question_btn5.render_queue = 2
question_btn5.z = -0.1

question_btn6 = Button(text='Почему я здесь?', color=color.gray, scale=(0.3, 0.07),
                      position=(0.1, 0.1), enabled=False, font='4205.otf')
question_btn6.text_entity.font = '4205.otf'
question_btn6.enabled = False
question_btn6.render_queue = 2
question_btn6.z = -0.1

question_btn7 = Button(text='Ты же тоже застрял здесь не так ли?', color=color.gray, scale=(0.3, 0.07),
                      position=(0.1, 0.0), enabled=False, font='4205.otf')
question_btn7.text_entity.font = '4205.otf'
question_btn7.enabled = False
question_btn7.render_queue = 2
question_btn7.z = -0.1

question_btn8 = Button(text='Тут есть опасность?', color=color.gray, scale=(0.3, 0.07),
                      position=(0.1, -0.1), enabled=False, font='4205.otf')
question_btn8.text_entity.font = '4205.otf'
question_btn8.enabled = False
question_btn8.render_queue = 2
question_btn8.z = -0.1

question_btn9 = Button(text='Куда мне идти?', color=color.gray, scale=(0.3, 0.07),
                      position=(0.1, -0.2), enabled=False, font='4205.otf')
question_btn9.text_entity.font = '4205.otf'
question_btn9.enabled = False
question_btn9.render_queue = 2
question_btn9.z = -0.1


girl_question_btn1 = Button(text='А ты целовалась?', color=color.gray, scale=(0.45, 0.07),
                           position=(-0.4, 0.2), enabled=False, font='4205.otf')
girl_question_btn1.text_entity.font = '4205.otf'
girl_question_btn1.enabled = False
girl_question_btn1.render_queue = 2
girl_question_btn1.z = -0.1

girl_question_btn2 = Button(text='Какое твое любимое блюдо?', color=color.gray, scale=(0.45, 0.07),
                           position=(-0.4, 0.1), enabled=False, font='4205.otf')
girl_question_btn2.text_entity.font = '4205.otf'
girl_question_btn2.enabled = False
girl_question_btn2.render_queue = 2
girl_question_btn2.z = -0.1

girl_question_btn3 = Button(text='.......', color=color.gray, scale=(0.45, 0.07),
                           position=(-0.4, 0.0), enabled=False, font='4205.otf')
girl_question_btn3.text_entity.font = '4205.otf'
girl_question_btn3.enabled = False
girl_question_btn3.render_queue = 2
girl_question_btn3.z = -0.1

# 3 отдельные кнопки вопросов для Bossa
bossa_question_btn1 = Button(text='Почему я здесь?', color=color.gray, scale=(0.45, 0.07),
                           position=(-0.4, 0.2), enabled=False, font='4205.otf')
bossa_question_btn1.text_entity.font = '4205.otf'
bossa_question_btn1.enabled = False
bossa_question_btn1.render_queue = 2
bossa_question_btn1.z = -0.1

bossa_question_btn2 = Button(text='Я не хочу выполнять эти дурацкие задания', color=color.gray, scale=(0.45, 0.07),
                           position=(-0.4, 0.1), enabled=False, font='4205.otf')
bossa_question_btn2.text_entity.font = '4205.otf'
bossa_question_btn2.enabled = False
bossa_question_btn2.render_queue = 2
bossa_question_btn2.z = -0.1

bossa_question_btn3 = Button(text='Если я выполню меня выпустят отсюда?', color=color.gray, scale=(0.45, 0.07),
                           position=(-0.4, 0.0), enabled=False, font='4205.otf')
bossa_question_btn3.text_entity.font = '4205.otf'
bossa_question_btn3.enabled = False
bossa_question_btn3.render_queue = 2
bossa_question_btn3.z = -0.1

# Кнопка "Назад"
back_btn = dont_care_button
back_btn.text = "Назад"
back_btn.position = (0.45, -0.1)
back_btn.scale = (0.2, 0.07)








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

rotation_speed = 480  # градусов в секунду Рулетка
hits = 0
attempts = 4

last_x_press_time = 0
x_cooldown = 0.2

enemy_portrait = None
player_battle_portrait = None
battle_background=None


enemy_hp_text = None
enemy_decorate=None
enemy_hp = 300

talk_button.render_queue = 2
dont_care_button.render_queue = 2
talk_button.z = -0.1
dont_care_button.z = -0.1
hit_text = None


player_hp = 150
player_stamina = 110
player_hp_text = None
player_stamina_text = None
blood_frame.render_queue = 3




# Добавьте в глобальные переменные
wave_effect_enabled = False
last_step_time = 0

thought_active = False
thought_text = ""
thought_progress = 0
thought_full_text = ""
thought_bg = None
thought_text_entity = None

#глобальные переменные для задания во сне
quest_active = False
quest_text_entity = None
quest_bg = None


# Добавляем глобальные переменные для системы перелетов
moon_interacted = False
current_moon_target = 0
moon_targets = [
    {"entity": Dream_house, "text": "Помнишь этот дом?", "offset": Vec3(10, 30, 0)},
    {"entity": Dream_house2, "text": "А это место тебе знакомо?", "offset": Vec3(0, 25, 0)},
    {"entity": Dream_house3, "text": "Здесь было так весело...", "offset": Vec3(0, 20, 0)},
    {"entity": Dream_house4, "text": "Пора прощаться...", "offset": Vec3(0, 15, 0)},
    {"entity": Dream_house5, "text": "Возвращайся домой...", "offset": Vec3(0, 10, 0)}]








class PygameSoundManager:
    def __init__(self):
        pygame.mixer.init()
        self.battle_active = False
        self.background_active = False
        self.bossa_active = False
        self.bossa_battle_active = False
        self.tonight_active = False
        self.dream_active = False
        self.battle_sound_thread = None
        self.background_sound_thread = None
        self.bossa_sound_thread = None
        self.bossa_battle_sound_thread = None
        self.tonight_sound_thread = None
        self.dream_sound_thread = None


        self.battle_channel = pygame.mixer.Channel(0)
        self.background_channel = pygame.mixer.Channel(1)
        self.bossa_channel = pygame.mixer.Channel(2)
        self.bossa_battle_channel = pygame.mixer.Channel(3)
        self.tonight_channel = pygame.mixer.Channel(4)
        self.dream_channel = pygame.mixer.Channel(5)

        self.battle_sound = None
        self.background_sound = None
        self.bossa_sound = None
        self.bossa_battle_sound = None
        self.tonight_sound = None
        self.dream_sound = None


        self.battle_volume = 0.5
        self.background_volume = 0.7
        self.bossa_volume = 0.6
        self.bossa_battle_volume = 0.8
        self.tonight_volume = 0.7
        self.dream_volume = 0.8

    def play_background_sound(self):

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

    # НОВЫЙ МЕТОД: Запуск музыки Dream.mp3
    def play_dream_sound(self):
        """Запускает музыку Dream.mp3"""
        self.stop_dream_sound()
        self.dream_active = True

        def dream_loop():
            try:
                self.dream_sound = pygame.mixer.Sound('Dream.mp3')
                self.dream_channel.set_volume(self.dream_volume)
                while self.dream_active:
                    if not self.dream_channel.get_busy():
                        self.dream_channel.play(self.dream_sound)
                    time.sleep(0.5)
            except Exception as e:
                print(f"Dream sound error: {e}")

        self.dream_sound_thread = threading.Thread(target=dream_loop, daemon=True)
        self.dream_sound_thread.start()
        print(f"💭 Pygame dream sound started (volume: {self.dream_volume})")

    # НОВЫЙ МЕТОД: Остановка музыки Dream.mp3
    def stop_dream_sound(self):
        """Останавливает музыку Dream.mp3"""
        self.dream_active = False
        self.dream_channel.stop()
        print("🔇 Pygame dream sound stopped")

    # НОВЫЙ МЕТОД: Управление громкостью Dream.mp3
    def set_dream_volume(self, volume):
        """Устанавливает громкость Dream.mp3 (0.0 - 1.0)"""
        if 0.0 <= volume <= 1.0:
            self.dream_volume = volume
            self.dream_channel.set_volume(volume)
            print(f"🔊 Dream volume set to: {volume}")
        else:
            print("❌ Volume must be between 0.0 and 1.0")

    def get_dream_volume(self):
        """Возвращает текущую громкость Dream.mp3"""
        return self.dream_volume

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

    def play_bossa_battle_sound(self):
        """Запускает музыку для боя с боссом bossa_battle.wav"""
        self.stop_bossa_battle_sound()  # Останавливаем предыдущую музыку
        self.stop_battle_sound()  # Останавливаем обычную музыку битвы
        self.bossa_battle_active = True

        def bossa_battle_loop():
            try:
                self.bossa_battle_sound = pygame.mixer.Sound('bossa_battle.wav')
                self.bossa_battle_channel.set_volume(self.bossa_battle_volume)
                while self.bossa_battle_active:
                    if not self.bossa_battle_channel.get_busy():
                        self.bossa_battle_channel.play(self.bossa_battle_sound)
                    time.sleep(0.5)
            except Exception as e:
                print(f"Bossa battle sound error: {e}")
                # Если файл не найден, используем обычную музыку битвы
                self.play_battle_sound()

        self.bossa_battle_sound_thread = threading.Thread(target=bossa_battle_loop, daemon=True)
        self.bossa_battle_sound_thread.start()
        print(f"👑 Pygame bossa battle sound started (volume: {self.bossa_battle_volume})")

    def stop_bossa_battle_sound(self):
        """Останавливает музыку боя с боссом"""
        self.bossa_battle_active = False
        self.bossa_battle_channel.stop()
        print("🔇 Pygame bossa battle sound stopped")

    # НОВЫЙ МЕТОД: Управление громкостью музыки босса в битве
    def set_bossa_battle_volume(self, volume):
        """Устанавливает громкость музыки босса в битве (0.0 - 1.0)"""
        if 0.0 <= volume <= 1.0:
            self.bossa_battle_volume = volume
            self.bossa_battle_channel.set_volume(volume)
            print(f"🔊 Bossa battle volume set to: {volume}")
        else:
            print("❌ Volume must be between 0.0 and 1.0")

    def get_bossa_battle_volume(self):
        """Возвращает текущую громкость музыки босса в битве"""
        return self.bossa_battle_volume

    def play_tonight_sound(self):
        """Запускает музыку tonight.mp3"""
        self.stop_tonight_sound()
        self.tonight_active = True

        def tonight_loop():
            try:
                self.tonight_sound = pygame.mixer.Sound('tonight.mp3')
                self.tonight_channel.set_volume(self.tonight_volume)
                while self.tonight_active:
                    if not self.tonight_channel.get_busy():
                        self.tonight_channel.play(self.tonight_sound)
                    time.sleep(0.5)
            except Exception as e:
                print(f"Tonight sound error: {e}")

        self.tonight_sound_thread = threading.Thread(target=tonight_loop, daemon=True)
        self.tonight_sound_thread.start()
        print(f"🌙 Pygame tonight sound started (volume: {self.tonight_volume})")

    def stop_tonight_sound(self):
        """Останавливает музыку tonight.mp3"""
        self.tonight_active = False
        self.tonight_channel.stop()
        print("🔇 Pygame tonight sound stopped")

    # НОВЫЙ МЕТОД: Управление громкостью tonight.mp3
    def set_tonight_volume(self, volume):
        """Устанавливает громкость tonight.mp3 (0.0 - 1.0)"""
        if 0.0 <= volume <= 1.0:
            self.tonight_volume = volume
            self.tonight_channel.set_volume(volume)
            print(f"🔊 Tonight volume set to: {volume}")
        else:
            print("❌ Volume must be between 0.0 and 1.0")

    def get_tonight_volume(self):
        """Возвращает текущую громкость tonight.mp3"""
        return self.tonight_volume

    # Обновляем метод остановки всех звуков
    def stop_all_sounds(self):
        """Останавливает все звуки"""
        self.stop_background_sound()
        self.stop_battle_sound()
        self.stop_bossa_sound()
        self.stop_bossa_battle_sound()
        self.stop_tonight_sound()
        self.stop_dream_sound()  # НОВОЕ: останавливаем Dream.mp3
        print("🔇 All pygame sounds stopped")

    # Обновляем пресеты громкости с добавлением Dream.mp3
    def set_volume_preset(self, preset_name):
        """Устанавливает громкость по пресету для всех звуков"""
        presets = {
            'normal': {'background': 0.5, 'battle': 0.7, 'bossa': 0.6, 'bossa_battle': 0.8, 'tonight': 0.7, 'dream': 0.8},
            'quiet': {'background': 0.3, 'battle': 0.4, 'bossa': 0.3, 'bossa_battle': 0.5, 'tonight': 0.4, 'dream': 0.5},
            'loud': {'background': 0.8, 'battle': 0.9, 'bossa': 0.8, 'bossa_battle': 1.0, 'tonight': 0.9, 'dream': 1.0},
            'menu': {'background': 0.2, 'battle': 0.0, 'bossa': 0.4, 'bossa_battle': 0.0, 'tonight': 0.5, 'dream': 0.6},
            'battle_focus': {'background': 0.3, 'battle': 0.8, 'bossa': 0.0, 'bossa_battle': 0.0, 'tonight': 0.0, 'dream': 0.0},
            'boss_focus': {'background': 0.2, 'battle': 0.0, 'bossa': 0.0, 'bossa_battle': 0.9, 'tonight': 0.0, 'dream': 0.0},
            'exploration': {'background': 0.6, 'battle': 0.0, 'bossa': 0.5, 'bossa_battle': 0.0, 'tonight': 0.0, 'dream': 0.0},
            'bossa_only': {'background': 0.0, 'battle': 0.0, 'bossa': 0.7, 'bossa_battle': 0.0, 'tonight': 0.0, 'dream': 0.0},
            'tonight_only': {'background': 0.0, 'battle': 0.0, 'bossa': 0.0, 'bossa_battle': 0.0, 'tonight': 0.8, 'dream': 0.0},
            'dream_only': {'background': 0.0, 'battle': 0.0, 'bossa': 0.0, 'bossa_battle': 0.0, 'tonight': 0.0, 'dream': 0.9},  # НОВЫЙ пресет
            'relaxed': {'background': 0.4, 'battle': 0.0, 'bossa': 0.6, 'bossa_battle': 0.0, 'tonight': 0.0, 'dream': 0.0},
            'romantic': {'background': 0.3, 'battle': 0.0, 'bossa': 0.4, 'bossa_battle': 0.0, 'tonight': 0.6, 'dream': 0.0},
            'mystical': {'background': 0.2, 'battle': 0.0, 'bossa': 0.0, 'bossa_battle': 0.0, 'tonight': 0.0, 'dream': 0.8}  # НОВЫЙ пресет
        }

        if preset_name in presets:
            bg_vol = presets[preset_name]['background']
            battle_vol = presets[preset_name]['battle']
            bossa_vol = presets[preset_name]['bossa']
            bossa_battle_vol = presets[preset_name]['bossa_battle']
            tonight_vol = presets[preset_name]['tonight']
            dream_vol = presets[preset_name]['dream']  # НОВОЕ

            self.set_background_volume(bg_vol)
            self.set_battle_volume(battle_vol)
            self.set_bossa_volume(bossa_vol)
            self.set_bossa_battle_volume(bossa_battle_vol)
            self.set_tonight_volume(tonight_vol)
            self.set_dream_volume(dream_vol)  # НОВОЕ
            print(f"🔊 Preset '{preset_name}' applied")

    # Обновляем метод запуска звука по имени
    def play_sound_by_name(self, sound_name):
        """Запускает звук по имени"""
        if sound_name == 'background':
            self.play_background_sound()
        elif sound_name == 'battle':
            self.play_battle_sound()
        elif sound_name == 'bossa':
            self.play_bossa_sound()
        elif sound_name == 'bossa_battle':
            self.play_bossa_battle_sound()
        elif sound_name == 'tonight':
            self.play_tonight_sound()
        elif sound_name == 'dream':  # НОВОЕ
            self.play_dream_sound()
        else:
            print(f"❌ Unknown sound: {sound_name}")

    # Обновляем метод остановки звука по имени
    def stop_sound_by_name(self, sound_name):
        """Останавливает звук по имени"""
        if sound_name == 'background':
            self.stop_background_sound()
        elif sound_name == 'battle':
            self.stop_battle_sound()
        elif sound_name == 'bossa':
            self.stop_bossa_sound()
        elif sound_name == 'bossa_battle':
            self.stop_bossa_battle_sound()
        elif sound_name == 'tonight':
            self.stop_tonight_sound()
        elif sound_name == 'dream':  # НОВОЕ
            self.stop_dream_sound()
        else:
            print(f"❌ Unknown sound: {sound_name}")

    # НОВЫЙ МЕТОД: Быстрое переключение на Dream.mp3
    def switch_to_dream(self):
        """Переключает на музыку Dream.mp3 (останавливает все остальные)"""
        self.stop_all_sounds()
        self.play_dream_sound()
        print("🔄 Переключено на Dream.mp3")

    def switch_to_tonight(self):
        """Переключает на музыку tonight.mp3 (останавливает все остальные)"""
        self.stop_all_sounds()
        self.play_tonight_sound()
        print("🔄 Переключено на tonight.mp3")

    def switch_to_background(self):
        """Переключает на фоновую музыку (останавливает все остальные)"""
        self.stop_all_sounds()
        self.play_background_sound()
        print("🔄 Переключено на фоновую музыку")

# Используйте этот менеджер вместо Ursina Audio
sound_manager = PygameSoundManager()
sound_manager.play_background_sound()


def take_quest_action():
    global full_text, current_text, text_progress


    take_quest_btn.enabled = False
    button1.enabled = False
    button2.enabled = False

    # Текст задания
    full_text = "Отлично! Вот твое задание: победи 3 врагов в лесу и вернись ко мне."
    current_text = ""
    text_progress = 0


    scene.text_printing_active = True


    def check_text_completion():
        if in_dialogue and not scene.text_printing_active:
            print("✅ Текст завершен - закрываем диалог")
            close_dialogue()
            collider_door2.position = (7, 11, 11.4)
        else:
            # Если текст еще печатается, проверяем снова через 0.1 секунду
            invoke(check_text_completion, delay=0.01)

    # Начинаем проверку через 3 секунды (время показа текста)
    invoke(check_text_completion, delay=3)

    # После завершения текста показываем кнопки снова
    def show_buttons_after_quest():
        if in_dialogue and not scene.text_printing_active:
            # Для Bossa показываем специальные кнопки
            take_quest_btn.enabled = True
            button1.enabled = True
            button2.enabled = True

    invoke(show_buttons_after_quest, delay=3)



def show_ordinary_questions():


    hide_all_question_buttons()


    if npc_name.text == "Человек 1":
        # Первые 3 кнопки для Человека 1
        question_btn1.enabled = True
        question_btn2.enabled = True
        question_btn3.enabled = True
    elif npc_name.text == "Человек 2":
        # Следующие 3 кнопки для Человека 2
        question_btn4.enabled = True
        question_btn5.enabled = True
        question_btn6.enabled = True
    elif npc_name.text == "Человек 3":
        # Последние 3 кнопки для Человека 3
        question_btn7.enabled = True
        question_btn8.enabled = True
        question_btn9.enabled = True



    back_btn.enabled = True
    back_btn.on_click = back_to_dialogue
    print(f"🔍 Показаны вопросы для {npc_name.text}, обработчик 'Назад' назначен")

# Функция для показа вопросов для Bossa
def show_bossa_questions():

    print("👑 show_bossa_questions() ВЫЗВАНА - начинаем показ вопросов")


    take_quest_btn.enabled = False
    button1.enabled = False
    button2.enabled = False
    button3.enabled = False


    bossa_question_btn1.enabled = True
    bossa_question_btn2.enabled = True
    bossa_question_btn3.enabled = True


    back_btn.enabled = True
    back_btn.on_click = back_to_dialogue

    print("👑 Вопросы для Bossa показаны! Основные кнопки скрыты.")


def show_girl_questions():

    print("👧 show_girl_questions() ВЫЗВАНА")


    button1.enabled = False
    button2.enabled = False
    button3.enabled = False
    take_quest_btn.enabled = False


    girl_question_btn1.enabled = True
    girl_question_btn2.enabled = True
    girl_question_btn3.enabled = True


    back_btn.enabled = True
    back_btn.on_click = back_to_dialogue_girl

    print("👧 Вопросы для Girl показаны! girl_question_btn1.enabled =", girl_question_btn1.enabled)


    def show_questions_after_delay():

        girl_question_btn1.enabled = True
        girl_question_btn2.enabled = True
        girl_question_btn3.enabled = True


        back_btn.enabled = True
        back_btn.on_click = back_to_dialogue_girl
        print("👧 Вопросы для Girl показаны!")

    invoke(show_questions_after_delay, delay=0.1)


def back_to_dialogue_bossa():

    print("🔙 Кнопка НАЗАД нажата для Bossa - возвращаемся к основным кнопкам")


    hide_all_question_buttons()

    # Возвращаем портреты в исходное положение (NPC говорит)
    character_portrait.animate_y(-0.1, duration=0.5, curve=curve.out_cubic)
    main_character_portrait.animate_y(-0.3, duration=0.5, curve=curve.out_cubic)


    take_quest_btn.enabled = True
    button1.enabled = True
    button2.enabled = True
    button3.enabled = False


    back_btn.enabled = False

    print("✅ Выход из вопросов - показаны основные кнопки для Bossa: Взять задание, Поговорить, Напасть")

def back_to_dialogue_girl():

    print("🔙 Кнопка НАЗАД нажата для Girl - возвращаемся к основным кнопкам")


    hide_all_question_buttons()

    # Возвращаем портреты в исходное положение (NPC говорит)
    character_portrait.animate_y(-0.1, duration=0.5, curve=curve.out_cubic)
    main_character_portrait.animate_y(-0.3, duration=0.5, curve=curve.out_cubic)


    button1.enabled = True
    button2.enabled = True
    button3.enabled = True
    take_quest_btn.enabled = False


    back_btn.enabled = False

    print("✅ Показаны основные кнопки для Girl: Поговорить, Напасть, Уйти")

def girl_question1_action():
    answer_question("У меня еще этого небыло")

def girl_question2_action():
    answer_question("Отбивная :)")

def girl_question3_action():
    answer_question('.......')



def question1_action():
    answer_question("Конечно,на часах сейчас ??NuLl часов и ??Null fминут\n\nсамое время заняться своими обыденными делами!")


def question2_action():
    answer_question("Ну как что,конечно же я тут стою и еще стою и еще стою и еще стою........")


def question3_action():
    answer_question("Всмысле что это за место? Это великий $%^#$%^&^%#$%^&*(*^ \nСамое красивое место во всей вселенной!\nЛюди здесь всегда счастливы!\nНикто никогда не болеет Нету войн Нету голода!\nЛюди здесь всегда счастливы!\nЛюди здесь всегда счастливы!")



def question4_action():
    answer_question("Зачем? Это место создано специально для нас,здесь мы в безопасности!")


def question5_action():
    answer_question("Я human_collidera=Entity(parent=humana,model='cube',position=(38,1,3.8)\n\nscale=(1,2,1),color=color.clear,collider='box')\n\nА тебя как зовут?")


def question6_action():
    answer_question("Ты здесь потому-что пожелал попасть сюда,вот и вся причина!")


def question7_action():
    answer_question("Застрял где? Не Pрипомню чтобы я был где-тO заточен,\n\nMеня тут никтO не держит!\n\nЕсли я захочу то моGу просто уйтI!")


def question8_action():
    answer_question("Будь осторожен в лесу - там водятся волки.")


def question9_action():
    answer_question("В офисе в конце улицы лучший эль в округе.")

def question10_action():
    answer_question("У меня еще этого небыло")

def question11_action():
     answer_question("Отбивная :)")

def question12_action():
    answer_question('.......')



def bossa_question1_action():
    answer_question("......................")


def bossa_question2_action():
    answer_question("Ты должен его выполнить,у тебя просто нет выбора")


def bossa_question3_action():
    answer_question(".....................")



def answer_question(answer_text):
    global full_text, current_text, text_progress

    print(f"🔍 answer_question() вызвана для NPC: {npc_name.text}")


    hide_all_question_buttons()

    # Анимация: NPC поднимается (говорит), игрок опускается
    character_portrait.animate_y(-0.1, duration=0.5, curve=curve.out_cubic)
    main_character_portrait.animate_y(-0.3, duration=0.5, curve=curve.out_cubic)


    full_text = answer_text
    current_text = ""
    text_progress = 0
    scene.text_printing_active = True

    # После ответа ВОЗВРАЩАЕМСЯ К ВОПРОСАМ
    def return_to_questions():
        print(
            f"🔍 return_to_questions() вызвана, in_dialogue={in_dialogue}, text_printing_active={scene.text_printing_active}")

        if in_dialogue and not scene.text_printing_active:
            print("✅ Условие выполнено - возвращаемся к вопросам")

            # Возвращаем портреты в исходное положение
            character_portrait.animate_y(-0.1, duration=0.5, curve=curve.out_cubic)
            main_character_portrait.animate_y(-0.3, duration=0.5, curve=curve.out_cubic)

            # ВОЗВРАЩАЕМ К ВОПРОСАМ
            if npc_name.text == "Босс":
                print("🔄 Показываем вопросы Bossa")
                show_bossa_questions()
            elif npc_name.text == 'Girl':
                print("🔄 Показываем вопросы Girl")
                show_girl_questions()
            else:
                print("🔄 Показываем обычные вопросы")
                show_ordinary_questions()
        else:
            print(f"❌ Условие не выполнено, проверяем снова...")
            invoke(return_to_questions, delay=0.5)

    invoke(return_to_questions, delay=0.1)


def hide_all_question_buttons():

    question_btn1.enabled = False
    question_btn2.enabled = False
    question_btn3.enabled = False
    question_btn4.enabled = False
    question_btn5.enabled = False
    question_btn6.enabled = False
    question_btn7.enabled = False
    question_btn8.enabled = False
    question_btn9.enabled = False


    bossa_question_btn1.enabled = False
    bossa_question_btn2.enabled = False
    bossa_question_btn3.enabled = False


    girl_question_btn1.enabled = False
    girl_question_btn2.enabled = False
    girl_question_btn3.enabled = False


    back_btn.enabled = False


def back_to_dialogue():
    print("🔙 Кнопка НАЗАД нажата - скрываем все вопросы")


    hide_all_question_buttons()

    # Возвращаем портреты в исходное положение (NPC говорит)
    character_portrait.animate_y(-0.1, duration=0.5, curve=curve.out_cubic)
    main_character_portrait.animate_y(-0.3, duration=0.5, curve=curve.out_cubic)


    if npc_name.text == "Босс":
        take_quest_btn.enabled = True
        button1.enabled = True
        button2.enabled = True
        button3.enabled = False
        print("✅ Показаны кнопки Bossa: Взять задание, Поговорить, Напасть")
    elif npc_name.text == "Girl":

        back_to_dialogue_girl()

        print("✅ Показаны кнопки Girl: Поговорить, Напасть, Уйти")
    else:
        button1.enabled = True
        button2.enabled = True
        button3.enabled = True
        take_quest_btn.enabled = False
        print("✅ Показаны обычные кнопки: Поговорить, Напасть, Уйти")



back_btn.on_click = back_to_dialogue



question_btn1.on_click = question1_action
question_btn2.on_click = question2_action
question_btn3.on_click = question3_action
question_btn4.on_click = question4_action
question_btn5.on_click = question5_action
question_btn6.on_click = question6_action
question_btn7.on_click = question7_action
question_btn8.on_click = question8_action
question_btn9.on_click = question9_action

girl_question_btn1.on_click = girl_question1_action
girl_question_btn2.on_click = girl_question2_action
girl_question_btn3.on_click = girl_question3_action

bossa_question_btn1.on_click = bossa_question1_action
bossa_question_btn2.on_click = bossa_question2_action
bossa_question_btn3.on_click = bossa_question3_action

back_btn.on_click = back_to_dialogue







def start_dialogue(npc_name_text, npc_line_text):
    global in_dialogue, current_text, text_progress, full_text, dialogue_stage, active_speaker

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
    dialogue_bg.scale_x = 0.1
    dialogue_bg.scale_y = 0.1
    dialogue_bg.enabled = True
    dialogue_bg.color = color.black66


    if npc_name_text == "Босс":
        character_portrait.texture = 'bossa.png'

        take_quest_btn.enabled = False  # Покажем после текста
        button1.enabled = False
        button2.enabled = False
        button3.enabled = False
        take_quest_btn.enabled = False
    elif npc_name_text == 'Girl':
        character_portrait.texture= 'Girl1.png'
        button1.enabled = False
        button2.enabled = False
        button3.enabled = False
        take_quest_btn.enabled = False

    else:
        character_portrait.texture = 'person1.png'

        button1.enabled = False
        button2.enabled = False
        button3.enabled = False
        take_quest_btn.enabled = False

    character_portrait.enabled = True
    main_character_portrait.enabled = True

    character_portrait.y = -0.3
    main_character_portrait.y = -0.3
    character_portrait.color = color.rgba(255, 255, 255, 0)
    main_character_portrait.color = color.rgba(255, 255, 255, 0)

    npc_name.enabled = False
    npc_line.enabled = False
    npc_line.text = " "

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
    vhs_overlay.enabled = False

    if hasattr(scene, 'text_printing_active') and scene.text_printing_active:
        if text_progress < len(full_text):
            text_progress = min(text_progress + text_speed * time.dt, len(full_text))
            current_text = full_text[:int(text_progress)]
            npc_line.text = current_text

            if not text_sound.playing:
                text_sound.play()
        else:
            print(f"📝 Текст завершен! text_progress={text_progress}, len(full_text)={len(full_text)}")
            scene.text_printing_active = False
            text_sound.stop()
            print(f"📝 text_printing_active установлен в: {scene.text_printing_active}")

            # ПОКАЗЫВАЕМ КНОПКИ ПОСЛЕ ЗАВЕРШЕНИЯ ТЕКСТА
            if battle_active:
                pass
            elif npc_name.text == "Босс" and dialogue_stage == 1:  # ТОЛЬКО начальный диалог
                take_quest_btn.enabled = True
                button1.enabled = True
                button2.enabled = True
                button3.enabled = False
                print("👑 Показаны начальные кнопки для Босса")
            elif npc_name.text == "Girl" and dialogue_stage == 1:  # ТОЛЬКО начальный диалог
                button1.enabled = True
                button2.enabled = True
                button3.enabled = True
                take_quest_btn.enabled = False
                print("👧 Показаны начальные кнопки для Girl: Поговорить, Напасть, Уйти")
            elif npc_name.text != "Girl" and dialogue_stage == 1:  # Для обычных NPC
                button1.enabled = True
                button2.enabled = True
                button3.enabled = True
                take_quest_btn.enabled = False
            # НЕ показываем кнопки когда dialogue_stage == 2 (режим вопросов)

def setup_conversation_buttons():
    global full_text, current_text, text_progress, dialogue_stage, active_speaker
    print(f"🔧 setup_conversation_buttons() вызвана для NPC: {npc_name.text}")

    # Гарантируем что кнопка "Поболтать" скрыта
    talk_button.enabled = False

    # Если это Bossa, показываем вопросы для Bossa
    if npc_name.text == "Босс":
        dialogue_stage = 2
        active_speaker = "equal"

        # Скрываем основные кнопки диалога
        take_quest_btn.enabled = False
        button1.enabled = False
        button2.enabled = False
        button3.enabled = False

        # Устанавливаем текст "Ну давай поговорим"
        full_text = "Ну давай поговорим"
        current_text = ""
        text_progress = 0
        scene.text_printing_active = True

        # После текста показываем вопросы для Bossa
        def show_bossa_questions_after_text():
            if in_dialogue and not scene.text_printing_active:
                show_bossa_questions()

        invoke(show_bossa_questions_after_text, delay=2)

        # Анимация портретов
        character_portrait.animate_y(-0.2, duration=0.8, curve=curve.out_cubic)
        main_character_portrait.animate_y(-0.2, duration=0.8, curve=curve.out_cubic)



    elif npc_name.text == 'Girl':

        print("🎯 Обрабатываем Girl в setup_conversation_buttons()")

        dialogue_stage = 2

        active_speaker = "equal"

        # Скрываем основные кнопки диалога

        button1.enabled = False

        button2.enabled = False

        button3.enabled = False

        take_quest_btn.enabled = False

        # Устанавливаем текст для Girl

        full_text = "Хорошо :) давай поговорим)!!"

        current_text = ""

        text_progress = 0

        scene.text_printing_active = True

        # Ждем завершения текста с проверкой

        def wait_for_text_completion():

            if in_dialogue and not scene.text_printing_active:

                print("✅ Текст завершен - показываем вопросы для Girl")

                show_girl_questions()

            else:

                # Если текст еще печатается, проверяем снова через 0.5 секунды

                print("⏳ Текст еще печатается, проверяем снова...")

                invoke(wait_for_text_completion, delay=0.5)

        # Начинаем проверку через 3 секунды (достаточное время для текста)

        invoke(wait_for_text_completion, delay=3.0)

        # Анимация портретов

        character_portrait.animate_y(-0.2, duration=0.8, curve=curve.out_cubic)

        main_character_portrait.animate_y(-0.2, duration=0.8, curve=curve.out_cubic)

    else:
        # Для обычных NPC показываем вопросы
        dialogue_stage = 2
        active_speaker = "equal"

        # Скрываем основные кнопки диалога
        button1.enabled = False
        button2.enabled = False
        button3.enabled = False
        take_quest_btn.enabled = False

        # Устанавливаем текст "Ну давай поговорим"
        full_text = "Ну давай поговорим"
        current_text = ""
        text_progress = 0
        scene.text_printing_active = True

        # После текста показываем вопросы для обычных NPC
        def show_ordinary_questions_after_text():
            if in_dialogue and not scene.text_printing_active:
                show_ordinary_questions()

        invoke(show_ordinary_questions_after_text, delay=2)

        # Анимация портретов
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
    global enemy_portrait, player_battle_portrait, enemy_hp_text, enemy_hp, battle_background, enemy_decorate
    global player_hp_text, player_stamina_text, player_stamina,blood_frame,player_hp

    def finish_close():
        global in_dialogue, battle_active, enemy_hp
        global enemy_portrait, player_battle_portrait, enemy_hp_text, battle_background, enemy_decorate
        global player_hp_text, player_stamina_text, player_stamina,blood_frame,player_hp

        sound_manager.stop_battle_sound()
        sound_manager.stop_bossa_battle_sound()
        if battle2_sound.playing:
            battle2_sound.stop()
        if battle_reaction_sound.playing:
            battle_reaction_sound.stop()
        sound_manager.set_background_volume(1)
        vhs_overlay.enabled = True
        dialogue_bg.enabled = False
        npc_name.enabled = False
        npc_line.enabled = False
        player.enabled = True
        dark_overlay.enabled = False
        character_portrait.enabled = False
        main_character_portrait.enabled = False
        enemy_decorate = False
        battle_background = False
        in_dialogue = False
        battle_active = False

        # Скрываем все кнопки
        button1.enabled = False
        button2.enabled = False
        button3.enabled = False
        talk_button.enabled = False
        dont_care_button.enabled = False
        take_quest_btn.enabled = False
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
        if player_hp_text:
            destroy(player_hp_text)
            player_hp_text = None
        if player_stamina_text:
            destroy(player_stamina_text)
            player_stamina_text = None
        if battle_background:
            destroy(battle_background)
            battle_background = None
        if enemy_decorate:
            destroy(enemy_decorate)
            enemy_decorate = None
        if blood_frame:
            blood_frame.alpha = 0

        # Сбрасываем HP врага и стамину игрока
        enemy_hp = 300
        player_stamina = 110
        player_hp=150

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

        # Проверяем наличие enemy_decorate
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
        take_quest_btn.enabled = False  # НОВОЕ: скрываем кнопку взятия задания
        invoke(finish_close, delay=0.9)

    animate_close()

# Добавляем обработчик для новой кнопки
take_quest_btn.on_click = take_quest_action



battle_active = False



def start_battle():
    global battle_active, full_text, current_text, text_progress, enemy_portrait, player_battle_portrait, enemy_hp_text,battle_background,\
        enemy_decorate

    battle_active = True
    sound_manager.stop_background_sound()
    sound_manager.stop_bossa_sound()
    if not battle_reaction_sound.playing:
        battle_reaction_sound.play()
    button1.enabled = False
    button2.enabled = False
    button3.enabled = False
    take_quest_btn.enabled=False

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
    global enemy_portrait, player_battle_portrait, enemy_hp_text, battle_background, enemy_decorate,enemy_hp
    global player_hp_text, player_stamina_text, blood_frame

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
    # Определяем тип врага (обычный или босс)
    # -----------------------------
    is_bossa_battle = (npc_name.text == "Босс")

    if is_bossa_battle:
        # НАСТРОЙКИ ДЛЯ БОССА
        enemy_texture = 'bossa_battle.png'  # портрет босса в бою
        enemy_decorate_texture = 'bossa_decorate.png'  # большой фон босса
        battle_back_texture = 'battleback2.jpg'  # фон битвы с боссом
        player_battle_portrait='personemeny2.jpg'
        enemy_decorate_scale=1.5
        enemy_hp = 500  # больше HP у босса
        print("⚔️ Битва с БОССОМ!")
    else:
        # НАСТРОЙКИ ДЛЯ ОБЫЧНОГО ВРАГА
        enemy_texture = 'enemy1.png'
        enemy_decorate_texture = 'enemy_decorate1.png'
        battle_back_texture = 'battleback1.png'
        enemy_decorate_scale=(0.6,0.6)
        player_battle_portrait = 'personemeny.png'
        enemy_hp = 300
        print("⚔️ Битва с обычным врагом")

    # -----------------------------
    # Портрет игрока
    # -----------------------------
    player_battle_portrait = Entity(
        parent=camera.ui,
        model='quad',
        texture=player_battle_portrait,
        scale=(0.30, 0.30),
        x=-0.61,
        y=-0.38
    )
    player_battle_portrait.color = color.rgba(1, 1, 1, 0)
    player_battle_portrait.animate_color(color.white, duration=1.0, delay=0.5)

    # -----------------------------
    # Текст HP игрока (слева)
    # -----------------------------
    player_hp_text = Text(
        parent=camera.ui,
        text=f"HP: {player_hp}",
        position=(-0.7, 0),
        scale=1.3,
        color=color.green,
        font='4205.otf'
    )
    player_hp_text.enabled = True

    # -----------------------------
    # Текст стамины игрока (слева)
    # -----------------------------
    player_stamina_text = Text(
        parent=camera.ui,
        text=f"Stamina: {player_stamina}",
        position=(-0.7, -0.1),
        scale=1.3,
        color=color.blue,
        font='4205.otf'
    )
    player_stamina_text.enabled = True

    # -----------------------------
    # Портрет врага (разный для босса и обычного врага)
    # -----------------------------
    enemy_portrait = Entity(
        parent=camera.ui,
        model='quad',
        texture=enemy_texture,
        scale=(0.3, 0.3),
        x=0.61,
        y=-0.38
    )
    enemy_portrait.color = color.rgba(1, 1, 1, 0)
    enemy_portrait.animate_color(color.white, duration=1.0, delay=0.5)

    # -----------------------------
    # Текст HP врага (справа)
    # -----------------------------
    enemy_hp_text = Text(
        parent=camera.ui,
        text=f"HP: {enemy_hp}",
        position=(0.7, -0.1),
        scale=1.3,
        color=color.red,
        font='4205.otf'
    )
    enemy_hp_text.enabled = True

    # -----------------------------
    # Декоративный враг на фоне (разный для босса)
    # -----------------------------
    enemy_decorate = Entity(
        parent=camera.ui,
        model='quad',
        texture=enemy_decorate_texture,
        scale=enemy_decorate_scale,
        x=0,
        y=0.1,
        z=0
    )
    enemy_decorate.color = color.rgba(1, 1, 1, 0)
    enemy_decorate.animate_color(color.white, duration=1.0, delay=0.5)

    # -----------------------------
    # Фон битвы (разный для босса)
    # -----------------------------
    battle_background = Entity(
        parent=camera.ui,
        model='quad',
        texture=battle_back_texture,
        scale=(2, 1),
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
        if is_bossa_battle:

            sound_manager.play_bossa_battle_sound()
            print("🎵 Запущена музыка босса в битве!")
        else:

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


def update_blood_frame():
    """Обновляет прозрачность кровавой рамки в зависимости от HP"""
    global blood_frame, player_hp

    if blood_frame and player_hp < 150:
        # Рассчитываем прозрачность в зависимости от HP
        if player_hp <= 50:
            # 20 HP или меньше - максимальная видимость
            blood_frame.alpha = 1
            blood_frame.color = color.rgb(0.8, 0, 0)  # Ярко-красный
        elif player_hp <= 100:
            # 70 HP или меньше - средняя видимость
            blood_frame.alpha = 0.6
            blood_frame.color = color.rgb(0.6, 0, 0)  # Средне-красный
        else:
            # Меньше 100 HP - минимальная видимость
            blood_frame.alpha = 0.01
            blood_frame.color = color.rgb(0.3, 0, 0)  # Темно-красный
    elif blood_frame and player_hp >= 150:
        # Если HP восстановилось до 100 или больше - скрываем рамку
        blood_frame.alpha = 0

def weak_attack_action():
    """Слабая атака - запускаем мини-игру с прямоугольником"""
    global battle_active, player_stamina, player_hp

    # Проверяем достаточно ли стамины
    if player_stamina < 30:
        print(" Недостаточно стамины для слабой атаки!")
        enemy_counter_attack()  # Враг контратакует
        return

    weak_attack_btn.enabled = False
    strong_attack_btn.enabled = False
    surrender_btn.enabled = False
    take_quest_btn.enabled=False

    # Тратим стамину
    player_stamina -= 30
    if player_stamina_text:
        player_stamina_text.text = f"Stamina: {player_stamina}"
    invoke(update_blood_frame, delay=0.1)

    def animate_dialogue_down():
        dialogue_bg.animate_y(-1.0, duration=0.8, curve=curve.in_quad)

        if player_battle_portrait:
            player_battle_portrait.animate_y(-1.0, duration=0.8, curve=curve.in_quad)

        if enemy_portrait:
            enemy_portrait.animate_y(-1.0, duration=0.8, curve=curve.in_quad)

        if enemy_hp_text:
            enemy_hp_text.animate_y(-1, duration=0.8, curve=curve.in_quad)
        if player_hp_text:
            player_hp_text.animate_y(-1,duration=0.8, curve=curve.in_quad)
        if player_stamina_text:
            player_stamina_text.animate_y(-1,duration=0.8, curve=curve.in_quad)

        invoke(start_weak_attack_minigame, delay=0.9)

    animate_dialogue_down()
    print("⚔️ Слабая атака! -30 стамины")

def strong_attack_action():
    """Сильная атака - запускаем мини-игру с анимацией"""
    global battle_active, dialogue_bg, player_battle_portrait, enemy_portrait, enemy_hp_text, battle_background, player_stamina, player_hp

    # Проверяем достаточно ли стамины
    if player_stamina < 50:
        print("❌ Недостаточно стамины для сильной атаки!")
        enemy_counter_attack()  # Враг контратакует
        return

    weak_attack_btn.enabled = False
    strong_attack_btn.enabled = False
    surrender_btn.enabled = False

    # Тратим стамину
    player_stamina -= 50
    if player_stamina_text:
        player_stamina_text.text = f"Stamina: {player_stamina}"
    invoke(update_blood_frame, delay=0.1)

    def animate_dialogue_down():
        dialogue_bg.animate_y(-1.0, duration=0.8, curve=curve.in_quad)
        if player_battle_portrait:
            player_battle_portrait.animate_y(-1.0, duration=0.8, curve=curve.in_quad)
        if enemy_portrait:
            enemy_portrait.animate_y(-1.0, duration=0.8, curve=curve.in_quad)
        if enemy_hp_text:
            enemy_hp_text.animate_y(-1, duration=0.8, curve=curve.in_quad)
        if player_hp_text:
            player_hp_text.animate_y(-1, duration=0.8, curve=curve.in_quad)
        if player_stamina_text:
            player_stamina_text.animate_y(-1, duration=0.8, curve=curve.in_quad)

        invoke(start_minigame, delay=0.9)

    animate_dialogue_down()
    print(" Сильная атака! -50 стамины")


def enemy_counter_attack():
    """Контратака врага при недостатке стамины"""
    global player_hp, player_stamina

    print(" Враг контратакует!")

    # Скрываем кнопки на время атаки
    weak_attack_btn.enabled = False
    strong_attack_btn.enabled = False
    surrender_btn.enabled = False

    # Восстанавливаем стамину игроку
    player_stamina = 110
    if player_stamina_text:
        player_stamina_text.text = f"Stamina: {player_stamina}"

    # Наносим урон игроку
    damage = 20
    player_hp -= damage
    if player_hp < 0:
        player_hp = 0

    if player_hp_text:
        player_hp_text.text = f"HP: {player_hp}"


    # Анимация опускания диалога
    def animate_dialogue_down():
        dialogue_bg.animate_y(-1.0, duration=1, curve=curve.in_quad)

        if player_battle_portrait:
            player_battle_portrait.animate_y(-1.0, duration=0.5, curve=curve.in_quad)

        if enemy_portrait:
            enemy_portrait.animate_y(-1.0, duration=0.5, curve=curve.in_quad)

        if enemy_hp_text:
            enemy_hp_text.animate_y(-1, duration=0.8, curve=curve.in_quad)
        if player_hp_text:
            player_hp_text.animate_y(-1, duration=0.8, curve=curve.in_quad)
        if player_stamina_text:
            player_stamina_text.animate_y(-1, duration=0.8, curve=curve.in_quad)

        # Запускаем анимацию удара
        invoke(enemy_attack_animation, delay=2)

    # Анимация удара врага
    def enemy_attack_animation():
        # Звук удара
        if attack2_sound:
            attack2_sound.play()

        # Тряска всех видимых объектов как в enemy_hit_animation
        def shake_all_objects():
            objects_to_shake = []

            # Добавляем все видимые объекты
            if dialogue_bg:
                objects_to_shake.append(dialogue_bg)
            if player_battle_portrait:
                objects_to_shake.append(player_battle_portrait)
            if enemy_portrait:
                objects_to_shake.append(enemy_portrait)
            if enemy_decorate:
                objects_to_shake.append(enemy_decorate)
            if battle_background:
                objects_to_shake.append(battle_background)
            if enemy_hp_text:
                objects_to_shake.append(enemy_hp_text)
            if player_hp_text:
                objects_to_shake.append(player_hp_text)
            if player_stamina_text:
                objects_to_shake.append(player_stamina_text)

            # Тряска каждого объекта
            for obj in objects_to_shake:
                if obj:
                    original_x = obj.x
                    for i in range(6):
                        invoke(setattr, obj, 'x', original_x + (0.03 if i % 2 == 0 else -0.03), delay=i * 0.05)
                    invoke(setattr, obj, 'x', original_x, delay=0.3)

        # Запускаем тряску
        shake_all_objects()

        blood_effect = Entity(
            parent=camera.ui,
            model='quad',
            texture='blood_effect.png',
            scale=0.5,
            color=color.rgb(80,0,0),
            alpha=0.5,
            position=(0, 0),
            z=-0.2
        )

        # Анимация крови КАК У damage_text
        blood_effect.animate_scale(2.5, duration=0.5, curve=curve.out_elastic)  # Увеличивается
        blood_effect.animate_position((0, 0.1), duration=1.0, curve=curve.out_quad)  # Поднимается
        blood_effect.animate('alpha', 0, duration=1.5, delay=0.5, curve=curve.linear)  # Исчезает

        # Удаляем через 2 секунды
        invoke(lambda: destroy(blood_effect), delay=2.0)
        invoke(update_blood_frame, delay=0.6)

        # Мелькание портрета игрока красным
        if player_battle_portrait:
            player_battle_portrait.animate_color(color.rgb(1, 0.2, 0.2), duration=0.1)
            invoke(player_battle_portrait.animate_color, color.white, 0.2, delay=0.1)

        # Текст урона
        # damage_text = Text(
        #     parent=camera.ui,
        #     text=f"-{damage} HP",
        #     position=(-0.4, -0.1),
        #     scale=2.0,
        #     color=color.red,
        #     background=True,
        #     font='4205.otf',
        #     background_color=color.rgba(0, 0, 0, 200)
        # )
        #
        # # Анимация текста урона
        # damage_text.animate_scale(3.0, duration=0.5, curve=curve.out_elastic)
        # damage_text.animate_position((-0.4, 0.2), duration=1.0, curve=curve.out_quad)
        # invoke(lambda: destroy(damage_text), delay=2.0)

        # Возвращаем диалог обратно
        invoke(animate_dialogue_up_after_counter, delay=1.5)

    # Возвращение диалога после контратаки
    def animate_dialogue_up_after_counter():
        dialogue_bg.animate_y(-0.6, duration=0.8, curve=curve.out_quad)

        if player_battle_portrait:
            player_battle_portrait.animate_y(-0.38, duration=0.8, curve=curve.out_quad)
            player_battle_portrait.animate_x(-0.61, duration=0.8, curve=curve.out_quad)

        if enemy_portrait:
            enemy_portrait.animate_y(-0.38, duration=0.8, curve=curve.out_quad)
            enemy_portrait.animate_x(0.61, duration=0.8, curve=curve.out_quad)

        if enemy_hp_text:
            enemy_hp_text.animate_y(-0.1, duration=0.8, curve=curve.in_quad)
        if player_hp_text:
            player_hp_text.animate_y(0, duration=0.8, curve=curve.in_quad)
        if player_stamina_text:
            player_stamina_text.animate_y(-0.1, duration=0.8, curve=curve.in_quad)

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

    # Запускаем контратаку
    animate_dialogue_down()


def surrender_action():
    # Сдаться - закрываем диалог
    global battle_active,player_hp,player_stamina

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
    player_hp = 150
    player_stamina = 110


    close_dialogue()
    print("🏳️ Сдался!")

def attack_action():
    # Обработчик для кнопки Напасть в основном диалоге
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
                print(" Все зоны сбиты! Задержка перед завершением...")
                invoke(end_minigame, delay=2.0)
            break

    if not hit:
        if miss_sound:
            miss_sound.play()
        print(" Мимо!")

    if hits >= 3:
        print(" Все зоны сбиты!")
        end_minigame()
    elif attempts == 0 and hits < 3:
        print(" Попытки закончились!")
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

    print(" Мини-игра завершена!")

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
            enemy_hp_text.animate_y(-0.1, duration=0.8, curve=curve.out_quad)
        if enemy_decorate:
            enemy_decorate.animate_y(0.1,duration=0.8, curve=curve.out_quad)
        if player_hp_text:
            player_hp_text.animate_y(0, duration=0.8,curve=curve.in_quad)
            player_hp_text.animate_x(-0.7, duration=0.8, curve=curve.in_quad)
        if player_stamina_text:
            player_stamina_text.animate_y(-0.1,duration=0.8,curve=curve.in_quad)
            player_stamina_text.animate_x(-0.7, duration=0.8, curve=curve.in_quad)


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
            print(f" Мини-игра: попал {hits} раз(а), урон {damage}, HP врага теперь {enemy_hp}")

        invoke(show_buttons_again, delay=0.9)

    animate_dialogue_up()


# ===== ПОКА ЧТО В ПЛАНАХ ДЛЯ БЕГА ======
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
        print(" Слабая атака! Промах!")


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

    print(" Мини-игра слабой атаки завершена!")

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
        enemy_hp_text.animate_y(-0.1, duration=0.8, curve=curve.out_quad)
    if enemy_decorate:
        enemy_decorate.animate_y(0.1, duration=0.8, curve=curve.out_quad)
    if player_hp_text:
        player_hp_text.animate_y(0, duration=0.8, curve=curve.in_quad)
        player_hp_text.animate_x(-0.7, duration=0.8, curve=curve.in_quad)
    if player_stamina_text:
        player_stamina_text.animate_y(-0.1, duration=0.8, curve=curve.in_quad)
        player_stamina_text.animate_x(-0.7, duration=0.8, curve=curve.in_quad)

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

def create_footstep_wave(position, scale=1.0, color=color.cyan):
    """
    Создает эффект волны как от капли воды в указанной позиции
    position: Vec3 - позиция в мире где сделать эффект
    scale: float - масштаб эффекта
    color: color - цвет волны
    """

    # Создаем основной круг волны
    wave_circle = Entity(
        model=Circle(24),  # Круг с 24 сегментами для плавности
        color=color,
        scale=0.1 * scale,  # Начинаем с маленького размера
        position=position + (0, 1, 0),
        rotation=(90,0,0),
        alpha=0.8
    )

    # Анимация расширения и исчезновения
    wave_circle.animate_scale(3.0 * scale, duration=1.5, curve=curve.out_quad)
    wave_circle.animate('alpha', 0, duration=1.5, curve=curve.in_quad)

    # Создаем вторую волну с задержкой для большего эффекта
    def create_second_wave():
        wave_circle2 = Entity(
            model=Circle(24),
            color=color.tint(0.3),  # Немного светлее
            scale=0.05 * scale,
            position=position + (0, 1, 0),
            rotation=(90,0,0),
            alpha=0.6
        )
        wave_circle2.animate_scale(2.5 * scale, duration=1.2, curve=curve.out_quad)
        wave_circle2.animate('alpha', 0, duration=1.2, curve=curve.in_quad)
        invoke(lambda: destroy(wave_circle2), delay=1.3)

    invoke(create_second_wave, delay=0.2)

    # Удаляем объекты после анимации
    invoke(lambda: destroy(wave_circle), delay=1.6)


# Альтернативная версия с текстурами для более красивого эффекта
def create_footstep_wave_advanced(position, scale=1.0, wave_color=color.cyan):
    """
    Улучшенная версия с несколькими кругами и эффектом свечения
    """

    # Основная волна
    main_wave = Entity(
        model=Circle(32),
        color=wave_color,
        scale=0.08 * scale,
        position=position + (0, 1, 0),
        rotation=(90, 0, 0),
        alpha=0.7
    )

    # Вторая волна (контур)
    outline_wave = Entity(
        model=Circle(32, mode='line'),
        color=wave_color.tint(0.5),
        scale=0.12 * scale,
        position=position + (0, 1, 0),
        rotation=(90, 0, 0),
        alpha=0.9,
        thickness=2
    )

    # Анимация основной волны
    main_wave.animate_scale(2.8 * scale, duration=1.8, curve=curve.out_circ)
    main_wave.animate('alpha', 0, duration=1.8, curve=curve.in_expo)

    # Анимация контура
    outline_wave.animate_scale(3.2 * scale, duration=1.5, curve=curve.out_circ)
    outline_wave.animate('alpha', 0, duration=1.5, curve=curve.in_expo)

    # Задержанная третья волна
    def create_delayed_wave():
        delayed_wave = Entity(
            model=Circle(24),
            color=wave_color.tint(-0.2),  # Темнее
            scale=0.15 * scale,
            position=position + (0, 1, 0),
            rotation=(90, 0, 0),
            alpha=0.4
        )
        delayed_wave.animate_scale(1.8 * scale, duration=1.0, curve=curve.out_quad)
        delayed_wave.animate('alpha', 0, duration=1.0, curve=curve.in_quad)
        invoke(lambda: destroy(delayed_wave), delay=1.1)

    invoke(create_delayed_wave, delay=0.4)

    # Удаление объектов
    invoke(lambda: destroy(main_wave), delay=1.9)
    invoke(lambda: destroy(outline_wave), delay=1.6)


def create_thought_system():
    """Создает элементы для отображения мыслей"""
    global thought_bg, thought_text_entity

    # Фон для текста (полупрозрачный черный)
    thought_bg = Entity(
        parent=camera.ui,
        model='quad',
        color=color.black66,
        scale=(0.8, 0.15),
        position=(0, -0.35, -1),
        enabled=False
    )

    # Текст мысли
    thought_text_entity = Text(
        parent=camera.ui,
        text="",
        position=(0, -0.35, -2),  # Такая же Y-позиция как у фона
        scale=1.5,
        color=color.white,
        font='4205.otf',
        enabled=False,
        origin=(0, 0)  # Центр как точка отсчета
    )


def start_thought(text):
    """Запускает отображение мысли"""
    global thought_active, thought_full_text, thought_text, thought_progress

    # ОСТАНАВЛИВАЕМ предыдущую мысль если она активна
    if thought_active:
        stop_thought()

    thought_active = True
    thought_full_text = text
    thought_text = ""
    thought_progress = 0

    # Сбрасываем состояние печати
    if hasattr(scene, 'thought_printing_active'):
        scene.thought_printing_active = False

    # Очищаем текст перед началом новой мысли
    thought_text_entity.text = ""

    # Включаем элементы
    thought_bg.enabled = True
    thought_text_entity.enabled = True

    # Сбрасываем анимации
    thought_bg.scale_y = 0.15  # Сразу нормальный размер
    thought_text_entity.color = color.white

    # Анимация появления
    thought_bg.scale_y = 0.1
    thought_bg.animate_scale_y(0.15, duration=0.5, curve=curve.out_quad)

    # Начинаем печатать текст
    scene.thought_printing_active = True
    print(f"🚀 Начата новая мысль: '{text}'")


def stop_thought():
    """Останавливает текущую мысль"""
    global thought_active

    if hasattr(scene, 'thought_printing_active'):
        scene.thought_printing_active = False

    thought_active = False

    # Останавливаем звук
    if text_sound.playing:
        text_sound.stop()

    print("🛑 Текущая мысль остановлена")


def update_thought_printing():
    """Обновляет печать текста мысли"""
    global thought_progress, thought_text

    if hasattr(scene, 'thought_printing_active') and scene.thought_printing_active:
        if thought_progress < len(thought_full_text):
            thought_progress = min(thought_progress + text_speed * time.dt, len(thought_full_text))
            thought_text = thought_full_text[:int(thought_progress)]
            thought_text_entity.text = thought_text

            if not text_sound.playing:
                text_sound.play()
        else:
            scene.thought_printing_active = False
            text_sound.stop()

            # Автоматически скрываем мысль через 3 секунды
            invoke(hide_thought, delay=3.0)
            print(f"✅ Мысль завершена: '{thought_full_text}'")


def hide_thought():
    """Скрывает мысль с анимацией"""
    global thought_active

    if thought_bg and thought_text_entity and thought_active:
        print(f"👋 Скрываем мысль: '{thought_full_text}'")

        # Анимация исчезновения
        thought_bg.animate_scale_y(0.1, duration=0.5, curve=curve.in_quad)
        thought_text_entity.animate_color(color.rgba(1, 1, 1, 0), duration=0.5)

        def disable_thought():
            if thought_bg and thought_text_entity:
                thought_bg.enabled = False
                thought_text_entity.enabled = False
                thought_text_entity.color = color.white
                thought_active = False
                print(f"🎯 Мысль полностью скрыта")

        invoke(disable_thought, delay=0.6)



































def update():
    global in_dialogue, pointer, minigame_active, speed_multiplier, last_step_time
    global thought_active, thought_progress, thought_text

    step_cooldown = 0.3

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

    if in_dialogue:
        press_e_text.enabled = False
        update_text_printing()
        return

    # ОБНОВЛЕНИЕ: Добавляем обновление мыслей
    if thought_active:
        update_thought_printing()
        # ЭФФЕКТ ВОЛНЫ ПРИ ХОДЬБЕ - РАБОТАЕТ ДАЖЕ ПРИ МЫСЛЯХ
        walking = held_keys['a'] or held_keys['w'] or held_keys['d'] or held_keys['s']

        if walking and player.grounded and wave_effect_enabled:
            current_time = time.time()

            if current_time - last_step_time > step_cooldown:
                step_offset = Vec3(0, 0, 0)
                if held_keys['w']:
                    step_offset = player.forward * 0.3
                elif held_keys['s']:
                    step_offset = -player.forward * 0.3
                elif held_keys['a']:
                    step_offset = player.left * 0.3
                elif held_keys['d']:
                    step_offset = player.right * 0.3

                step_position = player.position + step_offset + Vec3(0, -0.9, 0)
                create_footstep_wave_advanced(step_position, scale=0.8, wave_color=color.azure)
                last_step_time = current_time

            if not walk.playing:
                walk.play()
        else:
            if walk.playing:
                walk.stop()

    player_pos = player.position
    check_moon_interaction()

    if 'Dream_collider4' in globals() and Dream_collider4:
        if player.intersects(Dream_collider4).hit:
            print("🎯 Касание Dream_collider4 - телепортация на (0, 0, 0)")
            player.position = (0, 0, 0)

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
    in_zone5=(107 <= player_pos.x <= 113 and
              0.4 <= player_pos.y <= 0.7 and
              4.6 <= player_pos.z <= 8)
    in_zone6=(77<= player_pos.x <= 82 and
              0.4 <= player_pos.y <= 0.7 and
              4 <= player_pos.z <= 7)
    in_zone7=(107 <= player_pos.x <= 113 and
              0.4 <= player_pos.y <= 0.7 and
              -6.48 <= player_pos.z <= -3)



    in_door_zone = (125 <= player.position.x <= 131 and
                    -2 <= player.position.y <= 5 and
                    0 <= player.position.z <= 5)
    in_door_zone2=(10 <= player.position.x <= 11.9 and
                   8 <= player.position.y <= 17 and
                   11 <= player.position.z <= 12)
    in_door_zone3=(107 <= player.position.x <= 113 and
              0.4 <= player.position.y <= 0.7 and
              -6.48 <= player.position.z <= -3)
    in_door_zone4=(47 <= player.position.x <= 53 and
                   0.4 <= player.position.y <= 0.7 and
                   -6.6 <= player.position.z <= -4)

    press_e_text.enabled = ((human_collider.hovered and in_zone1) or
                            (human_collidera.hovered and in_zone2) or
                            (human_colliderb.hovered and in_zone3) or
                            bossa_collider.hovered and in_zone4 or
                            Tonight_girl_collider.hovered and in_zone5 or
                            Tonight_man_collider.hovered and in_zone6 or
                            Tonight_QuestMan_collider.hovered and in_zone7)

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
    door_text2.enabled = (in_door_zone2 and look_at_door)

    if hasattr(player, 'forward'):
        look_point = player.position + player.forward * 2
        if distance(look_point, collider_door3.position) < 3:
            look_at_door = True
    door_text3.enabled = (in_door_zone3 and look_at_door)

    if hasattr(player, 'forward'):
        look_point = player.position + player.forward * 2
        if distance(look_point, collider_door4.position) < 3:
            look_at_door = True
    door_text4.enabled = (in_door_zone4 and look_at_door)


    # --- Отладочный ---
    print(f"x={player_pos.x:.2f}  y={player_pos.y:.2f}  z={player_pos.z:.2f}  "
          f"in_door_zone={in_door_zone4}  смотрю_на_дверь={look_at_door}")




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

    print(" Тестирование боевого интерфейса...")

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
                    print(f" Скрыт: {obj_name}")
                except Exception as e:
                    print(f" Ошибка при скрытии {obj_name}: {e}")

    print(f"Всего скрыто объектов: {hidden_count}")


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
def hide_tonight_npc():
    npc_objects = [
        'Tonight_girl','Tonight_girl_collider','Tonight_man','Tonight_man_collider','Tonight_QuestMan','Tonight_QuestMan_collider'
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
def show_tonight_npcs():
    npc_objects = [
        'Tonight_girl','Tonight_girl_collider'
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

    npc_objects = [
        'Tonight_girl','Tonight_girl_collider','Tonight_man','Tonight_man_collider','Tonight_QuestMan_collider','Tonight_QuestMan'
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

def show_npcs():
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
                    print(f" Показан: {obj_name}")
                except Exception as e:
                    print(f" Ошибка при показе {obj_name}: {e}")

    print(f" Всего показано объектов: {shown_count}")

def teleport_player(x, y, z):

    player.position = (x, y, z)
    print(f" Игрок телепортирован в ({x}, {y}, {z})")


def teleport_with_fade(target_position, fade_duration=2):


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
    global in_dialogue, minigame_active, pointer, zones, hits, attempts, battle_active,wave_effect_enabled

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
    # --- Удаление всех обьектов ---
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
        in_zone5 = (106 <= player_pos.x <= 114 and 0.4 <= player_pos.y <= 0.7 and 0 <= player_pos.z <= 8)
        in_zone6 = (77 <= player_pos.x <= 82 and 0.4 <= player_pos.y <= 0.7 and 4 <= player_pos.z <= 7)
        in_zone7 = (107 <= player_pos.x <= 113 and 0.4 <= player_pos.y <= 0.7 and -6.48 <= player_pos.z <= -3)


        if human_collider.hovered and in_zone1:
            start_dialogue("Человек 1", "Привет! Рад тебя видеть. Что скажешь?")
        elif human_collidera.hovered and in_zone2:
            start_dialogue("Человек 2", "Привет! Я второй NPC.")
        elif human_colliderb.hovered and in_zone3:
            start_dialogue("Человек 3", "Здравствуй! Я третий NPC.")
        elif bossa_collider.hovered and in_zone4:
            start_dialogue("Босс","Вот тебе задание.")
        elif Tonight_girl_collider.hovered and in_zone5:
            start_dialogue("Girl","Привет друг!")
        elif Tonight_man_collider.hovered and in_zone6:
            start_dialogue('Man','О,я тебя знаю!')
        elif Tonight_QuestMan_collider.hovered and in_zone7:
            start_dialogue('Испуганный мужчина','Эй,подойди ближе а то нас услышат ОНИ!!!')

    # --- Взаимодействие с дверями ---
    if key == 'e':

        player_pos = player.position


        in_door_zone1 = (125 <= player_pos.x <= 131 and
                         -2 <= player_pos.y <= 5 and
                         0 <= player_pos.z <= 5)


        in_door_zone2 = (10 <= player_pos.x <= 11.9 and
                         8 <= player_pos.y <= 17 and
                         11 <= player_pos.z <= 12)

        in_door_zone3=(107 <= player.position.x <= 113 and
              0.4 <= player.position.y <= 0.7 and
              -6.48 <= player.position.z <= -3)

        in_door_zone4 = (47 <= player.position.x <= 53 and
                         0.4 <= player.position.y <= 0.7 and
                         -6.6 <= player.position.z <= -4)

        print(f"[DEBUG] Позиция игрока: x={player_pos.x:.2f}, y={player_pos.y:.2f}, z={player_pos.z:.2f}")
        print(f"[DEBUG] Дверь1: in_zone={in_door_zone1}")
        print(f"[DEBUG] Дверь2: in_zone={in_door_zone2}")
        print(f"[DEBUG] Дверь2: in_zone={in_door_zone3}")
        print(f"[DEBUG] Дверь2: in_zone={in_door_zone4}")

        # Проверяем расстояние до объектов дверей
        if 'collider_door1' in globals() and collider_door1:
            dist_to_door1 = distance(player_pos, collider_door1.position)
            print(f"[DEBUG] Расстояние до двери1: {dist_to_door1}")
        else:
            dist_to_door1 = 1000

        if 'collider_door2' in globals() and collider_door2:
            dist_to_door2 = distance(player_pos, collider_door2.position)
            print(f"[DEBUG] Расстояние до двери2: {dist_to_door2}")
        else:
            dist_to_door2 = 1000

        if 'collider_door3' in globals() and collider_door3:
            dist_to_door3 = distance(player_pos, collider_door3.position)
            print(f"[DEBUG] Расстояние до двери1: {dist_to_door1}")
        else:
            dist_to_door3 = 1000

        if 'collider_door4' in globals() and collider_door4:
            dist_to_door4 = distance(player_pos, collider_door4.position)
            print(f"[DEBUG] Расстояние до двери1: {dist_to_door4}")
        else:
            dist_to_door4 = 1000

        # Если находимся в зоне первой двери и близко к ней
        if in_door_zone1 and dist_to_door1 < 5:

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
                sound_manager.play_tonight_sound()
                collider_door1.position=(40,40,40)
                show_tonight_npcs()
                collider_door4.position=(50.07,2,-9)



            teleport_with_fade((126, 2.24, 2.64), fade_duration=3)
            invoke(exit_house, delay=1.5)

        elif in_door_zone3 and dist_to_door3 < 5:
            print("[DEBUG] ВЫХОД ИЗ ДОМА 2")
            switch_level()

        elif in_door_zone4 and dist_to_door4 < 5:
            def teleport_to_dream():
                Sky.texture = 'Dream3.png'
                ultra_safe_hide()
                hide_npcs()
                hide_tonight_npc()
                ground.color = color.clear
                ground.scale=(200,1,80)
                collider_door4.position=(40,40,40)
                moon.enabled=False
                Dream_collider1.enabled = True
                Dream_collider2.enabled = True
                Dream_collider3.enabled = True
                teleport_player(-93.7,0.5,-1.37)



                sound_manager.switch_to_dream()

                # УБЕДИТЕСЬ что переменная глобальная
                global wave_effect_enabled
                wave_effect_enabled = True

                print(f"DEBUG: wave_effect_enabled = {wave_effect_enabled}")

                create_footstep_wave_advanced(player.position + Vec3(0, -0.9, 0),
                                              scale=1.5,
                                              wave_color=color.azure)



            teleport_to_dream()
            invoke(lambda: start_thought("Где я?"), delay=3.0)
            invoke(lambda: start_thought("Что я здесь делаю?"), delay=9.0)
            invoke(lambda: start_thought("Мне страшно!!!"), delay=16.0)
            invoke(show_moon3, delay=21.0)
            invoke(lambda: show_quest("Задание: ........"), delay=2.0)


    # --- Закрытие диалогов ---
    if key in ('1', '2', '3') and in_dialogue and not battle_active:
        close_dialogue()

    # --- Быстрая смена уровня ---
    if key == 'p':
        print("[DEBUG] Ручной вызов switch_level() через P")
        switch_level()
        hide_npcs()

    # --- Прыжок ---
    if key == 'space' and not jump.playing:
        jump.play()

    # --- Выход ---
    if key == 'q':
        quit()
    if key=='v':
        ultra_safe_show()
        show_npcs()
    if key=='l':
        show_npcs()
    # --- Телепорт в квестовую комнату ---
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
    if key=='m':
        vhs_overlay.enabled=False
    if key=='n':
        vhs_overlay.enabled=True
create_thought_system()


def create_quest_system():
    """Создает элементы для отображения задания"""
    global quest_text_entity, quest_bg

    # Фон для задания (полупрозрачный черный)
    quest_bg = Entity(
        parent=camera.ui,
        model='quad',
        color=color.black66,  # Более прозрачный
        scale=(0.4, 0.08),
        position=(-0.65, 0.2, -1),  # Верхний левый угол
        enabled=False
    )

    # Текст задания
    quest_text_entity = Text(
        parent=camera.ui,
        text="",
        position=(-0.65, 0.2, -2),  # Такая же Y-позиция как у фона
        scale=1.5,
        color=color.white,
        font='4205.otf',
        enabled=False,
        origin=(0, 0)  # Центр как точка отсчета
    )


def show_quest(text):
    """Показывает задание"""
    global quest_active

    quest_active = True

    # Устанавливаем текст
    quest_text_entity.text = text

    # Включаем элементы
    quest_bg.enabled = True
    quest_text_entity.enabled = True

    # Анимация появления
    quest_bg.scale_x = 0.1
    quest_bg.animate_scale_x(0.4, duration=0.8, curve=curve.out_quad)

    print(f"📋 Задание показано: {text}")


def update_quest_text(new_text):
    """Обновляет текст задания"""
    if quest_text_entity:
        quest_text_entity.text = new_text
        print(f"📋 Задание обновлено: {new_text}")



















def hide_all_dream_objects():
    """Скрывает все объекты сцены Dream"""
    for target in moon_targets:
        target["entity"].enabled = False
        target["entity"].alpha = 0  # Делаем полностью прозрачными


def show_moon3():
    global moon_interacted,current_moon_target
    moon3.enabled=True
    moon3.scale = 0.1
    moon3.animate_scale((20, 20, 20), duration=2.0, curve=curve.out_elastic)
    moon_sound = Audio('moon1.ogg', loop=False, autoplay=False)
    moon_sound.play()
    invoke(lambda: update_quest_text("Задание: Иди к луне"), delay=1.0)
    current_moon_target=0
    hide_all_dream_objects()


def check_moon_interaction():
    """Проверяет приближение к текущей цели"""
    global moon_interacted, current_moon_target

    if moon3.enabled and not moon_interacted and current_moon_target < len(moon_targets):
        # Для первой цели (луна) проверяем расстояние до самой луны
        if current_moon_target == 0:
            dist_to_moon = distance(player.position, moon3.position)
            if dist_to_moon < 25:  # Расстояние до луны
                moon_interacted = True
                fly_to_next_target()
        else:
            # Для остальных целей проверяем расстояние к домам
            current_target = moon_targets[current_moon_target - 1]
            dist_to_target = distance(player.position, current_target["entity"].position)

            if dist_to_target < 25:  # Расстояние для взаимодействия с домами
                moon_interacted = True
                fly_to_next_target()


def fly_to_next_target():
    """Перелетает к следующей цели"""
    global current_moon_target, moon_interacted
    Dream_collider5.enabled = True

    print(f"🌙 Луна перелетает к цели {current_moon_target + 1}")

    # СНАЧАЛА показываем объекты для СЛЕДУЮЩЕЙ цели
    if current_moon_target == 3:  # Если летим к Dream_house4
        # Показываем оба объекта сразу
        show_dream_object(moon_targets[3]["entity"])  # Dream_house4
        show_dream_object(moon_targets[4]["entity"])  # Dream_house5

        # Включаем звук через 2 секунды
        invoke(lambda: Audio('Dream_alarm.mp3', loop=False, autoplay=True), delay=2.0)

        def check_teleport():
            dist = distance(player.position, target["entity"].position)
            if dist < 45:
                # 1. Сначала затемнение экрана
                dark_overlay.enabled = True
                dark_overlay.color = color.rgba(0, 0, 0, 0)
                dark_overlay.animate_color(color.rgba(0, 0, 0, 1), duration=3.0)
                if quest_text_entity and quest_text_entity.enabled:
                    quest_text_entity.enabled = False
                if quest_bg and quest_bg.enabled:
                    quest_bg.enabled = False

                # 2. После затемнения показываем текст с печатью
                def show_text_after_fade():
                    dream_text = Text(
                        parent=camera.ui,
                        text="",
                        position=(0, 0, -10),
                        scale=0.1,
                        color=color.white,
                        font='4205.otf'
                    )
                    dream_text.animate_scale(3.0, duration=2.0, curve=curve.out_elastic)

                    # Медленная печать текста
                    full_text = "Это был сон.."
                    text_progress = 0

                    def print_text():
                        nonlocal text_progress
                        if text_progress < len(full_text):
                            text_progress += 0.3  # Медленная печать
                            dream_text.text = full_text[:int(text_progress)]
                            invoke(print_text, delay=0.1)
                        else:
                            # Текст напечатан, ждем еще 3 секунды в темноте
                            invoke(lambda: teleport_and_fade_in(dream_text), delay=3.0)  # Передаем текст

                    print_text()

                # 3. Телепорт и растемнение после долгой паузы
                def teleport_and_fade_in(dream_text):  # Принимаем текст как параметр
                    # Телепорт
                    player.position = (0, 0, 0)
                    print("🔮 Телепортация на (0, 0, 0)")

                    switch_level()
                    ground.enabled=False
                    ground2.enabled=True
                    ground2.shader=lit_with_shadows_shader
                    ultra_safe_show()
                    Dream_house.enabled=False
                    Dream_house2.enabled=False
                    Dream_house3.enabled = False
                    Dream_house4.enabled = False
                    Dream_house5.enabled = False
                    Dream_collider5.enabled = False
                    moon3.enabled=False

                    # Растемнение
                    dark_overlay.animate_color(color.rgba(0, 0, 0, 0), duration=3.0)

                    # Убираем затемнение после анимации
                    invoke(lambda: setattr(dark_overlay, 'enabled', False), delay=3.1)

                    # Убираем текст с анимацией
                    dream_text.animate_color(color.rgba(1, 1, 1, 0), duration=2.0)
                    dream_text.animate_scale(0.1, duration=2.0, curve=curve.in_quad)
                    invoke(lambda: destroy(dream_text), delay=2.1)

                invoke(show_text_after_fade, delay=3.1)  # После затемнения
            else:
                invoke(check_teleport, delay=0.5)

        invoke(check_teleport, delay=2.5)


    if current_moon_target == 0:
        target = moon_targets[0]
        target_position = target["entity"].position + target["offset"]
        show_moon_text("Помнишь этот дом?")
        invoke(lambda: show_dream_object(target["entity"]), delay=1.0)
    else:
        target = moon_targets[current_moon_target]

        if current_moon_target == 3:
            target_position = target["entity"].position + Vec3(15, 30, 0)
        elif current_moon_target == 4:
            target_position = target["entity"].position + Vec3(15, 30, 0)
        else:
            target_position = target["entity"].position + target["offset"]

        show_moon_text(target["text"])

        # Для остальных целей показываем объекты как обычно
        if current_moon_target != 3:  # Dream_house4 уже показали выше
            invoke(lambda: show_dream_object(target["entity"]), delay=1.0)

    # Анимация перелета
    moon3.animate_position(target_position, duration=3.0, curve=curve.out_quad)
    moon3.animate_scale((15, 15, 15), duration=3.0, curve=curve.in_out_quad)

    # ТОЛЬКО ПОСЛЕ этого увеличиваем счетчик
    current_moon_target += 1

    # Сбрасываем флаг взаимодействия для следующей цели
    if current_moon_target < len(moon_targets):
        def reset_interaction():
            global moon_interacted
            moon_interacted = False
            print(f"🌙 Готов к взаимодействию с целью {current_moon_target + 1}")

        invoke(reset_interaction, delay=3.5)
    else:
        print("🌙 Луна завершила свой путь")
        # Последний перелет - луна улетает вдаль
        final_position = moon3.position + Vec3(0, 100, 100)
        moon3.animate_position(final_position, duration=5.0, curve=curve.out_quad)
        moon3.animate_scale((5, 5, 5), duration=5.0, curve=curve.in_quad)


def show_dream_object(entity):
    """Плавно показывает объект сцены Dream"""
    if not entity.enabled:
        entity.enabled = True
        entity.alpha = 0
        entity.animate('alpha', 1.0, duration=2.0, curve=curve.out_quad)
        print(f"🏠 Появляется объект: {entity}")


def show_moon_text(text):

    moon_text = Text(
        parent=camera.ui,
        text="",
        position=(0, 0.35, -2),
        scale=2.0,
        color=color.white,
        font='4205.otf',
        enabled=True
    )

    # Анимация появления
    moon_text.scale = 0.1
    moon_text.animate_scale(2.0, duration=1.0, curve=curve.out_elastic)


    start_moon_text_printing(moon_text, text)


def start_moon_text_printing(moon_text, full_text):

    moon_text_progress = 0
    moon_text_current = ""
    moon_text_speed = 60

    def update_moon_printing():
        nonlocal moon_text_progress, moon_text_current

        if moon_text_progress < len(full_text):
            moon_text_progress = min(moon_text_progress + moon_text_speed * time.dt, len(full_text))
            moon_text_current = full_text[:int(moon_text_progress)]
            moon_text.text = moon_text_current

            if not text_sound.playing:
                text_sound.play()

            invoke(update_moon_printing, delay=1 / 60)
        else:
            text_sound.stop()
            invoke(lambda: hide_moon_text(moon_text), delay=3.0)

    update_moon_printing()


def hide_moon_text(moon_text):

    moon_text.animate_scale(0.1, duration=0.8, curve=curve.in_quad)
    moon_text.animate_color(color.rgba(1, 1, 1, 0), duration=0.8)

    if text_sound.playing:
        text_sound.stop()

    invoke(lambda: destroy(moon_text), delay=0.9)



hide_all_dream_objects()


create_quest_system()
button1.on_click = setup_conversation_buttons  # "Поговорить"
button2.on_click = attack_action  # "Напасть"
button3.on_click = close_dialogue  # "Уйти"
talk_button.on_click = talk_action
dont_care_button.on_click = dont_care_action
weak_attack_btn.on_click = weak_attack_action
strong_attack_btn.on_click = strong_attack_action
surrender_btn.on_click = surrender_action
vhs_overlay = Entity(
    parent=camera.ui,
    model='quad',
    texture='vhs_effect6.mp4',
    scale=(1.8,1.8),
    color=color.white,
    alpha=0.3,
    z=-1
)
teleport_player(50.05,0.5,-6.47)
camera.rotation_y = -90
hide_tonight_npc()
app.run()








