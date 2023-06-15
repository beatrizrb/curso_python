from abc import ABC, abstractmethod
# tipagem é especificar o tipo de argumento que voce quer


class Conta(ABC):
    def __init__(self, agencia: int, numero: int, saldo: float = 0) -> None:
        self._agencia = agencia
        self._numero = numero
        self._saldo = saldo

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self._agencia!r}, {self._numero!r}, {self._saldo!r})'
        return f'{class_name}{attrs}'
        # return f'Conta({self._agencia}, {self._numero}, {self._saldo})'

    @property
    def saldo(self):
        return self._saldo

    @property
    def agencia(self):
        return self._agencia

    @abstractmethod
    # aqui estou especificando o tipo de retorno tambem
    def sacar(self, valor: float) -> float:
        ...

    def depositar(self, valor: float) -> float:
        self._saldo += valor
        self.detalhes(f'(DEPÓSITO {valor})')
        return self._saldo

    def detalhes(self, msg: str = '') -> None:
        print(f'O seu saldo é {self._saldo:.2f} {msg}')
        return None


class ContaCorrente(Conta):
    def __init__(self, agencia: int, conta: int, saldo: float = 0,
                 limite: float = 0):
        super().__init__(agencia, conta, saldo)
        self.limite = limite

    def sacar(self, valor: float) -> float:
        limite_maximo = -self.limite
        valor_pos_saque = self._saldo - valor
        if valor_pos_saque >= limite_maximo:
            self._saldo -= valor
            self.detalhes(f'(SAQUE {valor})')
            return self._saldo

        print('Não foi possível sacar o valor desejado')
        print(f'O seu limite é {-self.limite:.2f}')
        self.detalhes(f'SAQUE NEGADO {valor}')
        return self._saldo
    
    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self._agencia!r}, {self._numero!r}, {self._saldo!r}, '\
            f'{self.limite!r})'
        return f'{class_name}{attrs}'

class ContaPoupanca(Conta):
    def sacar(self, valor):
        if self._saldo - valor >= 0:
            self._saldo -= valor
            self.detalhes(f'(SAQUE {valor})')
            return self._saldo

        print('Não foi possível sacar o valor desejado')
        self.detalhes(f'(SAQUE NEGADO {valor})')
        return self._saldo

# cliente1 = Cliente('Beatriz', 24)
# cliente1.conta = ContaCorrente(22, 100, 200)
# banco1 = Banco()

# print(cliente1.conta)
# cliente2 = Cliente('Marcos', 24)
# cliente2.conta = ContaPoupanca(100, 66, 4)
# banco1.adicionar_cliente(cliente1, cliente1.conta)
# banco1.adicionar_cliente(cliente2, cliente2.conta)

# cliente3 = Cliente('Beatriz', 24)
# cliente3.conta = ContaPoupanca(100, 66, 4)
# banco1.checar(cliente3, 100)


if __name__ == '__main__':
    cp1 = ContaCorrente(111, 222, 0, 100)
    # cp1.sacar(1)
    # cp1.sacar(100)
    print(cp1)
