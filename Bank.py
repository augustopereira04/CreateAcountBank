import random
import getpass

contaBank = {
    "nome": None,
    "id": random.randint(1,100),
    "senha": None,
    "saldo": None,
    "Credito": None
}

def criaConta():
    Entrar = str(input("Vamos criar uma conta nova pra voce? "));
    if (Entrar == "sim"):
        print("Seja bem vindo ao nosso banco!!\n");
        nome = str(input("Qual o seu nome completo por favor? "));
        contaBank["nome"] = nome;
        print(f"Seja bem vindo {contaBank['nome']} seu id e {contaBank['id']}\n Use esse id para logar na sua conta");
        "\n"
        criptografia()
        login()
        saldo()
        infoConta()
        credito()

def criptografia():
        senha = getpass.getpass("Escolha uma senha de 8 digitos: ")
        contaBank["senha"] = senha



def login():
     Login = input("Entre seu login: ")
     senhaLogin = input("Entre com sua senha: ")
     if (Login == contaBank["id"]):
          print("Login bem sucedido")
     if (senhaLogin == contaBank["senha"]):
          print("Login bem sucedido")


def saldo():
     adicionaSaldo = str(input("Deseja adicionar saldo? "))
     if adicionaSaldo == "sim":
          valorAdicionaSaldo = int(input("Deseja adicionar quanto de saldo? "))
          contaBank["saldo"] = valorAdicionaSaldo
          print(f"Seu saldo atual agora e de R${contaBank['saldo']}")
     else:
          print("Quando quiser adicionar saldo so solicitar")


def infoConta():
     querInfo = str(input("Deseja ver as informacoes da sua conta?? "))
     if querInfo == "sim":
          print(f"Nome de usuario: {contaBank['nome']}")
          print(f"id: {contaBank['id']}")
          print(f"saldo: R${contaBank['saldo']}")
          print("Credito: necessita solicitar")


def credito():
     adicionarCredito = str(input("Deseja adicionar credito: "))
     if adicionarCredito == "sim":
          print("Seu caso sera enviado para uma analise")
     else:
          print("Quando quiser solicitar uma analise so clicar aqui")

criaConta()







