# COMO USAR A FUNÇÃO CLICK
import pyautogui
#click personalizado
pyautogui.click(x=1000, y=500, clicks=2, interval=0.0, button='left', duration=2)
#click na posicao atual (com botão esquerdo)
pyautogui.click()
pyautogui.click(button='left')
pyautogui.click(button='rigth')
pyautogui.click(button='middle')
# Clicar x vezes
pyautogui.click(clicks=10)
# Funções prontas parar clicks
pyautogui.doubleClick() #click duplo
pyautogui.rightClick() # botão direito
pyautogui.middleClick() # botão do meio
pyautogui.tripleClick() # clicar 3 vezes