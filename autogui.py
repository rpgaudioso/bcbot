import pyautogui
import datetime

pt = pyautogui.locateOnScreen('newMap.png')

print(pt)

now = datetime.datetime.now()
now_plus_10 = now + datetime.timedelta(minutes = 10)
print(now_plus_10.strftime("%b %d %Y %H:%M:%S"))

if(pt):
    ptCenter = pyautogui.center(pt)
    print(ptCenter)
    pyautogui.click(ptCenter)