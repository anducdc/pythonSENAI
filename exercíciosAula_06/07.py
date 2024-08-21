notaAluno = int(input('Digite a sua nota:\n'))

if notaAluno <=5:
    print('Nota Baixa...')
elif notaAluno >5 and notaAluno <= 8:
    print('Nota Média.')
else:
    print('Parabéns! Sua nota é alta!')
