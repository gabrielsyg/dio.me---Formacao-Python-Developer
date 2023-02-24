def menu():
    saldo = 0
    extrato = ''''''
    lista_cpf = list()
    lista_conta = list()
    clientes = list()
    numero_saque = 0
    while True:
        print('[1] - Depósito: ')
        print('[2] - Saque')
        print('[3] - Extrato')
        print('[4] - Saldo')
        print('[5] - Cadastrar usuário')
        print('[6] - Listar clientes')
        print('[7] - Criar conta')
        print('[8] - Listar contas')
        print('[0] - Sair')
        opcao = int(input('Digite sua operação: '))
        if opcao == 1:
            saldo, extrato = deposito(saldo, extrato)
        elif opcao == 2:
            numero_saque, saldo, extrato = saque(
                numero_saque=numero_saque,
                saldo=saldo,
                extrato=extrato
            )
        elif opcao == 3:
            extrato_bancario(saldo, extrato=extrato)
        elif opcao == 4:
            print(f'O seu saldo é R${saldo:.2f}')
        elif opcao == 5:
            criar_usuario(clientes, lista_cpf)
        elif opcao == 6:
            if clientes == []:
                print('=== Não há cliente cadastrado até o momento! ===')
            else:
                for cliente in clientes:
                    print(cliente)
        elif opcao == 7:
            criar_conta(lista_cpf, lista_conta)
        elif opcao == 8:
            if lista_conta == []:
                print('=== Não há conta cadastrada até o momento! ===')
            else:
                for conta in lista_conta:
                    print(conta)
        elif opcao == 9:
            print(lista_cpf)
        elif opcao == 0:
            print('Obrigado por utilizar nosso banco.')
            break
        else:
            print('Opção inválida, por favor selecione novamente a operação desejada.')


def deposito(saldo, extrato, /):
    valor_deposito = float(input('Informe o valor de seu depósito: '))
    saldo += valor_deposito
    extrato += f"Depósito:\tR$ {valor_deposito:.2f}\n"
    return saldo, extrato


def saque(*, numero_saque, saldo, extrato):
    if numero_saque != 3:
        valor_saque = float(input('Informe o valor de seu saque: '))
        if valor_saque > 500:
            print('Valor máximo de saque é de R$500,00.')
        elif valor_saque <= saldo:
            saldo -= valor_saque
            numero_saque += 1
            extrato += f"Saque:\t\tR$ {valor_saque:.2f}\n"
            print('Valor sacado!')
        else:
            print('Saldo insuficiente!')
    else:
        print('Limite de saque atingido.')
    return numero_saque, saldo, extrato


def extrato_bancario(saldo, /, *,  extrato):
    print("\n================ EXTRATO ================")
    print(extrato)
    print(f'O seu saldo é R${saldo:.2f}')
    print("==========================================")


def criar_usuario(clientes, lista_cpf):
    cliente = {}
    cpf = (input('Digite o CPF do cliente (Somente números): '))
    if cpf in lista_cpf:
        print('=== CPF já cadastrado! ===')
    else:
        lista_cpf.append(cpf)
        cliente['CPF'] = cpf
        nome = (input('Digite o nome do cliente: '))
        cliente['nome'] = nome
        data_nascimento = (input('Digite a data de nascimento do cliente: '))
        cliente['data_nascimento'] = data_nascimento
        logradouro = input(
            "Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
        cliente['endereco'] = logradouro
        clientes.append(cliente)
        print("=== Usuário criado com sucesso! ===")
        return clientes, lista_cpf


def criar_conta(lista_cpf, lista_conta):
    conta = []
    agencia = '0001'
    cpf = (input('Digite o CPF do cliente (Somente números): '))
    if cpf in lista_cpf:
        numero_conta = len(lista_conta) + 1
        conta.extend(numero_conta)
        conta.append(agencia)
        conta.append(cpf)
        print("=== Conta criada com sucesso! ===")
        lista_conta.append(conta)
    else:
        print('=== Usuário não cadastrado! ===')
    return lista_conta


menu()
