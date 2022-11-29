from PySimpleGUI import Window
import PySimpleGUI as sg


sg.theme('Dark Blue 3')

window_open = True

participantes = []

def botao(text: str):
    return sg.Button(text)


def input_participantes(placeholder):
    return (sg.Text(placeholder), sg.Input(key='-PARTICIPANTE-'))


window_inserir_participantes = Window(

    'Inserir quantidade de participantes',

    layout=[
        [sg.Text('Insira a quantidade de participantes: ')],
        [sg.InputText(key='-NUM-PARTICIPANTE-', do_not_clear=True, size=(5, 1))],
        [botao('Inserir Participantes'), botao('Sair')]
    ],

    size=(400, 100)
)


qtdParticipantes = values[0]


window_nomes = Window(

    'Insira os nomes',

    layout = [
        [input_participantes(i+1)] for i in range (qtdParticipantes)
    ],

    modal = True
)

while True:
    event, values = window_inserir_participantes.read()
    if event in (None, 'Sair'):
        break
    elif event == 'Inserir Participantes':
        print('pre {}'.format(qtdParticipantes))
        qtdParticipantes = int(values['-NUM-PARTICIPANTE-'])
        print('pos {}'.format(qtdParticipantes))
        window_nomes.read()

        
            

# def botao(text:str):
#     return sg.Button(text)

# def input_participantes(placeholder):

#     return (sg.Text(placeholder), sg.InputText())

# window_participantes = Window(
#     'Janela Participantes',
#     size = (800,800),
#     layout = [
#         [sg.Text('Quantos participantes possuem o grupo? ')],
#         [sg.InputText()],
#         [botao('Adicionar Participantes')],
# ],

#     element_justification='c'
# )

# lista = ['jose', 'jhonatan', 'jilerme', 'juca']

# window_nomes = Window(
#     'Janela Nomes',
#     size = (800, 800),
#     layout = [
#         [input_participantes(nome)] for nome in range(qtd_participantes)
# ],

#     element_justification='c'
# )

# while window_open:
#     event, values = window_participantes.read()

#     if event == 'Adicionar Participantes':
#         qtd_participantes = values[0]
#         window_open = False
#         window_participantes.close()
#         print(qtd_participantes)
#         window_nomes.read()
