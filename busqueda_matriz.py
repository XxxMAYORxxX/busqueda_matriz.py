# Definición de la matriz bidimensional 3x3
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


def buscar_valor(matriz, valor):
    """
    Busca un valor en una matriz bidimensional.

    :param matriz: Lista de listas (matriz) donde se realiza la búsqueda.
    :param valor: Valor a buscar en la matriz.
    :return: Tupla con la posición (fila, columna) del valor si se encuentra, None si no se encuentra.
    """
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                return (i, j)
    return None


def main():
    # Definir el valor a buscar
    valor_a_buscar = 5

    # Buscar el valor en la matriz
    resultado = buscar_valor(matriz, valor_a_buscar)

    # Mostrar resultados
    if resultado:
        print(f"El valor {valor_a_buscar} se encontró en la posición {resultado}.")
    else:
        print(f"El valor {valor_a_buscar} no se encontró en la matriz.")


if __name__ == "__main__":
    main()
