# Função para converter número binário para decimal
def binario_para_decimal(binario):
    decimal = 0
    tamanho = len(binario) - 1
    
    # Loop de repetição para calcular o número decimal
    for digito in binario:
        decimal += int(digito) * (2 ** tamanho)
        tamanho -= 1
    
    return decimal

# Entrada do usuário (número binário)
numero_binario = input("Digite um número natural na base binária: ")

# Chamando a função e exibindo o resultado
resultado = binario_para_decimal(numero_binario)
print(f'O número {numero_binario} em decimal é: {resultado}')
