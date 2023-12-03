# Leitura da lista de inteiros como uma string
lista_str = input("Digite a lista de inteiros separados por vírgula: ")

# Conversão da string para uma lista de inteiros
lista = [int(x) for x in lista_str.split(',')]

# Inicialização do índice e uso de while para percorrer a lista
indice = 0
while indice < len(lista):
    # Verifica se o número é negativo e o remove
    if lista[indice] < 0:
        lista.remove(lista[indice])
    else:
        indice += 1

# Impressão da nova lista
print("Lista sem números negativos:", lista)


# Cassia naelir de lima
# 20232014050031