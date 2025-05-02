## Minha primeira função

```python
def mostrar_cabecalho():
    print("****************************")
    print("PROGRAMA DE SOMA")
    print("Instruções: Insira dois números inteiros e receba a soma.")
    print("****************************")


mostrar_cabecalho()
n1 = int(input("Digite o primeiro valor: "))
n2 = int(input("Digite o segundo valor: "))
soma = n1 + n2

print(f"A soma é...: {soma}")
```

## Refatorando a calculadora - Parte 1

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

## Refatorando a calculadora - Parte 2

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

## Refatorando a calculadora - Parte 3

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

def soma():
    numero1 = int(input("Primeiro valor: "))
    numero2 = int(input("Segundo valor: "))
    print(f"Soma: {numero1 + numero2}")

def subtracao():
    numero1 = int(input("Primeiro valor: "))
    numero2 = int(input("Segundo valor: "))
    print(f"Subtração: {numero1 - numero2}")

def divisao():
    numero1 = int(input("Primeiro valor: "))
    numero2 = int(input("Segundo valor: "))
    if(numero2 == 0):
        print("Divisão impossível")
    else:
      print(f"Divisão: {numero1 / numero2}")

def multiplicacao():
    numero1 = int(input("Primeiro valor: "))
    numero2 = int(input("Segundo valor: "))
    print(f"Multiplicação: {numero1 * numero2}")


while(True):
  opcao = mostrar_menu()
  if(opcao == 1): soma()
  elif(opcao == 2): subtracao()
  elif(opcao == 3): divisao()
  elif(opcao == 4): multiplicacao()
  else:
      print("A aplicação será encerrada.")
      break
print("Fim.")
```

## Repetente

```python
def calcular_media_bimestre():
    nota_p1 = int(input("Nota P1: "))
    nota_p2 = int(input("Nota P2: "))
    media = (nota_p1 + nota_p2)/2
    print(f"Média do bimestre: {media}")
    return media

def calcular_resultado_final(medias, soma_final):
    print(f"Médias: {medias}")
    print(f"Pontos: {soma_final}")
    print(f"Resultado")
    if(soma_final >= 24):
        print("O aluno passou de ano.")
    else:
        print("O aluno não passou de ano.")

medias = []
soma_final = 0
qtd_bimestres = 4
for i in range(qtd_bimestres):
    media_bimestral = calcular_media_bimestre()
    soma_final += media_bimestral
    medias.append(soma_final)

calcular_resultado_final(medias, soma_final)
```
