# Como tirar print da tela inteira ou parte dela
import pyautogui

pyautogui.screenshot('tela.jpg') #dá-se o nome e a extensao | print da tela inteira
#print de parte da tela
pyautogui.screenshot('calculadora.jpg',region=(1531,159,323,531)) # Na region é passado a coordenada do primeiro ponto, o quanto voce vai andar a direita e o quanto vai andar pra baixo para realizar o print
