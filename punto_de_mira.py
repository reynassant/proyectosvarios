import matplotlib.pyplot as raton

lista_de_coordenadas = [
    [0, 0],
    [0.2, 0.31],
    [-0.4, 0.6],
    [-0.5, 1.1],
    [-0.9, 2],
    [-0.2, 3.3],
    [-0.7, 6.8],
    [-3, 7.1]
]


def maximo_abs(lista_de_coordenadas):
    maximo_total = 0

    for pareja_de_coordenadas in lista_de_coordenadas:
        maxim = abs(max(pareja_de_coordenadas))
        minim = abs(min(pareja_de_coordenadas))
        maximo_temporal = max(maxim, minim)
        if maximo_temporal > maximo_total:
            maximo_total = maximo_temporal

    return maximo_total


def calcula_hipotenusas(lista_de_coordenadas):
    lista_hipotenusa = []
    for coordenada in lista_de_coordenadas:
        hipotenusa = ((coordenada[0] ** 2 + coordenada[1]**2) ** (1/2))
        lista_hipotenusa.append(hipotenusa)
    return lista_hipotenusa


def dibuja_balas(lista_de_coordenadas):

    max_coord = maximo_abs(lista_de_coordenadas) + 1

    print(f"busca_máximo_coordenadas: [{max_coord}]")

    raton.xlim(-1 * max_coord, max_coord)
    raton.ylim(-1 * max_coord, max_coord)


    for pareja_de_coordenadas in lista_de_coordenadas:
        raton.plot(pareja_de_coordenadas[0], pareja_de_coordenadas[1], 'bo')
        raton.plot(0, 0, 'y+')
        raton.pause(0.50)
    raton.show()


# Este def recorre la lista entera

def iterar_lista(lista_de_coordenadas, lista_hipotenusa):

    contador_index = 0
    num_final = len(lista_de_coordenadas) - 1
    while(contador_index <= num_final):

        print(
            f'{lista_de_coordenadas[contador_index]} -- {lista_hipotenusa[contador_index]}')
        algo_misterioso(
            lista_de_coordenadas[contador_index], lista_hipotenusa[contador_index])
        contador_index += 1


def algo_misterioso(pareja_de_coordenadas, hipotenusa):

    return pareja_de_coordenadas


lista_hipotenusa = calcula_hipotenusas(lista_de_coordenadas)
iterar_lista(lista_de_coordenadas, lista_hipotenusa)

# print(lista_de_coordenadas)
# print(lista_hipotenusa)

dibuja_balas(lista_de_coordenadas)


# if __name__ == '__main__':
#     lista_de_coordenadas()
