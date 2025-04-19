import time
import pygame
import json
import os
from severanceDavidTypeSound import typeSoundDavid
base_path = os.path.dirname(os.path.abspath(__file__))
text_path = os.path.join(base_path, "dialogueScene1.json")
def loadScript(text_path):
    with open(text_path, "r") as f:
        return json.load(f)
script = loadScript(text_path)

def scene1(script, surface, font, color, pos):
    scene = script.get("scene1", [])
    # Iteration function
    for line in scene:
        typeSoundDavid(line, surface, font, color, pos)
        time.sleep(1)

