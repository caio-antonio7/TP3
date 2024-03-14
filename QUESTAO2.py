def analisar_frequencia_letras(texto):  
    frequencia_letras = {}
    texto = texto.lower()

    for char in texto:
        if char.isalpha(): 
            if char in frequencia_letras:
                frequencia_letras[char] += 1
            else:
                frequencia_letras[char] = 1

    return frequencia_letras

def exibir_histograma_frequencia(frequencia_letras):
    print("Histograma de Frequência de Letras:")
    for letra, frequencia in sorted(frequencia_letras.items()):
        print(letra + ": " + "*" * frequencia)

texto = str(input("Digite o texto: "))

frequencia_letras = analisar_frequencia_letras(texto)

exibir_histograma_frequencia(frequencia_letras)
