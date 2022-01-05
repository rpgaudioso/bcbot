
from ctypes.wintypes import RGB
import mouse
import pygetwindow
import logging
import pyautogui
from time import sleep

def checkEnergy():
    EMPTY_COLOR = (197,139,105)
    energy = 90

    mouse.move(-26, 6, False)
    mousePos = pyautogui.position()
 
    if(pyautogui.pixelMatchesColor(mousePos.x, mousePos.y, EMPTY_COLOR , tolerance=10)):
        energy = 50
        mouse.move(-30, 0, False)
        mousePos = pyautogui.position()
        if(pyautogui.pixelMatchesColor(mousePos.x, mousePos.y, EMPTY_COLOR , tolerance=10)):
            energy = 20

    print(energy)



# mouse.move(328, 466, True, .2)
# mouse.click()
# sleep(.4)
# mouse.click()
# mouse.move(-60, -260, False, .2) # prepare to work hero fist pos

# sleep(2)
# checkEnergy()

mousePos = pyautogui.displayMousePosition()
