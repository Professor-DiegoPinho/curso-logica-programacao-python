# Projeto: Gerenciador de Tarefas

## Briefing

- O mundo atual é muito dinâmico e por conta disso é muito difícil estar a par de todas as nossas tarefas, sejam pessoais ou profissionais (ou ambas).
- Existem inúmeras ferramentas no mercado que são “Listas de tarefas” e que nos ajudam a administrar tudo o que temos que fazer. No entanto, muitas delas são pagas e oferecem pouca flexibilidade de customização.
- Agora que já sabemos programar… por que não criamos o nosso próprio gerenciador de tarefas?
- Usando tudo o que você aprendeu até aqui, desenvolva um gerenciador de tarefas capaz de realizar os requisitos abaixo.
- ✅ **Requisitos obrigatórios**

  - Cada tarefa deve ser composta por (pelo menos):
    - Um título _(ex: Regar as plantas)_;
    - Uma descrição _(ex: Não é preciso regar as de plástico)_;
  - Como usuário, quero ser capaz de:

    1. Criar uma nova tarefa;
    2. Ver todas as minhas tarefas (pendentes) - Necessariamente neste formato:

       ```python
       [] (1) Regar | Regar as plantinhas #home
       [] (2) Correr | Fazer exercícios pra não morrer #personal
       ```

    3. Finalizar uma tarefa:
       - Você pode usar o índice da tarefa na lista para saber qual item remover.
       - Para remover um item da lista usando o índice, você pode usar a função `.pop(*<índice>*)`.
       - Por exemplo:
         ```python
         letras = ["a", "b", "c", "d", "e"]
         letras.pop(2)
         print(letras) # ['a', 'b', 'd', 'e']
         ```

- ☑️ **Bônus**
  - Como usuário, quero ser capaz de:
    - Ver a lista de tarefas que já foram concluídas;
    - Classificar as tarefas em listas
      - Mostrar agrupamento de listas ao mostrar as tarefas
