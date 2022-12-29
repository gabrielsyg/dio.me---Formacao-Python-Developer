extrato = []
saldo = 0
opcao = -1

valor_deposito = 0

numero_saque = 0
valor_saque = 0

while opcao != 0:
    print('[1] - Depósito: ')
    print('[2] - Saque')
    print('[3] - Extrato')
    print('[4] - Saldo')
    print('[0] - Sair')
    opcao = int(input('Digite sua operação: '))
    if opcao == 1:
        valor_deposito = float(input('Informe o valor de seu depósito: '))
        saldo += valor_deposito
        valor_deposito = f'+{str(valor_deposito)}'
        extrato.append(valor_deposito)
    elif opcao == 2:
        if numero_saque != 3:
            valor_saque = float(input('Informe o valor de seu saque: '))
            if valor_saque > 500:
                print('Valor máximo de saque é de R$500,00.')
            elif valor_saque <= saldo:
                saldo -= valor_saque
                numero_saque += 1
                valor_saque = f'-{str(valor_saque)}'
                extrato.append(valor_saque)
                print('Valor sacado!')
            else:
                print('Saldo insuficiente!')
        else:
            print('Limite de saque atingido.')
    elif opcao == 3:
        print(f'Extrato: {extrato}')
    elif opcao == 4:
        print(f'O seu saldo é R${saldo:.2f}')
    elif opcao == 0:
        print('Obrigado por utilizar nosso banco.')
    else:
        print('Opção inválida, por favor selecione novamente a operação desejada.')
