import random

print('Gerar cinco números aleatorios entre 1  e 50: \n')
for i in range(5):
    n = random.randint(1,50)
    print(f'Numero: {n}')


valor = random.random() #gera um numero aleatorio mas sem poder colocar um limite
print(f'Numero Gerado: {round(valor * 10, 2)}')

valor =  random.uniform(1,100) #numero real podendo especificar limites
print(f'Numero: {round(valor, 5)}')


L = [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30]
n = random.choice(L) #escolhe aleatoriamente
print(f'Numero escolhido: {n}')


L = [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30]
n = random.sample(L, 3) #consigo escolher mais de um numero aleatorio de uma lista

print(f'Numero escolhido: {n}')


#embaralhar
print(f'Exibir a lista original: {L}')
print(f'Embaralhar a lista e exibi-la: ')
n = random.shuffle(L)
print(L)