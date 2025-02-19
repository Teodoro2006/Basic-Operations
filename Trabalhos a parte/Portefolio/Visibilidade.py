'''
     Programador....: (C) Teodoro Poulson
     Data...........: 17/02/2025
     Observações....: Visibilidade
'''
x = 7

def procedimento():
    global x
    x = 40
    print(x)

def procedimento1():
    print(x)

procedimento()
procedimento1()
print(procedimento, procedimento1)