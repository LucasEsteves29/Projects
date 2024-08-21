import json, time, os

data_path = 'db.json'
contas = {}

def esperar():
    time.sleep(1)
    print('.')
    time.sleep(0.5)
    print('..')
    time.sleep(0.5)
    print('...')
    time.sleep(0.5)
    os.system('cls')

def salvar(contas, arquivo):
    dados = contas
    with open(arquivo, 'w', encoding='utf8') as arquivo:
        json.dump(
            dados,
            arquivo,
            ensure_ascii=False,
            indent=2
        )

def ler(arquivo):
    dados = {}

    try:
        with open(data_path, 'r', encoding='utf8') as arquivo:
            dados = json.load(arquivo)

            return dados


    except FileNotFoundError:
        print('Arquivo não existe')
        salvar(dados, data_path)

def criar_conta():
    os.system('cls')
    print("Vamos criar sua conta!")
    user = input('Digite o nome do seu usuário: ')

    while user in contas:
        user = input('Esse usuário já existe, tente outro: ')
    username = user
    esperar()
    print('Usuário selecionado! ')
    senha = input('Crie sua senha agora: ')
    contas[user] = {
        'username': username,
        'password': senha,
        'money': 100
         }
    esperar()
    print('Sua conta foi criada!') 
    time.sleep(2)

def logar():
    os.system('cls')
    password_login = contas[user_login]['password']

    password_attempt = input("Qual a sua senha? ")
        
    while password_attempt != password_login:
        password_attempt = input("Senha incorreta, tente novamente: ")

    esperar()
    print(f'Seja bem vindo {user_login}')

def depositar():
    os.system('cls')
    amount = int(input(f"Quanto você quer depositar {contas[user_login]['money']}$: "))

    while amount > (contas[user_login]['money']) and isinstance(amount, (int, float)):
        amount = int(input(f"Quantia insuficiente, quanto você quer depositar {contas[user_login]['money']}$: "))

    print('Quantia selecionada!')
    user_deposit = input("Para quem você deseja depositar? ")

    while user_deposit == user_login and user_deposit not in contas:

        user_deposit = input("usuário inválido, para quem você deseja depositar? ")

    contas[user_deposit]['money'] += amount
    contas[user_login]['money'] -= amount
    esperar()
    print('Quantia enviada!')
    time.sleep(2)
    os.system("cls")
    salvar(contas, data_path)

contas = ler(data_path)

while True:
    os.system('cls')
    print('Seja bem vindo ao MengoBank!')
    print('O que voce deseja fazer agora?')
    action = input('(E)ntrar, (C)riar: ').lower()

    while action not in ['e', 'c']:
        print('Escreva uma das opções!')
        action = input('(E)ntrar, (C)riar: ')

    if action == 'c'.lower():
        criar_conta()

    else:
        user_login = input('Qual o seu usuario? ')
        user_found = False
        if user_login in contas:
            user_found = True

        while user_found == False:
            user_login = input('Usuário não encontrado, tente novamente: ')
            if user_login in contas:
                user_found = True

        logar()
        
        time.sleep(1.5)
        os.system('cls')

        while True:

            print('O que você quer fazer agora')
            action = input('Comandos: (Di)nheiro (D)epositar, (S)air: ').lower()

            if action == 's':
                break

            elif action == 'd':
                depositar()

            else:
                print(f'{contas[user_login]['money']}$')
                time.sleep(1.5)
                os.system('cls')
    
    salvar(contas, data_path)
        

 