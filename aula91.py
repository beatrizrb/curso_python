# Introdução às Generator functions em Python
# generator = (n for n in range(1000000))

# toda função generator usa yield (que guarda o valor 
# e pausa a execução da função, e vai retornar 
# quando chamar no next)
# o return na função generator levanta exceção
# stopiteration
def generator(n=0, maximum=10):
    while True:
        yield n
        n += 1

        if n >= maximum: # para encerrar o loop
            return


gen = generator(maximum=10)
for n in gen:
    print(n)