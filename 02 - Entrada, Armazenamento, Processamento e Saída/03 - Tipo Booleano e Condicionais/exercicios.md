# Tipo booleano e condicionais

## Este brinquedo é para crianças

- Escreva um programa que recebe a idade do usuário e indica se ele está apto ou não a entrar no brinquedo.
- O brinquedo é para crianças menores de 12 anos.
- Por exemplo:

  ```python
  # exemplo 1
  Qual é a sua idade? # 10
  Você pode brincar!

  # exemplo 2
  Qual é a sua idade? # 14
  Você não pode brincar!
  ```

## Eu sou maior do que você!

- Escreva um programa que determina, entre dois números, qual é o maior entre eles.
- Se os números forem iguais, deve mostrar que eles são iguais.
- Por exemplo:

  ```python
  #exemplo 1
  Insira o primeiro número: # 20
  Insira o segundo número: # 40

  O número 40 é maior

  #exemplo 2
  Insira o primeiro número: # 20
  Insira o segundo número: # 20

  Os números são iguais
  ```

## Faixas de idade

- Escreva um programa que receba a idade do usuário e defina sua faixa com base na tabela abaixo:
  | Classificação| Faixa de idade |
  | ------------ | ------------ |
  | Crianças | 0 a 12 anos |
  | Adolescentes | 13 a 17 anos |
  | Adultos | Acima de 18 |
- Por exemplo:
  ```bash
  Qual a sua idade? #17
  Você é adolescente!
  ```

## Par ou ímpar?

- Escreva um programa que recebe um número inteiro do usuário e determina se o número é par ou ímpar.
- Exemplo:

  ```python
  # exemplo 1
  Qual número? # 12
  O número 12 é par!

  #exemplo 2
  Qual número? # 15
  O número 15 é ímpar!
  ```

- 🤔 Pense antes de codar: Na matemática, como você determina se um número é par?
    <aside>    
    Conseguimos descobrir se um número é par se ele for divisível por 2, ou seja, o resto da divisão dele por 2 precisa ser zero. No Python, podemos fazer essa perguntar com o operador de módulo `%`.
    
    Por exemplo:
    
    ```python
    print(100 % 2) # 0 resto da divisão
    ```
    
    Como podemos usar isso pra resolver esse desafio? 🤔
    </aside>
