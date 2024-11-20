import busio
import displayio
from digitalio import DigitalInOut, Direction, Pull
from adafruit_st7735r import ST7735R
import adafruit_imageload
import time
import board
import digitalio
from keypad import Keys
import gc

'''
#Buttons
btn_l = digitalio.DigitalInOut(board.GP12)
btn_r = digitalio.DigitalInOut(board.GP14)
btn_u = digitalio.DigitalInOut(board.GP13)
btn_d = digitalio.DigitalInOut(board.GP15)
btn_l.switch_to_input(pull=digitalio.Pull.DOWN)
btn_r.switch_to_input(pull=digitalio.Pull.DOWN)
btn_u.switch_to_input(pull=digitalio.Pull.DOWN)
btn_d.switch_to_input(pull=digitalio.Pull.DOWN)


#display
clock = board.GP2
mosi = board.GP3
miso = board.GP4
cs = board.GP5
reset = board.GP6
#Create shina
displayio.release_displays()
spi = busio.SPI(clock = clock, MOSI = mosi)
display_bus = displayio.FourWire(spi, command = miso, chip_select = cs, reset = reset)
display = ST7735R(display_bus, rotation = 270, width=160, height=128)


# Load the sprite sheet (bitmap)
sprite_sheet, palette = adafruit_imageload.load("/castle_sprite_sheet.bmp",
                                                    bitmap=displayio.Bitmap,
                                                    palette=displayio.Palette)
# delete white background on tile
palette.make_transparent(16)

spawn = [0,0]
enemys = []
loots = []

#width screen in tiles (10*16=160|8*16=128)
w = 10
h = 8

#Map of level (contain objects)
arena_map = []

#Create group for another sprites groups(this group go to display)
group = displayio.Group()
'''

'''==========================================REFACTOR ALL CODE=============================================='''

class Game():
    def start():
        pass
    def update():
        pass
    def render():
        pass
    def switch_scene():
        pass


class Scene():
    def add_layer():
        pass
    def update():
        pass
    def render():
     
     
class Layer():
    def add_abject():
        pass
    def update():
        pass
    def render():
        

class GameObject():
    def __init__(self, x,y,sprite=None,collider=None):
        self.x = x
        self.y = y
        self.sprite = sprite
        self.collider = collider
    
    def update():
        pass
    
    def draw():
        pass

class Player(GameObject):
    def move():
        pass
class Enemy(GameObject):
    def ai_logic():
        pass


class Collider():
    def check_collision():
        pass
    def get_bounds():
        pass


class Render():
    def draw_sprite():
        pass
    def clean_screen():
        pass
    

class InputHandler():
    def get_input():
        pass
    

class ResourceManager():
    def load_texture(path,transparent):
        # Load the sprite sheet (bitmap)
        sprite_sheet, palette = adafruit_imageload.load(path,bitmap=displayio.Bitmap,palette=displayio.Palette)                                                                                    
        # delete white background on tile
        palette.make_transparent(transparent)
        
    def get_texture():
        pass
    
textures = ResourceManager()
textures.load_texture("/castle_sprite_sheet.bmp", 16)
'''==========================================REFACTOR ALL CODE=============================================='''
'''class Visible():
    def __init__(self, w=1, h=1, w_tile=16, h_tile=16, sprite_scale = 1, sprite_number = 0, can_walk = True):
        self.width = w
        self.height = h
        self.tile_width = w_tile
        self.tile_height = h_tile
        
        self.sprite_group = None
        self.sprite = None
        self.sprite_scale = sprite_scale
        
        self.can_walk = can_walk
        self.sprite_number = sprite_number
        
    def view_create(self):
        self.sprite = displayio.TileGrid(sprite_sheet, pixel_shader=palette,
                                width = self.width,
                                height = self.height,
                                tile_width = self.tile_width,
                                tile_height = self.tile_height)
        sprite_group = displayio.Group(scale=self.sprite_scale)
        sprite_group.append(self.sprite)
        group.append(sprite_group)
        self.sprite_group = sprite_group
    
    def view_decreate(self):
        group.remove(self.sprite_group)
        
    def get_position(self):
        global arena_map
        pos = [None,None]
        for y, line in enumerate(arena_map):
            try:
                pos[0] = line.index(self)
                pos[1] = y
            except ValueError:
                continue
        return pos
    
    def move_sprite(self, xy):
        self.sprite.x = xy[0]*16
        self.sprite.y = xy[1]*16
        
    def move(self, x, y, temp_pos=True):
        global arena_map
        xobj,yobj = self.get_position()
        
        if arena_map[y][x].can_walk == True and temp_pos == False:
            arena_map[y][x], arena_map[yobj][xobj] = arena_map[yobj][xobj], arena_map[y][x]
        if arena_map[yobj + y][xobj + x].can_walk == True and temp_pos == True:
            nxt = arena_map[yobj + y][xobj + x]
            tmp = arena_map[yobj][xobj]
            arena_map[yobj + y][xobj + x] = tmp
            arena_map[yobj][xobj] = nxt
        
    def change_sprite(self, num, x_tile=0, y_tile=0):
        self.sprite[x_tile,y_tile] = num
    

class Heroe(Visible):         
    pass
        
class Enemy(Visible):        
    pass

class Loot(Visible):
    pass


class Floor(Visible):
    pass
class Wall(Visible):
    pass

class Area(Visible):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.view = [0,0]
        
    def set_view(self, xy=[0,0]):
        self.view[0] = xy[0]
        self.view[1] = xy[1]
    
    def view_area(self, layer=[]):
        global arena_map
        for y, row in enumerate(arena_map[self.view[1]:h+self.view[1]]):
            for x, obj in enumerate(row[self.view[0]:w+self.view[0]]):
                self.change_sprite(num=obj.sprite_number,x_tile=x,y_tile=y)

floor = Floor(sprite_number = 7, can_walk = True)
wall = Wall(sprite_number = 4, can_walk = False)
hero = Heroe(sprite_number = 1)


f = open("map.csv", 'r')
map_csv_str = f.read()
f.close()
map_csv_lines = map_csv_str.replace("\r", "").split("\n")
del map_csv_str
for y, line in enumerate(map_csv_lines):
    if line != '':
        line_x = []
        for x, tile_name in enumerate(line.split(";")):
            tn = int(tile_name)
            # env
            if tn == 3 or tn == 4 or tn == 5 or tn == 6 or tn == 8 or tn == 9 or tn == 10 or tn == 11:
                line_x.append(wall)
            if tn == 7:
                line_x.append(floor)
            # contactable
            if tn == 0:
                line_x.append(Enemy(sprite_number = 0, can_walk = False))
            if tn == 2:
                line_x.append(Loot(sprite_number = 2, can_walk = True))
            if tn == 1:
                line_x.append(hero)
            
        arena_map.append(line_x)
del map_csv_lines


print(f"Size of map  x:{len(arena_map[0])}|y:{len(arena_map)}")
#Create object castle
castle = Area(w=w,h=h)

#Add castle to main group sprites
castle.view_create()  

# Add the Group with all sprites to the Display
display.root_group = group

fps = 10
btn_l_down = False
btn_r_down = False
btn_u_down = False
btn_d_down = False

# Loop forever so you can enjoy your image
while True:
    time_start = time.time()
    if btn_l.value == True and btn_l_down == False:
        hero.move(-1,0)
        btn_l_down = True
    elif btn_l.value == False and btn_l_down == True:
        btn_l_down = False
        
    if btn_r.value == True and btn_r_down == False:
        hero.move(1,0)
        btn_r_down = True
    elif btn_r.value == False and btn_r_down == True:
        btn_r_down = False
        
    if btn_u.value == True and btn_u_down == False:
        hero.move(0,-1)
        btn_u_down = True
    elif btn_u.value == False and btn_u_down == True:
        btn_u_down = False
        
    if btn_d.value == True and btn_d_down == False:
        hero.move(0,1)
        btn_d_down = True
    elif btn_d.value == False and btn_d_down == True:
        btn_d_down = False
    
    #Math magick to detection what piece of map draw
    hero_pos = hero.get_position()
    castle.set_view([max(0, min(hero_pos[0] - w // 2, len(arena_map[0]) - w)), max(0, min(hero_pos[1] - h // 2, len(arena_map) - h))])
    castle.view_area()
    
    gc.collect()
    print(gc.mem_free(), end="\r")
    
    time.sleep(max(1/fps-(time.time()-time_start) ,0))
    '''
