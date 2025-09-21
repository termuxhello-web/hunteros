import sys
import sdl2
import sdl2.ext
from dock import Dock

# Init SDL2
sdl2.ext.init()
window = sdl2.ext.Window("HunterOS Rootless", size=(1024, 768))
window.show()

# Init Dock
dock = Dock(window)

running = True
while running:
    events = sdl2.ext.get_events()
    for event in events:
        if event.type == sdl2.SDL_QUIT:
            running = False
    # Render dock + desktop (update GUI)
    dock.render()

sdl2.ext.quit()
sys.exit(0)
