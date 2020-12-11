import pyautogui as pag
import keyboard
import time

poc = [805, 280]
pobd = [805, 276]
pobu = [805, 241]
cog = [900, 750]
end = [903, 189]
i = 0


def space():
    pag.keyDown("space")
    time.sleep(0.05)
    pag.keyUp("space")


def down():
    pag.keyDown("down")
    time.sleep(0.2)
    pag.keyUp("down")


while True:
    if keyboard.is_pressed("space"):
        while True:
            if pag.pixel(cog[0], cog[1])[0] < 255:
                if pag.pixel(poc[0], poc[1])[0] != 32 or pag.pixel(pobd[0], pobd[1])[0] != 32:
                    space()
                if pag.pixel(pobu[0], pobu[1])[0] != 32:
                    down()
            if pag.pixel(cog[0], cog[1])[0] >= 255:
                if pag.pixel(poc[0], poc[1])[0] != 255 or pag.pixel(pobd[0], pobd[1])[0] != 255:
                    space()
                if pag.pixel(pobu[0], pobu[1])[0] != 255:
                    down()
            #  if pag.pixel(end[0], end[1])[0] != 32:
            #      exit(0)
