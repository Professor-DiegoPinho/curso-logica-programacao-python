## Quantos pacientes você tem?

```python
quantidade_de_pacientes = 3
pacientes = []

for _ in range(quantidade_de_pacientes):
  nome = input("Qual é o primeiro nome do paciente? ")
  sobrenome = input("E o sobrenome? ")
  paciente = {
    "nome": nome,
    "sobrenome": sobrenome
  }

  pacientes.append(paciente)

print("Os pacientes cadastrados são:")
for paciente in pacientes:
  print(f"{paciente.get('nome')} {paciente.get('sobrenome')}")

```

## Nota Fiscal

```python
quantidade_de_produtos = int(input("Quantos produtos? "))
produtos = []

for _ in range(quantidade_de_produtos):
  nome = input("Produto: ")
  preco = float(input("Preço: "))
  produto = {
      "nome": nome,
      "preco": preco
  }
  produtos.append(produto)

total_compra = 0
print("\nNota fiscal")
for produto in produtos:
  total_compra += produto["preco"]
  print(f"- {produto['nome']}   R$ {produto['preco']:.2f}")

print(f"Total: R$ {total_compra:.2f}")
```

## Agenda de contatos

```python
num_contatos = 5
contatos = []

for index in range(num_contatos):
  print(f"Contato {index+1}")
  nome = input("Nome: ")
  telefone = input("Telefone: ")
  contato = {"nome": nome, "telefone": telefone}
  contatos.append(contato)

print("\nSEUS CONTATOS")
print("********************************")
for contato in contatos:
  print(f"{contato.get('nome')}: {contato.get('telefone')}")
```

## Eu tenho o seu número?

```python
contatos = [
    {"nome": "Lígia", "numero": "(11) 97112-1239", "email": "ligia_master@hotmail.com"},
    {"nome": "Carlos", "numero": "(21) 98234-5678", "email": "carlos.souza@gmail.com"},
    {"nome": "Fernanda", "numero": "(31) 99123-4567", "email": "fernanda_oliveira@yahoo.com"},
    {"nome": "Roberto", "numero": "(41) 98765-4321", "email": "roberto123@outlook.com"},
    {"nome": "Juliana", "numero": "(51) 99321-6789", "email": "juliana.lima@live.com"},
    {"nome": "Thiago", "numero": "(61) 98456-7890", "email": "thiago.brasilia@gmail.com"},
    {"nome": "Mariana", "numero": "(71) 99678-1234", "email": "mariana_rj@hotmail.com"},
    {"nome": "André", "numero": "(81) 98700-1122", "email": "andre_pe@icloud.com"},
    {"nome": "Patrícia", "numero": "(91) 98989-6543", "email": "paty.santos@yahoo.com"},
    {"nome": "Eduardo", "numero": "(85) 99444-5566", "email": "eduardo.ceara@gmail.com"},
]

contato_encontrado = None
contato_busca = input("Qual o nome do contato que você está procurando? ")
for contato in contatos:
  if(contato.get("nome") == contato_busca):
      contato_encontrado = contato
      break

print("*******************************")
print("CONTATO")
print("*******************************")
if(contato_encontrado == None):
    print("Não foi encontrado nenhum registro.")
else:
    print(f"Nome: {contato_encontrado.get('nome')}")
    print(f"Número: {contato_encontrado.get('numero')}")
    print(f"E-mail: {contato_encontrado.get('email')}")
```
