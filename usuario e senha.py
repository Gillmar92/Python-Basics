#Programa para checar usuário e senha, considerando certo quando ambos os valores são iguais

usuario = str(input('Digite seu usuario:'))
senha = str(input('Digite sua senha: '))

while True:
    if usuario == senha:
        print('Erro! Tente novamente')
        usuario = str(input('Digite seu usuario: '))
        senha = str(input('Digite sua senha: '))
    else:
        print('Bem vindo')
        break
