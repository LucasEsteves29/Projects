palavra = 'psicologia'
tentativas = 0
palavra_acertas = ''
import os

while True:
    
    tentativas += 1
    letra_digitada = input('Digite: ')

    while len(letra_digitada) != 1:
        letra_digitada = input('Digite apenas uma letra: ')
    
    if letra_digitada in palavra:
        palavra_acertas += letra_digitada
    
    palavra_secreta = ''
    for palavra_acertadas in palavra:
        if palavra_acertadas in palavra_acertas:
            palavra_secreta += palavra_acertadas
        elif palavra_acertadas not in palavra_acertas:
            palavra_secreta += '*'
    
    print(palavra_secreta)

    if palavra_secreta in palavra:
        print(f'PARABENS VOCE ACERTOU! \nVoce acertou em {tentativas} vezes!')
        input("Aperte enter para continuar: ")
        os.system('cls')
        break
    