menu = """
## SEJA BEM VINDO(A) AO BANCO ##
[1] DEPOSITAR
[2] SACAR
[3] EXTRATO
[4] SAIR
"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    print(menu)
    opcao = int(input("Escolha a opção: "))

    if opcao == 1:
        valor = float(input(f"Informe o valor para depósito: R$"))
        
        if valor <= 0:
            print("Erro! Insira um valor válido")
        else:
            saldo += valor
            print(f"Seu deposito de R${valor} reais foi realizado com sucesso!")
            extrato += f"Deposito R${valor:.2f} {"real\n" if valor == 1 else "reais\n"}"
    
    elif opcao == 2:

        valor = float(input("Informe o valor para saque: R$"))

        if valor <= 0:
            print("Falha na operação! Valor informado é inválido")
        elif valor > saldo:
            print("Saldo insuficiente!")
        elif valor > limite:
            print("Saque excede o limite")
        elif numero_saques >= LIMITE_SAQUES:
            print("Número máximo de saques excedido.")
        else:
            saldo -= valor
            numero_saques += 1
            print(f"Seu saque de R${valor:.2f} reais foi realizado com sucesso!")
            extrato += f"Saque: R${valor:.2f} reais\n"

    elif opcao == 3:
        print("====== EXTRATO ======")
        print("\nNenhuma transação realizada." if not extrato else extrato)
        print(f"\nSaldo: R${saldo:.2f} reais")
        print("====================='")

    elif opcao == 4:
        break

    else:
        print("Operação falhou! Informe uma opção válida para continuar.")
print("========= OBRIGADO POR SER NOSSO CLIENTE, VOLTE SEMPRE! =========")
