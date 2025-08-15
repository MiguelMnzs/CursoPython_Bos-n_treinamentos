import os

os.chdir('c:\\teste666')
print(f'Diretorio atual: {os.getcwd()}')


padrao_nome = input('Qual o padrao de nomes de arquivos a usar?')

for contador, arquivo in enumerate(os.listdir()):
    if os.path.isfile(arquivo):
        nome_arquivo, extensao_arquivo = os.path.splitext(arquivo)
        nome_arquivo = padrao_nome + ' ' +  str(contador)

        nome_novo = f'{nome_arquivo}{extensao_arquivo}'
    os.rename(arquivo, nome_novo)

print('\nArquivos Renomeados')