import pyautogui as pg
import pyperclip
from time import sleep

def escrever_mensagem(frase):
    pyperclip.copy(frase)
    pg.hotkey('Ctrl','v')


pg.click(73,1064,duration=2) # Acessar barra de pesquisa e clicar para escrever
escrever_mensagem('bloco de notas') # escrever oq procura, nesse caso, bloco de notas
pg.click(142,528, duration=2) # Mover cursor e Clicar em bloco de notas
pg.click(1153,307,duration=2) # Mover cursor e Clicar no espaço para escrever no bloco de notas
escrever_mensagem('Automação é incrível !!!') # Escrever a mensagem "AUTOMAÇÃO É INCRÍVEL !!!"