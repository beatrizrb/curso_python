# Teoria: python Special Methods, Magic Methods ou Dunder Methods
# Dunder = Double Underscore = __dunder__
# métodos dunder sao metodos do python, nao criamos dunder
# Antigo e útil: https://rszalski.github.io/magicmethods/
# https://docs.python.org/3/reference/datamodel.html#specialnames
# todos os metodos abaixo passam por um dunder method
# __lt__(self,other) - self < other
# __le__(self,other) - self <= other
# __gt__(self,other) - self > other
# __ge__(self,other) - self >= other
# __eq__(self,other) - self == other
# __ne__(self,other) - self != other
# __add__(self,other) - self + other
# __sub__(self,other) - self - other
# __mul__(self,other) - self * other
# __truediv__(self,other) - self / other
# __neg__(self) - -self
# __str__(self) - str
# __repr__(self) - str
# o __repr__ retornar uma str (representação do seu objeto)

class Ponto:
    def __init__(self, x, y, z='String'):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        # chama esse se precisar de representação de string
        # do objeto
        return f'({self.x}, {self.y})'

    def __repr__(self):
        # no __repr__ voce esta passando uma comunicação
        # para outros desenvolvedores de como voce quer que
        # esse objeto seja criado
        # class_name = self.__class__.__name__
        # mesma coisa acima e abaixo
        # (pegar o nome da classe dinamicamente)
        class_name = type(self).__name__
        print('oi')
        return f'{class_name}(x={self.x!r}, y={self.y!r}, z={self.z!r})'

    def __add__(self, other):
        return 'Beatriz'
p1 = Ponto(1, 2)
p2 = Ponto(978, 876)
#print(p1)
# abaixo voce chama o repr
#print(repr(p2))
p3 = p1 + p2
print(p3)
# chamando o repr abaixo dentro da string
print(f'{p2!r}')