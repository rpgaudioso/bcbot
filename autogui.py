import pyautogui
from time import sleep


# def findBtAndClick(name):
#     pt = pyautogui.locateOnScreen('{}.png'.format(name))
#     print(pt)
#     if(pt):
#         ptCenter = pyautogui.center(pt)
#         pyautogui.click(ptCenter)


# findBtAndClick('connectWallet')
# sleep(10)
# findBtAndClick('signIn')




pyautogui.screenshot('map.png', region=(0,0, 2560, 1080))
# pt = list(pyautogui.locateAllOnScreen('rock.png'))
# print(pt)