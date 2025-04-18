import time
import json
import pygame
import os
base_path = os.path.dirname(os.path.abspath(__file__))
sound_path = os.path.join(base_path, "Sounds", "bleep030.mp3")
pygame.mixer.init()
blipSound = pygame.mixer.Sound(sound_path)
def typeSoundDavid(text, delay = 0.03, sound_enabled=True):
    for char in text:
        print(char, end="", flush=True)
        if char.strip() and sound_enabled:
            blipSound.play()
        time.sleep(delay)
    print()
# Function Test Code
if __name__ == "__main__":
    typeSoundDavid("Hello John")