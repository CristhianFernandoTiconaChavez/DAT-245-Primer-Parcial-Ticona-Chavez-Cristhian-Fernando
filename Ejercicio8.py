def permutaciones(lista_de_nodos, vector_de_combinaciones, inicio, final, posicion, r, contador):
    if posicion == r:
        print(' '.join(map(str, vector_de_combinaciones)))
        contador[0] += 1
        return
    for i in range(inicio, final + 1):
        # Saltando los elementos ya usados
        if lista_de_nodos[i] not in vector_de_combinaciones[:posicion]:
            vector_de_combinaciones[posicion] = lista_de_nodos[i]
            permutaciones(lista_de_nodos, vector_de_combinaciones, 0, final, posicion + 1, r, contador)
            vector_de_combinaciones[posicion] = 0  # Limpiando la posición para la próxima permutación

lista_de_nodos = list(range(1, 9))  # 8 nodos
n = len(lista_de_nodos)
r = n  # Permutando todos los nodos
vector_de_combinaciones = [0] * r

contador = [0]

# Generando todas las permutaciones
permutaciones(lista_de_nodos, vector_de_combinaciones, 0, n - 1, 0, r, contador)

print(f"\nEl número total de caminos posibles es: {contador[0]}")
