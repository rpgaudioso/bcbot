from time import sleep
import mouse
import pygetwindow

# ---------------------------------------------------
# Properties
# ---------------------------------------------------
WAIT_SEC = 1
SCROLL_DELAY = .1
MOVE_SEC = .2
HERO_STRIP_HEIGHT = 44
HERO_STRIP_DIVIDER = 6
HERO_FIRST_POS_Y = -260
HERO_TOTAL_HEIGHT = 255
TOTAL_HEROS = 15

heros_working = 0
actualPos = 0

# ---------------------------------------------------
# Methods
# ---------------------------------------------------
def screenSetup():
    for x in range(4):
        win = pygetwindow.getWindowsWithTitle('Bombcrypto - Google Chrome')[x]
        win.size = (720, 540)
        if (x == 0):
            win.moveTo(0,0)
        elif (x == 1):
            win.moveTo(700,0)
        elif (x == 2):
            win.moveTo(0,520)
        elif (x == 3):
            win.moveTo(700,520)
        

def findHeroMenu(x=1):
    if (x == 1):
        mouse.move(365, 480, True, MOVE_SEC)
    elif (x == 2):
        mouse.move(1065, 480, True, MOVE_SEC)
    elif (x == 3):
        mouse.move(365, 1000, True, MOVE_SEC)
    elif (x == 4):
        mouse.move(1065, 1000, True, MOVE_SEC)


def openHeroMenu():
    mouse.click()
    sleep(WAIT_SEC)
    mouse.click()


def scrolDownHeroMenu():
    mouse.move(-150,-46,False, MOVE_SEC)
    sleep(WAIT_SEC)
    mouse.drag(0,0,0,-200,False, MOVE_SEC)
    sleep(WAIT_SEC)
    mouse.move(0,200,False, MOVE_SEC)
    sleep(WAIT_SEC)
    mouse.drag(0,0,0,-200,False, MOVE_SEC)
    sleep(WAIT_SEC)
    mouse.move(0,192,False, MOVE_SEC)
    sleep(WAIT_SEC)


def closeHeroMenu(screen=1):
    findHeroMenu(screen)
    mouse.move(40,-320,False, MOVE_SEC)
    sleep(WAIT_SEC)
    mouse.click()
    sleep(WAIT_SEC)
    mouse.move(0,100,False, MOVE_SEC)
    sleep(WAIT_SEC)
    mouse.click()
    sleep(WAIT_SEC)


def selecHeroes(screen=1, qt=15):
    findHeroMenu(screen)
    sleep(WAIT_SEC)
    mouse.move(-50, -50, False, MOVE_SEC)
    sleep(WAIT_SEC)
    # for x in range(qt):
    #     sleep(WAIT_SEC)
    #     mouse.click()

def selectHero(qtd=1, dir=-1):
    hero = 1

    mouse.move(-150, HERO_FIRST_POS_Y, False, MOVE_SEC)
    sleep(WAIT_SEC)

    for x in range(qtd-1):
        if(x < 10):
            print("scroll")
            for y in range(4):
                mouse.wheel(dir)
                sleep(SCROLL_DELAY)
            sleep(SCROLL_DELAY)
        else:
            if(x == 10):
               sleep(WAIT_SEC)
               mouse.move(0, 16, False)

            print("move mouse")
            mouse.move(0, ((HERO_STRIP_DIVIDER/2) + HERO_STRIP_HEIGHT)*-dir,False, SCROLL_DELAY )
            sleep(SCROLL_DELAY)





def prepareToWork():
    mouse.move(100, 0, False, MOVE_SEC)
    sleep(WAIT_SEC)


def work():
    mouse.click()
    sleep(WAIT_SEC)
    global heros_working
    heros_working += 1 
    print("A hero goes to work. Total working: {}".format(heros_working))


def prepareToRest():
    mouse.move(140, 0, False, MOVE_SEC)


def rest():
    mouse.click()
    sleep(WAIT_SEC)
    global heros_working
    heros_working -= 1 
    print(heros_working)


def restAll(total=15):
    mouse.move(140, 0, False, MOVE_SEC)
    for x in range(total):
        mouse.click()
        sleep(WAIT_SEC)
    mouse.move(-140, 0, False, MOVE_SEC)
    

def selectHeroDtU(delta):
    print("Select hero - delta: {}".format(delta))
    global actualPos
    delta2 = 0
    if(delta > 10):
        delta2 = delta -10
        delta = 10

    print("scroll up for {} times".format(delta))
    for x in range(delta):
        for y in range(4):
            mouse.wheel(1)
            sleep(SCROLL_DELAY)
        sleep(WAIT_SEC)
        actualPos += 1
    
    if(delta2 != 0):
        mouse.move(0, -16, False)
        sleep(WAIT_SEC)
        print("move mouse up for {} times".format(delta2))
        for x in range(delta2):
            mouse.move(0, ((HERO_STRIP_DIVIDER/2) + HERO_STRIP_HEIGHT)*-1,False, SCROLL_DELAY )
            sleep(SCROLL_DELAY)
            actualPos += 1

    print("actualPos: {}".format(actualPos))


def workList():
    delta = 0

    print("Heros to work: {}".format(HEROS_ORDER))

    for herosPos in HEROS_ORDER:
        global actualPos
        print("Finding hero pos: {}".format(herosPos))
        delta = TOTAL_HEROS-herosPos-actualPos-heros_working
        selectHeroDtU(delta)
        work()

# ---------------------------------------------------
# Main
# ---------------------------------------------------
# screenSetup()

HEROS_WORKING = 0
HEROS_ORDER = [1,5,10,15,14,12]
HEROS_ORDER.sort(reverse=True)

findHeroMenu(4)
openHeroMenu()
scrolDownHeroMenu()
prepareToWork()
workList()

# 1  539 sapo
# 5  543 kina
# 10 548 ninja
# 12 936 vamp
# 14 938 doge
# 15 939 chapeu