# Treap Implicito

import random

class Treap:
    def __init__(self, key, priority=None):
        self.key = key
        self.priority = priority or random.random()
        self.left = None
        self.right = None
        self.reverse = False
        self.size = 1
    
    @staticmethod
    def sizeOf(node):
        return 0 if node == None else node.size
    
    def recalc(self):
        self.size = 1 + self.sizeOf(self.left) + self.sizeOf(self.right)

    def split(self, key):
        Treap.push(self)

        currentIndex = self.sizeOf(self.left) + 1

        if currentIndex <= key:
            if self.right == None:
                return self, None
            else:
                left, right = self.right.split(key - currentIndex)
                self.right = left
                self.recalc()
                return self, right
        else:
            if self.left == None:
                return None, self
            else:
                left, right = self.left.split(key)
                self.left = right
                self.recalc()
                return left, self
    
    @staticmethod
    def push(node):
        # if node == None:
        #     return
        # if node.reverse:
        #     node.reverse = False
        #     node.left, node.right = node.right, node.left
        #     if node.left != None:
        #         node.left.reverse = not node.left.reverse
        #     if node.right != None:
        #         node.right.reverse = not node.right.reverse
        if node == None:
            return
        if not node.reverse:
            return
        
        node.reverse = False
        node.left, node.right = node.right, node.left

        if (node.left != None):
            node.left.reverse ^= True
        if (node.right != None):
            node.right.reverse ^= True
    
    @staticmethod
    def merge(left, right):
        Treap.push(left)
        Treap.push(right)

        if left == None:
            return right
        if right == None:
            return left

        if left.priority > right.priority:
            left.right = Treap.merge(left.right, right)
            left.recalc()
            return left
        else:
            right.left = Treap.merge(left, right.left)
            right.recalc()
            return right
    
    def insert(self, pos, key):
        left, right = self.split(pos)
        return self.merge(self.merge(left, Treap(key)), right)

    def reverse(self, l, r):
        left, middle = self.split(l)
        middle, right = middle.split(r - l)
        middle.reverse ^= True
        return self.merge(self.merge(left, middle), right)

    def print(self):
        if self.left != None:
            self.left.print()
        print(self.key, end=" ")
        if self.right != None:
            self.right.print()

# Considere un arreglo A[1..N], representando una permutación de los números de 1 a N.
# Se desea que ejecute N acciones de la forma multiswap(a, b). Esta acción consite en:
# (a) Intercambiar el valor en la posición a con el valor en la posición b.
# (b) Invocar multiswap(a+1,b+1)
# (c) El proceso termina cuando b se sale del rango del arreglo o a alcanza el primer
# valor de b utilizado

def multiswap(A, p):
    T = None
    for i in range(len(A)):
        if T == None:
            T = Treap(A[i])
        else:
            T = T.insert(i, A[i])
    
    # Esto no esta funcionando
    for a, b in p:
        left, middle = T.split(a - 1)

        print("-------------------")
        if left != None:
            print("left")
            print(Treap.print(left))
        middle, right = middle.split(b - a + 1)
        
        if middle != None:
            print("middle")
            print(Treap.print(middle))

        if right != None:
            print("right")
            print(Treap.print(right))
        print("-------------------")

        if middle != None:
            middle.reverse ^= True

        T = Treap.merge(left, Treap.merge(middle, right))

        print("*******************")
        T.print() 
        print()
        print("*******************")   

A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pairs = [(2, 5), (4, 7), (1, 9)]
multiswap(A, pairs)


                