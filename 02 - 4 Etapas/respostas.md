## Olá, mundo! (print)

```python
print("Olá, mundo!")
```

## Cartão de Visitas

```python
print("************************")
print("*   Nome: João Silva   *")
print("*   Profissão: Dev     *")
print("*   Cidade: São Paulo  *")
print("************************")
```

## Seja simpático com o usuário

```python
print(f"Olá, {input('Insira o seu nome: ')}! Seja bem-vindo(a)!")
```

## Você não me parece velho(a)

```python
ano_nascimento = int(input("Insira o seu ano de nascimento: "))
idade = 2025 - ano_nascimento
print(f"Você tem {idade} anos!")
```

## Posso dar o troco em bala?

```python
compra = float(input("Qual é o valor da compra? "))
pago = float(input("Quanto o cliente pagou? "))
troco = pago - compra
print(f"O valor do troco é: {troco}")
```

## Estou com frio em Celsius ou Fahrenheit?

```python
celcius = float(input("Qual é a temperatura em Celcius? "))
fahrenheit = celcius * 1.8 + 32
print(f"A temperatura em Fahrenheit é: {fahrenheit}")
```

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

## Autorização negada meu parceiro

```python
username = input("Insira o username: ")
password = input("Insira o password: ")
if(username == "admin" and password == "senhasegura"):
    print("Acesso concedido.")
else:
    print("Sei quem é você não, sai fora!")
```

## Posso ver a sua documentação?

```python
rg = input("Digite o seu RG: ")
cpf = input("Digite o seu CPF: ")
if(rg != "" or cpf != ""):
    print("Documentação cadastrada com sucesso!")
else:
    print("Preencha o RG ou o CPF!")
```

## Cores proibidas no clube

```python
idade = int(input("Qual é a sua idade: "))
cor_da_roupa = input("Qual é a cor da sua roupa? ")
if(idade>=18 and not(cor_da_roupa == "azul" or cor_da_roupa=="verde")):
    print("Seja bem-vindo(a)!")
else:
    print("Entrada proibida!")
```

## Sou obrigado a votar?

```python
idade = int(input("Digite sua idade: "))
if idade >= 18 and idade <= 70:
    print("O voto é obrigatório para você.")
else:
    print("O voto não é obrigatório.")
```

## Verificando múltiplos

```python
numero = int(input("Digite um número: "))
if(numero >= 100 and (numero % 2 == 0 or numero % 5 == 0)):
    print("O número é válido!")
else:
    print("O número é inválido!")
```
