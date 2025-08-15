# def <nome_funcao> ([argumentos as vezes opcionais]):
#     <intrucoes>

# EXEMPLO:
def mensagem():
    print('Estudar é bom d+!!!')
    print('Eu adoro estudar, estudar ')

#chamar função
mensagem()

# Função com argumentos
def soma(A, B):
    resultado = A + B
    print(resultado)

soma(12, 12)


# Função usando return
def mult(x, y):
    return x * y

a = 5
b = 8
c = mult(a, b)
print(f'O produto de {a} e {b} é {c}')


# 2
def div(k, j):
    if j != 0:
        return k / j
    else: 
        return 'Impossivel dividir por zero'

if __name__ == '__main__':
    a = int(input('Digite um numero: '))
    b = int(input('Digite outro numero: '))

    r = div(a, b)
    print(f'{a} dividido por {b} é igual a {r}')


# 3

def quadrado(val):
    quadrados = []
    for x in val:
        quadrados.append(x ** 2)
    return quadrados

if __name__ == '__main__':
    valores = [2, 5, 7, 9, 12]
    resultados = quadrado(valores)
    for g in resultados:
        print(g)


# def contar(num=11, caractere='+'):
#     for i in range(1,num):
#         print(caractere)

# if '__main__' == '__main__':
#     contar()


x = 5
y = 6
z = 3

def soma_mult(a, b,c = 0 ):
    if c == 0:
        return a * b
    else:
        return a + b + c
    
if __name__ == '__main__':
        res = soma_mult(x, y)
        print(res)

