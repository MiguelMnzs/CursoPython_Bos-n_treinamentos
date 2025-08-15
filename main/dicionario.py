# Dicionarios

elemento =  {
    'Z' : 3,
    'nome' : 'Litio',
    'grupo' : 'Metais Alcalinos',
    'Densidade' : 0.534
}

print(f'Elemento: {elemento['nome']}')
print(f'Grupo: {elemento['grupo']}')
print(f'Densidade:  {elemento['Densidade']}')
print(f'Z:  {elemento['Z']}')

print(f'O dicionario possui: {len(elemento)} elementos')

# Atualizar entrada 
elemento['grupo'] = 'Alcalinos'
print(elemento)

# adicionar entrada
elemento['periodo'] = 1
print(elemento)

# Exclusao de itens em dicionarios
del elemento['periodo'] # deleta elementos do dicionario
print(elemento)

elemento.clear() # limpa o dicionario
print(elemento)

del elemento # deleta o dicionario

print(elemento.items()) # Exibe as tuplas 
for item in elemento.items():
    print(item)

print(elemento.keys()) # Exibe uma lista com nome das chaves dos dicionarios
for item in elemento.keys():
    print(item)

print(elemento.values()) # Exibe uma lista com nome dos valores
for item in elemento.values():
    print(item)

for i,j in elemento.items(): #tabela dos valores do dicionarios
    print(F'{i}:{j}')




