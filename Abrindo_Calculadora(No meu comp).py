import pyautogui as ptg

ptg.sleep(1)
print(ptg.position())

#print(ptg.position())
#movendo o mouse até o botão do windows no meu pc
#ptg.moveTo(x=780, y=1057)
ptg.sleep(0.5)

#cliando no botão
ptg.click(x=780, y=1057)
ptg.sleep(0.5)

#movendo para a barra de pesquisa
#ptg.moveTo(x=854, y=339)
ptg.sleep(1)

#Clicando na barra de pesquisa
ptg.click(x=854, y=339)
ptg.sleep(1)

#Escrevendo
ptg.typewrite("Calculadora")
ptg.sleep(1)

#Movendo o mouse para o ícone
#ptg.moveTo(x=714, y=475)
ptg.sleep(1)
#Clicando
ptg.click(x=714, y=475)
ptg.click(x=714, y=475)


