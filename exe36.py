v=float(input('Qual o valor da casa?'))
s=float(input('Qual o seu salario?'))
p=int(input('Quantos anos será o pagamento?'))
pm= v / (p*12)
minimo = s * 30/100
print('Valor da parcela sera R$ {:.2f}'.format(pm))
if pm >= minimo:
    print('Seu emprestimo será recusado')
else:
    print('Seu emprestimo esta aprovado')