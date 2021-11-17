import pyautogui
import time


# nome do atalho que esta na area de trabalho
nome_atalho = 'sapi'
usuario = 'seu usuario'
senha   = 'sua senha'

# espera inicialização do computador
time.sleep(2)

# dimensões da tela
tamanho_tela      = pyautogui.size()
clique_horizontal = tamanho_tela.width // 2
clique_vertical   = tamanho_tela.height // 2

# clique com o mouse no centro da tela
pyautogui.click(clique_horizontal, clique_vertical)

# digita o nome do atalho com o teclado
pyautogui.typewrite(nome_atalho)

# abre e confirma
pyautogui.press('enter')
time.sleep(0.5)
pyautogui.press('left')
time.sleep(1)
pyautogui.press('enter')
time.sleep(7)

# usuario e senha - se necessário
pyautogui.typewrite(usuario)
pyautogui.press('tab')
pyautogui.typewrite(senha)
pyautogui.press('tab')
pyautogui.press('enter')