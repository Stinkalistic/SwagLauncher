import os
import subprocess
import keyboard
import time
selected = 0
options = ["Add Game"]
buttons = ["Add Game"]
gamepaths = []     
idx=0  
def load_games():
    global buttons,lines,idx
    with open("data//games.txt","r") as file:
            lines = [line.strip() for line in file.readlines()]
            if len(lines)>1:
                for i in range(len(lines) // 2):
                    if idx <len(lines):
                        buttons.append(lines[idx])
                        idx+=1
                    else:
                        break
                    gamepaths.append(lines[idx])
                    idx+=1
load_games()
def clear_console():
    command = 'cls' if os.name in ('nt', 'dos') else 'clear'
    os.system(command)
def update():
    global options
    clear_console()
    #print(len(buttons),selected)
    options = buttons.copy()
    options[selected] = "→" + options[selected] 
    for i in range(len(options)):
        print(options[i])
def add_game(name,path):
       with open("data//games.txt","a") as file:
           file.write(f"{name}\n{path}\n")
update()
while True:
    keypressed = keyboard.read_key()
    if keypressed == "down":
        selected+=1
        if selected>(len(options)-1):
            selected=0
        update()
        time.sleep(0.16)
    elif keypressed == "up":
        selected-=1
        if selected<0:
            selected=(len(options)-1)
        update()
        time.sleep(0.16)
    elif keypressed == "space":
        keyboard.press("backspace")
        if selected == 0:
            name = input("what is the name of the game?")
            path = input("what is the path to the file?")
            print("Saving game path...")
            add_game(name,path)
            load_games()
            update()
        else:
            time.sleep(0.16)
            print("launching game...")
            subprocess.run(gamepaths[selected-1])
            selected = 0
            time.sleep(0.10)
            update()