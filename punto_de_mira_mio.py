import matplotlib.pyplot as raton
import random

lista_de_coordenadas = [
    [0, 0],
    [0.20, 0.31],
    [-0.4, 0.6],
    [-0.5, 1.1],
    [-0.9, 2],
    [-0.2, 3.3],
    [-0.7, 6.8],
    [-3, 7.1]
]


def maximo_abs(lista_de_coordenadas):
    maximo_total = 0
    for pareja_de_coordenas in lista_de_coordenadas:
        maximo = abs(max(pareja_de_coordenas))
        minimo = abs(min(pareja_de_coordenas))
        maximo_temporal = max(maximo, minimo)
        if maximo_temporal > maximo_total:
            maximo_total = maximo_temporal

    return maximo_total


def calcula_hipotenusas(lista_de_coordenadas):
    lista_de_hipotenusas = []
    for coordenada in lista_de_coordenadas:
        hipotenusa = ((coordenada[0] ** 2 + coordenada[1] ** 2) ** (1/2))
        lista_de_hipotenusas.append(hipotenusa)
    return lista_de_hipotenusas


def dibuja_balas(lista_de_coordenadas):
    maximo_de_coordenadas = maximo_abs(lista_de_coordenadas) + 1

    print(f'Busca máximo de coordenadas {maximo_de_coordenadas}')

    raton.xlim(-1 * maximo_de_coordenadas, maximo_de_coordenadas)
    raton.ylim(-1 * maximo_de_coordenadas, maximo_de_coordenadas)

    for pareja_de_coordenadas in lista_de_coordenadas:
        raton.plot(pareja_de_coordenadas[0], pareja_de_coordenadas[1], 'bo')
        raton.plot(0, 0, 'y+')
        raton.pause(0.50)
    raton.show


def iterar_lista(lista_de_coordenadas, lista_de_hipotenusas):
    lista_final = []
    i = 0
    numero_final = len(lista_de_coordenadas) - 1

    while(i <= numero_final):
        lista_final.append(
            aleatorio(lista_de_coordenadas[i], lista_de_hipotenusas[i]))
        i += 1
    return lista_final


def aleatorio(pareja_sin_aleatoriedad, hipotenusa):
    desviacion_maxima = hipotenusa
    x = pareja_sin_aleatoriedad[0]
    y = pareja_sin_aleatoriedad[1]

    aleatorio_de_x = random.uniform(-1, 1)
    aleatorio_de_y = random.uniform(-1, 1)

    nueva_x = x + (aleatorio_de_x * desviacion_maxima)
    nueva_y = y + (aleatorio_de_y * desviacion_maxima)

    nueva_pareja = [nueva_x, nueva_y]

    return nueva_pareja


if __name__ == '__main__':
    lista_de_hipotenusas = calcula_hipotenusas(lista_de_coordenadas)
    lista_final = iterar_lista(lista_de_coordenadas, lista_de_hipotenusas)

    dibuja_balas(lista_final)
