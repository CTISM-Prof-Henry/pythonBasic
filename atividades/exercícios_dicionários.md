# Exercícios 

## Conjuntos

1. Utilizando conjuntos em Python, defina dois conjuntos: um com o nome de todos os áudios do Programa do Ratinho,
e outro com os áudios d'A Hora do Faro. Mostre na tela:

    * A interseção dos áudios dos programas
    * A união 
    * Os áudios que estão apenas no programa do Ratinho
    * Os áudios que estão apenas n'A Hora do Faro
    * A diferença da união com a interseção dos áudios dos dois programas
    * Após rodar o comando `pip install matplotlib-venn` na linha de comando do
      Anaconda (veja o tutorial no [pythonEssentials](https://github.com/CTISM-Prof-Henry/pythonEssentials/blob/main/chapters/packages.md)),
      utilize o template abaixo para renderizar o diagrama de Venn destes conjuntos:

```python
import matplotlib.pyplot as plt
from matplotlib_venn import venn2

venn2(subsets=(10, 5, 2), set_labels=('Group A', 'Group B'))
plt.show()
```

Documentação em https://www.python-graph-gallery.com/venn-diagram/

## Dicionários 

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

