#Programa para calcular o Valor do salário após um aumento

salario = float(input('Digite o salário inicial: '))
porcento = float(input('Digite a porcentagem de aumento: '))
novosalario = salario+salario*(porcento/100)
print('O novo salário será',novosalario,'reais')
