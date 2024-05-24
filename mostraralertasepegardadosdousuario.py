# Alertar e pedir informação no PyAutoGUI
import pyautogui

# #Pedir informação para usuario
# email = pyautogui.prompt(text='Digite seu e-mail', title='informações obrigatórias')
# print(f'Você digitou {email}')

# # informando um usuario
# pyautogui.alert(text='Iniciando sua automação', title='Automação de Login', button='OK')

resposta = pyautogui.confirm(text='Continuar rodando nossa automação ?', title='Confirmação',buttons=['sim','nao','Cancelar'])

if resposta == 'sim':
    print('Continuando automação')
elif resposta == 'não':
    print('Encerrando automação')
else:
    print('Cancelando automação')

# Pegar senha 
senha = pyautogui.password(text='Digite sua senha: ',title='dados de login', mask='*')
print(senha)