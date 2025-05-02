# Listas

## Dobra tudo!

- Escreva um programa que dobre uma sequência de números contidos em uma lista.
- A lista já deve estar inserida no seu código:
  ```python
  lista = [1,2,3,4,5]
  ```
- O programa deve processar esta lista e exibir o dobro de cada um.
- Exemplo:
  ```python
  Valores dobrados
  2
  4
  6
  8
  10
  ```

## Quem são os participantes?

- Escreva um programa capaz de cadastrar o nome de 5 participantes em um evento.
- Para cada participante, basta cadastrar seu primeiro nome.
- Ao final, seu programa deve exibir o nome de todos os integrantes.
- Utilize uma lista para administrar os nomes do participantes.
- Exemplo:

  ```python
  Qual é o nome do participante? # diego
  Qual é o nome do participante? # julia
  Qual é o nome do participante? # marcos
  Qual é o nome do participante? # rafaela
  Qual é o nome do participante? # alessandra

  Os participantes são:
  diego
  julia
  marcos
  rafaela
  alessandra
  ```

## Segue cadastrando!

- Escreva um programa que faz o registro de um determinado número de nomes.
- O número de nomes que será cadastrado fica por conta do usuário.
- Ao final, exiba todos os nomes que foram cadastrados.
- Exemplo:

  ```python
  Quantos nomes você irá cadastrar? 5

  5x
  Insira o nome: #nome

  Foram cadastrados 5 nomes
  nome1
  nome2
  nome3
  nome4
  nome5
  ```

## Este nome já está sendo usado?

- Escreva um programa que verifica de um determinado já está cadastrado.
- A lista de nomes já cadastrados é esta (utilize dentro do seu programa):
  ```python
  nomes = ["rogério", "felícia", "camila", "cláudia", "raissa"]
  ```
- O usuário vai inserir o nome que ele está procurando. Caso o programa encontre, deve avisar: “Nome encontrado!”.
- Caso contrário, não é preciso avisar nada.
- Exemplo:

  ```python
  Qual nome você procura? #camila
  Nome encontrado!

  Qual nome você procura? #dagoberto
  # o programa não retorna nada
  ```

## Junta isso pra mim?

- Um sistema legado usado por uma empresa cadastra o nome e o sobrenome dos usuários, no entanto, foi descoberto que ele armazena essas informações separadamente (utilize dentro do seu programa):
  ```python
  nomes = ["diego", "joão", "miguel"]
  sobrenomes = ["martins", "paulo", "pereira"]
  ```
- Escreva um programa que consiga exibir o nome dos usuários completos.
- Exemplo:
  ```python
  Nomes completos cadastrados:
  -> diego martins
  -> joão paulo
  -> miguel pereira
  ```

## Aprendendo a tabuada

- Você é uma pessoa de bom coração e quer ajudar os pequenos do ensino do fundamental a aprenderem a boa e velha tabuada.
- Como as crianças hoje já tem muito domínio da tecnologia, você fará isso através de um programa em Python.
- Escreva um programa que possibilite o usuário a escrever um número (de 1 a 10) e mostre a tabuada deste número.
- Exemplo:
  ```python
  Você quer a tabuada de qual número? # 3
  Tabuada do 3
  3 x 1 = 3
  3 x 2 = 6
  3 x 3 = 9
  3 x 4 = 12
  3 x 5 = 15
  3 x 6 = 18
  3 x 7 = 21
  3 x 8 = 24
  3 x 9 = 27
  3 x 10 = 30
  ```
- **🔥 Dica**: Ao usar o for… in range, você pode determinar o número de início e final da repetição. Veja:
  ```python
  for indice in range (20, 25):
  	print(indice)

  # 20
  # 21
  # 22
  # 23
  # 24
  ```
