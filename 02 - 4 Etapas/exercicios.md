# Print

## Olá, mundo! (print)

- Escreva o seu primeiro programa em Python!
- Seu programa deve exibir a mensagem "Olá, mundo!"
- Exemplo:
  ```python
  Olá, mundo!
  ```

## Cartão de Visitas

- Escreva um programa que represente o seu cartão de visitas virtual.
- O cartão de visita deve ter pelo menos 3 informações:
  - Nome;
  - Profissão;
  - Cidade.
- Exemplo:
  ```python
  ************************
  *   Nome: João Silva  *
  *   Profissão: Dev    *
  *   Cidade: São Paulo *
  ************************
  ```

# Input, variáveis e tipos de dados

## Seja simpático com o usuário

- Escreva um programa que receba o nome do usuário e o cumprimente com uma mensagem de boas-vindas.
- Exemplo:

  ```python
  Insira o seu nome: # Marquinhos
  Olá, Marquinhos! Seja bem-vindo(a)!
  ```

## Você não me parece velho(a)

- Escreva um programa que receba o ano de nascimento do usuário e descubra quantos anos ele tem.
- Exemplo:
  ```python
  Insira o seu ano de nascimento: # 1992
  Você tem 33 anos!
  ```

## Posso dar o troco em bala?

- Escreva um programa que receba o valor de uma compra, o pagamento feito pelo cliente e diga quanto precisa retornar de troco:
- Por exemplo:
  ```python
  Qual é o valor da compra? # 37.50
  Quanto o cliente pagou? # 40.00
  O valor do troco é: 2.50
  ```

## Estou com frio em Celsius ou Fahrenheit?

- Escreva um programa que converta uma temperatura de graus Celsius para Fahrenheit.
- A fórmula de conversão é:
  ```bash
  F = C × 1.8 + 32
  ```
- Por exemplo:
  ```python
  Qual é a temperatura em Celsius? 32
  O valor em Fahrenheit é: 89.6
  ```

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

# Operadores Lógicos

## Autorização negada meu parceiro

- Escreva um programa que simula o sistema de autenticação de um sistema.
- O usuário irá inserir o `username` e o `password`. Seu sistema deverá verificar se as informações inseridas batem com os dados abaixo:
  ```bash
  username: admin
  password: senhasegura
  ```
- Caso a informação inserida esteja correta, exibir a mensagem: `“Acesso concedido.”`
- Caso contrário: `“Sei quem é você não, sai fora!”`
- Por exemplo:

  ```python
  Insira o username: # joao
  Insira o password: # senhasegura

  Sei quem é você não, sai fora!
  ```

## Posso ver a sua documentação?

- Escreva um programa que cadastre a documentação do usuário.
- Existem duas opções de documento que são aceitas no sistema:
  - RG;
  - CPF.
- O sistema deve perguntas pelas duas e o usuário deve preencher as que quiser. Para as que ele quiser ignorar, ele simplesmente vai apertar `enter`.
- O usuário tem que preencher, necessariamente, PELO MENOS um dos documentos.
- Exemplo:

  ```python
  # Exemplo 1: Somente CPF
  Digite o seu RG: # vazio
  Digite o seu CPF: 1328309

  Documentação cadastrada com sucesso!

  # Exemplo 2: Nenhum documento
  Digite o seu RG: # vazio
  Digite o seu CPF: # vazio

  Preencha o RG ou CPF!
  ```

## Cores proibidas no clube

- Escreva um programa que valida se uma pessoa pode ou não entrar no clube.
- Existem 2 regras para entrar neste clube:
  1. Precisa ser maior de idade;
  2. Não pode estar usando as cores azul ou verde.
- Caso qualquer uma dessas regras seja violada, a pessoa é proibida de entrar.
- Exemplo:

  ```python
  Qual sua idade? 20
  Qual a cor da sua roupa? preto

  Seja bem-vindo!
  ```

## Sou obrigado a votar?

- Escreva um programa que diz pro usuário se ele é obrigado a votar ou não.
- No Brasil, o voto é obrigatório a partir dos 18 anos até os 70 anos.
- Exemplo:

  ```python
  # exemplo 1
  Digite sua idade: # 20
  O voto é obrigatório para você.

  # exemplo 2
  Digite sua idade: # 72
  O voto não é obrigatório.
  ```

## Verificando múltiplos

- Escreva um programa que determina se um número dado pelo usuário é:
  - maior ou igual a 100 E
  - múltiplo de 2 OU de 5.
- Por exemplo:
  ```python
  # exemplo 1
  Digite um número: # 150
  Este número é válido!

  # exemplo 2
  Digite um número: # 10
  Este número é inválido!

  # exemplo 3
  Digite um número: # 117
  Este número é inválido!
  ```
- 🔥 Dica: Para saber se um número é múltiplo de outro, usamos o operador de resto (`%`). Por exemplo: `numero % 2 == 0` ⇒ isso verifica se o número é divisível por 2.
