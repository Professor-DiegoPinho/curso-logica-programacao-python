## Quanto eu te devo?

```python
emprestimos = [1.90, 5.50, 6.70, 2.25, 3.20, 8.80]
total = 0
for emprestimo in emprestimos:
    total += emprestimo
print(f"Você me deve... R$ {total}")
```

## Qual é o item mais caro?

```python
precos = [1.90, 8.70, 99.90, 51.20, 88.00, 2.50, 21.00]
maior_valor = 0
for preco in precos:
    if(preco > maior_valor):
        maior_valor = preco
print(f"O maior preço da lista é... {maior_valor}")
```

## Você tem este item?

```python
produto_desejado = input("Qual produto você está procurando? ")
produtos = ["queijo", "tomate", "chocolate", "feijão", "sabão"]
disponivel = False
for produto in produtos:
    if(produto == produto_desejado):
        disponivel = True

if(disponivel == True):
    print(f"{produto_desejado} está disponível")
else:
    print(f"{produto_desejado} não está disponível")
```

## Um baita jogador da NBA

```python
pontos_por_jogo = [25, 30, 18, 22, 35, 40, 27, 15, 20, 32, 28, 33, 21, 19, 37, 29, 26, 34, 24, 18, 41, 30, 22, 25, 38, 31, 27, 20, 36, 28, 19, 23, 35, 40, 32, 21, 30, 33, 17, 26, 39, 31, 22, 24, 29, 37, 34, 28, 25, 19, 32, 30, 27, 21, 40, 35, 23, 31, 38, 26, 29, 24, 41, 18, 30, 37, 20, 35, 28, 33, 22, 19, 25, 32, 27, 29, 31, 26, 40, 34, 21, 38]

total = 0
for pontos in pontos_por_jogo:
    total = total + pontos
media = total / len(pontos_por_jogo)
print(f"A média de pontos foi... {media}")
```

## Me dê o dobro!

```python
qtd_valores = int(input("Quantos números você irá inserir? "))
valores = []
valores_dobrados = []
for i in range(qtd_valores):
    valor = int(input("Insira o número: "))
    valores.append(valor)
    valores_dobrados.append(valor*2)
print(f"Valores inseridos: {valores}")
print(f"Valores dobrados: {valores_dobrados}")
```
