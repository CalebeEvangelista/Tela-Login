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
    local = 0
    with open('login.txt' , 'r+') as arq:
        for linha in arq:
            linha = linha.strip(",")
            logins.append(linha.split())
            
        print(logins)
        
        for dado in logins:
            local = logins.index(login) 
            print(logins)
            user = dado[local]
            password = dado[local + 1]

            print(user)
            print(password)
    
        if login == user and senha == password:
            print("Usuário ja cadastrado!")
    return(login, senha)

def cadastrarLogin(login, senha):
    return True