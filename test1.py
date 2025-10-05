from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.shaders import lit_with_shadows_shader, basic_lighting_shader

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










app.run()