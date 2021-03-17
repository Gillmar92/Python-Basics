#Programa que troca as vogais de uma palavra por asterisco

palavra = input('Digite a palavra para retirar as vogais: ')
cont = 0
nova = ''#palavra com as vogais trocadas

while cont < len(palavra):
    if palavra[cont] in 'aeiou':
        nova = nova + '*'
    else:
        nova = nova + palavra[cont]

    cont = cont + 1


print (palavra)
print (nova)
    
