original_lista = [5, 7, 8, 15, 21]
nova_lista = [sum(original_lista[i:]) for i in range(len(original_lista))]
print(nova_lista)