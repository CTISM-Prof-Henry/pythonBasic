# Funções 

## Exercícios 

1. Crie uma função que eleve um número ao quadrado:

```python
def quadrado(x):
    pass
```

2. Crie uma função `aplica` que recebe dois parâmetros: uma outra função `func`, 
   e uma lista `a` de números inteiros. Faça com que a função `aplica` aplique
   a função `func` a cada um dos itens da lista `a`.

Exemplo: `func` é a função que eleva um número ao quadrado, e `a` é a lista 
`[2, 3, 4]`

Código:

```python
def aplica(funcao, lista):
   pass  # implementar função que aplica funcao a cada item da lista

def func(x):
    pass  # implementar função que eleva x ao quadrado

a = [2, 3, 4]
print(aplica(func, a))
```

Saída:

```bash
[4, 9, 16]
```

3. Modifique a função `aplica` do exercício anterior para aplicar a função
   `func` usando a função [map](
   https://docs.python.org/pt-br/3.9/library/functions.html#map), nativa de Python.
4. Modifique a função `aplica` do exercício anterior para aplicar a função
   `func` usando [list comprehension](https://docs.python.org/pt-br/3.9/tutorial/datastructures.html#list-comprehensions), um recurso nativo de Python.
5. Utilizando a função `reduce`, crie uma função que **soma** todos os números
   que estão contidos numa lista.

Código:

```python
from functools import reduce
from operator import *

print(reduce(func, [0, 1, 2, 3, 4]))
```

Saída:

```bash
10
```

6. Crie a documentação da função implementada nos exercícios 3, 4, e 5 utilizando
docstrings, como demonstrado no exemplo abaixo:

```python
def hello():
    """
    Retorna 'olá mundo'
    """

    return 'olá mundo!'
```

Para testar se a dosctring está corretamente formatada, execute o código-abaixo
na linha de comando do Anaconda, ou então no próprio código-fonte em que a função
`hello` foi implementada:

```python
help(hello)  
```

Aperte q (de quit) para sair da janela que abrir.

Melhore a documentação da função colocando uma listagem dos parâmetros de entrada,
seus tipos, o tipo de dado de saída da função, e uma descrição dos parâmetros de 
entrada e saída. 


7. [(Adaptado da WikiPython)](
https://github.com/CTISM-Prof-Henry/wikiPythonTerceirao/blob/main/groups/fun%C3%A7%C3%B5es1.md) 
   O Xaropinho não frequentou o Ensino Fundamental (pois obviamente ele é um rato) 
   e não sabe fazer cálculos matemáticos (apesar que, pensando agora, o Ratatouille
   sabe cozinhar...), e ele quer sua ajuda! **Crie uma função**
   para cada um dos operadores que ele escolheu: soma, subtração, divisão, 
   multiplicação, potência): ou seja, 5 funções no total. 

   Teste cada uma das funções para os seguintes valores de entrada:

   | variável A | variável B | 
   |:-----------|:-----------|
   | 2          | 2          |
   | 5          | 7          |
   | 3          | 13         |
   | 17         | 4          |
   | 21         | 15         |
   | 12         | 6          |

8. [(Adaptado da WikiPython)](
https://github.com/CTISM-Prof-Henry/wikiPythonTerceirao/blob/main/groups/fun%C3%A7%C3%B5es1.md) 
   Escreva uma função que recebe dois parâmetros, 
   `texto` e `caixa_alta`. O parâmetro `texto` **não possui** valor padrão, porém 
   o parâmetro `caixa_alta` possui o valor padrão `False`. Esta função deve 
   imprimir o texto `texto` na tela. Quando `caixa_alta = True`, o texto impresso 
   deve ser em MAIÚSCULAS. Quando `caixa_alta = False`, o texto deve ser impresso 
   (todo ele) em minúsculas (independente do usuário tê-lo digitado em minúsculas 
   ou não). Observe os exemplos:

Código:

```python
imprime('olá mundo!')  # vai imprimir 'olá mundo!'
imprime('OLÁ MUNDO!')  # vai imprimir 'olá mundo!'
imprime('olá mundo!', caixa_alta=False)  # vai imprimir 'olá mundo!'
imprime('Olá Mundo!', caixa_alta=False)  # vai imprimir 'olá mundo!'
imprime('olá mundo!', caixa_alta=True)  # vai imprimir 'OLÁ MUNDO!'
```

