import time

print('Bem vindo a calculadora!')
print('[S]omar')
print('[D]iminuir')
print('[M]ultiplicar')
print('[Di]vidir')

acao = input('Qual operacao voce deseja escolher:  ').lower()
ops = ['s', 'm', 'd', 'di']

while acao not in ops:
    acao = input('Operacao invalida, digite novamente:  ').lower()

time.sleep(1)
print('Operacao selecionada')

lista = []
while True:
    numero = input('Agora escolha os numeros ou digite [S]air:  ').lower()

    if numero.isdigit():
        numero = float(numero)
        lista.append(numero)

    elif numero == 's' and len(lista)>=2:
        print('Operacao concluida!')
        time.sleep(1)
        break

    else:
        print(f'Voce digitou um termo invalido \nOu nao possui dois numeros ainda\nDigite novamente.')
        time.sleep(1)


def somar(*args):
    soma = 0
    for numeros in args:
        soma += numeros

    return soma
soma = somar(*lista)

def diminuir(*args):
    diminuicao = lista[0] * 2   # Caso o numero inicial da diminuicao nao for o primeiro numero da lista, a conta sera com sinais invertidos.
    for numeros in args:
        diminuicao -= numeros

    return diminuicao
diminuicao = diminuir(*lista)

def dividir(*args):
    divisao = lista[0] ** 2   # Mesmo caso da diminuicao, caso o numero inicial for 1, ele ja sera dividido pelo primeiro numero da lista
    for numeros in args:
        divisao /= numeros

    return divisao
divisao = dividir(*lista)


def multiplicar(*args):
    multiplicacao = 1
    for numeros in args:
        multiplicacao *= numeros
    
    return multiplicacao
multiplicacao = multiplicar(*lista)

if acao == 's':
    print(f'A soma dos seus numeros foi {soma}')

elif acao == 'd':
    print(f'A diminuicao dos seus numeros foi {diminuicao}')

elif acao == 'm':
    print(f'A multiplicacao dos seus numeros foi {multiplicacao}')

else:
    print(f'A divisao dos seus numeros foi {divisao}')
    




    

    