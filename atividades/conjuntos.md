# Exercícios conjuntos

1. Utilizando conjuntos em Python, defina dois conjuntos: um com o nome de todos os áudios do Programa do Ratinho,
e outro com os áudios d'A Hora do Faro. Mostre na tela:

    * A interseção dos áudios dos programas
    * A união 
    * Os áudios que estão apenas no programa do Ratinho
    * Os áudios que estão apenas n'A Hora do Faro
    * A diferença da união com a interseção dos áudios dos dois programas

2. Utilizando os conjuntos do exercício anterior, faça uma **projeção** do 
   [Diagrama de Venn](https://pt.wikipedia.org/wiki/Diagrama_de_Venn).
   * [Crie um ambiente virtual](https://github.com/CTISM-Prof-Henry/pythonEssentials/blob/main/chapters/venvs.md#criando-pela-linha-de-comando)
   * Instale a biblioteca matplotlib: `conda install matplotlib --yes`
   * Instale a biblioteca matplotlib-venn: `pip install matplotlib-venn`  
   * Use o _template_ abaixo e faça os ajustes necessários para que ele mostre os conjuntos do exercício anterior. 
       * O código abaixo só ira se o arquivo em que ele foi escrito ele estiver aberto em 
         [um projeto do Pycharm que estiver usando o ambiente virtual recém criado](
         https://github.com/CTISM-Prof-Henry/pythonEssentials/blob/main/chapters/venvs.md#usando-pelo-pycharm), 
         ou se 
         [o ambiente virtual estiver ativado na linha de comando](https://github.com/CTISM-Prof-Henry/pythonEssentials/blob/main/chapters/venvs.md#usando-pela-linha-de-comando)
       * Você pode ver a documentação da função matplotlib-venn [aqui.](https://www.python-graph-gallery.com/venn-diagram/)
```python
import matplotlib.pyplot as plt
from matplotlib_venn import venn2

venn2(subsets=(10, 5, 2), set_labels=('Group A', 'Group B'))
plt.show()
```