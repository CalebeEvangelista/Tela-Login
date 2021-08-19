'''
Código para uma tela de login feito em Python.

FUNCIONALIDADES:
- Cadastrar usuário;
- Verificar cadastro (Senha e login);
- Tratar os erros;
'''

from Defs import buscarLogin, buscarSenha, gravarArquivo, logado, menu1, menu2
from os import system
import time
import stdiomask
from getpass import getpass

while True :
    opcao = menu1()
    if opcao == 1:
        #Cadastrar login novo
        system('cls')
        login = input("Digite o login: ")
        senha = stdiomask.getpass(prompt='Digite a senha: ', mask='*')
        if buscarLogin(login) == True:
            print("Nome de usuário em uso, digite outro!")
        else:
            gravarArquivo(login,senha)
        time.sleep(2)
        system('cls')
        print("Retornando para a tela inicial .")
        time.sleep(0.4)
        system('cls')
        print("Retornando para a tela inicial ..")
        time.sleep(0.4)
        system('cls')
        print("Retornando para a tela inicial ...")
        time.sleep(1)
    
    elif opcao == 2:
        system('cls')
        login = input("Digite o login: ")
        senha = stdiomask.getpass(prompt='Digite a senha: ', mask='*')
        if logado(login, senha) == True:
            menu2()
    
    elif opcao == 0:
        system('cls')
        print("Saindo do programa .")
        time.sleep(0.4)
        system('cls')
        print("Saindo do programa ..")
        time.sleep(0.4)
        system('cls')
        print("Saindo do programa ...")
        time.sleep(1)
        system('cls')
        print("Até mais!")
        time.sleep(1)
        break

    else:
        print("Digite uma opção valida!")