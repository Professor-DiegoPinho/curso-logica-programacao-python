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
