import random

def findTenLargest(array):
    maiores = []
    array_copia = array.copy()

    for _ in range(10):
        i_max = 0
        maior = array_copia[0]
        for i, num in enumerate(array_copia):
            if num > maior:
                maior = num
                i_max = i
        maiores.append(maior)
        array_copia.pop(i_max)

    return maiores


array = [random.randint(0,100) for _ in range(25)]
print(array)
print(findTenLargest(array))