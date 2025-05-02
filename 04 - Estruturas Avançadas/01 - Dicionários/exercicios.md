## Quantos pacientes você tem?

- Por uma aleatoriedade da vida, você agora está trabalhando na equipe de TI de um hospital e precisa ajudar a administrar o prontuário dos pacientes. Crie um programa para auxiliar no cadastro do prontuário do pronto socorro.
- Seu programa deve cadastrar o `nome`, `sobrenome` e `sintomas` dos pacientes e ao final exibi-los para o usuário.
- Você deve, necessariamente, utilizar um dicionário (mapa) para armazenar os dados dos pacientes.
- Exemplo:

  ```python
  Você deseja cadastrar quantos pacientes? # 3

  Nome do paciente: **Fernando**
  Sobrenome do paciente: **Alberto**
  Sintomas: **Dor nas costas**

  *****************************
  PACIENTES
  *****************************
  Fernando Alberto | Dor de barriga
  Luiz Costa | Dor de cabeça
  Júlia Penteado | Náusea e muita tontura
  ```

## Nota Fiscal

- Você está de volta ao mercado, mas desta vez, como um prestador de serviço de uma empresa de tecnologia especializada em comércio.
- Sua missão agora é atuar no sistema de emissão de nota fiscal.
- Faça um programa que lê uma quantidade de produtos (determinada pelo usuário) e informa o preço total da compra.
- Para cada leitura de produto, o usuário informa qual é produto e o seu respectivo preço.
- O programa deve gerar a nota fiscal com o preço total da compra no final:
- Exemplo:

  ```python
  Quantidade de produtos? # 3

  3x
  Produto: # sabão
  Preço: # 3.30

  ***************************
  NOTA FISCAL
  ***************************
  - Sabão (R$ 3.30)
  - Sabão (R$ 3.30)
  - Sabão (R$ 3.30)
  *****************
  Total: R$ 9.90
  ```

## Agenda de contatos

- Afim de organizar sua agenda de contatos, você resolveu usar suas habilidades em programação para fazer um algoritmo que te ajudasse nisso.
- Em especial, você pensou nos dicionários.
- Para iniciar sua aplicação, faça o registro de cinco contatos, cada um com um nome e um telefone. Ao final, exiba-os no formato abaixo:
  ```python
  NOME DO CONTATO: (XX) XXXXXX
  ```
- Exemplo:

  ```python
  Nome: # Felipinho
  Número: # (11) 9881-6721

  SEUS CONTATOS
  *********************************
  Felipinho: (11) 9881-6721
  ```

## Eu tenho o seu número?

- Você quer manter os seus contatinhos em ordem e por isso resolveu que seria uma boa ideia criar uma aplicação em Python para isso, afinal de contas, você já sabe tudo sobre listas e dicionários.
- Você criou a aplicação e agora tem uma série de números guardados.
- Mas para encontrar esses números agora ficou difícil… Crie um programa que permita o usuário a encontrar as informações de um determinado contato usando o nome como filtro.
- Cada contato contém as seguintes informações:
  - Nome;
  - Número;
  - E-mail.
- Você pode usar a lista de contatos abaixo:

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

  ```

- Por exemplo:

  ```python
  Qual o nome do contato que você está procurando? # Lígia

  ***************************
  CONTATO
  ***************************
  Nome: Lígia
  Número: (11) 97112-1239
  E-mail: ligia_master@hotmail.com
  ```

- E caso não encontre nenhum (variáveis auxiliares):

  ```python
  Qual o nome do contato que você está procurando? # Lígia

  ***************************
  CONTATO
  ***************************
  Não foi encontrado nenhum registro.
  ```
