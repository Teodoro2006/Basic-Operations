'''
         Programador.....: (C) Teodoro Poulson
         Data............: 03/02/2025
         Observações.....: Menu de Jogo
'''

'''
         Nome............: nomeFuncao
         Parametros......: Nenhum
         Retorno.........: Nenhum
         Observações.....: Primeiro exemplo. 
'''

def apresentarDadosUtilizador(nome = "Patricio", idade = 12):
    print(f"O seu nome é {nome} e idade {idade} ano(s).")
    return (idade + 1)

#Programa Principal 
variavel = apresentarDadosUtilizador("Patricio", 12)

print(f" No proximo ano ele vai ter {variavel} ano(s).")