class Pessoa:
    def __init__(self, nome: str, idade: int):
        self._nome = nome
        self._idade = idade
    
    @property
    def nome(self):
        return self._nome
    
    @property
    def idade(self):
        return self._idade
    

class Cliente(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self._conta = None

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.nome!r}, {self.idade!r})'
        return f'{class_name}{attrs}'
        
    @property
    def conta(self):
        return self._conta 
    
    @conta.setter
    def conta(self, conta):
        self._conta = conta

if __name__ == '__main__':
    import conta
    c1 = Cliente('Luiz', 40)
    c1.conta = conta.ContaCorrente(111, 222, 0, 0)
    print(c1)
    print(c1.conta)