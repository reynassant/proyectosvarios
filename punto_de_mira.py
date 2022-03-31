import matplotlib.pyplot as raton

x = [3, -2, -3, -1]
y = [3, 5, 3, 0]


def punto_de_mira():
    raton.plot(x[0], y[0], 'bo')
    raton.plot(x[1], y[1], 'bo')
    raton.plot(x[2], y[2], 'bo')
    raton.plot(x[3], y[3], 'bo')

    raton.ylabel('Y')
    raton.xlabel('X')
    raton.show()
    print("Hola punto de mira")

if __name__ == '__main__':
    punto_de_mira()