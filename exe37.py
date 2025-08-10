
n= int(input('Digite um número :'))
print('''Escolha uma das bases para conversão: 
[ 1 ] converter para Binario
[ 2 ] converter para Octal
[ 3 } converter para Hexadecimal''')
opção= int(input('Sua opção: '))
if opção == 1:
    print('{} cpnvertido para Binario é igual a {}'.format(n, bin(n)[2:]))
elif opção == 2:
    print(' {} convertido para Octal é Igual a {}'.format(n,oct(n)[:2]))
elif opção == 3:
    print(' {} convertido para Hexadecimal é igual a {}'.format( n,hex(n)[:2]))
else:
    print(' Opção invalida tente novamente')
