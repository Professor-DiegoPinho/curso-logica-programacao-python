## Dobra tudo!

```python
lista = [1,2,3,4,5]

print("Valores dobrados")
for numero in lista:
    print(numero*2)
```

## Quem são os participantes?

```python
participantes = []
for i in range(5):
	participante = input("Qual é o nome do participante? ")
	participantes.append(participante)

print("Os participantes são: ")
for participante in participantes:
	print(participante)
```

## Segue cadastrando!

```python
qtd_nomes = int(input("Quantos nomes você quer cadastrar? "))

nomes = []
for i in range(qtd_nomes):
    nomes.append(input("Insira o nome: "))

print(f"Foram cadastrados {len(nomes)} nomes")
for nome in nomes:
    print(nome)
```

## Este nome já está sendo usado?

```python
nomes = ["rogério", "felícia", "camila", "cláudia", "raissa"]

nome_procurado = input("Que nome você procura? ")
for nome in nomes:
if(nome == nome_procurado):
print("Nome encontrado!")
```

## Junta isso pra mim?

```python
nomes = ["diego", "joão", "miguel"]
sobrenomes = ["martins", "paulo", "pereira"]

print("Nomes completos cadastrados:")
for i in range(3):
  print(f"-> {nomes[i]} {sobrenomes[i]}")
```
