#Programa que pede 10 números à escolha do usuário e mostra o somatório dos números pedidos"

n = 1 
soma = 0

while n<=10:
    x = int (input(f'{n} número: '))
    soma = soma+x
    n = n+1

print('A soma dos números digitados é: ',soma)
