
class Armario:
    def __init__(self):
        self._itens = []
    def inserir(self, *item):
        print('Você está inserindo items!')
        for produto in item:
            self._itens.append(produto)
    def listar(self):
        print()
        print('Olhe como está o seu armário agora!')
        for a in self._itens:
            print(f'item {a.nome} pelo valor de {a.preco}')

class Produtos:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco





p2, p3 = Produtos('jaqueta de cashmere', 400), Produtos('vestido de tule', 200)
armario = Armario()
armario.inserir(p2, p3)
armario.listar()
