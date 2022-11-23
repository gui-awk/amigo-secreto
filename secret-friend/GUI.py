from PySimpleGUI import Window
import PySimpleGUI as sg


sg.theme('Dark Blue 3')

window_open = True

participantes = []
qtd_participantes = 1


def botao(text:str):
    return sg.Button(text)


def input_participantes(placeholder):

    return (sg.Text(placeholder), sg.InputText())

window_participantes = Window(
    'Janela Participantes',
    size = (800,800),
    layout = [
        [sg.Text('Quantos participantes possuem o grupo? ')], 
        [sg.InputText()],
        [botao('Adicionar Participantes')],
],

    element_justification='c'
)

lista = ['jose', 'jhonatan', 'jilerme', 'juca']

window_nomes = Window(
    'Janela Nomes',
    size = (800, 800),
    layout = [
        [input_participantes(nome)] for nome in range(qtd_participantes)
],

    element_justification='c'
)

while window_open:
    event, values = window_participantes.read()

    if event == 'Adicionar Participantes':
        qtd_participantes = values[0]
        window_open = False
        window_participantes.close()
        print(qtd_participantes)
        event_1, values_1 = window_nomes.read()
        







