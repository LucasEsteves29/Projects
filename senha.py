import time, os

conta = {}

def criar_conta():

    if len(conta) == 0:
        print('Parece que voce nao possui nenhuma conta, entao vamos criar!')

    else:
        pass

    usuario_desejado = input('Qual usuario voce deseja criar?  ')
    while usuario_desejado in conta:
        usuario_desejado = input('Usuario ja selecionado, escolha outro:  ')
    time.sleep(1)

    print('Usuario escolhido')

    senha = input('Agora escolha uma senha!  ')
            
    time.sleep(1)

    print('Agora vamos completar seu cadastro!')

    conta[usuario_desejado] = {
        'Senha': senha,     
        'Nome': input('Qual o seu nome?  '),
        'Idade': input('Qual sua idade?  '),
        'Altura': input('Qual sua altura?  '),
        'Cidade': input('Qual sua cidade?  ')
     }

    print('Tudo pronto')
    print('Seu login foi criado!')

    time.sleep(2)
    os.system('cls')

    return conta[usuario_desejado]
    

def logar():
 
    usuario_entrada = input('Digite seu usuario.  ')

    while usuario_entrada not in conta:
        usuario_entrada = input('Usuario nao encontrado, tente novamente.  ')

    senha_entrada = input('Agora digite sua senha.  ')
            
    tentativas = 1
    while senha_entrada != conta[usuario_entrada]['Senha']:
        senha_entrada = input(f'Senha errada, tente novamente.\n{tentativas}x tentativas:  ')
        tentativas += 1
        if tentativas >= 5:
            print('Voce usou o maximo de tentativas possiveis.')
            time.sleep(2)
            os.system("cls")           
            return
        else:
            continue

    time.sleep(2)

    print('Login efetuado com sucesso!')

    print(f'Bem vindo {conta[usuario_entrada]['Nome']}')

while True:
    acao_usuario = input('[C]riar uma conta, [E]ntrar ou [S]air?  ').lower()
    options = ["c", "e", "s"]

    while acao_usuario not in options:
        acao_usuario = input('Opção inválida, escreva novamente:  ')

    print('Opção selecionada!')

    if acao_usuario == "c":
        criar_conta()
    elif acao_usuario == "e":
        logar()
    else:
        break







