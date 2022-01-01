import pyautogui
import mouse
from time import sleep

# ---------------------------------------------------
# Methods
# ---------------------------------------------------
def getObjList(type, confidence=0.94):
    return list(pyautogui.locateAllOnScreen('objs/{}.png'.format(type), confidence=confidence))


walls = getObjList('wall')
print('walls: {}'.format(len(walls)))

rocks = getObjList('rock')
print('rocks: {}'.format(len(rocks)))

woods =  getObjList('wood', 0.9)
print('woods: {}'.format(len(woods)))

irons =  getObjList('iron')
print('irons: {}'.format(len(irons)))

# golds =  getObjList('gold')
# print('golds: {}'.format(len(golds)))

# crystals =  getObjList('crystal')
# print('crystals: {}'.format(len(crystals)))

# jails =  getObjList('jail')
# print('jails: {}'.format(len(jails)))

for item in woods:
    mouse.move((item.left+(item.width/2)), (item.top+(item.height/2)), True, 0.3)
    sleep(0.4)
