import time
import pyautogui
a=input('enter a message to spam:')
b=int(input('enter the number of messages:'))
time.sleep(5)
for i in range (b):
    pyautogui.typewrite(a)
    pyautogui.press("enter")
