import pyautogui
import time
import keyboard
import win32api
import win32con

Y1 = 550
FIELD_1 = [700, Y1]
FIELD_2 = [880, Y1]
FIELD_3 = [1040, Y1]
FIELD_4 = [1190, Y1]
Blue_Black = [16, 20, 19]


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.001)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


f = 0
while True:
    if keyboard.is_pressed("k") is True:
        break
    if keyboard.is_pressed("s") is True:
        f = 1
    if keyboard.is_pressed("q") is True:
        f = 0

    if f == 1:
        if pyautogui.pixel(FIELD_1[0], FIELD_1[1])[0] == 0 or pyautogui.pixel(FIELD_1[0], FIELD_1[1])[0] == 16:
            click(FIELD_1[0], FIELD_1[1])
        if pyautogui.pixel(FIELD_2[0], FIELD_2[1])[0] == 0 or pyautogui.pixel(FIELD_2[0], FIELD_2[1])[0] == 16:
            click(FIELD_2[0], FIELD_2[1])
        if pyautogui.pixel(FIELD_3[0], FIELD_3[1])[0] == 0 or pyautogui.pixel(FIELD_3[0], FIELD_3[1])[0] == 16:
            click(FIELD_3[0], FIELD_3[1])
        if pyautogui.pixel(FIELD_4[0], FIELD_4[1])[0] == 0 or pyautogui.pixel(FIELD_4[0], FIELD_4[1])[0] == 16:
            click(FIELD_4[0], FIELD_4[1])
        if keyboard.is_pressed("q") is True:
            f = 0
        if keyboard.is_pressed("k") is True:
            break
