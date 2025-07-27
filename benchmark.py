import random, string
from timeit import timeit
from memory_profiler import memory_usage
from itertools import combinations
from statistics import mean, stdev

# gera strings (caracteres minúsculos) de forma aleatória
# também tem como entrada a quantidade de strings aleatórias e o tamanho das mesmas
# dessa forma torna a reprodutibilidade mais legível e simplificada
def random_strings(qnt, tam):
    def gerar_string(tam):
        return ''.join(random.choice(string.ascii_lowercase) for _ in range(tam))
    return [gerar_string(tam) for _ in range(qnt)]

# faz benchmark de TEMPO da função
def bench_funcao_tempo(funcao, s1, s2, n):
    return timeit(lambda: funcao(s1, s2), number = n)

# faz benchmark de MEMÓRIA da função
def bench_funcao_mem(funcao, s1, s2):
    uso_mem = memory_usage((funcao, (s1, s2)), interval = 0.001)
    return max(uso_mem) - min(uso_mem)

# faz o benchmark de pares de strings
# não repete os pares e nem considera a ordem
def bench_pares_strings(funcao, lista_strings, repeticoes = 1):
    resultados = []
    for s1, s2 in combinations(lista_strings, 2):
        tempo = bench_funcao_tempo(funcao, s1, s2, repeticoes)
        memoria = bench_funcao_mem(funcao, s1, s2)
        resultados.append((s1, s2, tempo, memoria))
    return resultados

# mostra os resultado e calcula a média, desvio padrão, e tempo bruto do consumo
# que cada algoritmo leva em relação a tempo e memória
def exibe_resultados(resultados, titulo):
    tempos = [r[2] for r in resultados]
    memorias = [r[3] for r in resultados]
    n = len(resultados)

    tempo_total = sum(tempos)
    memoria_total = sum(memorias)
    
    media_tempo = mean(tempos)
    media_memoria = mean(memorias)
    
    desvio_tempo = stdev(tempos) if n > 1 else 0.0
    desvio_memoria = stdev(memorias) if n > 1 else 0.0

    print(f"\n{titulo}")
    print(f"Pares avaliados: {n}")
    print(f"Tempo total: {tempo_total:.6f}s")
    print(f"Memória total: {memoria_total:.6f} MiB")
    print(f"Média de tempo: {media_tempo:.6f}s")
    print(f"Desvio padrão do tempo: {desvio_tempo:.6f}s")
    print(f"Média de memória: {media_memoria:.6f} MiB")
    print(f"Desvio padrão da memória: {desvio_memoria:.6f} MiB")
    
# exibe um caso simples para um único par de escolha arbitrária
def bench_exibe_caso_simples(funcao, s1, s2, repeticoes):
    distancia = funcao(s1, s2)
    tempos = []
    memorias = []
    
    # faz a chamada dos benchmarks
    for _ in range(repeticoes):
        tempo = bench_funcao_tempo(funcao, s1, s2, 1)
        memoria = bench_funcao_mem(funcao, s1, s2)
        tempos.append(tempo)
        memorias.append(memoria)
        
    # utiliza da média como métrica quantitativa 
    # pois os resultados podem mudar a cada execução
    tempo_medio = sum(tempos) / repeticoes
    memoria_media = sum(memorias) / repeticoes
    
    print(f"Strings: '{s1}' e '{s2}'")
    print(f"Distância: {distancia}")
    print(f"Tempo médio: {tempo_medio:.6f}s")
    print(f"Uso de memória média: {memoria_media:.6f} MiB")
    