from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.shaders import lit_with_shadows_shader, basic_lighting_shader
from direct.filter.CommonFilters import CommonFilters
app=Ursina()
ground=Entity(model='cube',collider='mesh',texture='grass',scale=(100,1,100))
player=FirstPersonController(collider='box')
def input(key):
    if key == 'q':
        quit()
brick=load_texture('Test1.jpg')
box_Y=10
box_X=2
box_Z=1
box1=Entity(model='cube',color=color.red,collider='box',position=(1,1,1))
box2=Entity(model='cube',color=color.green,collider='box',position=(4,1,1))
box3=Entity(model='cube',color=color.blue,collider='box',position=(1,4,1))
box4=Entity(model='cube',color=color.gray,collider='box',position=(1,1,4))
box5=Entity(model='cube',color=color.red,collider='box',position=(box_Y,box_X,box_Z))
wall=Entity(model='cube',collider='box',texture='brick.jpg',scale=(20,10,2),position=(20,1,20))
sun = DirectionalLight(shadows=True)
sun.look_at(Vec3(-1,-1,-1))
sun.shadow_map_resolution = (32000, 32000)#больше четче тени

AmbientLight(color=color.rgb(100,100,100))
ground.shader = lit_with_shadows_shader
box1.shader = lit_with_shadows_shader
wall.shader=lit_with_shadows_shader
Sky=Sky()
filters = CommonFilters(base.win, base.cam)# если ошибка то так и нужно
filters.setBloom(intensity=2.0)


walk=Audio('walk.mp3',loop=True,autoplay=False)
jump=Audio('jump.mp3',loop=False,autoplay=False)
def update():
    walking=held_keys['a']or held_keys['w'] or held_keys['d']or held_keys['s']
    if walking and player.grounded:
        if not walk.playing:
            walk.play()
    else:
        if walk.playing:
            walk.stop()
def input(key):
    if key == 'space':
        if not jump.playing:
            jump.play()
    if key == 'q':
        quit()







app.run()



