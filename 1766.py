T = int(input())

for t in range(1, T + 1):
    n, m = (int(x) for x in input().split())

    renas = []
    for i in range(n):
        nome, peso, idade, altura = (x for x in input().split())
        renas.append((nome, int(peso), int(idade), float(altura)))
    
    # Dica:
    # Para ordenar uma lista em python com base em um critério específico, basta usar a função sorted() com o parâmetro key.
    # Exemplo:
    # renas = sorted(renas, key=lambda x: x[1])  # Ordena pela posição 1 (peso) (crescente)
    # renas = sorted(renas, key=lambda x: x[1], reverse=True)  # Ordena pelo peso (decrescente)

    # Imprima a resposta:
