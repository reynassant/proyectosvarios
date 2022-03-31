numeros = [10, 6, 8, 100, 400, 2]
nariz = [66, 14, 99 ,87, 2]

def lista_menor_10(numeros):
    lista_nueva = []
    for numero in numeros:
        if numero <= 10:
            lista_nueva.append(numero)
    return lista_nueva

print(lista_menor_10(numeros))
