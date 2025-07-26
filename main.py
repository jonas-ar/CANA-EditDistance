from algoritmo import editDistance, editDistance_space_optimized
from benchmark import random_strings, bench_pares_strings, exibe_resultados

if __name__ == "__main__":
    strings = random_strings(100, 100)
    
    print("Executando algoritmo da versão clássica...")
    resultado_classico = bench_pares_strings(editDistance, strings)
    exibe_resultados(resultado_classico, "Edit-Distance, versão clássica")
    
    print("\nExecutando algortimo da versão otimizada em espaço...")
    resultado_otimizado = bench_pares_strings(editDistance_space_optimized, strings)
    exibe_resultados(resultado_otimizado, "Edit-Distance otimizado em espaço")
    