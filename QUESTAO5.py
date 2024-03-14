def romano_para_decimal(romano):
    romano_valores = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    decimal = 0
    prev_valor = 0

    for char in romano[::-1]:
        valor = romano_valores[char]

        if valor < prev_valor:
            decimal -= valor
        else:
            decimal += valor

        prev_valor = valor

    return decimal

def decimal_para_romano(decimal):
    romano_valores = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L', 90: 'XC', 
                      100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}
    romano = ''

    for valor in sorted(romano_valores.keys(), reverse=True):
        while decimal >= valor:
            romano += romano_valores[valor]
            decimal -= valor

    return romano

numero_romano = str(input("Digite o número romano: "))
decimal = romano_para_decimal(numero_romano)
print(f"O número romano {numero_romano} é equivalente a {decimal} em decimal.")

numero_decimal = int(input("Digite o número decimal: "))
romano = decimal_para_romano(numero_decimal)
print(f"O número decimal {numero_decimal} é equivalente a {romano} em romano.")
