from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

time.sleep(2)


#Hotbar1:  X: 799 Y: 1062 RGB: (141,108,46)
#Hotbar2:  X: 838 Y: 1062 RGB: (141,108,46)
#Hotbar3:  X: 877 Y: 1062 RGB: (141,108,46)
#Hotbar4:  X: 916 Y: 1062 RGB: (141,108,46)
#Hotbar5:  X: 955 Y: 1062 RGB: (141,108,46)
#Hotbar6:  X: 994 Y: 1062 RGB: (141,108,46)
#Hotbar7:  X: 1033 Y: 1062 RGB: (141,108,46)
#Hotbar8:  X: 1072 Y: 1062 RGB: (141,108,46)
#Hotbar8:  X: 1111 Y: 1062 RGB: (141,108,46)

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(3)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    
while keyboard.is_pressed('.') == False:

    if pyautogui.pixel(799, 1062)[0] == 135:
        while pyautogui.pixel(799, 1062)[0] == 135:
            keyboard.press_and_release('1')
            click(900, 600)

    if pyautogui.pixel(838, 1062)[0] == 135:
        while pyautogui.pixel(838, 1062)[0] == 135:
            keyboard.press_and_release('2')
            click(900, 600)

    if pyautogui.pixel(879, 1062)[0] == 135:
        while pyautogui.pixel(879, 1062)[0] == 135:
            keyboard.press_and_release('3')
            click(900, 600)

    if pyautogui.pixel(919, 1062)[0] == 135:
        while pyautogui.pixel(919, 1062)[0] == 135:
            keyboard.press_and_release('4')
            click(900, 600)

    if pyautogui.pixel(959, 1062)[0] == 135:
        while pyautogui.pixel(959, 1062)[0] == 135:
            keyboard.press_and_release('5')
            click(900, 600)

    if pyautogui.pixel(999, 1062)[0] == 135:
        while pyautogui.pixel(999, 1062)[0] == 135:
            keyboard.press_and_release('6')
            click(900, 600)

    if pyautogui.pixel(1039, 1062)[0] == 135:
        while pyautogui.pixel(1039, 1062)[0] == 135:
            keyboard.press_and_release('7')
            click(900, 600)

    if pyautogui.pixel(1079, 1062)[0] == 135:
        while pyautogui.pixel(1079, 1062)[0] == 135:
            keyboard.press_and_release('8')
            click(900, 600)

    if pyautogui.pixel(1119, 1062)[0] == 135:
        while pyautogui.pixel(1119, 1062)[0] == 135:
            keyboard.press_and_release('9')
            click(900, 600)
    
