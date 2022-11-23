import random
import turtle

#fazer verificação do sorteio
def verificar(participantes, sorteio):
    for i in range(len(participantes)):
        if participantes[i] == sorteio[i]:
            return False
    return True

#lista vazia de participantes e o input do total de participantes
def qtd_participantes():
    quantidade_participantes = int(input("Quantos participantes possuem o grupo? "))
    participantes = []
    return len(quantidade_participantes)

#adicionar participantes (e seus nomes) à lista vazia de acordo com o numero total de participantes
for i in range(quantidade_participantes):
    nome = input("Qual nome do {}º participante? ".format(i+1))
    participantes.append(nome)
    print('Participantes inseridos: \n{}\n'.format(participantes))
    

#sorteio randomico a usando a função de verificação do sorteio dentro de um while
def sortear():
    sorteio = random.sample(participantes, len(participantes))
        while not verificar(participantes, sorteio):
            sorteio = random.sample(participantes, len(participantes))



#criação de arquivos txt com nome do participante, e o conteúdo é quem ele sorteou
for i in range(len(participantes)):   
    arquivo = open("{}.txt".format(participantes[i]), "w", encoding="utf-8")
    arquivo.write("Bem vindo ao sorteio do amigo secreto! O seu amigo secreto  é: {} ".format(sorteio[i]))
    arquivo.write("\nO presente que o seu amigo secreto escolheu é: {}".format(presente))
    arquivo.close()

