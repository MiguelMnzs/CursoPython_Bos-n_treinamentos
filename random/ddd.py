# Solicita dois valores do usuário
valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))

# Compara os valores
if valor1 > valor2:
    print("O maior valor é:", valor1)
elif valor2 > valor1:
    print("O maior valor é:", valor2)
else:
    print("Os dois valores são iguais.")
