valorTotal = float(input('Digite o valor do produto para calcular o desconto de 10%\n'))

valorDesconto = valorTotal / 10

valorFinal = valorTotal - valorDesconto

print('O produto de R$', valorTotal, 'recebeu um corte de R$', valorDesconto, 'e agora custa R$', valorFinal)
