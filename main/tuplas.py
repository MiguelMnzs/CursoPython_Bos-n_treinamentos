# Tuplas são imutaveis(o conteudo de uma tupla não pode ser mudado dps de criado)

halogenios = ('F', 'cl', 'Br', 'I', 'At')
gases_nobres = ('He', 'Ne', 'Ar', 'Xe','Kr', 'Rn')
elementos = halogenios + gases_nobres

# Operações que não podem ser usadas com tuplas:
# .sort(), .append(), .reverse(), por()..... Ou qualuqer outra que modifique os valores das tuplas 


# Criando uma lista a partir de uma tupla
lista = list(halogenios)
#lista[0] = 'H' 
# Listas podem ser modificadas
print(lista)


# Criando uma tupla a partir de uma lista
dados = ['Li', 'Na', 'K', 'Rb', 'Cs', 'Fr']
alcalinos = tuple(dados) #aqui eu transfomei a lista em tupla
print(alcalinos)