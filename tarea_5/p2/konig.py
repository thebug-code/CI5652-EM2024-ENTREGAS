import networkx as nx


def is_prime(n):
    """ "pre-condition: n is a nonnegative integer
    post-condition: return True if n is prime and False otherwise."""
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2  # return False
    k = 3
    while k * k <= n:
        if n % k == 0:
            return False
        k += 2
    return True


def count_num_to_delete(C: set) -> int:
    """
    Calcula la cantidad minima de numeros que se deben eliminar del conjunto C para que no haya dos numeros en el conjunto
    que sumen un numero primo.
    """

    # Separa el conjunto C en dos conjuntos disjuntos
    # C1 contiene los numeros pares
    # C2 contiene los numeros impares
    C1 = set()
    C2 = set()

    for c in C:
        if c % 2 == 0:
            C1.add(c)
        else:
            C2.add(c)

    # Crea un digrafo vacio
    G = nx.DiGraph()

    # Añade una arista entre cada par de numeros en C1 y C2 si la suma de los numeros es un numero primo
    for c1 in C1:
        for c2 in C2:
            if is_prime(c1 + c2):
                G.add_edge(c1, c2)

    # Calcula el emparejamiento maximo usando el algoritmo de Hopcroft-Karp
    matching = nx.bipartite.maximum_matching(G)

    # Calcula la cantidad de aristas en el emparejamiento maximo
    num_edges = len(matching) // 2

    return num_edges


C = {2, 4, 1, 3, 8, 12, 13}
print(count_num_to_delete(C))

# La division del conjunto C en C1 y C2 toma tiempo O(n)
# La creacion de las conexiones entre los nodos de C1 y C2 toma tiempo O(n^2),
# asumiendo que la funcion is_prime toma tiempo O(1)
# El calculo del emparejamiento maximo usando el algoritmo de Hopcroft-Karp toma
# tiempo O(E * sqrt(V)), donde E es el numero de aristas y V es el numero de vertices
# E = O(n^2) ya que hay n^2 posibles conexiones entre los nodos de C1 y C2 (no se si es correcto)
# V = O(n) ya que hay n nodos en total
# Por lo tanto, el tiempo total de ejecucion es O(n^2 * sqrt(n))
