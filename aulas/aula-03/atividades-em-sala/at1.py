# Criar um conjunto vazio chamado frutas
frutas = set()

# Adicionar frutas ao conjunto
frutas.update(["maçã", "banana", "uva", "laranja", "morango"])

# Imprimir o conjunto de frutas
print("Conjunto de frutas antes dos compostos:", frutas)

# Adicionar compostos ao conjunto de frutas
frutas.update(["banana prata", "laranja valência", "uva itália"])

# Imprimir o conjunto de frutas atualizado com os compostos
print("Conjunto de frutas com os compostos:", frutas)

# Verificar se a fruta "banana" está presente no conjunto frutas
if "banana" in frutas:
    print("A fruta banana está presente no conjunto frutas.")
else:
    print("A fruta banana não está presente no conjunto frutas.")