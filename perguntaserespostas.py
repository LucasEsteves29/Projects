import os, time

acertos = 0

todas_perguntas = [

    {
        'Pergunta': 'Quanto eh 1+1?',
        'Opcoes': [1, 2, 3, 4,],
        'Resposta': '2'
    },

    {
        'Pergunta': 'Quanto eh 8-10?',
        'Opcoes': [-2, 0, 2, 18],
        'Resposta': "-2"
    },

    {
        'Pergunta': 'Quanto eh 10*20?',
        'Opcoes': [10, 20, 30 , 200],
        'Resposta': "200"
    }

]

numero_perguntas = 1
for perguntas in todas_perguntas:
    os.system('cls')

    print(f'Pergunta de numero {numero_perguntas}\n')
    numero_perguntas += 1

    pergunta = perguntas.get('Pergunta')
    print(pergunta)
    
    
    for indice, opcoes in enumerate(perguntas['Opcoes']):
        print(f'{indice}) {opcoes}')
        
    
    resposta = input('Qual opcao esta correta?  ')

    if resposta == perguntas['Resposta']:
        print('Parabens voce acertou!!!!')
        acertos +=1
        time.sleep(2)

    else:
        print('Voce errou...')

quantidade_de_perguntas = len(todas_perguntas)

print(f'De {quantidade_de_perguntas} voce acertou {acertos}!!!')