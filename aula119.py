# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']
import os
import json


#print(add1(len(todo)-1))

def listar(tarefas):
    print()
    if not tarefas:
        print('Nada a listar')
        return #estou usando o return para parar a executação da função aqui (guard clause)
    print('TAREFAS:')
    print(*tarefas, sep='\n')
    print()


def desfazer(tarefas, tarefas_refazer):
    print()
    if not tarefas:
        print('Nada a desfazer.')
        return
    tarefa = tarefas.pop()
    print(f'{tarefa=} foi removido da lista de tarefas.')
    tarefas_refazer.append(tarefa)
    listar(tarefas)
    print()

def refazer(tarefas, tarefas_refazer):
    print()
    if not tarefas_refazer:
        print('Nada a refazer.')
        return
    tarefa = tarefas_refazer.pop()
    print(f'{tarefa=} adicionada na sua lista de tarefas.')
    tarefas.append(tarefa)
    listar(tarefas)
    print()
    
def adicionar(tarefa, tarefas):
    print()
    if not tarefa:
        print(f'Você não digitou uma tarefa')
        return
    tarefas.append(tarefa)
    print(f'{tarefa=} foi adicionada na lista de tarefas.')
    listar(tarefas)
    print()

def ler(tarefas, caminho_arquivo):
    dados = []
    try:
        with open(caminho_arquivo, 'r', encoding='utf8') as arquivo:
            dados = json.load(arquivo)
    except FileNotFoundError:
        print('Arquivo não existe')
        salvar(tarefas, caminho_arquivo)
    return dados


def salvar(tarefas, caminho_arquivo):
    dados = tarefas
    with open(caminho_arquivo, 'w', encoding='utf8') as arquivo:
        dados = json.dump(tarefas, arquivo, indent=2, ensure_ascii=False)
    return dados


CAMINHO_ARQUIVO = 'aula119.json'
tarefas = ler([], CAMINHO_ARQUIVO)
tarefas_refazer = []




while True:
    print('Comandos: listar, desfazer, refazer.')
    action = input('Digite uma tarefa ou comando: ')
   

    comandos = { # esta pausando as funções
        'listar': lambda: listar(tarefas),
        'desfazer': lambda: desfazer(tarefas, tarefas_refazer),
        'refazer': lambda: refazer(tarefas, tarefas_refazer),
        'clear': lambda: os.system('clear'),
        'adicionar': lambda: adicionar(action, tarefas)
        
    }
    comando = comandos.get(action) if comandos.get(action) is not None else \
        comandos['adicionar']
    
    comando()
    salvar(tarefas, CAMINHO_ARQUIVO)
        
    """ if action == 'listar':
        listar(tarefas)
        continue
        
    elif action == 'desfazer':
        desfazer(tarefas, tarefas_refazer)
        listar(tarefas)
        continue
        
    elif action == 'refazer':
        refazer(tarefas, tarefas_refazer)
        listar(tarefas)
        continue

    elif action == 'clear':
        os.system('cls') # executando um comando dentro do codigo
        continue
            
    else:
        adicionar(action, tarefas)
        listar(tarefas)
        continue """
    # PARA COMENTAR SHIFT + ALT + A
        



