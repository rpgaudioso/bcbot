import pyautogui
import mouse
from time import sleep

# ---------------------------------------------------
# Methods
# ---------------------------------------------------
def getObjList(type, confidence=0.94):
    return list(pyautogui.locateAllOnScreen('imgs/items/{}.png'.format(type), confidence=confidence))

sleep(6)

walls = getObjList('wall')
if (walls == []):
    walls = getObjList('wall2')
print('walls: {}'.format(len(walls)))

rocks = getObjList('rock')
if (rocks == []):
    rocks = getObjList('rock2')
print('rocks: {}'.format(len(rocks)))

woods =  getObjList('wood', 0.9)
if (woods == []):
    woods = getObjList('wood2', 0.92)
print('woods: {}'.format(len(woods)))

irons =  getObjList('iron')
if (irons == []):
    irons = getObjList('iron2')
print('irons: {}'.format(len(irons)))

golds =  getObjList('gold')
if (golds == []):
    golds = getObjList('gold2')
print('golds: {}'.format(len(golds)))

crystals =  getObjList('crystal')
if (crystals == []):
    crystals = getObjList('crystal2')
print('crystals: {}'.format(len(crystals)))

# jails =  getObjList('jail')
# print('jails: {}'.format(len(jails)))

# for item in woods:
#     mouse.move((item.left+(item.width/2)), (item.top+(item.height/2)), True, 0.3)
#     sleep(0.4)
