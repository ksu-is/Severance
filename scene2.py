import time
import json
import os
from TVPCPUTypeSound import typeSoundCPU
from scene1FunctionList import loginFunction
from TVPDavidTypeSound import typeSoundDavid
from TVPJacobTypeSound import typeSoundJacob
base_path = os.path.dirname(os.path.abspath(__file__))
text_path = os.path.join(base_path, "dialogueScene2.json")

def loadScript(text_path):
    with open(text_path, "r") as f:
        return json.load(f)
    
script = loadScript(text_path)

def scene2(script, surface, font, color, pos):
    scene = script.get("scene1", [])
    time.sleep(3)

    # Iteration function
    for line in scene:
        if "textCPU" in line:
            typeSoundCPU(line["textCPU"], surface, font, color, pos)
            time.sleep(1)
        elif "textDavid" in line:
            typeSoundDavid(line["textDavid"], surface, font, color, pos)
            time.sleep(1)
        elif "textJacob" in line:
            typeSoundJacob(line["textJacob"], surface, font, color, pos)
            time.sleep(1)
        elif "sleep" in line:
            time.sleep(line["sleep"])
        else:
            for key in line:
                match key:
                    case "loginFunction":
                        loginFunction(surface, font, color, pos)
                    case "fileInvestigation":
                        #fileInvestigation(surface, font, color, pos)
                        pass
