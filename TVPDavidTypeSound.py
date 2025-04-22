import time
import json
import pygame
import os
base_path = os.path.dirname(os.path.abspath(__file__))
sound_path = os.path.join(base_path, "Sounds", "bleep027.mp3")
pygame.mixer.init()
blipSound = pygame.mixer.Sound(sound_path)
def typeSoundDavid(text, surface, font, color, pos, delay=0.06, sound_enabled=True, wrap_limit=50):
    displayed = ""
    x, y = pos
    font = pygame.font.SysFont("Arial", 14)
    line_spacing = font.get_linesize()

    final_surfaces = []

    for i, char in enumerate(text):
        displayed += char

        if len(displayed.replace("\n", "")) % wrap_limit == 0:
            displayed += "\n"

        surface.fill((0, 0, 0))
        lines = displayed.split("\n")

        final_surfaces = []
        for index, line in enumerate(lines):
            text_surface = font.render(line, True, color)
            surface.blit(text_surface, (x, y + index * line_spacing))
            final_surfaces.append(text_surface)

        pygame.display.flip()
        if char.strip() and sound_enabled:
            blipSound.play()

        pygame.event.pump()
        time.sleep(delay)

    return final_surfaces
# Function Test Code
if __name__ == "__main__":
    typeSoundDavid("Hello John", )