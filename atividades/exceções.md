# Exceções

Depois do seu divórcio com Kim Kardashian, Kanye West tem se sentido muito triste,
e fazendo coisas **estranhas**. O site TMZ reportou por exemplo que ele tem 
assistido a muitas e muitas horas do Programa do Ratinho. 

Ajude Ye a superar o término desta relação tratando as **exceções** que ocorrem
nos códigos-fonte abaixo.

* Em um primeiro nomento, **Não corrija o erro que os código-fonte apresentam. 
Apenas trate as exceções.** (vamos deixar o artista fazer a arte dele)
* Depois, refaça cada um dos exercícios, corrigindo o código de maneira que ele
  rode sem exceções (vamos dar uma mãozinha para Ye se recuperar)


1. **(resolvido)** Use uma cláusula `try` e outra cláusula `except` para tratar
   a exceção abaixo. Especifique o tipo de exceção que está sendo tratada, e 
   atribua-a para uma variável de nome `error`.

```python
string = \
    "No one man should have all that power\n" + \
    "The clock's ticking, I just count the hours\n" + \
    "Stop tripping, I'm tripping off the power\n" + \
    21 + "st-century schizoid man)"
```

Solução:

```python
try:
    string = \
    "No one man should have all that power\n" + \
    "The clock's ticking, I just count the hours\n" + \
    "Stop tripping, I'm tripping off the power\n" + \
    21 + "st-century schizoid man)"

    print(string)

# cláusula except trata exceções do tipo TypeError, 
# e caso uma exceção seja capturada, a atribui para 
# uma variável de nome error
except TypeError as error:  
    print('o tempo vai curar esse erro:', error)  # o tempo cura tudo.
```

2. Use a cláusula `finally` para, independentemente se o código abaixo executar
   com erros ou não, a frase `letra da música father stretch my hands pt 1` 
   seja impressa na tela.

```python
letra1 = \
    "Beautiful morning, you're the sun in my morning, babe\n" + \
    "Nothing unwanted\n" + \
    "Beautiful morning, you're the sun in my morning, babe\n" + \
    "Nothing unwanted\n" + \
    "\n" + \
    "I just want to feel liberated, I, I, na-na-na\n" + \
    "I just want to feel liberated, I, I, na-na-na\n" + \
    "If I ever instigated, I'm sorry\n" + \
    "Tell me, who in here can relate? I, I, I"

print(letra2)
```

3. Use duas cláusulas `except` para tratar os dois tipos de exceção que o código
   abaixo gera.

```python
all_of_the_lights = [
    'Cop lights', 'flashlights', 'spotlights', 'Strobe lights', 'street lights'
]

for i in range(6):
    if i < 2:
        print(all_of_the_lights[i], end=', ')
    elif (i == 2) or (i == 4):
        print(all_of_the_lights[i])
    elif 2 < i <= len(all_of_the_lights):
        print(all_of_the_lights[i], end=', ')
    
raise ValueError(
    '\nFast life, drug life\nThug life, rock life\nEvery night (all of the nights)'
)
```

4. Corrija o código abaixo, especificando o tipo de exceção que a cláusula 
`except` irá capturar, e corrigindo o caminho relativo dentro do carregamento
de imagem da cláusula `except`, de forma que ele carregue corretamente uma imagem.

```python
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

try:
    img = Image.open("imagens/cura_onde_doi.jpg")  
except:  # especificar o tipo de exceção aqui
    # caminho relativo: trocar por absoluto ou corrigir o relativo
    img = Image.open("imagens/curou_onde_doia.jpg")  
finally:
    plt.imshow(img)
    plt.axis('off')
    plt.show()
```
