import pyautogui
import mouse
from time import sleep

# ---------------------------------------------------
# Methods
# ---------------------------------------------------
def getObjList(type, confidence=0.92):
    return list(pyautogui.locateAllOnScreen('imgs/items/new/{}.png'.format(type), confidence=confidence))


def getRocksQtt():
    rocks = getObjList('rock1')
    if (rocks == []):
        rocks = getObjList('rock2')
    # print('rocks: {}'.format(len(rocks)))
    return len(rocks)

def getChestsQtt():
    woods =  getObjList('wood')
    if (woods == []):
        woods = getObjList('wood2')
    # print('woods: {}'.format(len(woods)))

    irons =  getObjList('iron')
    # print('irons: {}'.format(len(irons)))

    golds =  getObjList('gold')
    if (golds == []):
        golds = getObjList('gold2')
    # print('golds: {}'.format(len(golds)))

    crystals =  getObjList('crystal', confidence=0.84)
    # print('crystals: {}'.format(len(crystals)))

    return len(woods)+len(irons)+len(golds)+len(crystals)

sleep(6)
print(getRocksQtt())
print(getChestsQtt())



# jails =  getObjList('jail')
# print('jails: {}'.format(len(jails)))

# for item in woods:
#     mouse.move((item.left+(item.width/2)), (item.top+(item.height/2)), True, 0.3)
#     sleep(0.4)
