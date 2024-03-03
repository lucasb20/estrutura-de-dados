def somaSubconjunto(inicio, numeros, total, soma):
    if inicio >= total:
        return soma == 0
    if somaSubconjunto(inicio+1, numeros, total, soma-numeros[inicio]):
        return True
    return somaSubconjunto(inicio+1, numeros, total, soma)
    
print(somaSubconjunto(0, [1,2,3,4], 4, 9))