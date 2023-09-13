import time
from random import random
import pyautogui

bookmark_xy = (630, 85)
login_xy = (1080, 360)
first_button_xy = (1640, 350)
button_count = 7
button_color = (51, 122, 183)
hovered_color = (40, 96, 144)
stop_x_limit = 400

# get coordinates
# while True:
#     print(pyautogui.position())
#     input()
#     time.sleep(0.5)

while True:
    im = pyautogui.screenshot()
    if im.getpixel(bookmark_xy) == button_color:
        pyautogui.click(*bookmark_xy)
        while True:
            im = pyautogui.screenshot()
            if im.getpixel(bookmark_xy) != hovered_color:
                break
        print('login')
    else:    
        for i in range(button_count):
            x = first_button_xy[0]
            y = first_button_xy[1] + 50 * i
            if im.getpixel((x, y)) == button_color:
                pyautogui.click(x, y)
                break
            pyautogui.moveTo(x, y, duration = 0)
    time.sleep(random()*2)
    if pyautogui.position().x < stop_x_limit:
        break
    pyautogui.click(*bookmark_xy)
    time.sleep(0.2)
    if pyautogui.position().x < stop_x_limit:
        break
