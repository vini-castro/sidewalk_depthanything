import numpy as np
def pixel_mean(lista):
    media = 0
    for i in lista:
        if not np.isinf(i):
            media = media + i
    return media / len(lista)


def pixel_sum(lista):
    media = pixel_mean(lista)
    result = 0
    for i in lista:
        if np.isinf(i):
            result = result + media
        else:
            result = result + i
    return result
