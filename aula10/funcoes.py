#max() -->arrays
#min() -->arrays
#len() -->arrays
#sum()

numeros = [1, 2 , 5 , 40, 100, 58]

def media (numeros):
    resultado = sum(numeros) / len(numeros)
    return resultado

print(media(numeros))


#numeroIdade = int(input('Digite a sua idade:\n'))
#numeroAno = int(input('Digite o ano atual:\n'))

def idade (numeroIdade, numeroAno):
    final = numeroAno - numeroIdade
    return final

#print('Você nasceu em:', idade(numeroIdade, numeroAno))
print('Você nasceu em:', idade(34, 2024))


#def saudacao(nome)
def saudacao():
    #print(f'Olá{nome}')
    print('Olá mundo!')

#saudacao('Luciano')
saudacao()


def ola(nome, mensagem='Olá'):
    print(mensagem, nome)

#ola('Luciano', 'oi')
ola('Luciano')

def dividir (numero01, numero02):
    resposta = numero01 // numero02 #--> divisao absoluta
    resto = numero01 % numero02
    return resposta, resto

divisao = dividir(10,2)

print(divisao) #--> resultado é uma tupla


somar = lambda c, d: c + d

print(somar(5, 9))


def exibir_informacoes(*args):
    print('Argumentos posicionais: ', args)

exibir_informacoes(1,4, 'Luciano', 'Teste')

def exibir_informacoes2(**args):
    print('Argumentos nominais: ', args)

exibir_informacoes2(nome='Luciano', idade=30, curso='python')


pessoa = {
    'nome': 'Anderson',
    'idade': 34,
    'estado_civil': 'solteiro',
    'escolaridade': 'mestre' 
    #/\Chave (key)     /\Valor(value)
},
pessoa2 = {
    'nome': 'Luciano',
    'idade': 30,
    'estado_civil': 'casado',
    'escolaridade': 'especialista' 
}

# ==

pessoas=[{
    'nome': 'Anderson',
    'idade': 34,
    'estado_civil': 'solteiro',
    'escolaridade': 'mestre' 
    #/\Chave (key)     /\Valor(value)
},
{
    'nome': 'Luciano',
    'idade': 30,
    'estado_civil': 'casado',
    'escolaridade': 'especialista' 
}]

print(pessoas[1])