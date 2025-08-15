nome = 'Miguel '
letra = nome[2]
print(letra)
print(len(nome))

curso = ' estudando python' 

print(nome + "está" + curso)
print("\n")

frase = 'Vamos estudar!'
# palavras = frase.split()
# print(palavras[1])
# print(palavras)

# for palavra in palavras:
#     print(palavra)

print(frase[0:5])

email = input('Digite seu endereco de email: ')
arroba = email.find("@")
print(arroba)
usuario = email[0:arroba]
dominio = email[arroba+1:]
print(usuario)
print(dominio)

produtos = 'carbonato de sodio e oxido de zinco'
print('sodio' in produtos)
print('magnesio' in produtos)

item = 'hipoclorito'
pos = item.find('clor')
print(pos)
pos = item.find('flu')
print(pos)

objeto_celeste = 'galaxia esperial m31'
print(objeto_celeste.upper()) # Caixa alta
print(objeto_celeste.lower()) # Caixa baixa
print(objeto_celeste.title()) # Cada letra de cada palavra em caixa alta
print(objeto_celeste.capitalize()) # Pimeira letra em caixa alta

suplemento = 'cloreto de magnesio'
n_suplemento = suplemento.replace("magnesio", "zinco") # substitue palavra de uma string atraves de uma nova variavel
print(objeto_celeste.upper()) 
print(suplemento)
print(n_suplemento)

frase = '          ômega 3 é bom para a saude!     '
print(frase)
print(frase.lstrip()) # elimana espaços somente a esquerda
print(frase.rstrip()) # elimana espaços somente a direita
print(frase.strip()) # elimana espaços a esquerda  e a direita

# alinhamento de texto para exibição
fruta = 'Abacate'
print(fruta)
print(fruta.rjust(20)) # .just(quantas espaços a pular, alinhando a direita)
print(fruta.ljust(20)) # .just(quantas espaços a pular, alinhando a esquerda)
print(fruta.center(20)) # .just(quantas espaços a pular, alinhando ao centro)
print(fruta.center(20, '-')) # .just(quantas espaços a pular, caractere a serem adicionados ao redor da palavra)

p = 'Miguel Menezes'
print(p.startswith('Miguel')) # Verifica se inicia com determinado caracter
print(p.endswith('Menezes')) # Verifica se termina com determinado caracter

# Docstrings (Texto geralmente extenso para explicar algo) 
