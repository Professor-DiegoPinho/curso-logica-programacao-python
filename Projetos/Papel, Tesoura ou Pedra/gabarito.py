import random

rodadas = int(input("Quantas rodadas?: "))
pontuacao_jogador = 0
pontuacao_maquina = 0

opcoes = ["papel", "tesoura", "pedra"]
for _ in range(rodadas):
  opcao = input("Papel, tesoura ou pedra?: ")
  opcao_maquina = random.choice(opcoes)
  print(f"-- Jogador: {opcao}")
  print(f"-- Computador: {opcao_maquina}")
  if(opcao == opcao_maquina):
    print("Empate!")
  elif(
    (opcao == "tesoura" and opcao_maquina == "papel") or
    (opcao == "papel" and opcao_maquina == "pedra") or
    (opcao == "pedra" and opcao_maquina == "tesoura")
  ):
    print("Vencedor: Você!")
    pontuacao_jogador = pontuacao_jogador + 1
  else:
    print("Vencedor: Computador")
    pontuacao_maquina = pontuacao_maquina + 1
print("Resultado:")
print(f"Jogador: {pontuacao_jogador}")
print(f"Computador: {pontuacao_maquina}")

if(pontuacao_jogador == pontuacao_maquina):
  print("O jogo empatou!")
elif(pontuacao_jogador > pontuacao_maquina):
  print("Você venceu!")
else: 
  print("O computador venceu!")