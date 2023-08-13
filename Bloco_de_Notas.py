import pyautogui as py
from time import sleep

#Win + R ao mesmo tempo
py.hotkey('win', 'r')
sleep(1)

#deletando qualquer coisa escrita no Executor
py.press('del')
sleep(1)

#escrevendo notepad
py.typewrite('notepad')
sleep(1)

#pressionando enter para abrir o bloco de notas
py.press('enter')
sleep(3)

#Escrevendo alguma frase
py.write('hello,world')
sleep(3)

#Pegando a janela ativa e apertando para fechar
sleep(2)
fechar = py.getActiveWindow()
sleep(2)
fechar.close()
sleep(1)


#pressionando tab para ir na opção "não salvar"
py.press('tab')
sleep(3)
py.press('enter') #apertando enter para fechar sem salvar

print(">> !! AUTOMAÇÃO ENCERRADA !! <<")
