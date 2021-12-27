import pyautogui
from time import sleep


def findBtAndClick(name):
    pt = pyautogui.locateOnScreen('{}.png'.format(name))
    print(pt)
    if(pt):
        ptCenter = pyautogui.center(pt)
        pyautogui.click(ptCenter)


findBtAndClick('connectWallet')
sleep(10)
findBtAndClick('signIn')
