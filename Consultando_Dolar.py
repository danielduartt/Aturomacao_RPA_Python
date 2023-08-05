import pyautogui as pag
pag.sleep(1)

#Movendo o mouse para o ícone do brave
pag.moveTo(x=908, y=1054)
pag.sleep(2)
#clicando nele
pag.click(x=908, y=1054)
#apertando enter
pag.press('enter')
pag.sleep(2)
#movendo o mouse para a barra de pesquisa
pag.moveTo(x=975, y=44)
#clicando nela
pag.click(x=975, y=44)
pag.sleep(1)
#delentando o link escrito nela (caso haja)
pag.press('del')
#escrevendo "Valor dolar"
pag.typewrite("Valor dolar")
pag.sleep(1)
#Pesquisanso após apertar enter
pag.press('enter')
