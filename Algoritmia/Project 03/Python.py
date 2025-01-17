'''
      Programador...: Teodoro Poulson
      Data..........: 10/01/2025
      Observação....: Gerar número do EuroMilhões
'''
import random

print("Prémio do EuroMilhões")

print("Números")

Números = [random.randint(1,51) for _ in range(5)]
print(Números)
print("Estrelas")

Estrelas = [random.randint(1,13) for _ in range(2)]
print(Estrelas)
