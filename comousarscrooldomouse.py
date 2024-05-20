# Como simular "Rolagem" do mouse
import pyautogui
from time import sleep

pyautogui.moveTo(56,99, duration=0.3)
pyautogui.click(button='right', duration=1)
pyautogui.move(50,15, duration=0.5)
pyautogui.click()
pyautogui.click(372,16, duration=0.2)
sleep(9)
pyautogui.moveTo(710,469, duration=0.7)
pyautogui.scroll(-1500)
sleep(5)