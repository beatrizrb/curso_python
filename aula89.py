# dir, hasattr e getattr em Python
# dir traz todos os atributos da variavel
string = 'Luiz'
metodo = 'upper'
# hasattr checa se tem determinado nome dentro

if hasattr(string, metodo):
    print('Existe upper')
    print(getattr(string, metodo)()) # esta pegando o metodo, esse segundo () faz com que ele seja executado
else:
    print('Não existe o método', metodo)