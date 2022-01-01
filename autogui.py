import pyautogui
from time import sleep


sleep(6)
pyautogui.screenshot('map_current.png', region=(0,0, 2560, 1080))

pt = list(pyautogui.locateAllOnScreen('wall3.png'))
print(len(pt))

print('rock')

pt = list(pyautogui.locateAllOnScreen('rock3.png' ))
print(len(pt))