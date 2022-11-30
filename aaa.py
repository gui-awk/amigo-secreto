import PySimpleGUI as sg

sg.theme('Black')


layout_sorteio = [      [sg.Text("Insira número de participantes: "), sg.Input(key = '-QUANTIDADE-', do_not_clear = True, size = (3, 1))],
                [sg.Button('Adicionar Participantes'), sg.Button('Sair')]
]


window_sorteio = sg.Window('Sorteio', layout_sorteio)


def formatInputInformation(participantes):
        participantes = []
        participantes.append(values['-QUANTIDADE-'])
        qtd_participantes = participantes[0]
        return qtd_participantes


layout_nomes = [      [input_participantes(i+1) for i in range(qtd_participantes+1) ],
                [sg.Button('Sair')]
]


window_nomes = sg.Window('Nomes', layout_nomes)


def input_participantes(placeholder):
    return (sg.Text(placeholder), sg.Input(key='-PARTICIPANTE-', do_not_clear = True, size = (20, 1)))


while True:
        event, values = window_sorteio.read()
        if event in (sg.WIN_CLOSED, 'Sair'):
                break
        elif event == 'Adicionar Participantes':
                window_nomes.read()
                sg.popup(formatInputInformation(values['-QUANTIDADE-']))


window_sorteio.close()