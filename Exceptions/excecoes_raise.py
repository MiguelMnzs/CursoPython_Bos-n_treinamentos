from math import sqrt  # Importa a função sqrt (raiz quadrada) da biblioteca math

# Define uma exceção personalizada para números negativos
class NegativeNumberError(Exception):
    def __init__(self):
        pass  # Não faz nada adicional, mas poderia receber mensagens ou dados

# Garante que o código abaixo só execute se o arquivo for rodado diretamente
if __name__ == '__main__':
    while True:  # Loop infinito para repetição até que seja interrompido por 'break'
        try:
            # Solicita ao usuário um número e converte para inteiro
            num = int(input('Digite um número positivo: '))
            
            # Se o número for negativo, lança a exceção personalizada
            if num < 0:
                raise NegativeNumberError
        
        # Captura especificamente a exceção NegativeNumberError
        except NegativeNumberError:
            print(f'Número fornecido é negativo!')
        
        # Executa se nenhuma exceção foi gerada no try
        else:
            # Calcula e arredonda a raiz quadrada do número
            print(f'A raiz quadrada de {num} é {round(sqrt(num))}')
            
            # Interrompe o loop, encerrando o programa
            break
        
        # Sempre executa, mesmo se ocorrer exceção
        finally:
            print('Fim de calculo')
