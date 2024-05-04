
''' Escopo do projeto:

1 - Objetivo do Projeto:
        *Desenvolver um sistema bancário
        *Modernizar as operações bancárias utilizando a linguagem Python.

2 - Funcionalidades da Primeira Versão:
        *Implementar três operações: depósito, saque e extrato.

3 - Depósito:
        *Permitir depósitos de valores positivos na conta bancária.
        *Todos os depósitos devem ser armazenados em uma variável.
        *Os depósitos devem ser exibidos na operação de extrato.

4 - Saque:
        *Permitir até três saques diários.
        *Limite máximo de R$ 500,00 por saque.
        *Exibir uma mensagem se o usuário não tiver saldo suficiente para o saque.
        *Todos os saques devem ser armazenados em uma variável.
        *Os saques devem ser exibidos na operação de extrato.

5 - Extrato:
        *Listar todos os depósitos e saques realizados na conta.
        *Exibir o saldo atual da conta no final da listagem.
        *Se o extrato estiver vazio, exibir a mensagem: "Não foram realizadas movimentações."
        *Os valores devem ser exibidos no formato "R$ xxx.xx".
'''

##### inicio do programa ####

menu ='''
    
================== MENU ==================
  [d] - Depositar
  [s] - Sacar
  [e] - Extrato
  [q] - Sair
==========================================
=> Informe a operação desejada: '''

#### variaveis ####

saldo = 0
valor_limite_saque = 500
extrato = ""
numero_saques = 0
QTD_SAQUE_LIMITE = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("\n=> Informe o valor do depósito: "))

        if valor > 0: # valores positivos
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"  #variavel para salvar eventos

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("\n=> Informe o valor do saque: "))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > valor_limite_saque
        excedeu_saques = numero_saques >= QTD_SAQUE_LIMITE

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"  
            numero_saques += 1  #armaze qtde de saques 

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")