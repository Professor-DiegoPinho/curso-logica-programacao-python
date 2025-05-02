## Minha primeira função

- O código abaixo funciona, mas podemos melhorá-lo fazendo uma pequena refatoração.
- Refatore o código abaixo criando uma função chamada `mostar_cabecalho()` para isolar o cabeçalho:

  ```python
  print("****************************")
  print("PROGRAMA DE SOMA")
  print("Instruções: Insira dois números inteiros e receba a soma.")
  print("****************************")

  n1 = int(input("Digite o primeiro valor: "))
  n2 = int(input("Digite o segundo valor: "))
  soma = n1 + n2

  print(f"A soma é...: {soma}")
  ```

## Refatorando a calculadora - Parte 1

- O código abaixo funciona, no entanto, está ficando muito difícil de dar manutenção nele.
- Vamos melhorá-lo usando funções.
- Código:

  ```python
  while(True):
    print("""
    Que operação você deseja fazer?

    1 - soma
    2 - subratração
    3 - divisão
    4 - multiplicação
    0 - sair
    """)

    opcao = int(input("Digite a sua opção: "))
    if(opcao == 1):
      numero1 = int(input("Primeiro valor: "))
      numero2 = int(input("Segundo valor: "))
      print(f"Soma: {numero1 + numero2}")
    elif(opcao == 2):
      numero1 = int(input("Primeiro valor: "))
      numero2 = int(input("Segundo valor: "))
      print(f"Subtração: {numero1 - numero2}")
    elif(opcao == 3):
      numero1 = int(input("Primeiro valor: "))
      numero2 = int(input("Segundo valor: "))
      if(numero2 == 0):
          print("Divisão impossível")
      else:
        print(f"Divisão: {numero1 / numero2}")
    elif(opcao == 4):
        numero1 = int(input("Primeiro valor: "))
        numero2 = int(input("Segundo valor: "))
        print(f"Multiplicação: {numero1 * numero2}")
    else:
        print("A aplicação será encerrada.")
        break
  print("Fim.")

  ```

- O primeiro passo é isolar o menu em uma função. Crie uma função chamada `mostrar_menu()` para isolar ele.

## Refatorando a calculadora - Parte 2

- Altere a função `mostrar_menu()` para juntar o comportamento destes dois códigos:
  ```python
    mostrar_menu()
    opcao = int(input("Digite a sua opção: "))
  ```
- Para isso, a função `mostrar_menu()` deverá fazer um retorno.
- Faça as alterações necessárias:

  ```python
  def mostrar_menu():
    print("""
    Que operação você deseja fazer?

    1 - soma
    2 - subratração
    3 - divisão
    4 - multiplicação
    0 - sair
    """)

  while(True):
    mostrar_menu()
    opcao = int(input("Digite a sua opção: "))
    if(opcao == 1):
      numero1 = int(input("Primeiro valor: "))
      numero2 = int(input("Segundo valor: "))
      print(f"Soma: {numero1 + numero2}")
    elif(opcao == 2):
      numero1 = int(input("Primeiro valor: "))
      numero2 = int(input("Segundo valor: "))
      print(f"Subtração: {numero1 - numero2}")
    elif(opcao == 3):
      numero1 = int(input("Primeiro valor: "))
      numero2 = int(input("Segundo valor: "))
      if(numero2 == 0):
          print("Divisão impossível")
      else:
        print(f"Divisão: {numero1 / numero2}")
    elif(opcao == 4):
        numero1 = int(input("Primeiro valor: "))
        numero2 = int(input("Segundo valor: "))
        print(f"Multiplicação: {numero1 * numero2}")
    else:
        print("A aplicação será encerrada.")
        break
  print("Fim.")

  ```

## Refatorando a calculadora - Parte 3

- Assim como você fez anteriormente, separe as operações de soma, subtração, divisão e multiplicação em funções separadas.
- Faça as alterações necessárias:

  ```python
  def mostrar_menu():
    print("""
    Que operação você deseja fazer?

    1 - soma
    2 - subratração
    3 - divisão
    4 - multiplicação
    0 - sair
    """)

    return int(input("Digite a sua opção: "))

  while(True):
    opcao = mostrar_menu()
    if(opcao == 1):
      numero1 = int(input("Primeiro valor: "))
      numero2 = int(input("Segundo valor: "))
      print(f"Soma: {numero1 + numero2}")
    elif(opcao == 2):
      numero1 = int(input("Primeiro valor: "))
      numero2 = int(input("Segundo valor: "))
      print(f"Subtração: {numero1 - numero2}")
    elif(opcao == 3):
      numero1 = int(input("Primeiro valor: "))
      numero2 = int(input("Segundo valor: "))
      if(numero2 == 0):
          print("Divisão impossível")
      else:
        print(f"Divisão: {numero1 / numero2}")
    elif(opcao == 4):
        numero1 = int(input("Primeiro valor: "))
        numero2 = int(input("Segundo valor: "))
        print(f"Multiplicação: {numero1 * numero2}")
    else:
        print("A aplicação será encerrada.")
        break
  print("Fim.")

  ```

## Repetente

- Escreva um programa que ajude a escola a calcular a média final dos alunos.
- A média é composta pela soma das notas dos quatro bimestres, sendo que:
  - Cada bimestre é composto pela nota média simples de duas provas.
- A soma precisa dar acima de 24 pontos.
- Utilize funções para organizar o código.
- Exemplo:
  ```python
  Nota P1: 10
  Nota P2: 10
  Média do bimestre: 10.0
  Nota P1: 10
  Nota P2: 10
  Média do bimestre: 10.0
  Nota P1: 10
  Nota P2: 10
  Média do bimestre: 10.0
  Nota P1: 10
  Nota P2: 10
  Média do bimestre: 10.0

  Médias: [10.0, 20.0, 30.0, 40.0]
  Pontos: 40.0
  Resultado
  O aluno passou de ano.
  ```
