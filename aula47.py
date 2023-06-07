"""
Faça um jogo para o usuário adivinhar qual \
a palavra secreta.
-Você vai propor uma palavra secreta qualquer 
e vai dar a possibilidade para o usuário digitar
apenas uma letra.
- Qual o usuário digitar uma letra, você vai 
conferir se a letra digitada está na palavra
secreta.
- Se a letra digitada estiver na palavra 
secreta; exiba a letra;
- Se a letra não estiver; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
import os 
palavra_secreta = 'segredo'
tentativas = 0
palavra_formada = '*' * len(palavra_secreta)
while True:
    if '*' not in palavra_formada:
        print('Parabéns, você acertou!')
        break
    letra = input('Digite uma letra: ')
    tentativas += 1
    #for i in range(len(palavra_secreta)):

    if letra in palavra_secreta:
        for i in range(len(palavra_secreta)):
            if palavra_secreta[i] == letra:
                palavra_formada = palavra_formada[:i] + letra + palavra_formada[i+1:]
    print(palavra_formada)
    print(tentativas)
    #os.system('cls')
    


