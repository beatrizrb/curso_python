import conta
import pessoas


class Banco:
    def __init__(self, agencias: list[int] | None= None, 
                 clientes: list[pessoas.Pessoa] | None = None, 
                 contas: list[conta.Conta] | None = None):
        # aqui embaixo estou sinalizando que se agencia for None
        # quero que seja uma lista vazia
        self.agencias = agencias or []
        self.clientes = clientes or []
        self.contas = contas or []
        # self.lista = {}

    def checar_agencia(self, conta):
        if conta.agencia in self.agencias:
            return True
        return False

    def checar_cliente(self, cliente):
        if cliente in self.clientes:
            return True
        return False
    
    def checar_conta(self, conta):
        if conta in self.contas:
            return True
        return False
    
    def se_conta_e_do_cliente(self, cliente: pessoas.Cliente, conta):
        if conta is cliente.conta:
            return True
        return False
    
    def autenticar(self, cliente, conta):
        return self.checar_agencia(conta) and \
            self.checar_cliente(cliente) and \
            self.checar_conta(conta) and \
            self.se_conta_e_do_cliente(cliente, conta)


    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.agencias!r}, {self.clientes!r}, {self.contas!r})'
        return f'{class_name}{attrs}'
    
    """def adicionar_cliente(self, clientes: pessoas.Pessoa, contas: conta.Conta):
        self.lista[clientes] = contas

    def checar(self, clientes, valor):
        if clientes in self.lista.keys():
            checar_conta = clientes.conta == self.lista[clientes]
            # checar_conta = repr(self._contas) in repr(clientes.conta)
            checar_agencia = clientes.conta.agencia == self.lista[clientes].agencia
            if checar_conta and checar_agencia:
                print('Parabens, voce está no banco')
                self.lista[clientes].sacar(valor)
                return self.lista[clientes].detalhes()
        print('voce não está no banco')"""

if __name__ == '__main__':
    c1 = pessoas.Cliente('Luiz', 30)
    cc1 = conta.ContaCorrente(111, 222, 0, 0)
    c1.conta = cc1
    c2 = pessoas.Cliente('Beatriz', 15)
    cp1 = conta.ContaPoupanca(112, 223, 100)
    c2.conta = cp1
    banco = Banco()
    banco.clientes.extend([c1, c2])
    banco.contas.extend([cc1, cp1])
    banco.agencias.extend([cc1._agencia, cp1._agencia])
    #print(banco.autenticar(c1, cc1))
    if banco.autenticar(c1, cc1):
        cc1.depositar(100)
        cc1.sacar(40)