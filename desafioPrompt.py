import pyautogui
import pyperclip
from time import sleep

usuario = pyautogui.prompt('Digite seu usuário: ',title='dados de login')
senha = pyautogui.password('Informe sua senha: ',title='dados de login',mask='*')

def escrever_dados(frase):
    pyperclip.copy(frase)
    pyautogui.hotkey('Ctrl','v')

pyautogui.click(82,1066, duration=2)
escrever_dados('bloco de notas')
sleep(1)
pyautogui.click(105,525, duration=1)
pyautogui.click(1119,333,duration=1)
escrever_dados(f'O usuário digitado é: {usuario}')
pyautogui.hotkey('Enter')
escrever_dados(f'A senha digitada é: {senha}')


#resolução do professor
#import pyautogui
usuario = pyautogui.prompt('Digite seu usuário: ',title='dados de login')
senha = pyautogui.password('Informe sua senha: ',title='dados de login',mask='*')

pyautogui.click(1076,286,duration=2)
pyautogui.typewrite(usuario)
pyautogui.press('enter')
pyautogui.typewrite(senha)
