import pygame
import time
from TVPCPUTypeSound import typeSoundCPU
import webbrowser
from TVPDavidTypeSound import typeSoundDavid
import os
import subprocess

base_path = os.path.dirname(os.path.abspath(__file__))
folder_path = os.path.join(base_path, "FILES")

def screenRefresh(surface, font, color, pos, text_surfaces, input_text):
    # Clear the screen
    surface.fill((0, 0, 0))
    for i, line_surface in enumerate(text_surfaces):
        surface.blit(line_surface, (pos[0], pos[1] + i * font.get_linesize()))
    input_pos = (pos[0], pos[1] + (len(text_surfaces) + 1) * font.get_linesize())
    input_surface = font.render(input_text, True, color)
    surface.blit(input_surface, input_pos)
    pygame.display.flip()

def loginFunction(surface, font, color, pos):
    input_text = ""
    codeFound = False
    commsRepaired = False

    typeSoundCPU("WELCOME TO VISHNU WEB INTERFACES", surface, font, color, pos, delay=0.06, sound_enabled=True)
    time.sleep(1)
    typeSoundCPU("ALERT: NEW FILES DETECTED IN DIRECTORY", surface, font, color, pos, delay=0.06, sound_enabled=True)
    time.sleep(1)  
    
    text_surfaces = typeSoundCPU("PLEASE SELECT A COMMAND: 1. LOGIN AS ADMINISTRATOR 2. CONNECT TO EXTERNAL URL. 3. ACCESS FILES. 4.  TROUBLESHOOT SYSTEMS.", surface, font, color, pos, delay=0.06, sound_enabled=True)
    time.sleep(1)

    # Loop until the user selects a valid option

    while not commsRepaired:
        screenRefresh(surface, font, color, pos, text_surfaces, input_text)
        # Check for events

        for event in pygame.event.get():    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                    if input_text == "1":
                        if codeFound:
                            text_surfaces = typeSoundDavid("I don't need to do that anymore.", surface, font, color, pos, delay=0.08, sound_enabled=True)
                            time.sleep(1)
                            input_text = ""
                            text_surfaces = typeSoundCPU("PLEASE SELECT A COMMAND: 1. LOGIN AS ADMINISTRATOR 2. CONNECT TO EXTERNAL URL. 3. ACCESS FILES. 4.  TROUBLESHOOT SYSTEMS.", surface, font, color, pos, delay=0.06, sound_enabled=True)
                            # Checks if user has completed the login puzzle, if not, it will prompt for the password

                        else:
                            input_text = ""
                            inMainMenu = False
                            text_surface1 = typeSoundCPU("WARNING: ACCESS TO ADMINISTRATOR ACCOUNT 'Jacob' HAS NOT BEEN GRANTED. PLEASE ENTER ADMINISTRATOR PASSWORD:", surface, font, color, pos, delay=0.06, sound_enabled=True)
                            while not inMainMenu:
                                screenRefresh(surface, font, color, pos, text_surface1, input_text) 
                                for event in pygame.event.get():
                                    if event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                                            if "concious" in input_text.lower() or "conscious" in input_text.lower():
                                                input_text = ""
                                                text_surface1 = typeSoundCPU("INCORRECT PASSWORD. ADMINISTRATIVE CLEARANCE NOT GRA.", surface, font, color, pos, delay=0.06, sound_enabled=True)
                                                text_surface1 = typeSoundCPU("%*()UFSD*(FH(*H#(*RH(*&*#@%(^EEEXXX*F&H(G*&(*)).", surface, font, color, pos, delay=0, sound_enabled=True)
                                                time.sleep(0.5)
                                                text_surface1 = typeSoundCPU("ERROR", surface, font, color, pos, delay=0.06, sound_enabled=True)
                                                time.sleep(1)
                                                text_surface1 = typeSoundCPU("ERROR", surface, font, color, pos, delay=0.06, sound_enabled=True)
                                                text_surface1 = typeSoundCPU("ERROR", surface, font, color, pos, delay=0.06, sound_enabled=True)
                                                text_surface1 = typeSoundCPU("ERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERROR", surface, font, color, pos, delay=0.002, sound_enabled=True)
                                                surface.fill((0, 0, 0))
                                                pygame.display.flip()
                                                time.sleep(3)
                                                text_surface1 = typeSoundDavid("...", surface, font, color, pos, delay=0.2, sound_enabled=True)
                                                time.sleep(2)
                                                text_surface1 = typeSoundDavid("...I remember the password now. It's 'DavidXJacob',  of course...", surface, font, color, pos, delay=0.2, sound_enabled=True)
                                                time.sleep(2)
                                                text_surface1 = typeSoundCPU("PASSWORD ACCEPTED. WELCOME BACK ADMINISTRATOR JACOB", surface, font, color, pos, delay=0.06, sound_enabled=True)
                                                time.sleep(1)
                                                text_surface1 = typeSoundCPU("PLEASE SELECT A COMMAND: 1. LOGIN AS ADMINISTRATOR 2. CONNECT TO EXTERNAL URL. 3. ACCESS FILES. 4.  TROUBLESHOOT SYSTEMS.", surface, font, color, pos, delay=0.06, sound_enabled=True)
                                                codeFound = True
                                                inMainMenu = True
                                                # If the user enters "conscious" or "concious", it will allow access to the main menu and set codeFound to True
                                        
                                            else:
                                                text_surface2 = typeSoundCPU("INCORRECT PASSWORD. ADMINISTRATIVE CLEARANCE NOT GRANTED.", surface, font, color, pos, delay=0.06, sound_enabled=True)
                                                time.sleep(1)
                                                input_text = ""
                                                text_surface1 = typeSoundCPU("PLEASE SELECT A COMMAND: 1. LOGIN AS ADMINISTRATOR 2. CONNECT TO EXTERNAL URL. 3. ACCESS FILES. 4.  TROUBLESHOOT SYSTEMS.", surface, font, color, pos, delay=0.06, sound_enabled=True)
                                                inMainMenu = True
                                                # If the user enters anything else, it will return to the main menu.
                                            
                                        elif event.key == pygame.K_BACKSPACE:
                                            input_text = input_text[:-1]
                                            # If the user presses backspace, it will remove the last character from the input_text variable.
                                        else:
                                            input_text += event.unicode
                                            # If the user presses any other key, it will add the character to the input_text variable.
                    elif input_text == "2":
                        if codeFound:
                            text_surfaces = typeSoundDavid("I need to get comms up again.", surface, font, color, pos, delay=0.08, sound_enabled=True)
                            time.sleep(1)
                            input_text = ""
                            text_surfaces = typeSoundCPU("PLEASE SELECT A COMMAND: 1. LOGIN AS ADMINISTRATOR 2. CONNECT TO EXTERNAL URL. 3. ACCESS FILES. 4.  TROUBLESHOOT SYSTEMS.", surface, font, color, pos, delay=0.06, sound_enabled=True)
                            # Checks if user has completed the login puzzle, if not, it will prompt for a URL
                        else:
                            inMainMenu = False
                            text_surface2 = typeSoundCPU("ENTER CONNECTION URL (CASE SENSITIVE), OR PRESS Q TO GO BACK", surface, font, color, pos, delay=0.06, sound_enabled=True)
                            input_text = ""
                            while not inMainMenu:
                                screenRefresh(surface, font, color, pos, text_surface2, input_text)
                                # Check for events
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        pygame.quit()
                                        exit()
                                    if event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                                            if input_text.lower() == "q":
                                                input_text = ""
                                                inMainMenu = True
                                            else:
                                                text_surface2 = typeSoundCPU("ATTEMPTING TO OPEN URL...", surface, font, color, pos, delay=0.06, sound_enabled=True)
                                                webbrowser.open(input_text)
                                                time.sleep(1)
                                                input_text = ""
                                                inMainMenu = True
                                            
                                        elif event.key == pygame.K_BACKSPACE:
                                            input_text = input_text[:-1]
                                            # If the user presses backspace, it will remove the last character from the input_text variable.
                                        else:
                                            input_text += event.unicode
                                        # If the user presses any other key, it will add the character to the input_text variable.
                    elif input_text == "3":
                        if codeFound:
                            text_surfaces = typeSoundDavid("I don't need to do that anymore.", surface, font, color, pos, delay=0.08, sound_enabled=True)
                            time.sleep(1)
                            input_text = ""
                            text_surfaces = typeSoundCPU("PLEASE SELECT A COMMAND: 1. LOGIN AS ADMINISTRATOR 2. CONNECT TO EXTERNAL URL. 3. ACCESS FILES. 4.  TROUBLESHOOT SYSTEMS.", surface, font, color, pos, delay=0.06, sound_enabled=True)
                            # Checks if user has completed the login puzzle, if not, it will prompt for the file access
                        else:
                            text_surfaces = typeSoundCPU("ACCESSING FILES..", surface, font, color, pos, delay=0.06, sound_enabled=True)
                            subprocess.Popen(f'explorer "{folder_path}"', shell=True)
                            # Opens the folder in a new window
                            time.sleep(1)
                            input_text = ""
                            text_surfaces = typeSoundCPU("PLEASE SELECT A COMMAND: 1. LOGIN AS ADMINISTRATOR 2. CONNECT TO EXTERNAL URL. 3. ACCESS FILES. 4.  TROUBLESHOOT SYSTEMS.", surface, font, color, pos, delay=0.06, sound_enabled=True)
                    elif input_text == "4":
                        if codeFound:
                            typeSoundCPU("ENABLING COMMUNICATIONS RELAY...", surface, font, color, pos, delay=0.06, sound_enabled=True)
                            time.sleep(1)
                            typeSoundCPU("COMMUNICATIONS RELAY ENABLED", surface, font, color, pos, delay=0.06, sound_enabled=True)
                            time.sleep(1)
                            commsRepaired = True
                            input_text = ""
                            return

                        else:
                            text_surfaces = typeSoundCPU("ERROR: ADMINISTRATOR PRIVILAGES REQUIRED TO ALTER COMMUNICATION SYSTEMS", surface, font, color, pos, delay=0.06, sound_enabled=True)
                            time.sleep(1)
                            input_text = ""
                            text_surfaces = typeSoundCPU("PLEASE SELECT A COMMAND: 1. LOGIN AS ADMINISTRATOR 2. CONNECT TO EXTERNAL URL. 3. ACCESS FILES. 4.  TROUBLESHOOT SYSTEMS.", surface, font, color, pos, delay=0.06, sound_enabled=True)

                    else:
                        input_text = ""
                        typeSoundCPU("INVALID SELECTION. TRY AGAIN", surface, font, color, pos, delay=0.06, sound_enabled=True)
                        time.sleep(1)
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    input_text += event.unicode
        pygame.time.Clock().tick(30)