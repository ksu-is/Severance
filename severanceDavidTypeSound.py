import time
import json
import pygame
import os
base_path = os.path.dirname(os.path.abspath(__file__))
sound_path = os.path.join(base_path, "Sounds", "bleep030.mp3")
pygame.mixer.init()
blipSound = pygame.mixer.Sound(sound_path)
def typeSoundDavid(text, surface, font, color, pos, delay=0.06, sound_enabled=True):
    displayed = ""
    for char in text:
        displayed += char
        surface.fill((0, 0, 0))  # Clear screen with black
        text_surface = font.render(displayed, True, color)
        surface.blit(text_surface, pos)
        pygame.display.flip()  # Update the screen
        if char.strip() and sound_enabled:
            blipSound.play()
        time.sleep(delay)
    print()
# Function Test Code
if __name__ == "__main__":
    typeSoundDavid("Hello John",)