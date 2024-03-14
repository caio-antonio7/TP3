def calcular_media(numeros):
    numeros = numeros.replace(',', '.')
    numeros = numeros.split()
    numeros_float = [float(num) for num in numeros]
    media = sum(numeros_float) / len(numeros_float)
    return media

numeros_input = input("Digite uma sequência de números separados por espaço: ")

try:
    media = calcular_media(numeros_input)
    print("A média dos números é:", media)
except ValueError:
    print("Erro: Certifique-se de que digitou números válidos separados por espaço.")
