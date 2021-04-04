valora = int(input('VALOR A '))
valorb = int(input('VALOR B '))

if valora > valorb:
    print('o numero {} é maior que {} '.format(valora, valorb))
elif valora < valorb:
    print('o numero {} é maior que {} '.format(valorb, valora))
else:
    print('os valores {} e {} são iguais '.format(valora, valorb))
