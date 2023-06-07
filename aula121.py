# classe é um molde que gera novas instancias/objetos
# Métodos em instâncias de classes Python
# Hard coded - É algo que foi escrito diretamente no código
# o metodo init sempre retorna None
class Carro:
    def __init__(self, nome):
        self.nome = nome

    def acelerar(self):
        print(f'{self.nome} está acelerando...')


string = 'Luiz'
print(string.upper())

fusca = Carro('Fusca')
print(fusca.nome)
fusca.acelerar()

celta = Carro(nome='Celta')
print(celta.nome)
celta.acelerar()