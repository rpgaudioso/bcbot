import pyautogui
import mouse
from time import sleep

# ---------------------------------------------------
# Methods
# ---------------------------------------------------
def getObjList(type, confidence=0.8):
    return list(pyautogui.locateAllOnScreen('imgs/items/{}.png'.format(type), confidence=confidence))


def getRocksQtt():
    rocks = getObjList('rock-n')
    # if (rocks == []):
    #     rocks = getObjList('rock2')
    #     if (rocks == []):
    #         rocks = getObjList('rock3')
    # print('rocks: {}'.format(len(rocks)))
    return len(rocks)

def getChestsQtt():
    woods =  getObjList('wood-n', confidence=0.94)
    # if (woods == []):
    #     woods = getObjList('wood2')
    print('woods: {}'.format(len(woods)))

    irons =  getObjList('iron-n')
    print('irons: {}'.format(len(irons)))

    golds =  getObjList('gold-n')
    # if (golds == []):
    #     golds = getObjList('gold2')
    print('golds: {}'.format(len(golds)))

    crystals =  getObjList('crystal-n', confidence=0.84)
    print('crystals: {}'.format(len(crystals)))

    return len(woods)+len(irons)+len(golds)+len(crystals)

sleep(6)
print(getRocksQtt())
print(getChestsQtt())



# jails =  getObjList('jail')
# print('jails: {}'.format(len(jails)))

# for item in woods:
#     mouse.move((item.left+(item.width/2)), (item.top+(item.height/2)), True, 0.3)
#     sleep(0.4)
