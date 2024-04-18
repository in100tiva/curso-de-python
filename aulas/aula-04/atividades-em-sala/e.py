def lista_de_numeros_pares(lista:list):
    for numero in lista:
        if numero%2==0: 
            print(numero)

lista_qualquer = [1,2,3,4,5]

lista_de_numeros_pares(lista_qualquer)