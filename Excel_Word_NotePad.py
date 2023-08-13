import pyautogui as py


def abrirExcel():
    py.hotkey('win', 'r')
    py.sleep(1)
    py.typewrite('Excel')
    py.sleep(1)
    py.press('enter')

def abrirWord():
    py.hotkey('win', 'r')
    py.sleep(1)
    py.typewrite('winword')
    py.sleep(1)
    py.press('enter')

def abrirNotePad():
    py.hotkey('win', 'r')
    py.sleep(1)
    py.typewrite('notepad')
    py.sleep(1)
    py.press('enter')


op = py.confirm(">> !! Clique na opção desejada abaixo !! <<",
      buttons = ['Word', 'Excel', "NotePad"])

if op == 'Excel':
    print("Abrindo o excel no seu computador! ")
    abrirExcel()
elif op == 'Word':
    print('Abrindo o Word no seu computador! ')
    abrirWord()
else:
    print("Abrindo o NotePad no seu computador! ")
    abrirNotePad()
