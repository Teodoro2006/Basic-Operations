'''
         Programador.....: (C) Teodoro Poulson
         Data............: 14/02/2025
         Observações.....: Tabela de Verdade do AND e o OR
'''

print("Tabela de Verdade do AND")

print(f"A  B  |  F = A AND B ")
print(f"---------------------")
print(f"0  0  |  {False and False}")
print(f"0  1  |  {False and True} ")
print(f"1  0  |  {True and False} ")
print(f"1  1  |  {True and True}")

print("\n Tabela de Verdade do OR")

print(f"A  B  |  F = A OR B ")
print(f"--------------------")
print(f"1  1  | {True and True}")
print(f"0  1  | {False and True}")
print(f"1  0  | {True and False}")
print(f"0  0  | {False and False}")


