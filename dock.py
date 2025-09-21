import sdl2
import sdl2.ext

class Dock:
    def __init__(self, window):
        self.window = window
        self.icons = ["Terminal", "FileManager", "Settings"]

    def render(self):
        # Render dock background
        self.window.refresh()
        # Render icons (placeholder)
        for i, icon in enumerate(self.icons):
            print(f"Dock icon: {icon}")  # Replace bằng render thực SDL2
