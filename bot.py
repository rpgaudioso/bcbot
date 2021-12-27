from re import S
from time import sleep
import mouse
import pygetwindow
import logging
import pyautogui
import datetime


# ---------------------------------------------------
# Properties
# ---------------------------------------------------
KEEP_ALIVE_SEC = 240 
FARM_CICLE_MAX = 12  # 48 min
FARM_CICLE_MED = 8   # 32 min
FARM_CICLE_MIN = 4   # 16 min
WAIT_SEC = 1.5
WAIT_SIGN_IN = 10
SCROLL_DELAY = .03
MOVE_SEC = .2
HERO_STRIP_HEIGHT = 44
HERO_STRIP_DIVIDER = 6
HERO_FIRST_POS_Y = -260
HERO_TOTAL_HEIGHT = 255
TOTAL_HEROS = 15
TOTAL_SCREENS = 4

activeHeroesQuatity = 0
actualPos = 0
farmCicle = 8

# ---------------------------------------------------
# Methods
# ---------------------------------------------------
def screenSetup():
    for screen in range(4):
        win = pygetwindow.getWindowsWithTitle('Bombcrypto - Google Chrome')[screen]
        win.size = (720, 540)
        if (screen == 0):
            win.moveTo(0,0)
        elif (screen == 1):
            win.moveTo(700,0)
        elif (screen == 2):
            win.moveTo(0,520)
        elif (screen == 3):
            win.moveTo(700,520)
        

def findHeroesMenu(screen):
    if (screen == 1):
        mouse.move(365, 480, True, MOVE_SEC)
    elif (screen == 2):
        mouse.move(1065, 480, True, MOVE_SEC)
    elif (screen == 3):
        mouse.move(365, 1000, True, MOVE_SEC)
    elif (screen == 4):
        mouse.move(1065, 1000, True, MOVE_SEC)


def openHeroesMenu():
    mouse.click()
    sleep(WAIT_SEC)
    mouse.click()


def scrolDownHeroesMenu():
    mouse.move(-150,-46,False, MOVE_SEC)
    sleep(WAIT_SEC)
    mouse.drag(0,0,0,-250,False, MOVE_SEC)
    sleep(WAIT_SEC)
    mouse.move(0,242,False, MOVE_SEC)
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
    global activeHeroesQuatity
    global actualPos
    activeHeroesQuatity += 1 
    actualPos -= 1
    logging.debug("actualPos: {}".format(actualPos))
    logging.debug("A hero goes to work. Total working heroes: {}".format(activeHeroesQuatity))


def putHeroesToRest(total=15):
    global activeHeroesQuatity

    logging.info("Put heroes to rest...")
    mouse.move(-15, HERO_FIRST_POS_Y, False, MOVE_SEC)
    sleep(WAIT_SEC)

    for x in range(total):
        mouse.click()
        sleep(WAIT_SEC)

    activeHeroesQuatity = 0
    mouse.move(15, -HERO_FIRST_POS_Y, False, MOVE_SEC)
    logging.info("Put heroes to rest - done!")



def selectHero(position):
    logging.debug("Select hero in position: {}".format(position))
    global actualPos
    
    delta = actualPos - position
    delta2 = 0
    logging.debug("-------------------- actualPos: {}  --- position: {} --> Delta: {}".format(actualPos,position, delta))

    if (delta + activeHeroesQuatity >= 9 ):
        delta2 = delta - 9
       
    

    logging.debug("scroll up for {} times".format(delta))
    for x in range(delta):
        for y in range(4):
            mouse.wheel(1)
            sleep(SCROLL_DELAY)
        sleep(WAIT_SEC)
        actualPos -= 1
    

    if (delta2 != 0):
        mouse.move(0, -16, False, MOVE_SEC)
        sleep(WAIT_SEC) 
        logging.debug("move mouse up for {} times".format(delta2))
        for x in range(delta2):
            mouse.move(0, ((HERO_STRIP_DIVIDER/2) + HERO_STRIP_HEIGHT)*-1,False, MOVE_SEC )
            sleep(MOVE_SEC)
            actualPos -= 1


    logging.debug("actualPos: {}".format(actualPos))
    sleep(WAIT_SEC) 


def getHeroesPosToWork(screen):
    
    if (farmCicle == FARM_CICLE_MIN):
        logging.info("getting fastest heroes...")
        if (screen == 1):
            # heroes = [13,2,5]
            heroes = [13,2,5,9,12]
        elif (screen == 2):
            # heroes = [14,6,1,2]
            heroes = [14,6,1,2,3]
        elif (screen == 3):
            # heroes = [7,13,10,11]
            heroes = [7,13,10,11,1]
        elif (screen == 4):
            # heroes = [5,8,10,2]
            heroes = [5,8,10,2,13]

    if (farmCicle == FARM_CICLE_MED):
        logging.info("getting not so fastest heroes...")
        if (screen == 1):
            # heroes = [9,12,14,15]
            heroes = [14,15,4,6,7]
        elif (screen == 2):
            # heroes = [8,7,12,4,15]
            heroes = [4,15]
        elif (screen == 3):
            # heroes = [1,6,12,3,8]
            # heroes = [6,12,3,8,9,15]
            heroes = [1]
        elif (screen == 4):
            heroes = [15,4,6,14,3]
            # heroes = [1]

    elif (farmCicle == FARM_CICLE_MAX):
        logging.info("getting slowest heroes...")
        if (screen == 1):
            heroes = [10,11,1,3,8]
        elif (screen == 2):
            heroes = [11,13,5,9,10]
        elif (screen == 3):
            # heroes = [9,15,4,5,2,11,14]
            heroes = [4,5,2,11,14]
        elif (screen == 4):
            heroes = [11,12,9,1,7]
    
    heroes.sort(reverse=True)
    return heroes


def startTeamWork(screen):
    global actualPos
    actualPos = 15

    heroesPosToWork = getHeroesPosToWork(screen)
    logging.info("Heroes going to work by their positions: {}".format(heroesPosToWork))

    for position in heroesPosToWork:
        selectHero(position)
        doWorkAction()

def goToMainMenu(screen):
    findHeroesMenu(screen)
    mouse.move(-290, -370, False, MOVE_SEC)
    mouse.click()

def goToTreasureHunt(screen):
    findHeroesMenu(screen)
    mouse.move(0, -190, False, MOVE_SEC)
    mouse.click()

def startFarm(screen):
    findHeroesMenu(screen)
    openHeroesMenu()
    putHeroesToRest(5)
    scrolDownHeroesMenu()
    prepareToWork()
    startTeamWork(screen)
    closeHeroesMenu(screen)


def keepAlive():
    global farmCicle
    farmCicle += 1
    logging.info("Keep alive running in farm cicle: {}/{}".format(farmCicle, FARM_CICLE_MAX))

    handleSignIn()
    
    for screen in range(TOTAL_SCREENS):
        screen+=1
        handleNewMap()

        if (farmCicle == FARM_CICLE_MAX or farmCicle == FARM_CICLE_MED or farmCicle == FARM_CICLE_MIN):
            logging.info("Starting farm in screen: {}".format(screen))
            startFarm(screen)
        else:
            logging.info("Keeping alive screen: {}".format(screen))
            goToMainMenu(screen)
            goToTreasureHunt(screen)

    handleNewMap()

    if (farmCicle == FARM_CICLE_MAX):
        farmCicle = 0

    nextTick = (datetime.datetime.now() + datetime.timedelta(seconds = KEEP_ALIVE_SEC)).strftime("%b %d %Y %H:%M:%S")

    logging.info("Keep alive ending .. See you again at cicle {} in {}".format(farmCicle+1, nextTick))
    sleep(KEEP_ALIVE_SEC)
    keepAlive()


def handleNewMap():
    logging.debug('Handling new map...')
    pt = pyautogui.locateOnScreen('newMap.png')
    
    logging.debug(pt)

    if(pt):
        ptCenter = pyautogui.center(pt)
        logging.debug(ptCenter)
        pyautogui.click(ptCenter)

    logging.debug('Handling new map - done!')


def handleSignIn():
    logging.debug('Handling sign in...')
    finded = findBtAndClick('connectWallet')
    if (finded == True):
        sleep(WAIT_SIGN_IN)
        findBtAndClick('signIn')
        sleep(WAIT_SIGN_IN)
        #loading...
        findBtAndClick('treasureHunt')
        sleep(WAIT_SEC)
    logging.debug('Handling sing in - done!')



def findBtAndClick(name):
    pt = pyautogui.locateOnScreen('{}.png'.format(name))
    if(pt):
        logging.info('Button {} finded! Center and clickin it!'.format(name))
        ptCenter = pyautogui.center(pt)
        pyautogui.click(ptCenter)
        return True
    return False

# ---------------------------------------------------
# Main
# ---------------------------------------------------
def main():
    logging.basicConfig(encoding='utf-8', level=logging.DEBUG, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
    # screenSetup()
    # logging.info("Starting bot!!")
    # keepAlive()
    startFarm(3)


main()