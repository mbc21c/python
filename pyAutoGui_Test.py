import pyautogui
import sys
import time

print('####################################################')
print('######################### by zeromini  `18.3.5 #####')
print('######################################### ver 0.02 #')
print('####################################################')
print('####################################################')

def keyboard_macro():
    time.sleep(5)
    pyautogui.keyDown('alt')
    time.sleep(5)
    pyautogui.press('t')
    time.sleep(5)
    pyautogui.keyUp('alt')
    time.sleep(5)
    pyautogui.press('r')
    time.sleep(5)
    pyautogui.press('enter')
    time.sleep(5)
    pyautogui.keyDown('alt')
    time.sleep(5)
    pyautogui.press('t')
    time.sleep(5)
    pyautogui.keyUp('alt')
    time.sleep(5)
    pyautogui.press('s')
    time.sleep(5)
    pyautogui.press('enter')
    time.sleep(5)


sign = str(input('>>'))

if sign == 'A':
    print(' Automouse is running')
    while True:
        if sign == 'Y':
            print(' 마우스 좌표를 읽기위해 원하는 위치에 마우스를 놓고 Y를 눌러주세요 ')
            sign2 = str(input('>>'))
            if sign2 == 'Y':
                x, y = pyautogui.position()
                print(' 입력하신 좌표값은  {}, {}'.format(x,y))
                sys.stdout.flush()         
            print(' Delay Time을 입력해주세요 Ex) 5 = 5초, 300 = 5분')
            time2 = int(input('>>'))
            print(time2)
            print(' 프로그램이 구동 됩니다..........')
            print(' 프로그램을 종료하기 위해서는 윈도우 X 박스를 눌러주세요')
            while True:
                pyautogui.click(x,y)
                time.sleep(time2)
                pyautogui.press('enter')


elif sign == 'K':
    print('  Delay Time을 입력해주세요 Ex) 5 = 5초, 300 = 5분')
    time2 = int(input('>>'))
    print(time2)
    print(' 프로그램 구동을 시작 합니다 ')
    print(' 프로그램을 종료하기 위해서는 윈도우 X 박스를 눌러주세요')
    while True:

         keyboard_macro()    
         time.sleep(time2)