'''
Código para uma tela de login feito em Python.

FUNCIONALIDADES:
- Cadastrar usuário;
- Verificar cadastro (Senha e login);
- Tratar os erros;
'''

from Defs import buscarLogin, gravarArquivo
from os import system
import time

while True :
    system('cls')
    print("############################################")
    print("### 1 - Cadastrar login novo    ############")
    print("### 2 - Fazer Login             ############")
    print("### 0 - Sair                    ############")
    opcao = int(input("### Digite o digito da escolha: "))
    print("############################################")
    time.sleep(0.5)

    while opcao != 0 :
        system('cls')
        if opcao == 1:
            #Cadastrar login novo
            login = input("Digite o login: ")
            senha = input("Digite a senha: ")
            gravarArquivo(login, senha)
            time.sleep(0.4)
            print("Cadastrado com sucesso!")
            time.sleep(0.5)
            print("Voltando a tela inicial ...")
            buscarLogin(login, senha)
            time.sleep(0.7)
            opcao = 0
            time.sleep(10)