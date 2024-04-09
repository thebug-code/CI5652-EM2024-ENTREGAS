# https://www.geeksforgeeks.org/introduction-and-approximate-solution-for-vertex-cover-problem/

# Programa que calcula el vertex cover de un grafo no dirigido
from collections import defaultdict

# Grafo como lista de adyacencia
class Graph:

	def __init__(self, vertices):
		self.V = vertices              # numero de vertices
		self.graph = defaultdict(list) # lista de adyacencia

	# Agrega una arista al grafo
	def addEdge(self, u, v):
		self.graph[u].append(v)

	# Imprime el vertex cover
	def printVertexCover(self):
		
		# Iniciliza todos los vertices como no visitados
		visited = [False] * (self.V)
		
		# Recorre todas las aristas
		for u in range(self.V):
			
			# Una arista solo se elige cuando ambos vertices no han sido visitados
			if not visited[u]:
				
				# Recorre todos los vertices adyacentes a u
				# y selecciona el primero que no ha sido visitado
				# (selecciona una arista (u, v) de las aristas restantes)
				for v in self.graph[u]:
					if not visited[v]:
						
						# Agrega los vertices u y v al conjunto de resultados
						# Se marcan como visitados para que todas las aristas que
						# los contienen sean ignoradas
						visited[v] = True
						visited[u] = True
						break

		# Imprime los vertices seleccionados (vertex cover)
		for j in range(self.V):
			if visited[j]:
				print(j, end = ' ')
				
		print()

if '__main__' == __name__:
	# Grafo de prueba
	g = Graph(5)
	# g.addEdge(0, 1)
	# g.addEdge(0, 2) 
	# g.addEdge(1, 3) 
	# g.addEdge(3, 4) 
	# g.addEdge(4, 5) 
	# g.addEdge(5, 6)

	g.addEdge(0, 2)
	g.addEdge(2, 4)
	g.addEdge(4, 1)
	g.addEdge(4, 3) 

	g.printVertexCover()
