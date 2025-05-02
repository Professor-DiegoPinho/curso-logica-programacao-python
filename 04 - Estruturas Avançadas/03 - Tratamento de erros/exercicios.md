# Tratamento de erros

## Conversão Segura

- O software na mão do usuário pode ser uma loucura. Para evitar que coisas malucas aconteçam, precisamos ter que preparar o código para lidar com possíveis erros.
- Escreva um programa que peça ao usuário para digitar um número inteiro. Se ele digitar algo inválido, exiba uma mensagem e peça para tentar novamente.
- Exemplo:
  ```python
  Digite um número inteiro: # string
  Erro! Digite um número inteiro válido.
  ```

## Divisão Segura

- Todos aprendemos na escola que na operação de divisão, o valor do divisor nunca pode ser zero. No entanto, se não tomamos cuidado em nosso código, esse tipo de operação pode ser catastrófico.
- Escreva um programa que solicite dois números ao usuário e divida o primeiro pelo segundo. Trate os seguintes erros:
  - Divisão por zero (`ZeroDivisionError`).
  - Entrada inválida (`ValueError`) se o usuário digitar algo que não seja um número.
- Por exemplo:

  ```python
  # exemplo 1
  Digite o primeiro número: # 24
  Digite o segundo número: # 0
  Erro: Não é possível dividir por zero.

  # exemplo 2
  Digite o primeiro número: # vinte
  Erro: Entrada inválida. Digite apenas números.
  ```

## Soma de lista

- Já fizemos soma de lista várias vezes. Dada uma lista com N valores, iteramos e eles somamos dentro de uma variável auxiliar acumuladora. Pois bem, agora faremos um pouquinho diferente.
- Peça ao usuário uma lista de números separados por vírgula e some todos os valores. Trate o erro caso ele digite algo inválido.
- Por exemplo:
  ```python
  Digite números separados por vírgula: #10, 20, 30
  A soma é: 60
  ```
- **Dica 🔥**: Para fazer isso, trate a entrada como uma string e a divida usando a função `split()`
