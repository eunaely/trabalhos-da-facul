def sao_anagramas(palavra1, palavra2):
    # Remove espaços e converte todas as letras para minúsculas
    palavra1 = palavra1.replace(" ", "").lower()
    palavra2 = palavra2.replace(" ", "").lower()
    
    # Verifica se as palavras têm o mesmo comprimento
    if len(palavra1) != len(palavra2):
        return False
    
    # Converte as palavras para listas de caracteres para facilitar a comparação
    lista_palavra1 = list(palavra1)
    lista_palavra2 = list(palavra2)
    
    # Ordena as listas de caracteres
    lista_palavra1.sort()
    lista_palavra2.sort()
    
    # Verifica se as listas ordenadas são iguais
    if lista_palavra1 == lista_palavra2:
        return True
    else:
        return False

# Solicita as palavras ao usuário
palavra1 = input("Digite a primeira palavra: ")
palavra2 = input("Digite a segunda palavra: ")

# Verifica se as palavras são anagramas
if sao_anagramas(palavra1, palavra2):
    print(f"{palavra1} e {palavra2} são anagramas.")
else:
    print(f"{palavra1} e {palavra2} não são anagramas.")
