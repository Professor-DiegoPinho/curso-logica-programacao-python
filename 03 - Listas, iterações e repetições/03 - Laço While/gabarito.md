## Mudando de perspectiva

```python
numeros = [1,2,3,4,5,6,7,8,9,10]
contador = 0
while(contador < len(numeros)):
    numero = numeros[contador]
    print(numero)
    contador = contador + 1
```

## Enquanto eu refatoro

```python
participantes = ["maria", "pedro", "joaquim", "dagoberto", "luiza", "isabela"]
print("************* Participantes *************")
contagem = 0
while contagem < len(participantes):
  print(f"{contagem} - {participantes[contagem]}")
  contagem = contagem + 1

```

## Contagem regressiva

```python
count = int(input("Digite um número para a contagem: "))
while(count >= 0):
    print(count)
    count = count - 1
```

## Só pare de somar quando eu avisar

```python
valor = 0
soma = valor
while(valor >= 0):
    soma += valor
    valor = int(input("Digite um número: "))
print(f"A soma dos números é: {soma}")
```

## Adivinha o número!

```python
import random

valor_aleatorio = random.randint(1,10)
chute = 0
tentativas = 0

print(valor_aleatorio)

while(chute != valor_aleatorio):
    chute = int(input("Tente adivinhar o número: "))
    if(chute != valor_aleatorio): tentativas = tentativas + 1

print("Parabéns, você acertou!")
print(f"Número de tentativas: {tentativas}")
```

## Em que horário você está disponível?

```python
horarios = ["09:00 (indisponível)", "10:00 (indisponível)", "11:00 (indisponível)", "12:00", "13:00 (indisponível)", "14:00"]
horario_disponivel = ""

for horario in horarios:
    if(not "indisponível" in horario):
        horario_disponivel = horario
        break

if(horario_disponivel):
    print(f"O primeiro horário disponível é às {horario_disponivel}")
else:
    print("Não há horários disponíveis.")
```

## Quero somente arquivos de imagem

```python
arquivos = ["relatorio.pdf", ".config", "dados.csv", "temp.tmp", "imagem.png"]
arquivos_de_imagem = []

for arquivo in arquivos:
    if not arquivo.endswith(".png"):
        continue
    arquivos_de_imagem.append(arquivo)

print("Arquivos de Imagem:")
print(arquivos_de_imagem)

```
