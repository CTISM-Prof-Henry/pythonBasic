# Exercícios funções

Estes exercícios foram adaptados do [PythonBrasil](https://wiki.python.org.br/https://wiki.python.org.br/ExerciciosFuncoes).

As resoluções estão [aqui.](resoluções/funções_wikipython)

1. Faça um função para imprimir:

    ```
    1
    2   2
    3   3   3
    .....
    n   n   n   n   n   n  ... n
    ```

    para um `n` informado pelo usuário. Use uma função que receba um valor `n` inteiro e imprima até a n-ésima linha. 

2. Faça uma função para imprimir:

    ```
    1
    1   2
    1   2   3
    .....
    1   2   3   ...  n
    ```

    para um `n` informado pelo usuário. Use uma função que receba um valor `n` inteiro e imprima até a n-ésima linha. 

3. Faça uma função que recebe três números inteiros como parâmetro. Faça com que a função cheque o tipo dos parâmetros, 
   e lance uma exceção do tipo `TypeError` caso qualquer um dos parâmetros não seja um número (inteiro ou flutuante).
   Faça a função **retornar** a soma dos três parâmetros.
4. Faça uma função que recebe um número inteiro como parâmetro. Faça com que a função cheque o tipo do parâmetro, e 
   lance uma exceção do tipo `TypeError` caso o valor passado não seja um número. Faça a função retornar -1, 0 ou 1, 
   dependendo se o número for respectivamente negativo, zero ou positivo.
5. Faça uma função que converta um horário que está expresso em 24 horas para a notação de 12 horas. Por exemplo, o 
   programa deve converter `14:25` em `2:25 P.M`. A entrada da função é uma string, no formato `HH:MM`. A string a ser
   retornada deve estar no formato `HH:MM A.M` ou `HH:MM P.M`, dependendo do horário. Use zeros caso a hora tenha 
   apenas um dígito (por exemplo, `01:00 A.M`).
6. Faça uma função que recebe um número inteiro como parâmetro, e retorna o número de dígitos que este número inteiro 
   possui. Faça com que a função cheque o tipo parâmetro passado, e lance uma exceção do tipo `TypeError` caso o 
   parâmetro não seja um número inteiro.
7. Crie uma função que recebe um número inteiro como parâmetro, e retorna o seu inverso. Faça com que a função cheque o 
   tipo parâmetro passado, e lance uma exceção do tipo `TypeError` caso o parâmetro não seja um número inteiro. Reverso
   do número. Exemplo de entrada e saída: `127` deve ser transformado em `721`.
8. Crie uma função que recebe uma string com uma data no formato `DD/MM/AAAA`, e retorna uma string com a data no 
   formato `DD de mêsPorExtenso de AAAA`. Cheque o tipo do parâmetro passado para a função, e lance uma exceção do tipo
   `TypeError` caso o parâmetro não seja do tipo string.
9. Crie uma função que recebe uma palavra, e retorna uma versão embaralhada dela. A função deve retornar uma nova 
   palavra a cada execução, como no exemplo abaixo:
   
   ```python
   palavra = 'python'
   print(embaralha(palavra))  # imprime, por exemplo, 'hynpto', ou qualquer outra combinação de letras de 'python'
   print(embaralha(palavra))  # imprime, por exemplo, 'hynotp', ou qualquer outra combinação de letras de 'python'
   print(embaralha(palavra))  # imprime, por exemplo, 'tyhpno', ou qualquer outra combinação de letras de 'python'
   ```
10. Desenha moldura. Construa uma função que desenhe um retângulo na tela usando os caracteres `+` , `−` e `|`. 
    Esta função deve receber dois parâmetros, `linhas` e `colunas`, que são as dimensões do retângulo a ser impresso
    na tela.