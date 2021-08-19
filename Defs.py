import time
from os import system

def menu1():
    system('cls')
    print("############################################")
    print("### 1 - Cadastrar login novo    ############")
    print("### 2 - Fazer Login             ############")
    print("### 0 - Sair                    ############")
    opcao = int(input("### Digite o digito da escolha: "))
    print("############################################")
    time.sleep(0.5)
    return opcao

def menu2():
    system('cls')
    print("Você está logado!")
    time.sleep(1)
    escolha = input("Caso deseje sair aperte qualquer tecla!")
    system('cls')
    print("Saindo da sua conta .")
    time.sleep(0.4)
    system('cls')
    print("Saindo da sua conta ..")
    time.sleep(0.4)
    system('cls')
    print("Saindo da sua conta ...")
    time.sleep(1)
    system('cls')
    print("Deslogado com sucesso!")
    time.sleep(1)

def procurarArquivo():
    try:
        arq = open('login.txt', 'rt')
        arq.close()
    except:
        return False
    else:
        return True

def gravarArquivo(login, senha):
    if buscarLogin(login) == False:
        with open('login.txt' , 'a+') as arq:
            arq.writelines(f'{login} {senha}\n')
            arq.seek(0)
            print("Usuário cadastrado com sucesso!")
        
def buscarLogin(login):
    #Primeiro você cria uma lista (logins = []), depois abre o arquivo com o 'with', em seguida para (for) cada linha no arquivo (arq) você vai dividir os argumentos com uma, e depois separar eles dentro da lista criada no começo.
    logins = []
    local = 0
    with open('login.txt' , 'r+') as arq:
        for linha in arq:
            linha = linha.strip(",")
            logins.append(linha.split())       
        
        for dado in logins:
            if logins[local][0] == login:
                return True
            else:
                local = local + 1
    return False

def buscarSenha(login, senha):
    logins = []
    local = 0
    with open('login.txt' , 'r+') as arq:
        for linha in arq:
            linha = linha.strip(",")
            logins.append(linha.split())       
        
        for dado in logins:
            if logins[local][0] == login:
                if logins[local][1] == senha:
                    return True
            else:
                local = local + 1
    return False

def logado(login, senha):
    if buscarLogin(login) and buscarSenha(login,senha) == True:
        print("Usuário logado com sucesso !")
        return True
    elif buscarLogin(login) == True and buscarSenha(login,senha) == False:
        print("Senha incorreta, tente novamente !")
        return False
    elif buscarLogin(login) == False and buscarSenha(login,senha) == True:
        print("Login incorreto, tente novamente!")
        return False
    else:
        print("Login e senha incorretos, tente novamente ou cadastre um novo usuário!")
        return False