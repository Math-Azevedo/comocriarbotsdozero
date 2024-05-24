# como quebrar cpctha com reconhecimento simples de imagem
import pyautogui

# print(pyautogui.locateOnScreen('numero_4.png'))#encontrando as coordenadas proximo à imagem
#Resultado do print: Box(left=1318, top=503, width=70, height=46) , isso significa que o left é o ponto inicial da imagem encontrada, o top é o ponto mais alto encontrado, o wifth é a largura e o height é a altura.


# # encontrar a coordenada do centro de uma imagem
# print(pyautogui.locateCenterOnScreen('numero_4.png'))
# #como usar na pratica
# pyautogui.click(1353,526,duration=1)

captcha = pyautogui.locateCenterOnScreen('google.PNG')
pyautogui.click(captcha)