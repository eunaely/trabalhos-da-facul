# Inicializa uma lista vazia para armazenar os números inseridos
numeros = []

# Lê os números até que um número não positivo seja digitado
while True:
    num = int(input("Digite um número positivo (ou um número não positivo para encerrar): "))
    
    # Verifica se o número é positivo
    if num > 0:
        numeros.append(num)
    else:
        break

# Inicializa uma lista para armazenar os números que aparecem repetidos
repetidos = []

# Percorre a lista de números e verifica se algum número se repete
for i in range(len(numeros)):
    # Se o número não estiver na lista de repetidos e aparecer novamente, adiciona à lista
    if numeros[i] not in repetidos and numeros.count(numeros[i]) > 1:
        repetidos.append(numeros[i])

# Imprime os números repetidos
print("Números repetidos na lista:", repetidos)


# Cassia naelirde lima
# 20232014050031