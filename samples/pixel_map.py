"""
Tilengine python example:
	Pixel mapping transform demo
"""

import sys
sys.path.append("../src")
from tilengine import Engine, Window, Tilemap, PixelMap
from math import sin, radians

# helper constants
WIDTH = 400
HEIGHT = 240

# load layer assets and basic setup
def setup_layer(layer, name):
	tilemap = Tilemap.fromfile(name)
	layer.setup(tilemap)

# init
engine = Engine.create(WIDTH, HEIGHT, 1, 0, 0)
foreground = engine.layers[0]

# setup layers
engine.set_load_path("assets/zelda")
setup_layer(foreground, "zelda.tmx")

# build pixel mapping table of WIDTH*HEIGHT PixelMap elements
num_pixels = WIDTH * HEIGHT
pixel_map = (PixelMap * num_pixels)()
for y in range(HEIGHT):
	for x in range(WIDTH):
		index = y * WIDTH + x
		pixel_map[index].dx = x + int(sin(radians(x + y * 3)) * 16)
		pixel_map[index].dy = y + int(sin(radians(x - y * 3)) * 16)
foreground.set_pixel_mapping(pixel_map)

# main loop
window = Window.create()
while window.process():
	foreground.set_position(40, window.num_frame)
