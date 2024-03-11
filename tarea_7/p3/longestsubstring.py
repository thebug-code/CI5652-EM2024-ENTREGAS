# Bordes de un string

import sys


# Calcula el arreglo correspondiente a la funcion de prefijo de s
def longest_border(s):
    p = [0] * len(s)

    for i in range(1, len(s)):
        k = p[i - 1]
        while k > 0 and s[k] != s[i]:
            k = p[k - 1]
        if s[k] == s[i]:
            k += 1
        p[i] = k

    # Obtiene el string que es prefijo y sufijo de s
    longest_border = s[0 : p[len(s) - 1]]
    return longest_border


if __name__ == "__main__":
    s = sys.argv[1]
    print(longest_border(s))
