def cifra_de_cesar(texto, numero):
    texto_cifrado = ""
    for char in texto:
        if char.isalpha():  # verifica se o caractere é uma letra
            valor_ascii = ord(char)  # obtém o valor ASCII do caractere
            valor_cifrado = (valor_ascii - 97 + numero) % 26 + 97  # aplica a cifragem de César
            if char.isupper():  # verifica se o caractere é maiúsculo
                valor_cifrado -= 32  # converte de minúsculo para maiúsculo
            char_cifrado = chr(valor_cifrado)  # converte o valor ASCII de volta para caractere
            texto_cifrado += char_cifrado
        else:
            texto_cifrado += char  # mantém os caracteres que não são letras inalterados
    return texto_cifrado

# Entrada do usuário
texto = input("Digite o texto a ser cifrado: ")
numero = int(input("Digite o número para cifragem de César: "))

# Chama a função e imprime o texto cifrado
texto_cifrado = cifra_de_cesar(texto, numero)
print("Texto cifrado: ", texto_cifrado)
