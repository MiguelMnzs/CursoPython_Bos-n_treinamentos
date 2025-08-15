# Funcoes Lambda (anonimas)
# sintaxe:
# lambda argumentos: expressao

# quadrado = lambda x: x**2

# for i in range(1,4):
#     print(quadrado(i))

# par = lambda x: x%2 == 0
# print(par(8))


# temp = lambda f: (f - 32) * 5/9
# print(temp(212))



# Função map()
# sintaxe:
# map(função, iteravel)

# num = [1,2,3,4,5,6,7,8]
# dobro = list(map(lambda x: x*2, num))
# print(dobro,'\n')


# palavras = ['Python','é','uma','linguagem','de', 'programacao']
# maiusculas = list(map(str.upper, palavras))
# print(maiusculas,'\n')


# # Função filter()
# # Sintaxe:
# # filter(funcao, sequencia)
# def numero_pares(n):
#     return n % 2 == 0

# numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13]

# num_par = list(filter(numero_pares, numeros))
# print(num_par)

# # Exemplo com lambda
# num_impar = list(filter(lambda x: x % 2 != 0, numeros))
# print(num_impar)


# Função reduce()
# Sintaxe:
# reduce(Funcao, sequencia, valor_inicial)

from functools import reduce

# def mult(x,y):
#     return x * y
# numeros = [1,2,3,4,5,6]
# total = reduce(mult, numeros)
# print(total)


# Soma cumulativa dos quadrados de valores, usando expresão lambda
numeros = [1,2,3,4]
total = reduce(lambda x, y: x**2 + y**2, numeros) 
print(total)