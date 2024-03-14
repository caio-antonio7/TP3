import re

def validar_senha(senha):
    if len(senha) < 8:
        return False, "A senha deve ter pelo menos 8 caracteres."

    if not re.search("[A-Z]", senha):
        return False, "A senha deve conter pelo menos uma letra maiúscula."

    if not re.search("[a-z]", senha):
        return False, "A senha deve conter pelo menos uma letra minúscula."

    if not re.search("[0-9]", senha):
        return False, "A senha deve conter pelo menos um número."

    if not re.search("[!@#$%^&*()_+]", senha):
        return False, "A senha deve conter pelo menos um símbolo: !@#$%^&*()_+"

    return True, "A senha é válida."

senha = input("Digite a senha: ")

valido, mensagem = validar_senha(senha)
print(mensagem)
