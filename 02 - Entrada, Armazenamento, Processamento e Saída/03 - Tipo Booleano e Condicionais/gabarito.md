## Este brinquedo é para crianças

```python
idade = int(input("Qual é a sua idade? "))
if(idade < 12):
    print("Você pode brincar!")
else:
    print("Você não pode brincar!")
```

## Eu sou maior do que você!

```python
n1 = int(input("Insira o primeiro número: "))
n2 = int(input("Insira o segundo número: "))
if(n1 > n2):
    print(f"O número {n1} é maior.")
elif (n1 < n2):
    print(f"O número {n2} é maior.")
else:
    print("Os números são iguais.")
```

## Faixas de idade

```python
idade = int(input("Qual é sua idade? "))
if (idade >= 18):
    print("Você é adulto.")
elif(idade >= 12):
    print("Você é adolescente.")
else:
    print("Você é criança.")
```

## Par ou ímpar?

```python
numero = int(input("Qual é o número? "))
if(numero % 2 == 0):
    print("O número é par.")
else:
    print("O número é ímpar.")
```
