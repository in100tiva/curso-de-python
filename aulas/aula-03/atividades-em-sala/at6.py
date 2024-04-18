# Função para receber os conjuntos e exibir a interseção
def intersecao_conjuntos():
    # Receber os conjuntos do usuário
    conjunto1 = set(input("Digite os elementos do primeiro conjunto separados por vírgula: ").split(","))
    conjunto2 = set(input("Digite os elementos do segundo conjunto separados por vírgula: ").split(","))

    # Calcular e exibir a interseção dos conjuntos
    intersecao = conjunto1.intersection(conjunto2)
    print("Interseção dos conjuntos:", intersecao)

# Chamada da função para testar o programa
intersecao_conjuntos()
