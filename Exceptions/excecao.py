
# Exceção é um objeto que representa um erro que ocorreu ao executar o programa.
# blocos try ... except

class NegativeNumberError(Exception):
    def __init__(self):
        pass

def div(k, j):
    return round(k / j, 2)

if __name__ == '__main__':
    while True:
        try:
            n1 = int(input('Digite um numero: '))
            n2 = int(input('Digite outro numero: '))
            if n1 < 0 or n2 < 0:
                raise NegativeNumberError
            break
        except ValueError:
            print('Ocorreu um erro ao ler o valor inserido. Tente Novamente')
        except NegativeNumberError:
            print('Numero Negativo, tente novamente')

    try:   # Dentro do Try é colocado o codigo que pode gerar um erro especifico
        r = div(n1, n2)
    except ZeroDivisionError: # Captura a exceção que pode ocorrer e faz o tratamento para evitar a falha da aplicação 
        print('Não é possivel dividir por zero!')
    except:  
        print('Ocorreu um erro inesperado. Tente Novamente!')
    else:
        print(r)
    finally:  # Sempre será executado independe de erro ou não
        print('\nFim do Calculo')


# n1 = int(input('Digite um numero: '))
# n2 = int(input('Digite outro numero: '))

# try: # Dentro do Try é colocado o codigo que pode gerar um erro especifico
#     r = round(n1 / n2, 2)
# except ZeroDivisionError: #Captura a exceção que pode ocorrer e faz o tratamento pata evitar a falha da aplicação 
#     print('Não é possivel dividir por zero!')
# else: # Opcional
#     print(r)
