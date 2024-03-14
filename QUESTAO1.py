def contar_vogais_consoantes(frase):
    vogais = 'aeiouAEIOU'
    num_vogais = 0
    num_consoantes = 0
    
    for char in frase:
        if char.isalpha():
            if char in vogais:
                num_vogais += 1
            else:
                num_consoantes += 1
    
    return num_vogais, num_consoantes

frase = input("Digite uma frase: ")

num_vogais, num_consoantes = contar_vogais_consoantes(frase)

print("Número de vogais:", num_vogais)
print("Número de consoantes:", num_consoantes)
