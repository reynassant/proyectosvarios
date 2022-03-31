lista = [1, 3, 6 ,8 ,11]

#Este codigo falla si los numeros a eliminar estan seguidos ya que el .remove se mueve por indice y al borrar el elemento todos los elementos se mueven.

def resultado(lista):
    for dato in lista:
        if dato >= 10:
            lista.remove(dato)
    return lista

print(resultado(lista))