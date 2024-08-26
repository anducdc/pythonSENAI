from fcntl import LOCK_WRITE
from re import T
from socket import CAN_RAW_LOOPBACK


texto = 'Luciano Ferreira             '

texto.capitalize()

print(texto.capitalize())

#   .lower()
#   .upper()
#   .replace('ç','c')
#   .strip() ------> remover espaços antes e depois
#   .split() ---> string em array
#   .join()                 ' '.join(nome_array)   -----> array em string
#   .slice() ---> print(cidade[12:16]) - imprimir caracteres dos índices especificados

#palindromo = 'Arara'
#if palindromo.lower() ==[::-1].lower():                          [::-1] ---> inverte uma String
#   #print(é palindromo)
#else:
#   print('não é palindromo')

#LISTA.PY

#C   R   U   D
#R   E   P   E
#E   A   D   L
#A   D   A   E
#T       T   T
#E       E   E

#.append() ---> adicionar um elemento ao array
#.extend(['Shina', 'Maryn']) ---> adiciona vários elementos à array
#.insert(0, 'Athena') ---> adicionar elemento ao índice específico
#.remove('Shun') ---:remover um elemento pelo valor
#.pop() --->exclui o ultimo elemento da lista, (#numerodoindice) = excluir elemento de indice específico
#.index('Hyoga) ---> mostra o número de índice de um elemento
#.sort() ---> ordena a lista de forma crescente
#.reverse
#.del frutas[0] ---> deleta elemento na posição específica
#.clear --->limpar array
#.count('Aldebaran') ---> conta a quantidade de elementos com este valor