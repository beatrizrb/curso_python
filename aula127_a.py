# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.
# na 127_a vou salvar os dados e na b vou recuperar os dados
import json

class Taylor:
    def __init__(self, nome, ano, nota):
        self.nome = nome
        self.ano = ano
        self.nota = nota
    def get_nota(self):
        return self.nota + 10

a1 = Taylor('Midnights', 2023, 10)
a2 = Taylor('Folklore', 2021, 8)
a3 = Taylor('Evermore', 2022, 7)
#print(type(vars(a1)))

lista = [vars(a1),a2.__dict__,a3.__dict__]

def fazer_dump():
    print('fazendo o dump')        
    with open('json127.json', 'w') as file:
    #json.dump(vars(a) for a in lista, file, indent=2, ensure_ascii=False) 
        json.dump(lista, file, indent=2, ensure_ascii=False)
    #json.dump(vars(a1), file, indent=2, ensure_ascii=False)

if __name__ == '__main__':
    # colocamos esse if para impedir que quando eu importar esse modulo em outro lugar
    # impedir que ele execute automaticamente o fazer_dump, ele só vai executar se eu estiver
    # executando esse arquivo diretamente
    fazer_dump()
    print('ELE É O __MAIN__')

