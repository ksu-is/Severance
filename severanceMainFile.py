import time
import json
import pygame
import os
from flask import Flask, render_template
from threading import Thread
import logging
import flask.cli
from scene1 import scene1
def loadScript(text_path):
    with open(text_path, "r") as f:
        return json.load(f)
    
flask.cli.show_server_banner = lambda *args, **kwargs: None
logging.getLogger('werkzeug').setLevel(logging.ERROR)

base_path = os.path.dirname(os.path.abspath(__file__))
text_path = os.path.join(base_path, "dialogueScene1.json")

script = loadScript(text_path)
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("myfleshbleedsacidgrey.html")

def run_flask():
    app.run(debug=False, use_reloader=False)

base_path = os.path.dirname(os.path.abspath(__file__))
sound_path = os.path.join(base_path, "Sounds", "bleep030.mp3")
pygame.mixer.init()
blipSound = pygame.mixer.Sound(sound_path)

def main():
    flask_thread = Thread(target=run_flask)
    flask_thread.daemon = True
    flask_thread.start()
    
   
    pygame.init()
    screen = pygame.display.set_mode((600, 400))
    pygame.display.set_caption("AESOPWEBUI.EXE")
    font = pygame.font.SysFont("consolas", 14)
    pos = (50,250)
    color = (255,255,255)
    WHITE = (255, 255, 255)
    scene1(script, screen, font, color, pos)

    pygame.quit()

if __name__ == "__main__":
    main()