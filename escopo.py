var_global = 'Curso Completo de Python' # Disponivel dentro e fora da função

def escreve_texto():
    global var_global #Referencia a uma variavel global fora da função
    var_global = 'Banco de dados com SQL' #Criar uma variavel global dentro da função não sobrescreve a que está fora, ela cria um nova com o mesmo nome mas será local e disponivel somente dentro da função.

    var_local = 'Miguel Menezes'  # Disponivel dentro de uma função
    print(f'Variavel Global: {var_global}')
    print(f'Variavel Local: {var_local}')


if __name__ == '__main__':
    print(f'Executar a função escreve_texto() ')
    escreve_texto()

    print('Tentar acessar as variaveis diretamente: ')
    print(f'Variavel Global: {var_global}')
   # print(f'Variavrl Local: {var_local}') variavel local so pode ser chamada dentro da função


