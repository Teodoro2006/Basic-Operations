'''
     Programador....: (C) Teodoro Poulson
     Data...........: 12/02/2025
     Observações....: Estudo e Analise de Variáveis
'''
numero = 23                 # Variável do tipo inteiro
nota = 19.56                # Variável do tipo real
nome = "Teodoro"            # Variável do tipo string
apelido = "Poulson"         # Variável do tipo string
resposta = True             # Variável do tipo booleano

print("Tipos de variáveis: ")
print("numero -> ", type(numero))
print("nota -> ", type(nota))
print("nome -> ", type(nome))
print("resposta -> ", type(resposta))

resultado = numero + 56 # Operação Soma

print(f"O resultado entre {numero} + 56 faz ser = {resultado}")

nome_completo = (nome +" " + apelido)
print(f"O nome completo do utilizador é {nome_completo}")

