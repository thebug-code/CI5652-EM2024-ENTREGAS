# https://www.geeksforgeeks.org/freivalds-algorithm/

# Freivald’s Algorithm
import random 
N = 2

def freivald(A, B, C):
	"""
	Dada tres matrices cuadradas A, B y C calcula A*(B*r) y C*r donde r es un vector aleatorio de 0s y 1s
	"""
	
	# Genera un vector aleatorio
	r = [0] * N
	for i in range(0, N) :
		r[i] = (int)(random.randrange(509090009) % 2)

	# Calcula B*r
	br = [0] * N
	for i in range(0, N) :
		for j in range(0, N) :
			br[i] = br[i] + B[i][j] * r[j]

	# Calcula C*r
	cr = [0] * N
	for i in range(0, N) :
		for j in range(0, N) :
			cr[i] = cr[i] + C[i][j] * r[j]

	# Calcula A*(B*r)
	axbr = [0] * N
	for i in range(0, N) :
		for j in range(0, N) :
			axbr[i] = axbr[i] + A[i][j] * br[j]

	# Verifica si A*(B*r) - C*r = 0
	# for i in range(0, N) :
	# 	if (axbr[i] - cr[i] != 0) :
	# 		return False
			
	return axbr, cr


def isProduct(A, B, C, k, tol=0.0001):
	"""
	Dada tres matrices cuadradas A, B y C verifica si A*B = C usando el algoritmo de Freivald k veces
	con una tolerancia de error tol
	"""

	for _ in range(k):
		axbr, cr = freivald(A, B, C)
		if any(abs(axbr[i] - cr[i]) > tol for i in range(N)):
			return False
	return True

	# for i in range(0, k) :
	# 	if (freivald(A, B, C) == False) :
	# 		return False
	# return True
		

	
		
if __name__ == "__main__":
	# Matriz A (posible inversa de B)
	# A = [ [ 4, 3, 3 ], [ -2, -1, -2 ], [-1, -1, -3 ] ]
	# # Matriz B
	# B = [ [ 1, 0, 3 ], [ 0, 1, -2 ], [ 1, 1, 2 ] ]

	A = [ [1, 0, 0 ], [ -4, 1, 0 ], [ 1, -1, 1] ]
	B = [ [1, 0, 0 ], [ 4, 1, 0 ], [ 3, 1, 1] ]

	# Matriz C (matriz identidad)
	N = len(A)
	C = [ [0] * N for i in range(N) ]
	for i in range(0, N) :
		C[i][i] = 1
	
	# Numero de veces que se ejecutara el algoritmo de Freivald
	k = 10

	# Verifica si A*B = C
	if isProduct(A, B, C, k):
		#print("No lo se Rick, tal vez A*B = C")
		print("A*B = C")
	else:
		print("A*B != C")
