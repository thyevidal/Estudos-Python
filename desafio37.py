n = int(input('Qual valor deseja converter? '))
print('Para qual base deseja converter?\n1 - para binário\n2 - para octal\n3 - para hexadecimal')
escolha = int(input(''))

if escolha == 1:
    print('binario')
elif escolha == 2:
    print('octal')
elif escolha == 3:
    print('hexadecimal')
else:
    print('\033[1;31;43mValor digitado é invalido!\033[m ')