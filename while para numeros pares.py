#Programa em que o usuário digita um número e o python imprime a sequência de números pares até
#o número digitado

x = int(input('Digite até qual número devo imprimir: '))
y = 0

while y<=x:
    if y%2==0:
        print(y)
    else: print(f' {y} não é par')
    y = y+1
    
