def contar_caracteres(string):
    total_caracteres = len(string)
    maiusculas = sum(1 for char in string if char.isupper())
    minusculas = sum(1 for char in string if char.islower())
    numeros = sum(1 for char in string if char.isdigit())
    especiais = total_caracteres - (maiusculas + minusculas + numeros + string.count(' '))
    barras_de_espaco = string.count(' ')

    return total_caracteres, maiusculas, minusculas, numeros, especiais, barras_de_espaco

string = input("Digite uma string: ")

total, maiusculas, minusculas, numeros, especiais, barras_de_espaco = contar_caracteres(string)

print("Total de caracteres:", total)
print("Letras maiúsculas:", maiusculas)
print("Letras minúsculas:", minusculas)
print("Números:", numeros)
print("Caracteres especiais:", especiais)
print("Barras de espaço:", barras_de_espaco)
