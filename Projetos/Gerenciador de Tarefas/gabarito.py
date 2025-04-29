tarefas = []

print("Gerenciador de tarefas supimpa")
while True:
    print("Qual ação você gostaria de fazer?")
    print("0 - Sair")
    print("1 - Adicionar uma nova tarefa")
    print("2 - Concluir uma tarefa")
    print("3 - Mostrar todas as tarefas")
    opcao = int(input("Selecione: "))
    if(opcao == 1):
      tarefa = {
        "titulo": input("Qual o título da tarefa? "),
        "descricao": input("Qual a descrição da tarefa? ")
      }
      tarefas.append(tarefa)
    elif(opcao == 2):
      id = int(input("Qual é o identificador da tarefa?" ))
      tarefas.pop(id)
      print("Tarefa concluída!")
    elif(opcao == 3):
      if(len(tarefas) > 0):
        for indice,tarefa in enumerate(tarefas):
          print(f"[] ({indice}) {tarefa.get('titulo')} | {tarefa.get('descricao')}")
      else:
        print("Não há tarefas a serem concluídas.")
    elif(opcao == 0):
      print("Obrigado por utilizar este programa! Até a próxima!")
      break
    else:
      print("Opção inválida. Tente novamente")