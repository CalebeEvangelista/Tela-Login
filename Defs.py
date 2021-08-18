from time import time

def procurarArquivo():
    try:
        arq = open('login.txt', 'rt')
        arq.close()
    except:
        return False
    else:
        return True

def gravarArquivo(login, senha):
    with open('login.txt' , 'a+') as arq:
        arq.writelines(f'{login} {senha}\n')
        arq.seek(0)
        print(arq.readlines())
        
def buscarLogin(login, senha):
    #Primeiro você cria uma lista (logins = []), depois abre o arquivo com o 'with', em seguida para (for) cada linha no arquivo (arq) você vai dividir os argumentos com uma, e depois separar eles dentro da lista criada no começo.
    logins = []

    with open('login.txt' , 'r+') as arq:
        for linha in arq:
            linha = linha.strip(",")
            logins.append(linha.split())
            print(logins)

        for dado in logins:
            user = dado[0]
            password = dado[1]
            print(login)
            print(senha)
    
        if login == user and senha == password:
            print("Usuário ja cadastrado!")

    return(login, senha)
