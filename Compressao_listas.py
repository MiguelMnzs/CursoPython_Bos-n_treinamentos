# numeros = [1,4,7,9,10,12,21]

# quadrados = list(map(lambda num: num**2, numeros))
# print(quadrados)

#  Usando compreensão de listas

# quadrados = [num**2 for num in numeros]
# print(quadrados)

# criar uma lita de numeros pares de 0 a 10

# pares = [num for num in range(11) if num % 2 == 0]
# print(pares)


# frase = 'Ai toma'.lower()
# vogais = ['a', 'e', 'i', 'o', 'u']

# lista_vogais = [v for v in frase if v in vogais]
# print(len(lista_vogais))
# print(lista_vogais)

# Distributiva entre valors de duas listas

distributiva = [k * m for k in [2,3,5] for m in [10,20,30]]
print(distributiva)