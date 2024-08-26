senha = int(input('Digite a senha de quatro dígitos\n'))

while senha != 1234:
    senha = int(input('Senha incorreta. Tente novamente:\n'))
    if senha == 1234:
        print('Seja bem-vindo de volta!')
        break