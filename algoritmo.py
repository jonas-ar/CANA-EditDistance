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
            dp[i][j] = min(dp[i - 1][j] + 1, 
                           dp[i][j - 1] + 1, 
                           dp[i - 1][j - 1] + custo)
            
    return dp[m][n]

s1 = "kitten"
s2 = "sitting"
distancia = editDistance(s1, s2)
print(distancia)