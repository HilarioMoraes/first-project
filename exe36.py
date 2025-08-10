v = float(input('Qual o valor da casa? '))
s = float(input('Qual o seu salário? '))
p = int(input('Quantos anos será o pagamento? '))

pm = v / (p * 12)  # valor da parcela mensal
minimo = s * 0.3   # 30% do salário

print('Valor da parcela será R$ {:.2f}'.format(pm))

if pm > minimo:
    print('Seu empréstimo foi recusado.')
else:
    print('Seu empréstimo está aprovado!')
