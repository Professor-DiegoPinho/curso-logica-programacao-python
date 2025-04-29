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
