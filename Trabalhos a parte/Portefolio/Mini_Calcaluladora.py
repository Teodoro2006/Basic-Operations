'''
     Programador....: (C) Teodoro Poulson
     Data...........: 17/02/2025
     Observações....: Mini Calculadora
'''
# Contéudo do Menu
def calculadora():
   print("****  MENU  ****")
   print("A - adição")
   print("S - Subtração")
   print("M - Multiplicação")
   print("D - Divisão")
   



#Dados de Execução
def dadosDoMenu():
     opcao = input("Introduza uma opção de menu válida [A, S, M, D, T]: ")
     return opcao.upper()

def devolverOperacao(textoinput):
    numero = int(input(textoinput))

    return numero


   
def adicao(operandoA, operandoB):
    return operandoA + operandoB

def subtracao(operandoA, operandoB):
    return operandoA - operandoB

def multiplicacao(operandoA, operandoB):
    return operandoA * operandoB

def divisao(operandoA, operandoB):
    if operandoB == 0:
      return "Opeção Invalida!!"
    else:
      return operandoA / operandoB


# Distingir os dados
def analiseDoMenu(opcao):
     
    if(opcao in["A", "S","M", "D","I"]):
        operandoA = devolverOperacao("Introduza um operando A: ")
        operandoB = devolverOperacao("Introduza um operando B: ")
    if(opcao == "A"):
       resultado = adicao(operandoA, operandoB)
       print(f"{operandoA} + {operandoB} = {resultado}")
       print("adição")
    elif(opcao == "S"):
       resultado = subtracao(operandoA, operandoB)
       print(f"{operandoA} - {operandoB} = {resultado}")
       print("Subtração")
    elif(opcao == "M"):
       resultado = multiplicacao(operandoA, operandoB)
       print(f"{operandoA} * {operandoB} = {resultado}")
       print("Multiplicação")
    elif(opcao == "D"):
         resultado = divisao(operandoA, operandoB)
         print(f"{operandoA} / {operandoB} = {resultado}")
         print("Divisão")
    elif(opcao == "T"):
        print("****** Adeus, e até a proxima!! ******")
    else:
       print("Opção errada")
opcao = "****** Adeus, e até a proxima!! ******"

while(opcao != 'T'):
    calculadora()
    opcao = dadosDoMenu()
    analiseDoMenu(opcao)

def nova_partida(input):
    # 1 - Sim; 2 - Não
    return input == '1'

