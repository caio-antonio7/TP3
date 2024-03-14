def substituir_palavra(texto, palavra_antiga, palavra_nova):
    novo_texto = texto.replace(palavra_antiga, palavra_nova)
    return novo_texto

texto = input("Digite o texto: ")
palavra_antiga = input("Digite a palavra a ser substituída: ")
palavra_nova = input("Digite a nova palavra: ")

novo_texto = substituir_palavra(texto, palavra_antiga, palavra_nova)

print("Texto com a palavra substituída:")
print(novo_texto)
