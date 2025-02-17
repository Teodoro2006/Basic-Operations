'''
     Programador....: (C) Teodoro Poulson
     Data...........: 17/02/2025
     Observações....: Procedimento de Funções 
'''
# Exemplo de um procedimento e Função
def procedimento(nome, idade):
    print(f"Olá {nome} !!") 
    print(f"A tua idade é {idade}")

def funcao(numero1, numero2):
    return numero1 + numero2

procedimento("Ricardinho", 18)
resultado = funcao(3, 7)
print(resultado)
