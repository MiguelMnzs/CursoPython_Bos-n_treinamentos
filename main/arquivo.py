# # Manipulação de arquivos de texto.


# manipulador = open('arquivo.txt', 'r', encoding='utf-8')

# print(f'\nMetodo read(): \n')
# print(manipulador.read())  # Ler o texto

# print(manipulador.readline()) # Retorna uma linha de texto

# print(manipulador.readlines()) # Retorna uma lista de valores com as strings do arquivo de texto

# texto = input('Qual termo deseja procurar no arquivo: ')

# try:
#     manipulador = open('C:\\Users\\Miguel Ricardo\\OneDrive\\Documentos\\Pytest INDT\\aitoma.txt', 'r', encoding='utf-8')
#     for linhas in manipulador:
#         linhas = linhas.rstrip()
#         if texto in linhas:
#             print('A linha foi encontrada')
#             print(linhas)

#         print(linhas)
# except IOError:
#     print(f'Não foi possivel abrir o arquivo')
# else:
#     manipulador.close() # Close fecha o acesso a esses arquivos e libera memoria 


# Escrever em arquivos de texto

try:
    manipulador = open('C:\\Users\\Miguel Ricardo\\OneDrive\\Documentos\\Pytest INDT\\aitoma.txt', 'w', encoding='utf-8')
    manipulador.write('aloooooo?\n')
    manipulador.write('ai toma ')

except IOError:
    print(f'Não foi possivel abrir o arquivo')
else:
    manipulador.close() # Close fecha o acesso a esses arquivos e libera memoria 
