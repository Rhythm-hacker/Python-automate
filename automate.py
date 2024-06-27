import pyautogui as auto
import time
time.sleep(5)
#for how many seconds do you need to stop until second message goes
n=eval(input("enter number"))
for i in range(n):
    auto.typewrite("My first Hackclub project")
    auto.press("enter")
