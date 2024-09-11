import random

numeros = [random.randint(1, 100) for _ in range(10)]

multiplos_de_tres = [num for num in numeros if num % 3 == 0]

print("Números gerados:", numeros)
print("Múltiplos de 3:", multiplos_de_tres)
