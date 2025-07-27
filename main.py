from algoritmo import editDistance, editDistance_space_optimized
from benchmark import random_strings, bench_pares_strings, exibe_resultados, bench_exibe_caso_simples

if __name__ == "__main__":
    print("O benchmark irá gerar strings aleatórias e formar pares, por favor...")
    n1 = int(input("Digite a quantidade de strings aleatórias: "))
    n2 = int(input("Digite o tamanho das strings: ")) # cuidado ao colocar um valor muito grande no tamanho das strings
    strings = random_strings(n1, n2)
    
    print("Executando algoritmo da versão clássica...")
    resultado_classico = bench_pares_strings(editDistance, strings)
    exibe_resultados(resultado_classico, "Edit-Distance, versão clássica")
    
    print("\nExecutando algortimo da versão otimizada em espaço...")
    resultado_otimizado = bench_pares_strings(editDistance_space_optimized, strings)
    exibe_resultados(resultado_otimizado, "Edit-Distance otimizado em espaço")
    
    opcao = input("\nDeseja realizar o benchmark dos algoritmos com um caso simples? (s/n): ").strip().lower()
    
    if opcao == "s":
        s1 = input("Digite a primeira palavra: ").strip()
        s2 = input("Digite a segunda palavra: ").strip()
        while True:
            try:
                repeticoes = int(input("Digite o número de repetições que você deseja realizar os benchmarks: "))
                if repeticoes > 0:
                    break
                else:
                    print("Digite um número maior que 0.")
            except ValueError:
                print("A entrada não é válida. Somente números inteiros são aceitos.")
        
        print("Versão clássica do algoritmo: ")
        bench_exibe_caso_simples(editDistance, s1, s2, repeticoes)
        print("\nVersão otimizada em espaço do algoritmo: ")
        bench_exibe_caso_simples(editDistance_space_optimized, s1, s2, repeticoes)
    else:
        print("Encerrado pelo usuário")
        