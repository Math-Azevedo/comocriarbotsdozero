import pyautogui as pa
from time import sleep

# FORMA 1: ACESSANDO A PÁGINA CLICANDO (COM O BOTAO ESQUERDO) NO LINK DISPONIBILIZADO ABAIXO DA AULA
pa.click(554,1022, button='right', duration=2 )
pa.click(639,803, duration=0.5)
pa.click(348,16, duration=0.5)
sleep(3)
pa.moveTo(621,322, duration=0.8)
pa.scroll(-2000)

# FORMA 2: ACESSANDO A PÁGINA COPIANDO O LINK E COLANDO NO NAVEGADOR
pa.click(554,1022, button='right', duration=2 ) # movendo cursor ate o LINK
pa.click(611,967, duration=1) # movendo até o COPIAR ENDERECO DE LINK e copiando o mesmo
sleep(1) # pausa de 1s
pa.click(286,19, duration=1) # clicando para abrir uma nova aba no navegador
pa.click(207,62, button='right', duration=1) # clicando com botao direito na barra de endereço para abrir lista de opções
pa.click(398,246, duration=1) # clicando na opção para colar o link na barra do navegador e acessar
sleep(3)# pausa de 3s
pa.moveTo(621,322, duration=1) # movendo o cursor para a pagina
pa.scroll(-2000) # scroolando até o titulo historia