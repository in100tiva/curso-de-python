n1 = 6
n2 = 6
n3 = 5

if n1 > n2 and n1 > n3:
    print("n1 é maior que todos!")
elif n2 > n1 and n2 > n3:
    print("n2 é maior que todos!")
elif n1 == n2 and n1 == n3:
    print("Todos os números são iguais!")
elif n1 == n2:
    print("n1 e n2 são iguais e maiores que n3!")
elif n1 == n3:
    print("n1 e n3 são iguais e maiores que n2!")
elif n2 == n3:
    print("n2 e n3 são iguais e maiores que n1!")
else:
    print("n3 é maior que todos!")
