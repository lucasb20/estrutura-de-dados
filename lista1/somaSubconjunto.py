def somaSubconjunto(index, numeros, soma):
    if index == len(numeros):
        return soma == 0
    if somaSubconjunto(index+1, numeros, soma-numeros[index]):
        return True
    return somaSubconjunto(index+1, numeros, soma)


print(somaSubconjunto(0, [1,2,3,4], 9))