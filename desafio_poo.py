import datetime
from abc import ABC, abstractmethod, abstractproperty

class Cliente:
    def __init__(self, endereco) -> None:
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, endereco, nome, data_nascimento, cpf) -> None:
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf


class Conta:
    def __init__(self, numero_conta, cliente) -> None:
        self._saldo = 0
        self._numero_conta = numero_conta
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)

    @property
    def saldo(self):
        return self._saldo
    
    @property
    def numero_conta(self):
        return self._numero_conta
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico
    
    def sacar(self, valor):
        valor = valor
        if valor <= self._saldo:
            self._saldo -= valor
            print("Operação realizada com sucesso.")
            return True
        elif valor > self._saldo:
            print("Operação falhou, você não possui saldo suficiente.")
            return False
        else:
            print("Operação falhou, o valor informado é inválido.")
            return False

    def depositar(self, valor):
        if valor >= 0:
            self._saldo += valor
            print("Operação realizada com sucesso.")
        else:
            print("Operação falhou, o valor informado é inválido.")
            return False
        return True
    
class ContaCorrente(Conta):
    def __init__(self, numero_conta, cliente, limite=500, limite_saques=3) -> None:
        super().__init__(numero_conta, cliente)
        self.limite = limite
        self.limite_saques = limite_saques

    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacao in self.historico.
             transacoes if transacao["tipo"] == "Saque"] 
        )

        excedeu_limite = valor > self.limite
        excedeu_saques = numero_saques >= self.limite_saques

        if excedeu_limite:
            print("Operação falhou, o valor do saque excedeu o limite.")
        elif excedeu_saques:
            print("Operação falhou, o número máximo de saques excedeu o limite.")
        else:
            return super().sacar(valor)
        
        return False
    
    def __str__(self) -> str:
        return f"""
        Agência: {self.agencia}\n
        C/C: {self.numero}\n
        Titular: {self.cliente.nome}
        """

class Historico:
    def __init__(self) -> None:
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes
    
    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.datetime.now().strftime
                ("%d-%m-%Y %H:%M%s"),
            }
        )

class Transacao(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass

    @abstractmethod
    def registrar(self, conta):
        pass

class Saque(Transacao):
    def __init__(self, valor) -> None:
        self._valor = valor

    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

class Deposito(Transacao):
    def __init__(self, valor) -> None:
        self._valor = valor

    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)
        

def menu():
    menu = """\n
    [1] - Depósito
    [2] - Saque
    [3] - Extrato
    [4] - Nova conta
    [5] - Listar contas
    [6] - Novo usuário
    [0] - Sair
    """
    

if __name__ == "__main__":
    menu()