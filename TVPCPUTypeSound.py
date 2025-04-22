import time
import json
import pygame
import os
base_path = os.path.dirname(os.path.abspath(__file__)) # Get the base path of the current file
sound_path = os.path.join(base_path, "Sounds", "bleep030.mp3") # Path to the sound file 
pygame.mixer.init() # Initialize the mixer module for sound playback
blipSound = pygame.mixer.Sound(sound_path) # Load the sound file into a Sound object

def typeSoundCPU(text, surface, font, color, pos, delay=0.06, sound_enabled=True, wrap_limit=50): 

    displayed = "" # Initializes the displayed text as an empty string
    x, y = pos  # Unpacks the position tuple into x and y coordinates
    line_spacing = font.get_linesize() # Gets the height of a line of text in pixels

    final_surfaces = [] 

    for i, char in enumerate(text): # Iterates over each character in the input text
        displayed += char 

        if len(displayed.replace("\n", "")) > 0 and len(displayed.replace("\n", "")) % wrap_limit == 0: # Checks if the displayed text has reached the wrap limit  
            displayed += "\n"

        surface.fill((0, 0, 0))
        lines = displayed.split("\n") # Splits the displayed text into lines based on newline characters

        final_surfaces = []
        for index, line in enumerate(lines):  
            text_surface = font.render(line, True, color)
            surface.blit(text_surface, (x, y + index * line_spacing))  # Draws the text surface on the main surface at the specified position
            final_surfaces.append(text_surface) 

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        if char.strip() and sound_enabled: # Checks if the character is not just whitespace and if sound is enabled
            blipSound.play()

        pygame.event.pump() 
        time.sleep(delay)

    return final_surfaces
# Function Test Code
if __name__ == "__main__":
    typeSoundCPU("Hello John")