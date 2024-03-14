def cifra_cesar(texto, chave, modo):
    resultado = ''

    for char in texto:
        if char.isalpha():
            if char.isupper():
                inicio = ord('A')
            else:
                inicio = ord('a')
            deslocamento = (ord(char) - inicio + chave * modo) % 26 + inicio
            resultado += chr(deslocamento)
        else:
            resultado += char

    return resultado

mensagem = input("Digite a mensagem: ")
chave = int(input("Digite a chave (um número inteiro): "))

mensagem_codificada = cifra_cesar(mensagem, chave, 1)
print("Mensagem codificada:", mensagem_codificada)


mensagem_decodificada = cifra_cesar(mensagem_codificada, chave, -1)
print("Mensagem decodificada:", mensagem_decodificada)
