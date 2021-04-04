
valordacasa = int(input('Qual o valor da casa? '))
salario = int(input('Qual o seu salario? '))
meses = int(input('Em quantas prestações pretende pagar? '))
prestacao = valordacasa/meses
porcentagem = 30

if prestacao >= (porcentagem*salario)/100:
    print('\033[4;31;43mLamento mas seu pedido foi negado!\033[m ')

print('O valor da prestação ficará: {} R$'.format(prestacao))