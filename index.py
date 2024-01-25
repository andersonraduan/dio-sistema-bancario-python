menu = """
[d] deposito
[s] saque
[e] extrato
[q] sair
"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do deposito: "))
        
        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R$ {valor:.2f}\n"
        else:
            print("Operação inválida! O valor deve ser maior que 0")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saque = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Saque não permitido. Saldo insuficiente")
        
        elif excedeu_limite:
            print("Valor de saque acima do permitido (R$500,00)")
        
        elif excedeu_saque:
            print("Número de saques execedido")
    
        elif valor > 0:
            saldo -= valor
            extrato = f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print("Saque efetuado com sucesso")

        else:
            print("Operação falhou, valor informado é inválido")
    
    elif opcao == "e":
        print("\n========== EXTRATO ==========")
        print("Não foram encontradas movimentações" if not extrato else extrato)
        print(f"Saldo R$: {saldo:.2f}\n")
        print("\n=============================")
    
    elif opcao == "q":
        print("Sair")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")