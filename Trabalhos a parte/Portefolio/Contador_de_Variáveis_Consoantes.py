'''
         Programador.....: (C) Teodoro Poulson
         Data............: 14/02/2025
         Observações.....: Contador de vogais e consoantes
'''

# Solicitar ao usuário para inserir uma palavra
palavra = str(input("Apresente uma palavra a sua escolha: "))
print(f" {palavra}")

# Definindo as vogais e consoantes
vogais = 'aeiouAEIOU'
consoantes = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'

# Inicializando os contadores
num_vogais = 0
num_consoantes = 0

# Algoritmo para contar as vogais e consoantes
for letra in palavra:
    if letra in vogais:
        num_vogais += 1
    elif letra in consoantes:
        num_consoantes += 1

# Exibindo os resultados
print(f'Essa palavra tem {num_vogais} vogais.')
print(f'Essa palavra tem {num_consoantes} consoantes.')

