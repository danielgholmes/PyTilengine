"""
Tilengine python example:
    Column offset feature demo
"""

import sys
sys.path.append("../src")
from tilengine import Engine, Window, Tilemap

from ctypes import c_int
from math import sin, radians

WIDTH = 400
HEIGHT = 240


# load layer assets and basic setup
def setup_layer(layer, name):
	tilemap = Tilemap.fromfile(name)
	layer.setup(tilemap)
	engine.set_background_color(tilemap)


# initialise
engine = Engine.create(WIDTH, HEIGHT, 3, 0, 0)
foreground = engine.layers[0]
background = engine.layers[1]
base_layer = engine.layers[2]

# setup the layers
engine.set_load_path("assets/sonic")
setup_layer(foreground, "Sonic_md_fg1.tmx")
setup_layer(background, "Sonic_md_bg1.tmx")
setup_layer(base_layer, "Base.tmx")

# create and assign column offset array
num_columns = int(WIDTH / 8 + 2)
columns = (c_int * num_columns)()
foreground.set_column_offset(columns)

# game loop
x_world = 0
window = Window.create()
while window.process():
	for n in range(num_columns):
		columns[n] = int(sin(radians(x_world * 4 + n * 7)) * ((abs(sin(radians(x_world / 4)) * 12)) + 4))
	foreground.set_position(x_world, 0)
	background.set_position(x_world / 4, 0)
	x_world += 2
