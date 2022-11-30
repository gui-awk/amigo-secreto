from PySimpleGUI import Window
import PySimpleGUI as sg


sg.theme('Dark Blue 3')


window_open = True


participantes = []

def format_input_information(values):
    participantes = ' , Quantidade de participantes: ' + values['-NUM-PARTICIPANTES-'] 

def store_info(values, participantes):
    participantes.append(format_input_information(values))


def botao(text: str):
    return sg.Button(text)


def input_participantes(placeholder):
    return (sg.Text(placeholder), sg.Input(key='-PARTICIPANTE-'))


window_inserir_participantes = Window(

    'Inserir quantidade de participantes',

    layout=[
        [sg.Text('Insira a quantidade de participantes: ')],
        [sg.InputText(key='-NUM-PARTICIPANTES-', do_not_clear=True, size=(5, 1))],
        [botao('Inserir Participantes'), botao('Sair')]
    ],

    size=(700, 700)
)
i = 0
while True:
    event, values = window_inserir_participantes.read()
    if event in (None, 'Sair'):
        break
    elif event == 'Inserir Participantes':
        window_inserir_participantes.extend_layout(window_inserir_participantes, [[sg.Text('teste'), sg.Input(key=f'-IN-{i}-')]])
        i += 1
        sg.popup(format_input_information(values))