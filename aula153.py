# Método especial __call__
# callable é algo que pode ser executado com parênteses
# Em classes normais, __call__ faz a instância de uma
# classe "callable".
# o __call__ faz a instancia ser executavel
class CallMe:
    def __init__(self, phone):
        self.phone = phone

    def __call__(self, nome, *args, **kwargs):
        b = f'{nome} está chamando {self.phone}'
        return b


call1 = CallMe('23945876545')
retorno = call1('Luiz Otávio', 12343, 'margarida')
print(retorno)