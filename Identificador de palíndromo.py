#Programa para identificar se uma palavra e palíndrome

texto = str(input('Digite a palavra para checar se é palíndrome: '))
invertido = texto[::-1]

if texto == invertido:
    print('Palíndromo encontrado')
else:
    print('Não é palíndromo')

    
