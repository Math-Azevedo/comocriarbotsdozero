# Como usar botões e atalhos do teclado
import pyautogui
import pyperclip
from time import sleep

pyautogui.click(891,1065, button='right', duration=1)
pyautogui.click(846,988, duration=2)
pyautogui.click(709,504, duration=2)
pyautogui.click(486,56, duration=2)

def inserir_escrita(escrita):
    pyperclip.copy(escrita)
    pyautogui.hotkey('Ctrl','v')

inserir_escrita('https://membros.devaprender.com/auth/login')
sleep(2)
pyautogui.hotkey('enter')
sleep(3)

# Navegar e clicar no campo email e inserir o email
pyautogui.click(1344,516,duration=1)
inserir_escrita('digite_seu_email')
# Apertar tab para ir pro proximo campo
pyautogui.hotkey('Tab')
# Digitar minha senha
inserir_escrita('digite_sua_senha')
sleep(1)

pyautogui.click(1449,750,duration=1)
