from time import sleep
import mouse
import pygetwindow

# ---------------------------------------------------
# Properties
# ---------------------------------------------------
WAIT_SEC = 1
KEEP_ALIVE_SEC = 20
SCROLL_DELAY = .1
MOVE_SEC = .2
HERO_STRIP_HEIGHT = 44
HERO_STRIP_DIVIDER = 6
HERO_FIRST_POS_Y = -260
HERO_TOTAL_HEIGHT = 255
TOTAL_HEROS = 15
TOTAL_SCREENS = 4


heroes_working = 0
actualPos = 0
keepAliveCounter = 0

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
        

def findHeroesMenu(x=1):
    if (x == 1):
        mouse.move(365, 480, True, MOVE_SEC)
    elif (x == 2):
        mouse.move(1065, 480, True, MOVE_SEC)
    elif (x == 3):
        mouse.move(365, 1000, True, MOVE_SEC)
    elif (x == 4):
        mouse.move(1065, 1000, True, MOVE_SEC)


def openHeroesMenu():
    mouse.click()
    sleep(WAIT_SEC)
    mouse.click()


def scrolDownHeroesMenu():
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


def closeHeroesMenu(screen):
    findHeroesMenu(screen)
    mouse.move(40,-320,False, MOVE_SEC)
    sleep(WAIT_SEC)
    mouse.click()
    sleep(WAIT_SEC)
    mouse.move(0,100,False, MOVE_SEC)
    sleep(WAIT_SEC)
    mouse.click()
    sleep(WAIT_SEC)


def prepareToWork():
    mouse.move(100, 0, False, MOVE_SEC)
    sleep(WAIT_SEC)


def doWorkAction():
    mouse.click()
    sleep(WAIT_SEC)
    global heroes_working
    heroes_working += 1 
    print("A hero goes to work. Total working heroes: {}".format(heroes_working))


def putHeroesToRest(total=15):
    global heroes_working

    print("Put heroes to rest...")
    mouse.move(-15, HERO_FIRST_POS_Y, False, MOVE_SEC)
    sleep(WAIT_SEC)

    for x in range(total):
        mouse.click()
        sleep(WAIT_SEC)

    heroes_working = 0
    mouse.move(15, -HERO_FIRST_POS_Y, False, MOVE_SEC)
    print("Put heroes to rest - done!")


def selectHero(delta):
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


def getHeroesPosToWork():
    heros =  [1,5,15,11,14,9]
    # heros =  [4]
    heros.sort(reverse=True)

    return heros

def startTeamWork():
    global actualPos
    actualPos = 0
    delta = 0

    heroesPosToWork = getHeroesPosToWork()
    print("Heroes going to work by positions: {}".format(heroesPosToWork))

    for herosPos in heroesPosToWork:
        print("Finding hero in position: {}".format(herosPos))
        delta = TOTAL_HEROS-herosPos-actualPos-heroes_working
        selectHero(delta)
        doWorkAction()



def startFarm(screen):
    findHeroesMenu(screen)
    openHeroesMenu()
    putHeroesToRest(1)
    scrolDownHeroesMenu()
    prepareToWork()
    startTeamWork()


def keepAlive():
    global keepAliveCounter
    print("Keep alive running: {}".format(keepAliveCounter))
    keepAliveCounter += 1

    for screen in range(TOTAL_SCREENS):
        screen+=1
        findHeroesMenu(screen)
        openHeroesMenu()
        closeHeroesMenu(screen)
        
        if (keepAliveCounter%5 == 0):
            print('iniciando farm')
            # startFarm(screen)

    if (keepAliveCounter%5 == 0):
        keepAliveCounter = 0

    print("Keep alive ending .. See you agin in {} seconds!".format(KEEP_ALIVE_SEC))
    sleep(KEEP_ALIVE_SEC)
    keepAlive()

# ---------------------------------------------------
# Main
# ---------------------------------------------------
def main():
    # screenSetup()
    keepAlive()

main()