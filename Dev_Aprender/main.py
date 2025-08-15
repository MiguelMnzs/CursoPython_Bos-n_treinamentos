# # Variaveis
# Capacidade_Armazenamento = 1000
# print(f'Armazenamento disponivel: {Capacidade_Armazenamento}')

# # Numeros Inteiros(int)
# Idade = 15
# print(f'Idade de Julia é: {Idade}')

# # Numeros Decimais(float)
# media_semestre = 8.76
# print(f'Media Semestral: {media_semestre}')

# # Textos(string)
# Biografia = 'Lorem ipsum dolor sit amet. Ut molestiae reprehenderit est consequuntur doloribus eos laboriosam cumque sed distinctio impedit. Id galisum dolorum ut ullam sint ad expedita omnis vel iusto adipisci est consequatur laboriosam nam culpa voluptates aut culpa galisum. Ut repudiandae voluptatem sed velit necessitatibus sed sunt consectetur ut quas perferendis. Aut ipsum animi id quia quia et nihil galisum ut nihil expedita aut officiis quia aut officia tempora sit ipsum molestias. Sed ipsam dolorem ab minus eius et vero quaerat id fugiat voluptas ex deleniti animi ut neque voluptatem eos laborum esse. Nam fuga voluptas vel possimus illum quo delectus repudiandae et velit provident est ipsam incidunt eos rerum dicta qui molestiae expedita. 33 cumque sunt non officia fugiat ut commodi expedita At ducimus deserunt. 33 necessitatibus quisquam qui unde possimus ea doloribus illum id aliquid quibusdam et necessitatibus ipsa.'

# print(Biografia)

# # Booleanos( True ou false)

# Porta_Aberta = True
# Porta_Fechada = False

# Problema 1 - Valor Hora
# Escreve um programa que retorna o valor hora de um funcionario
# com base no seu salario mensal e horas trabalhadas por mes.

'''
5Q's

1- Salario Mensal, Horas trabalhas por mes.
2- Dividir o salario mensal pelas horas trabalhadas e calcular o valor hora.
3- 
4- O programa deve realizar o calculo de subtracao e exibir na tela o valor hora do 
funcionario. 
5- 
Input salario mensal
input horas trabalhadas por mes
resultado = salario mensal - horas trabalhadas
print resultado

'''


class NegativeNumberError(Exception):
    def __init__(self):
        pass

if __name__=='__main__':
    while True:
        try:
            Salario_mensal = float(input('Digite seu salario mensal: '))
            Horas_mensais = int(input('Digite a Quandidade de horas trabalhadas por mes:'))
            if Salario_mensal < 0 or Horas_mensais < 0:
                raise NegativeNumberError
            break
        except ValueError:
             print('Ocorreu um erro ao ler o valor inserido. Tente Novamente')
            
        except NegativeNumberError:
            print(f'Numeros negativos não são suportados')
            
    try:
        Valor_hora = int(Salario_mensal) / Horas_mensais
    except ZeroDivisionError:
        print(f'Impossivel dividir por zero')
    except:  
        print('Ocorreu um erro inesperado. Tente Novamente!')
    else:
        print(f'Valor hora: {round(Valor_hora,2)}')
    finally:  # Sempre será executado independe de erro ou não
        print('\nFim do Calculo')
            



