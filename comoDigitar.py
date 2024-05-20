# COMO DIGITAR COM PYAUTOGUI
import pyautogui
from time import sleep
import pyperclip #importando biblioteca para usar acentos

def escrever_frase(frase):
    pyperclip.copy(frase)
    pyautogui.hotkey('ctrl','v')


#  - icone
# 874,953 - google
# 747,520 - conta google
# 527,18 - nova aba
# 568,64 - barra endereco

pyautogui.click(891,1065, button='right', duration=1)
pyautogui.click(874,953, duration=2)
pyautogui.click(709,504, duration=2)
pyautogui.click(527,18, duration=2)
pyautogui.click(568,64, duration=1)
escrever_frase('www.google.com.br') # Escrevendo uma mensagem através de uma função
sleep(1)
pyautogui.hotkey('Enter') # apertando o enter do teclado
sleep(3)
pyautogui.click(774,522, duration=0.5)
pyautogui.typewrite('dev aprender') # escrevendo mensagem
sleep(1)
pyautogui.hotkey('Enter') # apertando o enter do teclado
sleep(2)
pyautogui.click(298,554,duration=2)

