import ctypes
import sys
from datetime import datetime
from functools import partial
from time import sleep

import pyautogui
from PIL import ImageGrab

platform = 'bluestacks'

pyautogui.FAILSAFE = False
counter = 1
monitor = 1
gems = 0

ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)

if monitor == 1:
   monitor = 2560

roundAnnounce = f'\nStart Round {counter}: {datetime.now().strftime("%I:%M:%S %p")}\n'

print('='*(len(roundAnnounce)-1) + f'{roundAnnounce}' + '='*(len(roundAnnounce)-1))


def is_admin():
   try:
      return ctypes.windll.shell32.IsUserAnAdmin()
   except:
      return False


if is_admin():
   if platform == 'bluestacks':
      while True:
         # print(pyautogui.position())
         if pyautogui.locateOnScreen('images/RETRYBS.png', confidence=0.95, region=(870+monitor, 30, 790, 1375)):
            print(f"Collected: {gems} gems")
            sleep(5)
            pyautogui.click(pyautogui.center(pyautogui.locateOnScreen('images/RETRYBS.png', confidence=0.95, region=(870+monitor, 30, 790, 1375))))
            counter += 1
            roundAnnounce = f'\nStart Round {counter}: {datetime.now().strftime("%I:%M:%S %p")}\n'
            print('='*(len(roundAnnounce)-1) + f'{roundAnnounce}' + '='*(len(roundAnnounce)-1))
            gems = 0
         else:
            if pyautogui.locateOnScreen('images/CLAIM5BS.png', confidence=0.9, region=(870+monitor, 280, 235, 450)):
               try:
                  pyautogui.click(pyautogui.center(pyautogui.locateOnScreen('images/CLAIM5BS.png', confidence=0.9, region=(870+monitor, 280, 235, 450))))
                  gems += 5
               except:
                  pass
            elif pyautogui.locateOnScreen('images/FLOATGEMS.png', confidence=0.42, region=(1080+monitor, 245, 380, 370)):
               try:
                  pyautogui.click(pyautogui.center(pyautogui.locateOnScreen('images/FLOATGEMS.png', confidence=0.42, region=(1080+monitor, 245, 380, 370))))
                  gems += 2
               except:
                  pass
            elif pyautogui.locateOnScreen('images/ICONBS.png', confidence=0.98, region=(1070+monitor, 1315, 195, 85)):
               try:
                  pyautogui.click(pyautogui.center(pyautogui.locateOnScreen('images/ICONBS.png', confidence=0.98, region=(1070+monitor, 1315, 195, 85))))
               except:
                  pass
            elif pyautogui.locateOnScreen('images/BUYSTATEBS.png', confidence=0.99, region=(1080+monitor, 930, 25, 120)) and pyautogui.locateOnScreen('images/MONEYBS.png', confidence=0.98, region=(900+monitor, 55, 30, 45)):
               try:
                  pyautogui.click(pyautogui.center(pyautogui.locateOnScreen('images/BUYSTATEBS.png', confidence=0.8, region=(1080+monitor, 930, 25, 120))))
               except:
                  pass
            elif pyautogui.locateOnScreen('images/DEMONBS.png', confidence=0.98, region=(894+monitor, 645, 97, 71)):
               try:
                  pyautogui.click(pyautogui.center(pyautogui.locateOnScreen('images/DEMONBS.png', confidence=0.95, region=(894+monitor, 645, 97, 71))))
               except:
                  pass
         sleep(1.5)
   else:
      while True:
         # print(pyautogui.position())
         if pyautogui.locateOnScreen('images/RETRY.png', confidence=0.9):
            print(f"Collected: {gems} gems")
            sleep(1.5)
            pyautogui.click(pyautogui.center(pyautogui.locateOnScreen('RETRY.png', confidence=0.9)))
            counter += 1
            roundAnnounce = f'+\nStart Round {counter}: {datetime.now().strftime("%I:%M:%S %p")}\n'
            print('='*(len(roundAnnounce)-1) + f'{roundAnnounce}' + '='*(len(roundAnnounce)-1))
            gems = 0
         else:
            if pyautogui.locateOnScreen('images/CLAIM5.png', confidence=0.9, region=(886+monitor, 48, 219, 682)):
               try:
                  pyautogui.click(pyautogui.center(pyautogui.locateOnScreen('images/CLAIM5.png', confidence=0.9)))
                  gems += 5
               except:
                  pass
            elif pyautogui.locateOnScreen('images/FLOATGEMS.png', confidence=0.42, region=(1067+monitor, 206, 350, 430)):
               try:
                  pyautogui.click(pyautogui.center(pyautogui.locateOnScreen('images/FLOATGEMS.png', confidence=0.42, region=(1067+monitor, 206, 350, 430))))
                  gems += 2
               except:
                  pass
            elif pyautogui.locateOnScreen('images/ICON.png', confidence=0.98, region=(689+monitor, 1370, 450, 60)):
               try:
                  pyautogui.click(pyautogui.center(pyautogui.locateOnScreen('images/ICON.png', confidence=0.98, region=(689+monitor, 1370, 450, 60))))
               except:
                  pass
            elif pyautogui.locateOnScreen('images/BUYSTATE.png', confidence=0.98, region=(307+monitor, 949, 45, 125)) and pyautogui.locateOnScreen('images/MONEY.png', confidence=0.97, region=(15+monitor, 20, 160, 55)):
               try:
                  pyautogui.click(pyautogui.center(pyautogui.locateOnScreen('images/BUYSTATE.png', confidence=0.5, region=(307+monitor, 949, 45, 125))))
               except:
                  pass
         sleep(3)
else:
   ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
