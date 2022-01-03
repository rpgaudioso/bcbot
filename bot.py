from re import S
from time import sleep
import mouse
import pygetwindow
import logging
import pyautogui
import datetime
import config as cf
import duallog as log

# ---------------------------------------------------
# Properties
# ---------------------------------------------------
# KEEP_ALIVE_SEC = 240 
# FARM_CICLE_MAX = 12  # 48 min
# FARM_CICLE_MED = 8   # 32 min
# FARM_CICLE_MIN = 4   # 16 min
KEEP_ALIVE_SEC = 260 
FARM_CICLE_MAX = 13 
FARM_CICLE_MED = 9  
FARM_CICLE_MIN = 5  
WAIT_SEC = 1.5
WAIT_SIGN_IN = 15
SCROLL_DELAY = .03
MOVE_SEC = .2
HERO_STRIP_HEIGHT = 44
HERO_STRIP_DIVIDER = 6
HERO_FIRST_POS_Y = -260
HERO_TOTAL_HEIGHT = 255
TOTAL_HEROS = 15
TOTAL_SCREENS = 4

activeHeroesQuatity = 0
currentPos = 0
farmCicle = 7

# TODO: think about maintenance time
STOP_TIME = datetime.time( 6,0,0 ) # Time, without a date
START_TIME = datetime.time( 7,30,0 ) # Time, without a date
onOff = True



# ---------------------------------------------------
# Methods
# ---------------------------------------------------


def screenSetup():
    for screen in range(4):
        win = pygetwindow.getWindowsWithTitle('Bombcrypto - Google Chrome')[screen]
        # win.size = (720, 540)
        win.size = (658, 516)
        if (screen == 0):
            win.moveTo(0,0)
        elif (screen == 1):
            win.moveTo(650,0)
        elif (screen == 2):
            win.moveTo(0,520)
        elif (screen == 3):
            win.moveTo(650,520)
        

def findHeroesMenu(screen):
    if (screen == 1):
        mouse.move(328, 466, True, MOVE_SEC)
    elif (screen == 2):
        mouse.move(978, 466, True, MOVE_SEC)
    elif (screen == 3):
        mouse.move(328, 986, True, MOVE_SEC)
    elif (screen == 4):
        mouse.move(978, 986, True, MOVE_SEC)


def goFullscreen(screen):
    findHeroesMenu(screen)
    mouse.move(306, 26, False, MOVE_SEC)
    mouse.click()


def quitFullscreen():
    pyautogui.hotkey('esc')


def openHeroesMenu():
    mouse.click()
    sleep(WAIT_SEC*2)
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
    mouse.move(-60, HERO_FIRST_POS_Y, False, MOVE_SEC)
    sleep(WAIT_SEC)


def doWorkAction():
    mouse.click()
    sleep(WAIT_SEC)
    global activeHeroesQuatity
    activeHeroesQuatity += 1 
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



def selectHero(desiredPos):
    logging.debug("Select hero in desired position: {}".format(desiredPos))
    global currentPos
    
    delta = desiredPos - currentPos

    logging.debug("-------------------- currentPos: {} --- desiredPos: {} --> Delta: {}".format(currentPos,desiredPos, delta))

    for x in range(delta):
        if(currentPos<11):
            logging.debug("+++++++++++++++++++++ scroll up")
            for y in range(4):
                mouse.wheel(-1)
                sleep(SCROLL_DELAY)
        elif(currentPos==11):
            logging.debug("================================= adjust")
            for y in range(4):
                mouse.wheel(-1)
                sleep(SCROLL_DELAY)
            mouse.move(0, ((HERO_STRIP_DIVIDER/2) + HERO_STRIP_HEIGHT), False, MOVE_SEC )
            mouse.move(0, 16, False)
            sleep(WAIT_SEC)
        elif(currentPos>11):
            logging.debug("+++++++++++++++++++++ move mouse")
            mouse.move(0, ((HERO_STRIP_DIVIDER/2) + HERO_STRIP_HEIGHT), False, MOVE_SEC )
            sleep(MOVE_SEC)
   
        currentPos += 1
        logging.debug("currentPos: {}".format(currentPos))


def getHeroesPosToWork(screen):
    
    if (farmCicle == FARM_CICLE_MIN):
        logging.info("getting fastest heroes...")
        if (screen == 1):
            heroes = [13,2,5,9,12,14]
        elif (screen == 2):
            heroes = [14,6,1,2,3]
        elif (screen == 3):
            heroes = [7,13,10,1,6,12,3,8]
        elif (screen == 4):
            heroes = [5,8,10,2,13,15,4,6,14]

    if (farmCicle == FARM_CICLE_MED):
        logging.info("getting not so fastest heroes...")
        if (screen == 1):
            heroes = [4,6,7,10,11,15]
        elif (screen == 2):
            heroes = [8,7,12,4,15]
        elif (screen == 3):
            heroes = [9,15]
        elif (screen == 4):
            heroes = [3,11,12]

    elif (farmCicle == FARM_CICLE_MAX):
        logging.info("getting slowest heroes...")
        if (screen == 1):
            heroes = [1,3,8]
        elif (screen == 2):
            heroes = [11,13,5,9,10]
        elif (screen == 3):
            heroes = [4,5,2,11,14]
        elif (screen == 4):
            heroes = [9,1,7]
    
    heroes.sort(reverse=False)
    return heroes


def startTeamWork(screen):
    global currentPos
    currentPos = 1

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
    prepareToWork()
    startTeamWork(screen)
    closeHeroesMenu(screen)


def keepAlive():
    global onOff
    global farmCicle
    farmCicle += 1
    logging.info("Keep alive running in farm cicle: {}/{}".format(farmCicle, FARM_CICLE_MAX))

    if(onOff):
        
        handleSignIn()
        handleNewMap()
        
        for screen in range(TOTAL_SCREENS):
            screen+=1

            if (farmCicle == FARM_CICLE_MAX or farmCicle == FARM_CICLE_MED or farmCicle == FARM_CICLE_MIN):
                logging.info("Starting farm in screen: {}".format(screen))
                startFarm(screen)
            else:
                logging.info("Keeping alive screen: {}".format(screen))
                goToMainMenu(screen)
                goToTreasureHunt(screen)


    if (farmCicle == FARM_CICLE_MAX):
        farmCicle = 0

    
    # if(datetime.datetime.now().time() > STOP_TIME and datetime.datetime.now().time() < START_TIME):
    #     onOff = False
    # else:
    #     onOff = True

    logging.info('onOff: {}'.format(onOff))

    nextTick = (datetime.datetime.now() + datetime.timedelta(seconds = KEEP_ALIVE_SEC)).strftime("%b %d %Y %H:%M:%S")
    logging.info("Keep alive ending .. See you again at cicle {} in {}".format(farmCicle+1, nextTick))
    openSystemClock()
    sleep(KEEP_ALIVE_SEC)
    keepAlive()


def handleNewMap():
    logging.info('Handling new map...')
    newMapBtns = list(pyautogui.locateAllOnScreen('imgs/gui/new-map.png'))
    
    if(newMapBtns):
        for btn in newMapBtns:
            btnPos = pyautogui.center(btn)
            currentTime = datetime.datetime.now().strftime("%b-%d-%Y-%H-%M-%S")
            pyautogui.screenshot('imgs/screenshots/map-{}.png'.format(currentTime))
            pyautogui.click(btnPos)
            sleep(1)
            # goFullscreen(1)
            # sleep(5)
            # quitFullscreen()

    logging.info('Handling new map - done!')


def handleSignIn():
    logging.info('Handling signIn...')

    connectBtns = list(pyautogui.locateAllOnScreen('imgs/gui/connect-wallet.png'))
    if(connectBtns):
        logging.warning('{} screens need to signIn ... starting process!'.format(len(connectBtns)))
        
        for btn in connectBtns:
            logging.info('Sign in screen...')
            signInHappyPath(btn)

            okBtn = pyautogui.locateCenterOnScreen('imgs/gui/ok.png')
            if(okBtn):
                pyautogui.click(okBtn)
                sleep(WAIT_SIGN_IN) # Time to reload credits screen
                signInHappyPath(btn)

            treasureHuntBtn = pyautogui.locateCenterOnScreen('imgs/gui/treasure-hunt.png')
            pyautogui.click(treasureHuntBtn)
            sleep(WAIT_SIGN_IN/3)
            logging.info('Sign in screen done!')

    logging.info('Handling singIn - done!')


def signInHappyPath(btn):
    btnPos = pyautogui.center(btn)
    mouse.move(btnPos.x,btnPos.y-100,True)
    mouse.click()
    pyautogui.hotkey('ctrl','f5')
    sleep(WAIT_SIGN_IN) # Time to reload credits screen
    pyautogui.click(btnPos)
    sleep(WAIT_SIGN_IN/2) # Wait confirmation pop-up
    signInBtn = pyautogui.locateCenterOnScreen('imgs/gui/sign-in.png')
    pyautogui.click(signInBtn)
    sleep(WAIT_SIGN_IN) # Wait main menu


def findBtAndClick(name):
    pt = pyautogui.locateOnScreen('{}.png'.format(name))
    if(pt):
        logging.info('Button {} finded! Center and clickin it!'.format(name))
        ptCenter = pyautogui.center(pt)
        pyautogui.click(ptCenter)
        return True
    return False

    pyautogui.locateOnWindow()


def openSystemClock():
    mouse.move(2470, 1055, True, MOVE_SEC)
    mouse.click()


# ---------------------------------------------------
# Main
# ---------------------------------------------------
def main():
    cf.init()
    log.init()
    # screenSetup()

    logging.info("Starting bot!!")
    keepAlive()

    # goFullscreen(1)
    # sleep(5)
    # quitFullscreen()

main()