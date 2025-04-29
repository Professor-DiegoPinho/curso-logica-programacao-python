# Projeto: Papel, Tesoura ou Pedra

## Briefing

- Você ficou entediado na sua aula de informática da escola por ela ser muito básica e sem graça e então resolveu usar suas habilidades em programação para criar um jogo de Pedra, Papel ou Tesoura (porque isso sim é interessante).
- Usando o Python, implemente um jogo de Jo Ken Po em que o usuário enfrentará o computador.
- O jogo deve permitir que:
  - O usuário insira a quantidade de rodadas que ele jogará;
  - Para cara rodada, ele deve escolher entre: “tesoura”, “papel” ou “pedra”;
  - O computador deverá fazer um jogada aleatória.
  - Para cada rodada, deve aparecer qual foi a jogada do usuário, do computador e qual foi o resultado, sendo possível ter empate se ambos escolherem a mesma opção.
  - Ao final, o jogo deve mostrar o placar final e quem ganhou.
- Exemplo:

  ```python
  Quantas rodadas? # 3

  # primeira rodada
  Papel, tesoura ou pedra? #papel
  Resultado:
  -- Jogador: papel
  -- Computador: tesoura
  Vencedor: Computador

  # segunda rodada
  Papel, tesoura ou pedra? #papel
  Resultado:
  -- Jogador: papel
  -- Computador: tesoura
  Vencedor: Computador

  # terceira rodada
  Papel, tesoura ou pedra? #papel
  Resultado:
  -- Jogador: papel
  -- Computador: tesoura
  Vencedor: Computador

  Resultado final:
  -- Jogador: 0
  -- Computador: 3
  O computador venceu!
  ```
