# Algoritmo de Graham para Capas de Convexidad

Este programa calcula las capas de convexidad de un conjunto de puntos en el plano cartesiano utilizando el algoritmo de Graham.

## Descripción

El programa recibe un conjunto de puntos y calcula el polígono convexo más pequeño que los contiene, conocido como la capa convexa. Luego, elimina los puntos que forman parte de esta capa y repite el proceso para encontrar las capas internas hasta que no queden puntos.

## Uso

Para ejecutar el programa, utiliza el siguiente comando:

```bash
python grahamscan.py <puntos>
```

Donde `<puntos>` es una secuencia de números que representan las coordenadas \(x, y\) de los puntos. Por ejemplo en:

```bash
python grahamscan.py 0 3 1 1 2 2 4 4 0 0 1 2 3 1 3 3
```

Los puntos a considerar son: \(0, 3\), \(1, 1\), \(2, 2\), \(4, 4\), \(0, 0\), \(1, 2\), \(3, 1\) y \(3, 3\).



