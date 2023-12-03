# Inicialização das variáveis
notas = [
    [20222014050134, 0, 45, 10, 100],
    # ... (restante dos dados fornecidos)
]

total_alunos = len(notas)
media_desejada = 60
soma_notas = 0
alunos_acima_media = 0

# Loop sobre cada aluno
for aluno in notas:
    # Cálculo da nota ponderada
    nota_ponderada = aluno[1]*2 + aluno[2]*2 + aluno[3]*3 + aluno[4]*3
    # Adição da nota ponderada à soma total
    soma_notas += nota_ponderada
    # Verificação se o aluno atingiu a média desejada
    if nota_ponderada >= media_desejada:
        alunos_acima_media += 1

# Cálculo da média da turma
media_turma = soma_notas / total_alunos

# Impressão dos resultados
print(f"Alunos acima da média: {alunos_acima_media}")
print(f"Média da turma: {media_turma}")


# Cassia naelir de lima
# 20232014050031