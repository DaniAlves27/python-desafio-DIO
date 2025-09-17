def depositar(saldo, extrato):
    valor = float(input("Informe o valor do depósito: "))

    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato


def sacar(saldo, extrato, limite, numero_saques, LIMITE_SAQUES):
    valor = float(input("Informe o valor do saque: "))

    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
        valor = 0

    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
        valor = 0

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
        valor = 0

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print(f"Você sacou: R$ {valor:.2f}")
    else:
        print("Operação falhou! O valor informado é inválido.")
        valor = 0

    return saldo, extrato, numero_saques



def exibir_extrato(saldo, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")


def menu():
    return input("""
---------------
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
---------------
=> """)


# Programa principal
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = menu()

    if opcao == "d":
        saldo, extrato = depositar(saldo, extrato)

    elif opcao == "s":
        saldo, extrato, numero_saques = sacar(saldo, extrato, limite, numero_saques, LIMITE_SAQUES)

    elif opcao == "e":
        exibir_extrato(saldo, extrato)

    elif opcao == "q":
        print("Obrigado por usar nossos serviços!")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
