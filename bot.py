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
KEEP_CICLE_SEC = 360
FARM_CICLE_LIMIT = 2
WAIT_SEC = 1.5
WAIT_SIGN_IN = 15
WAIT_NEW_MAP = 2
WAIT_LOADING = 0.1
SCROLL_DELAY = .03
SCROLL_ADJUST_DELAY = 1
MOVE_SEC = .05
WAIT_CHECK_ENERGY = .01
HERO_STRIP_HEIGHT = 44
HERO_STRIP_DIVIDER = 8
HERO_FIRST_POS_X = -68
HERO_FIRST_POS_Y = -258
HERO_TOTAL_HEIGHT = 255
TOTAL_HEROS = 15
TOTAL_SCREENS = 4

MAP_STATE_STRIKERS = 'strikers'
MAP_STATE_NORMALS  = 'normals'
MAP_STATE_ROCKERS  = 'rockers'

currentPos = 0
farmCicle = 1
mapState = MAP_STATE_NORMALS



# TODO: think about maintenance time
MAINTENANCE = False
MAINTENANCE_START_TIME = datetime.time(6, 0, 0)   # Time, without a date
MAINTENANCE_END_TIME   = datetime.time(8, 30, 0)  # Time, without a date
underMaintenance = False



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


def goFullscreen():
    pyautogui.hotkey('F11')
    fullscreenBtn = pyautogui.locateCenterOnScreen('imgs/gui/full-screen.png')
    pyautogui.click(fullscreenBtn)


def quitFullscreen():
    pyautogui.hotkey('F11')


def openHeroesMenu():
    mouse.click()
    sleep(WAIT_SEC)
    mouse.click()
    sleep(WAIT_SEC)


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
    mouse.click()
    sleep(WAIT_SEC)
    mouse.move(0,100,False, MOVE_SEC)
    mouse.click()

def doClickAction():
    if(mapState == MAP_STATE_NORMALS):
        energy = checkEnergy()
        logging.debug('Hero energy is: {}'.format(energy))
        
        # Click work
        if(energy == 'high'):
            btnOff = checkWorkBtnOff()
            if(btnOff):
                mouse.click()
                logging.info('click work')
                checkActionLoaded()

        # Click rest
        elif(energy == 'low'):
            mouse.move(40, 0, False)
            btnOff = checkRestBtnOff()
            if(btnOff):
                mouse.click()
                logging.info('click rest')
                checkActionLoaded()
            mouse.move(-40, 0, False)

    else:  
        mouse.click()
        logging.info('click work')
        checkActionLoaded()


def putHeroesToRest():
    logging.info("Put heroes to rest...")
    mouse.move(-15, HERO_FIRST_POS_Y - 25, False, MOVE_SEC)
    mouse.click()
    sleep(WAIT_SEC)
    mouse.move(15, -HERO_FIRST_POS_Y + 25, False, MOVE_SEC)
    logging.info("Put heroes to rest - done!")


def selectHero(desiredPos):
    # logging.debug("Select hero in desired position: {}".format(desiredPos))
    global currentPos
    
    delta = desiredPos - currentPos

    # logging.debug("-------------------- currentPos: {} --- desiredPos: {} --> Delta: {}".format(currentPos,desiredPos, delta))

    for x in range(delta):
        if(currentPos<11):
            # logging.debug("+++++++++++++++++++++ scroll up")
            for y in range(4):
                mouse.wheel(-1)
                sleep(SCROLL_DELAY)
            if(currentPos==10):
                mouse.move(0, 5, False, MOVE_SEC)
                sleep(SCROLL_ADJUST_DELAY)

        elif(currentPos==11):
            # logging.debug("================================= adjust")
            for y in range(4):
                mouse.wheel(-1)
                sleep(SCROLL_DELAY)

            mouse.move(0, ((HERO_STRIP_DIVIDER/2) + HERO_STRIP_HEIGHT + 2), False, MOVE_SEC)
            sleep(SCROLL_ADJUST_DELAY)

        elif(currentPos>11):
            # logging.debug("+++++++++++++++++++++ move mouse")
            mouse.move(0, ((HERO_STRIP_DIVIDER/2) + HERO_STRIP_HEIGHT), False, MOVE_SEC)
   
        currentPos += 1
        # logging.debug("currentPos: {}".format(currentPos))


def getHeroesPosToWork(screen):

    if(mapState == MAP_STATE_STRIKERS):
        if (screen == 1):
            heroes = [2,13,15,9]
        elif (screen == 2):
            heroes = [1,2,6,14]
        elif (screen == 3):
            heroes = [7,10,13,12]
        elif (screen == 4):
            heroes = [5,7,15,9]
    elif(mapState == MAP_STATE_ROCKERS):
        if (screen == 1):
            heroes = [8,5,6,10,11]
        elif (screen == 2):
            heroes = [15,4,13,12,11]
        elif (screen == 3):
            heroes = [15,2,3,8,11,14]
        elif (screen == 4):
            heroes = [1,4,6,11,13]
    else:
        heroes = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]


    heroes.sort(reverse=False)
    return heroes


def startTeamWork(screen):

    mouse.move(HERO_FIRST_POS_X, HERO_FIRST_POS_Y, False, MOVE_SEC)
    sleep(WAIT_SEC)

    global currentPos
    currentPos = 1

    heroesPosToWork = getHeroesPosToWork(screen)
    logging.info("Heroes going to work by their positions: {}".format(heroesPosToWork))

    for position in heroesPosToWork:
        selectHero(position)
        doClickAction()


def goToMainMenu(screen):
    findHeroesMenu(screen)
    mouse.move(-290, -370, False, MOVE_SEC)
    mouse.click()


def goToTreasureHunt(screen):
    findHeroesMenu(screen)
    mouse.move(0, -190, False, MOVE_SEC)
    mouse.click()


def startFarm(screen):
    checkMapState(screen)
    findHeroesMenu(screen)
    openHeroesMenu()

    if(mapState != MAP_STATE_NORMALS):
        putHeroesToRest()

    checkHeroesListLoaded()
    startTeamWork(screen)
    closeHeroesMenu(screen)


def checkHeroesListLoaded():
    # 237 215 186 -> hero bar background
    HERO_LIST_LOADING_COLOR = (115, 91, 83)

    sleep(WAIT_LOADING)
    mouse.move(0, -100, False)
    mousePos = pyautogui.position()

    loading = True
    while(loading == True):
        # print('check load')
        if(pyautogui.pixelMatchesColor(mousePos.x, mousePos.y, HERO_LIST_LOADING_COLOR, tolerance=2)):
            # print('is loading')
            sleep(WAIT_LOADING)
        else:
            # print('loading complete')
            loading = False

    mouse.move(0, 100, False)


def checkActionLoaded():
    HERO_BAR_BG_COLOR = (243, 220, 191)

    sleep(WAIT_LOADING)
    mousePos = pyautogui.position()
    pix = pyautogui.pixel(mousePos.x, mousePos.y)
    print(pix)
    loading = True
    while(loading == True):
        print('check load')
        pix = pyautogui.pixel(mousePos.x, mousePos.y)
        print(pix)
        if(pyautogui.pixelMatchesColor(mousePos.x, mousePos.y, HERO_BAR_BG_COLOR, tolerance=2)):
            print('is loading')
            sleep(WAIT_LOADING)
        else:
            print('loading complete')
            loading = False


def checkMapState(screen):
    findHeroesMenu(screen)
    global mapState
    mouse.move(0, -70, False,.1)
    mouse.click()
    goFullscreen()
    rocks = getRocksQtt()
    chests = getChestsQtt()

    if(rocks > 100 and chests > 20):
        mapState = MAP_STATE_STRIKERS
    # elif(rocks > 5 and rocks < 10):
    #     mapState = MAP_STATE_ROCKERS // contar os baus com a vida zerada no rockers
    else:
        mapState = MAP_STATE_NORMALS

    quitFullscreen()

    logging.info("Map state is: {}".format(mapState))


def checkIsUnderMaintenance():
    global underMaintenance
    if(MAINTENANCE):
        if(datetime.datetime.now().time() > MAINTENANCE_START_TIME and datetime.datetime.now().time() < MAINTENANCE_END_TIME):
            underMaintenance = True
        else:
            underMaintenance = False


def keepCicle():
    global underMaintenance
    global farmCicle
    farmCicle += 1

    checkIsUnderMaintenance()

    if(underMaintenance == False):
        logging.info("Running in cicle: {}/{}".format(farmCicle, FARM_CICLE_LIMIT))
        handleSignIn()
        
        for screen in range(TOTAL_SCREENS):
            screen += 1

            # if (farmCicle == FARM_CICLE_LIMIT):
            logging.info("Starting farm in screen: {}".format(screen))
            startFarm(screen)

            goToMainMenu(screen)
            goToTreasureHunt(screen)
   
        handleSignIn()

    else:
        logging.info("Server is under maintenance! Running in cicle: {}/{}".format(farmCicle, FARM_CICLE_LIMIT))


    if (farmCicle == FARM_CICLE_LIMIT):
        farmCicle = 0

    nextTick = (datetime.datetime.now() + datetime.timedelta(seconds = KEEP_CICLE_SEC)).strftime("%b %d %Y %H:%M:%S")
    logging.info("Keep cicle ending .. See you again at cicle {} in {}".format(farmCicle+1, nextTick))
    openSystemClock()
    sleep(KEEP_CICLE_SEC)
    keepCicle()


def handleNewMap():
    logging.info('Handling new map...')
    newMapBtns = list(pyautogui.locateAllOnScreen('imgs/gui/new-map.png'))
    
    if(newMapBtns):
        for btn in newMapBtns:
            btnPos = pyautogui.center(btn)
            pyautogui.click(btnPos)
            sleep(WAIT_NEW_MAP)
            goFullscreen()
            currentTime = datetime.datetime.now().strftime("%b-%d-%Y-%H-%M-%S")
            pyautogui.screenshot('imgs/screenshots/map-{}.png'.format(currentTime))
            quitFullscreen()

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


def checkEnergy():
    # mousePos = pyautogui.displayMousePosition()
    EMPTY_COLOR = (197, 139, 105)
    energy = 'high'

    mouseInitPos = pyautogui.position()

    mouse.move(-25, 10, False, WAIT_CHECK_ENERGY)
    mousePos = pyautogui.position()
    if(pyautogui.pixelMatchesColor(mousePos.x, mousePos.y, EMPTY_COLOR)):
        energy = 'medium'
        mouse.move(-50, 0, False, WAIT_CHECK_ENERGY)
        mousePos = pyautogui.position()
        if(pyautogui.pixelMatchesColor(mousePos.x, mousePos.y, EMPTY_COLOR)):
            energy = 'low'

    mouse.move(mouseInitPos.x, mouseInitPos.y, True, WAIT_CHECK_ENERGY)
    
    return energy


def checkWorkBtnOff():
    WORK_BTN_OFF_COLOR = (91, 135, 95)
    mousePos = pyautogui.position()
    # pix = pyautogui.pixel(mousePos.x, mousePos.y)
    # print("btn work: {}".format(pix))
    if(pyautogui.pixelMatchesColor(mousePos.x, mousePos.y, WORK_BTN_OFF_COLOR, tolerance=4)):
        return True
    else:
        return False


def checkRestBtnOff():
    REST_BTN_OFF_COLOR = (173, 84, 18)
    mousePos = pyautogui.position()
    # pix = pyautogui.pixel(mousePos.x, mousePos.y)
    # print("btn rest: {}".format(pix))
    if(pyautogui.pixelMatchesColor(mousePos.x, mousePos.y, REST_BTN_OFF_COLOR, tolerance=4)):
        return True
    else:
        return False


def openSystemClock():
    mouse.move(2470, 1055, True, MOVE_SEC)
    mouse.click()


def getItemList(type, confidence=0.94):
    return list(pyautogui.locateAllOnScreen('imgs/{}.png'.format(type), confidence=confidence))



def getObjList(type, confidence=0.92):
    return list(pyautogui.locateAllOnScreen('imgs/items/{}.png'.format(type), confidence=confidence))


def getRocksQtt():
    rocks = getObjList('rock1')
    if (rocks == []):
        rocks = getObjList('rock2')
        if (rocks == []):
            rocks = getObjList('rock3')
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

# ---------------------------------------------------
# Main
# ---------------------------------------------------
def main():
    cf.init()
    log.init()
    # screenSetup()

    logging.info("Starting bot!!")
    keepCicle()

main()