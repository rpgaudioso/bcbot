from time import sleep
import mouse
import pygetwindow

# ---------------------------------------------------
# Properties
# ---------------------------------------------------
WAIT_SEC = 1
SCROLL_DELAY = .1
MOVE_SEC = .4
HERO_STRIP_HEIGHT = 44
HERO_STRIP_DIVIDER = 6
HERO_FIRST_POS_Y = -260
HERO_TOTAL_HEIGHT = 255

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
    mouse.move(-100,-46,False, MOVE_SEC)
    sleep(WAIT_SEC)
    mouse.drag(0,0,0,-200,False, MOVE_SEC)
    sleep(WAIT_SEC)
    mouse.move(0,200,False, MOVE_SEC)
    sleep(WAIT_SEC)
    mouse.drag(0,0,0,-200,False, MOVE_SEC)
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

def scroll(qtd=1, dir=-1):
    hero = 1

    for x in range(qtd):
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
            mouse.move(0, ((HERO_STRIP_DIVIDER/2) + HERO_STRIP_HEIGHT)*-dir,False, MOVE_SEC )
            sleep(WAIT_SEC)

# ---------------------------------------------------
# Main
# ---------------------------------------------------
# screenSetup()
# findHeroMenu(1)
# openHeroMenu()
# scrolDownHeroMenu()
# selecHeroes(1,2)
# closeHeroMenu(1)


# findHeroMenu(3)
# openHeroMenu()
# scrolDownHeroMenu()
# selecHeroes(3,2)
# closeHeroMenu(3)


findHeroMenu(1)
openHeroMenu()

HEROS_WORKING = 0
HEROS_ORDER = [3,5,1,7,9,2]

mouse.move(-150, HERO_FIRST_POS_Y, False, MOVE_SEC)
sleep(WAIT_SEC)

scroll(14);
# scroll(1,1);

# mouse.move(0, HERO_STRIP_HEIGHT, False, MOVE_SEC)


# HERO_STRIP_HEIGHT = 44
# HERO_STRIP_DIVIDER = 6

sleep(WAIT_SEC)
# closeHeroMenu(1)


