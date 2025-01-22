'''
      Programador...: Teodoro Poulson
      Data..........: 20/01/2025
      Observação....: Calcular a area de um retângulo
'''

def calcular_area_retangulo(comprimento: float, largura: float) -> float:
    return comprimento * largura

comprimento = float(input("Introduza o comprimento do retângulo: "))
largura = float(input("Introdua a largura do retângulo: "))

area = calcular_area_retangulo(comprimento, largura)

print(f"A área do retângulo é: {area:.2f}")