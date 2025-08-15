# #Lista: representa uma sequencia de valores

# # sintaxe: nome_lista = [valores]

# n1 = [1,2,3,4,5,6,7]
# n2 = [8,9,10,11,12,13]
# valores = n1 + n2 #Vai concatenar(juntar) as listas
# valores[0] = 9 #Atribuir um novo valor especificando a posicao e a nova entrada de dados
# '''
# -1... Pega os valores do final da lista ate o inicio
#  0... do inicio ao fim
#  sempre inicia com 0 
# '''

# # lens verifica o comprimento de uma lista
# # sort() ordena os valores de uma lista em ordem crescente
# # sum soma dos valores
# # .reverse= inverte a ordem 
# # .append(numero a inserir) insere um novo elemento no final da lista
# # .pop() remove o ultimo elemento da lista
# # .insert(posicao,valor)
#lower() transforma tudo em minusculo

# #valores sequencias
# print(valores[0:0]) #slice


# planetas = ['Mercurio', 'Vênus', 'Marte,', 'Saturno', 'Urano', 'Netuno']
# for planeta in planetas:
#     print(planeta)


#Script bebidas

def recebe_letras():
    letras = []

    for repetir in range(5):
        letra = input(f'Digite uma letra do alfabeto: ').lower()
        letras.append(letra)

    while True:
        condicao = input(f'Você quer ordenar as letras? (s/n): ').lower()
        if condicao in ['s', 'sim', 'yes', 'y']:
            letras.sort()
            break
        elif condicao in ['nao', 'n', 'não']:
            break
        else: 
            print('Digite um comando valido! ')

    return letras

resultado = recebe_letras()
print(resultado)

