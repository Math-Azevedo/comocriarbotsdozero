# Como pegar e arrastar algo para outro lugar

import pyautogui

for i in range(9):
    # Mover até a coordenada
    pyautogui.moveTo(1136,258,duration=2)
    #  Clicar e Arrastar até um ponto e Soltar
    pyautogui.dragTo(1120,453, button='left', duration=2 ) # INformando no parametro qual botao deve ser clicado
    # Repetir 9 vezes
