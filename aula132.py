# @property + @setter - getter e setter no modo Pythônico
# setter é um metodo que voce usa para configurar um determinado atributo
# - como getter
# - p/ evitar quebrar código cliente
# - p/ habilitar setter
# - p/ executar ações ao obter um atributo
# Atributos e métodos que começar com um ou dois underlines
# não devem ser usados fora da classe.
#  🐍🤓🤯🤯🤯🤯
class Caneta:
    def __init__(self, cor):
        # private protected
        self.cor = cor
        self._cor_tampa = None

    @property # metodo para obter o valor
    def cor(self):
        print('ESTOU NO GETTER')
        return self._cor

    @cor.setter # metodo para configurar o valor
    def cor(self, valor):
        print('ESTOU NO SETTER')
        self._cor = valor

    @property
    def cor_tampa(self):
        return self._cor_tampa

    @cor_tampa.setter
    def cor_tampa(self, valor):
        self._cor_tampa = valor


caneta = Caneta('Azul')
print('-'*30)
# getter -> obter valor
caneta.cor = 'Rosa'
print('-'*30)
#caneta.cor_tampa = 'Azul'
#print('-'*30)
print(caneta.cor)
print('-'*30)
#print(caneta.cor_tampa)