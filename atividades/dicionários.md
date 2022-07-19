# Exercícios dicionários 

1. Escreva uma função em Python que recebe dois dicionários, e concatena ambos.

_Template:_

```python
def concatena(d1: dict, d2: dict):
    pass

resposta = concatena({'a': 1, 'b': 2}, {'c': 3, 'd': 4})
print(resposta)
```

Saída: 

```bash
{'a': 1, 'b': 2, 'c': 3, 'd': 4}
```

2. Escreva um script que itera sobre todos os itens de um dicionário, imprimindo-os na tela.

_Template:_

```python
meu_dict = {'a': 1, 'b': 2}
resposta = imprime_dicionario(meu_dict)
print(resposta)
```

Saída:

```bash
a: 1
b: 2
```

3. Escreva um script que pergunta um par `(chave, valor)` ao usuário, e adiciona este par de valores à um, dicionário, que foi inicializado vazio. Quando o usuário não digitar nada e der apenas um ENTER, o script deve
parar de construir o dicionário, e imprimir seu conteúdo na tela.

Saída:

```bash
Digite um par (chave, valor): a, 2
Digite um par (chave, valor): b, 3
Digite um par (chave, valor): 

O dicionário construído é
{'a': 2, 'b': 3}
```

