'''
         Programador.....: (C) Teodoro Poulson
         Data............: 03/02/2025
         Observações.....: Calcular a media (Funções)
'''

def calcularMedia(nota1 = 13, nota2 = 16, nota3 = 19):
    if((nota1 >= 0) and (nota2 >= 0) and (nota3 >= 0)):
         return(nota1 + nota2 + nota3 / 3)
    else:
        return -1

nota1 = float(input("Introduza a nota1: "))

nota2 = float(input("Introduza a nota2: "))

nota3 = float(input("Introduza a nota3: "))

print(nota1 + nota2 + nota3 / 3)

media = calcularMedia(nota1, nota2, nota3)

print(f"A nota final do aluno é {media}.")
