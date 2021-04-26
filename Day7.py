#Task N°7
import abc
import numpy as np
class Graph(abc.ABC):

    def __init__(self, num_vertices, directed = False):
        self.num_vertices = num_vertices
        self.directed = directed

    @abc.abstractmethod
    def add_edge(self, v1, v2, weight):
        pass

    @abc.abstractmethod
    def remove_edge(self, v1, v2, weight):
        pass

    @abc.abstractmethod    
    def get_adjacent_vertices(self, v):
        pass
        
    @abc.abstractmethod
    def is_adjacent(self, v1,v2):
        pass
        
    @abc.abstractmethod
    def get_indegree(self, v):
        pass
        
    @abc.abstractmethod
    def get_edge_weight(self, v1, v2):
        pass
        
    @abc.abstractmethod
    def show(self):
        pass
        

class AdjacencyMatrixGraph(Graph):

    def __init__(self, num_vertices, directed = False):
        super(AdjacencyMatrixGraph, self).__init__(num_vertices, directed)
        self.matrix = np.zeros( (num_vertices, num_vertices) )

    def add_edge(self,v1,v2, weight = 1):
        if v1 >= self.num_vertices or v2 >= self.num_vertices or v1 < 0 or v2 < 0:
            raise ValueError("Verices out of bounds")

        if weight == 0:
            raise ValueError("Edges cannot have a weight of 0")
        
        self.matrix[v1][v2] = weight

        if self.directed == False:
            self.matrix[v2][v1] = weight
    
    def remove_edge(self, v1,v2):
        if v1 >= self.num_vertices or v2 >= self.num_vertices or v1 < 0 or v2 < 0:
            raise ValueError("Verices out of bounds")

        self.matrix[v1][v2] = 0
        if self.directed == False:
            self.matrix[v2][v1] = 0

    def get_adjacent_vertices(self, v):
        if v < 0 or v >= self.num_vertices:
            raise ValueError("Cannot access the vertex")   

        adjacent_vertices = []
        for i in range(self.num_vertices):
            if self.matrix[v][i] > 0:
                adjacent_vertices.append(i)

        return adjacent_vertices

    def is_adjacent(self, v1, v2):
        if v1 >= self.num_vertices or v2 >= self.num_vertices or v1 < 0 or v2 < 0:
            raise ValueError("Verices out of bounds")
        return self.matrix[v1][v2] != 0

    def get_indegree(self, v):
        if v < 0 or v >= self.num_vertices:
            raise ValueError("Cannot access the vertex") 
        indegree = 0
        for i in range(self.num_vertices):
            if self.matrix[i][v] > 0:
                indegree = indegree + 1
        return indegree

    def get_edge_weight(self, v1,v2):
        return self.matrix[v1][v2]

    def show(self):
        for i in range(self.num_vertices):
            for v in self.get_adjacent_vertices(i):
                print(i, "-->", v)

    def __str__(self):
        retval = ''
        for i in self.matrix:
            for j in i:
                retval += str(int(j)) + '\t'
            retval += '\n'
        return retval

# INSTANCIATION
g = AdjacencyMatrixGraph(4, directed = True)
g.add_edge(0,1)
g.add_edge(0,3)
g.add_edge(1,3)
g.add_edge(3,2)
g.show()
g.remove_edge(1,3)
print("After removal")
print(g)

#Task N°8
class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

    def get_left_child(self):
        return self.left

    def set_left_child(self, left):
        self.left = left

    def get_right_child(self):
        return self.right

    def set_right_child(self, right):
        self.right = right

    def get_value(self):
        return self.data

    def set_value(self, value):
        self.data = value

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        
        print(self.data)
        
        if self.right:
            self.right.print_tree()


def insert(head, node):
    if head == None:
        return node

    if node.get_value() <= head.get_value():
        head.set_left_child(insert(head.get_left_child(), node))
    else:
        head.set_right_child(insert(head.get_right_child(), node))

    return head

class MyQueue:
 
    def __init__(self):
        self.items = []
 
    def is_empty(self):
        return len(self.items) == 0
 
    def enqueue(self, item): # add an element at the end, complexity = O(1)
        self.items.append(item)
 
    def dequeue(self): # removing an element from the beginning of a queue, complexity = O(1)
        return self.items.pop(0)
 
    def size(self):
        return len(self.items)
 
    def peek(self): # read the first element, complexity = O(1)  
        if self.is_empty():
            raise Exception("Empty queue")
        return self.items[0]

def breadth_first(node):

    if(node == None):
        raise Exception("No root found")

    path = []
    queue = MyQueue()
    queue.enqueue(node)

    while queue.size() > 0:
        current = queue.dequeue()
        path.append(current.data)
        
        if current.get_left_child() != None:
            queue.enqueue(current.get_left_child())
        if current.get_right_child() != None:
            queue.enqueue(current.get_right_child())
    return path 

def depth_first_order(node):
    path = []
    if node:
        path = path + depth_first_order(node.get_left_child())
        path.append(node.data)
        path = path + depth_first_order(node.get_right_child())
    return path 

# INSTANCIATION
"""
A = Node(10)
B = Node(5)
C = Node(25)
D = Node(12)
E = Node(33)
F = Node(18)

head = insert(None, A)
insert(head, B)
insert(head, C)
insert(head, D)
insert(head, E)
insert(head, F)

"""
A = Node(45)
B = Node(2)
C = Node(33)
D = Node(54)
E = Node(25)
F = Node(68)
G = Node(72)
H = Node(81)
I = Node(23)

head = insert(None, E)
insert(head, B)
insert(head, C)
insert(head, I)
insert(head, A)
insert(head, G)
insert(head, F)
insert(head, D)
insert(head, H)
insert(head, Node(100))

head.print_tree() # printed in order 

print(breadth_first(E))
print(depth_first_order(E))

#print(breadth_first(A))
#print(depth_first_order(A))

