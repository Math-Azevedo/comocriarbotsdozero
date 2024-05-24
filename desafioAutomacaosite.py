# 1) Navegue até o site https://cursoautomacao.netlify.app/
# 2) Encontre e clique no campo "Digite seu nome" dentro de "exemplos Alertas" e digite seu nome
# 3) Clique em alerta, para gerar a alerta
# 4) Feche a alerta
# 5) Suba a página totalmente para cima
# 6) Desça apenas o suficiente para conseguir chegar até a secção que contém os arquivos para o quais irá fazer o download e click no botão de download para realizar o downlaod dos arquivos excel e pdf.
# 7) Depois de ter feito isso, crie uma alerta que diz "VOCÊ TERMINOU"

import webbrowser as web
import pyautogui as gui
import pyperclip as pp
from time import sleep

web.open_new('https://cursoautomacao.netlify.app/') #PASSO 1
sleep(3)
gui.moveTo(678,258,duration=0.8) #PASSO 2
gui.scroll(-1020) #PASSO 2
gui.click(1519,299,duration=0.8) #PASSO 2

def mensagem(frase):
    pp.copy(frase)
    gui.hotkey('Ctrl','v')

mensagem('Matheus') #PASSO 2
gui.click(1468,336, duration=0.8) #PASSO 3
gui.click(1140,194,duration=0.8) #PASSO 4
gui.move(300,0)
sleep(1)
gui.scroll(-1950) #PASSO 5
sleep(1)
gui.scroll(1000) #PASSO 6
sleep(1)
gui.click(453,390,duration=1) #PASSO 6
sleep(1)
gui.click(497,444,duration=1) #PASSO 6
sleep(1)
gui.click(668,384,duration=1) #PASSO 6
sleep(1)
gui.click(497,444,duration=1) #PASSO 6
sleep(1)
gui.alert(text='VOCÊ TERMINOU!!!',title='Fim de execução',button='Finalizar') #PASSO 7