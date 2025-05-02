## Conversão Segura

```python
try:
    numero = int(input("Digite um número inteiro: "))
    print(f"Você digitou o número {numero}.")
except ValueError:
    print("Erro! Digite um número inteiro válido.")
```

## Divisão Segura

```python
try:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    resultado = num1 / num2
    print(f"Resultado: {resultado}")
except ZeroDivisionError:
    print("Erro: Não é possível dividir por zero.")

except ValueError:
    print("Erro: Entrada inválida. Digite apenas números.")
```

## Soma de lista

```python
try:
  entrada = input("Digite números separados por vírgula: ")
  numeros = [float(num.strip()) for num in entrada.split(",")]  # Converte para float
  soma = sum(numeros)
  print(f"A soma é: {soma}")
except ValueError:
  print("Erro: Certifique-se de digitar apenas números separados por vírgula.")
```
