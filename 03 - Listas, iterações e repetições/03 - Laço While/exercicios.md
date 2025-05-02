## Mudando de perspectiva

- O `for…in` não é a única forma de iterar no Python. Também podemos usar o `while`.
- Sabendo disso, refatore a repetição abaixo para usar a estrutura do `while` ao invés do `for..in`.
- Código:
  ```python
  numeros = [1,2,3,4,5,6,7,8,9,10]
  for numero in range(len(numeros)):
      print(numero)
  ```

## Enquanto eu refatoro

- O código abaixo apresenta a lista de todos os participantes de uma competição. Refatore o código para usar o laço de repetição `while` ao invés do `for`:
  ```python
  ************* Participantes *************
  0 - maria
  1 - pedro
  2 - joaquim
  3 - dagoberto
  4 - luiza
  5 - isabela
  ```
  ```python
  participantes = ["maria", "pedro", "joaquim", "dagoberto", "luiza", "isabela"]
  print("************* Participantes *************")
  for indice,participante in enumerate(participantes):
      print(f"{indice} - {participante}")
  ```

## Contagem regressiva

- Boas notícias! Suas habilidades com programação são tão impressionantes que você foi contratado para fazer o software de contagem regressiva do próximo foguete que será lançado a lua.
- Escreva um programa capaz de fazer uma contagem regressiva a partir de um número fornecido pelo usuário.
- Exemplo:

  ```python
  Digite um número para a contagem: # 5

  5
  4
  3
  2
  1
  0

  Fim da contagem!
  ```

## Só pare de somar quando eu avisar

- Elabore um programa que faz a soma dos números que o usuário inserir enquanto eles forem positivos. A partir do momento que o usuário inserir um número menor que zero, a conta deve ser encerrada.
- Por exemplo:
  ```python
  Digite um número: 5
  Digite um número: 8
  Digite um número: 3
  Digite um número: -1
  A soma dos números é: 16
  ```

## Adivinhe o número!

- Neste programa, o computador escolhe um número secreto entre **1 e 10.**
- O usuário precisa tentar adivinhar este número. Enquanto ele estiver errando, o programa deve continuar pedindo um número.
- Quando ele acertar, exiba uma mensagem de parabéns e o número de tentativas.
- Por exemplo:
  ```python
  Tente adivinhar o número entre 1 e 10: 5
  Tente novamente!
  Tente adivinhar o número entre 1 e 10: 8
  Parabéns! Você acertou! Foram 2 tentativas.
  ```

## Em que horário você está disponível?

- Você é uma pessoa extremamente ocupada, então resolveu utilizar uma agenda virtual para manter todos os seus compromissos em dia.
- Um colega está tentando te chamar a dias para fazer alguma coisa mas você nunca encontra um horário.
- Dada a lista de horários abaixo e comando `break`, elabore um algoritmo que mostre o primeiro horário disponível:
  ```python
  horarios = ["09:00 (indisponível)", "10:00 (indisponível)", "11:00 (indisponível)", "12:00", "13:00 (indisponível)", "14:00"]
  ```
- Por exemplo:
  ```python
  O primeiro horário disponível é às 12:00
  ```
- Se não houver nenhum horário disponível:
  ```python
  Não há horários disponíveis.
  ```
- **🔥 Dica**: Para saber se uma string possui uma determinada palavra ou letra, podemos usar a seguinte estrutura:
  ```python
  # contém a palavra "muito"?
  frase = "Era um dia muito bonito"
  if "muito" in frase:
  	print("Contém a palavra!")
  else:
  	print("Não tem a palavra!")
  ```

## Quero somente arquivos de imagem

- Para fazer o processamento adequado de uma solução de software, você precisa que seus clientes te enviem os arquivos, no entanto, as vezes eles acabam enviando outros arquivos que não tem nada a ver.
- Dada uma lista de arquivos representadas pelos seus nomes, filtre a lista para ficar somente com os arquivos de extensão`.png`.
- Use esta lista e o comando `continue`:
  ```python
  arquivos = ["relatorio.pdf", ".config", "dados.csv", "temp.tmp", "imagem.png"]
  ```
- Por exemplo:
  ```python
  Arquivos de imagem
  ["imagem.png"]
  ```
- **🔥 Dica**: Use a função includes para saber se o arquivo corresponde ao que você procura:
  ```python
  arquivo = "imagem.png"
  if arquivo.endsWith(".png"):
  	print("arquivo válido")
  else:
  	print("arquivo inválido")
  ```
