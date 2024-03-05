# https://www.geeksforgeeks.org/find-lca-in-binary-tree-using-rmq/

# Python3 program to find LCA of u and v by
# reducing the problem to RMQ
from math import log2, floor
from typing import List

class Node:
	
	def __init__(self, val: int):
		
		self.val, self.left, self.right = val, None, None

class BinaryTree:
	
	def __init__(self, root: Node):
		
		self.root = root
		self.val_max = self._get_max_val()
		self.euler = [0] * (2 * self.val_max - 1)
		self.level = [0] * (2 * self.val_max - 1)
		self.f_occur = [-1] * (self.val_max + 1)
		self.fill = 0
		self.segment_tree = []

	def _get_max_val(self):
		
		stack = [self.root]
		max_val = -1
		
		while stack:
			x = stack.pop()
			if x.val > max_val:
				max_val = x.val
			if x.left:
				stack.append(x.left)
			if x.right:
				stack.append(x.right)
				
		return max_val
	''' A recursive function to get the minimum value in a given range 
	of array indexes. The following are parameters for this function. 
	
	st --> Pointer to segment tree 
	index --> Index of current node in the segment tree. Initially 
			0 is passed as root is always at index 0 
	ss & se --> Starting and ending indexes of the segment represented 
				by current node, i.e., st[index] 
	qs & qe --> Starting and ending indexes of query range '''
	def rmq_util(self, index, ss, se, qs, qe) -> int:
		
		# If segment of this node is part of given range
		# then return the min of the segment
		if qs <= ss and qe >= se:
			return self.segment_tree[index]

		# If segment of this node is outside 
		# the given range
		elif se < qs or ss > qe:
			return -1

		# If part of this segment overlaps with
		# given range
		mid = (ss + se) // 2
		
		q1 = self.rmq_util(2 * index + 1, 
						ss, mid, qs, qe)
		q2 = self.rmq_util(2 * index + 2, mid + 1,
						se, qs, qe)
							
		if q1 == -1:
			return q2
		if q2 == -1:
			return q1
		return (q1 if self.level[q1] < 
					self.level[q2] else q2)
					
	# Return minimum of elements in range from
	# index qs (query start) to qe (query end). 
	# It mainly uses rmq_util()
	def rmq(self, n: int, qs: int, qe: int) -> int:
		
		if qs < 0 or qe > n - 1 or qs > qe:
			print('invalid input')
			return -1
			
		return self.rmq_util(0, 0, n - 1, qs, qe)
		
	# A recursive function that constructs Segment
	# Tree for array[ss..se]. si is index of 
	# current node in segment tree st 
	def construct_segment_tree_util(self, si, ss,
									se, arr):

		# If there is one element in array,
		# store it in current node of segment tree
		# and return
		if ss == se:
			self.segment_tree[si] = ss
		else:

			# If there are more than one elements,
			# then recur for left and right subtrees and
			# store the min of two values in this node
			mid = (ss + se) // 2
			index_left, index_right = si * 2 + 1, si * 2 + 2
			self.construct_segment_tree_util(
				index_left, ss, mid, arr)
			self.construct_segment_tree_util(
				index_right, mid+1, se, arr)
			
			if (arr[self.segment_tree[index_left]] < 
				arr[self.segment_tree[index_right]]):
				self.segment_tree[si] = self.segment_tree[index_left]
			else:
				self.segment_tree[si] = self.segment_tree[index_right]
	
	# Function to construct segment tree from given 
	# array. This function allocates memory for segment
	# tree and calls construct_segment_tree_util() 
	# to fill the allocated memory 
	def construct_segment_tree(self, arr: List, n: int):
		
		# Height of segment tree 
		x = floor(log2(n) + 1)
		
		# Maximum size of segment tree 
		max_size = 2 * (1 << x) - 1	 # 2*pow(2,x) -1
		
		self.segment_tree = [0] * max_size
		
		# Fill the allocated memory st 
		self.construct_segment_tree_util(
			0, 0, n - 1, arr)
	
	# Recursive version of the Euler tour of T 
	def euler_tour(self, node: Node, lev: int):
		
		# If the passed node exists
		if node is not None:
			self.euler[self.fill] = node.val
			self.level[self.fill] = lev
			self.fill += 1
			
			# If unvisited, mark first occurrence
			if self.f_occur[node.val] == -1:
				self.f_occur[node.val] = self.fill - 1

			# Tour left subtree if exists and remark
			# euler and level arrays for parent on
			# return
			if node.left is not None:
				self.euler_tour(node.left, lev + 1)
				self.euler[self.fill] = node.val
				self.level[self.fill] = lev
				self.fill += 1

			# Tour right subtree if exists and 
			# remark euler and level arrays for
			# parent on return
			if node.right is not None:
				self.euler_tour(node.right, lev + 1)
				self.euler[self.fill] = node.val
				self.level[self.fill] = lev
				self.fill += 1
	
	# Returns LCA of nodes n1, n2 (assuming they are 
	# present in the tree) 
	def find_lca(self, u: int, v: int):
		
		# Start euler tour with root node on level 0
		self.euler_tour(self.root, 0)
		
		# Construct segment tree on level array
		self.construct_segment_tree(self.level,
								2 * self.val_max - 1)
								
		# For rmq to work, u must be smaller than v
		if self.f_occur[u] > self.f_occur[v]:
			u, v = v, u
			
		# Start and end of query range
		qs = self.f_occur[u]
		qe = self.f_occur[v]
		
		# Query for index of lca in tour
		index = self.rmq(2 * self.val_max - 1, qs, qe)
		
		# Return lca node and its index in euler array
		return self.euler[index], index


# Predicado p
def p(x, y):
	return x % 2 == 0 and y % 2 == 0

def forall(x, y):
	r = True

	# Recorrido desde el LCA hasta el nodo u
	for i in range(index, -1, -1):
		if tree.euler[i] == u:
			break
		r = r and p(tree.euler[i], tree.euler[i - 1])

	# Recorrido desde el LCA hasta el nodo v
	for i in range(index, len(tree.euler)):
		if tree.euler[i] == v:
			break
		r = r and p(tree.euler[i], tree.euler[i + 1])
	
	return r

def exists(x, y):
	r = False

	# Recorrido desde el LCA hasta el nodo u
	for i in range(index, -1, -1):
		if tree.euler[i] == u:
			break
		r = r or p(tree.euler[i], tree.euler[i - 1])

	# Recorrido desde el LCA hasta el nodo v
	for i in range(index, len(tree.euler)):
		if tree.euler[i] == v:
			break
		r = r or p(tree.euler[i], tree.euler[i + 1])
	
	return r
	

# Driver code
if __name__ == "__main__":
	
	root = Node(1)
	root.left = Node(2)
	root.right = Node(3)
	root.left.left = Node(4)
	root.left.right = Node(5)
	root.right.left = Node(6)
	root.right.right = Node(7)
	root.left.right.left = Node(8)
	root.left.right.right = Node(9)

	tree = BinaryTree(root)
	u, v = 4, 9
	lca, index = tree.find_lca(u, v)
	
	print("forall({}, {}) = {}".format(u, v, forall(u, v)))
	print("exists({}, {}) = {}".format(u, v, exists(u, v)))
		
# This code is contributed by Rajat Srivastava