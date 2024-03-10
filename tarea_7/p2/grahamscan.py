# Convex Hull usando el algoritmo de Graham Scan

from functools import cmp_to_key
import sys

# Clase para almacenar las coordenadas x y y de los puntos
class Point:
	def __init__(self, x = None, y = None):
		self.x = x
		self.y = y

# Punto de referencia para ordenar los puntos con respecto al primer punto
p0 = Point(0, 0)

# Elimina de la lista de puntos el punto con coordenadas (x, y)
def remove_point(points, x, y):
	for i in range(len(points)):
		if points[i].x == x and points[i].y == y:
			points.pop(i)
			break

# Retorna la distancia al cuadrado entre dos puntos
def distSq(p1, p2):
	return ((p1.x - p2.x) * (p1.x - p2.x) +
			(p1.y - p2.y) * (p1.y - p2.y))


# Calcula la orientación de tres puntos
# Retorna 0 si son colineales, 1 si es en sentido horario y 2 si es en sentido antihorario
def orientation(p, q, r):
	val = ((q.y - p.y) * (r.x - q.x) -
		(q.x - p.x) * (r.y - q.y))
	if val == 0:
		return 0
	elif val > 0:
		return 1
	else:
		return 2

# Función para comparar dos puntos con respecto al primer punto
def compare(p1, p2):

	# Calcula la orientación de los tres puntos
	o = orientation(p0, p1, p2)
	if o == 0:
		if distSq(p0, p2) >= distSq(p0, p1):
			return -1
		else:
			return 1
	else:
		if o == 2:
			return -1
		else:
			return 1

# Imprime el convex hull de un conjunto de n puntos
def convexHull(points, n, layer_count=0):

	# Busca el punto con la coordenada y más pequeña
	ymin = points[0].y
	min = 0
	for i in range(1, n):
		y = points[i].y

		# Pick the bottom-most or choose the left
		# most point in case of tie
		if ((y < ymin) or
			(ymin == y and points[i].x < points[min].x)):
			ymin = points[i].y
			min = i

	# Place the bottom-most point at first position
	points[0], points[min] = points[min], points[0]

	# Ordena los n - 1 puntos por su ángulo polar con respecto al primer punto
	p0 = points[0]
	points = sorted(points, key=cmp_to_key(compare))

	# Si dos o más puntos tienen el mismo ángulo con respecto a p0,
	# se eliminan todos menos el que está más lejos de p0
	m = 1 # Tamaño del arreglo modificado
	for i in range(1, n):
	
		# Remueve i mientras el ángulo de i y i+1 es el mismo con respecto a p0
		while ((i < n - 1) and
		(orientation(p0, points[i], points[i + 1]) == 0)):
			i += 1

		points[m] = points[i]
		m += 1 # Actualiza el tamaño del arreglo modificado
		
	# Si el tamaño del arreglo modificado es menor a 3, no es posible calcular el convex hull
	if m < 3:
		return

	# Crea una pila vacía y agrega los primeros tres puntos
	S = []
	S.append(points[0])
	S.append(points[1])
	S.append(points[2])

	# Procesa los n-3 puntos restantes
	for i in range(3, m):
	
		# Mientras el ángulo formado por el penúltimo, el último y el punto i
		# sea en sentido antihorario se remueve el top
		while ((len(S) > 1) and
		(orientation(S[-2], S[-1], points[i]) != 2)):
			S.pop()
		S.append(points[i])

	# Imprime el contenido de la pila
	print("Capa {layer_count}:".format(layer_count=layer_count))
	while S:
		p = S[-1]
		print("({px}, {py})".format(px=p.x, py=p.y))
		remove_point(points, p.x, p.y)
		S.pop()
	
	# Aumenta el contador de capas
	layer_count += 1
	convexHull(points, len(points), layer_count)

if __name__ == "__main__":
	# Verifica que el número de argumentos sea el correcto
	if ((len(sys.argv) - 1) % 2 != 0):
		print("El número de argumentos debe ser par")
		sys.exit(1)

	# Extrae los puntos de los argumentos
	points = []
	for i in range(1, len(sys.argv), 2):
		points.append(Point(int(sys.argv[i]), int(sys.argv[i+1])))
	n = len(points)
	convexHull(points, n)
