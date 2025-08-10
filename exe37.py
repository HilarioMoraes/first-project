
n = int(input('Digite um número: '))
print('''Escolha uma das bases para conversão: 
[ 1 ] converter para Binário
[ 2 ] converter para Octal
[ 3 ] converter para Hexadecimal''')

opcao = int(input('Sua opção: '))

if opcao == 1:
    print('{} convertido para Binário é igual a {}'.format(n, bin(n)[2:]))
elif opcao == 2:
    print('{} convertido para Octal é igual a {}'.format(n, oct(n)[2:]))
elif opcao == 3:
    print('{} convertido para Hexadecimal é igual a {}'.format(n, hex(n)[2:]))
else:
    print('Opção inválida. Tente novamente.')
