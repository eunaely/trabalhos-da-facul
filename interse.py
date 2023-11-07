def interseccao(s1, s2):
  """
  Determina o tamanho da interseção entre dois segmentos de reta no eixo x.

  Args:
    s1: Dados do primeiro segmento de reta.
    s2: Dados do segundo segmento de reta.

  Returns:
    O tamanho da interseção entre os segmentos de reta, ou -1 se não houver interseção.
  """

  # Verifica se os segmentos se interceptam.
  if s1[1] <= s2[0] or s2[1] <= s1[0]:
    return -1

  # Calcula o tamanho da interseção.
  tamanho = max(0, min(s2[1], s1[1]) - max(s1[0], s2[0]))

  return tamanho