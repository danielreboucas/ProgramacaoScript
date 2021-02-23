import PySimpleGUI as psg


layout = [
    [psg.Text('0', size=(15,0), justification='right', key='screen')],
    [psg.Button('C', size=(6,0), key='C'), psg.Button('CE', size=(6,0), key='CE')],
    [psg.Button('7', size=(2,0), key='7'), psg.Button('8', size=(2,0), key='8'), psg.Button('9', size=(2,0), key='9'), psg.Button('÷', size=(2,0), key='/')],
    [psg.Button('4', size=(2,0), key='4'), psg.Button('5', size=(2,0), key='5'), psg.Button('6', size=(2,0), key='6'), psg.Button('x', size=(2,0), key='*')],
    [psg.Button('1', size=(2,0), key='1'), psg.Button('2', size=(2,0), key='2'), psg.Button('3', size=(2,0), key='3'), psg.Button('-', size=(2,0), key='-')],
    [psg.Button('0', size=(2,0), key='0'), psg.Button('.', size=(2,0), key='.'), psg.Button('=', size=(2,0), key='='), psg.Button('+', size=(2,0), key='+')],
]

window = psg.Window('Calculadora').layout(layout)

expression = []


def click_event(event):
    if event in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-', '*', '/', '.']:
        expression.append(event)
    if event in ['C', 'CE']:
        expression.clear()
        window['screen'].update(value='0')
    if event == '=':
        x = ''.join(expression)
        result = eval(x)
        window['screen'].update(value='{:.4f}'.format(result))
    window.refresh()


while True:
    event, values = window.Read()
    print(event)
    if event == psg.WIN_CLOSED or event == 'Exit':
        break
    click_event(event)

window.close()
