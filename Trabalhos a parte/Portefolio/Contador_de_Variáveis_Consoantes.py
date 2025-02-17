'''
         Programador.....: (C) Teodoro Poulson
         Data............: 14/02/2025
         Observações.....: Contador de vogais e consoantes
'''


palavra = str(input("Apresente uma palavra a sua escolha: "))
print(f" {palavra}")


vogais = 'aeiouAEIOU'
consoantes = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'


contadorVogais = 0
contadorConsoantes = 0


for letra in palavra:
    if letra in vogais:
        contadorVogais += 1
    elif letra in consoantes:
        contadorConsoantes += 1


print(f'Essa palavra tem {contadorVogais} vogais.')
print(f'Essa palavra tem {contadorConsoantes} consoantes.')

