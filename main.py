from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

# Blok türleri
block_types = [
    {'name': 'grass', 'texture': 'grass'},
    {'name': 'stone', 'texture': 'brick'},
    {'name': 'dirt', 'texture': 'brick'},
    {'name': 'wood', 'texture': 'wood'},
]

current_block = 0

# Voxel sınıfı
class Voxel(Button):
    def __init__(self, position=(0,0,0), texture='grass'):
        super().__init__(
            parent=scene,
            position=position,
            model='cube',
            origin_y=.5,
            texture=texture,
            color=color.white,
            highlight_color=color.lime,
        )

    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                voxel = Voxel(position=self.position + mouse.normal, texture=block_types[current_block]['texture'])
            if key == 'right mouse down':
                destroy(self)

# Daha büyük dünya oluştur (16x16, 10 katman)
for y in range(10):
    for z in range(16):
        for x in range(16):
            if y < 3:
                voxel = Voxel(position=(x, y, z), texture='brick')
            elif y < 6:
                voxel = Voxel(position=(x, y, z), texture='brick')
            else:
                voxel = Voxel(position=(x, y, z), texture='grass')

# Blok seçici
def update():
    global current_block
    for i in range(len(block_types)):
        if held_keys[str(i+1)]:
            current_block = i
            print(f"Seçili blok: {block_types[current_block]['name']}")

# Oyuncu kontrolü
player = FirstPersonController()

app.run()