planeta_anao = {'Plutão','Ceres','Eris','Haumea','Makemake'}
print(len(planeta_anao))

# print('Ceres' in planeta_anao)


# for astro in planeta_anao:
#     print(astro.upper(), end='')

# astros = ['Lua', 'Venus', 'Sirius', 'Lua', 'Marte']
# print(astros, end=' ')
# astro_set = set(astros)
# print(astro_set)

astro1 = {'Lua', 'Venus', 'Sirius', 'marte'}
astro2 = {'Lua', 'Venus', 'Sirius', 'marte', 'Cometa de Halley'}

print(astro1 != astro2)
print (astro1 | astro2) # juntar os dois conjuntos 
print(astro1.union(astro2)) # uniao de conjuntos 

print(astro1 & astro2) # ou
print (astro1.intersection(astro2)) # apenas elementos em comum


# Diferença entre os conjuntos
print(astro1 ^ astro2)     
print(astro1.symmetric_difference(astro2))


# Adicionar elementos
astro1.add('Urano')
astro2.add('Sol')

# remover
astro1.remove('Urano')
astro2.discard('Sol')
astro1.pop() #remove um elemento aleatorio
astro1.clear() #Remove os elementos dos conjuntos 






