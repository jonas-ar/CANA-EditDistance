def editDistance(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    
    # inicializa os casos bases
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
        
    # preenche a matriz
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if (s1[i - 1] == s2[j - 1]):
                custo = 0
            else:
                custo = 1
            dp[i][j] = min(dp[i - 1][j] + 1, # deleção
                           dp[i][j - 1] + 1, # inserção
                           dp[i - 1][j - 1] + custo) # substituição
            
    return dp[m][n]

def editDistance_space_optimized(s1, s2):
    # garante que s1 seja a menor string
    # melhora a otimização de espaço
    n, m = len(s1), len(s2)
    if n > m:
        s1, s2 = s2, s1
        n, m = m, n
        
    linha_atual = range(n + 1)
    for i in range(1, m + 1):
        # só é necessário a linha anterior e a linha atual da matriz,
        # não ela inteira. Isso economiza memória
        #
        # a linha atual é reiniciada para calcular a nova linha da matriz,
        # definindo o custo de transformação em uma string vazia (deletar),
        # preenchendo o restante da linha com zeros para serem calculados
        linha_anterior, linha_atual = linha_atual, [i] + [0] * n
        for j in range(1, n + 1):
            # calcula o custo das operações
            insercao, remocao = linha_anterior[j] + 1, linha_atual[j - 1] + 1
            substituicao = linha_anterior[j - 1]
            # se houver caracteres diferentes, há custo na substituição
            if s1[j - 1] != s2[i - 1]:
                substituicao += 1
            # escolhe a melhor operação baseando-se no seu custo
            linha_atual[j] = min(insercao, remocao, substituicao)

    return linha_atual[n]
