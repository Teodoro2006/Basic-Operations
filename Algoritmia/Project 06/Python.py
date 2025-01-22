'''
     Programador...: Teodoro Poulson
     Data..........: 22/01/2025
     Observações...: Calcular a média de um aluno
'''
aluno = str(input("Digite o nome do aluno: "))

ELF = float(input("Introduzir a média do em ELF: "))

IMEI = float(input("Introduzir a média do em IMEI: "))

SDAC = float(input("Introduzir a média do em SDAC: "))

CD = float(input("Introduzir a média do em CD: "))

media = (SDAC + IMEI + CD + ELF / 4 );

if [media > 9.5]:
            print(f"O {aluno} transitou!!")
else: 
            print(f"O {aluno} não transitou!!")