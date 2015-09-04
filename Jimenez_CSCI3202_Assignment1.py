import Queue
import random

class AIQueue:
	aiqueue = Queue.Queue()
	def put(self, a):
		if isinstance(a ,(int)):
			self.aiqueue.put(a)
		else:
			print "This queue only accepts integer values."
	def get(self):
		print self.aiqueue.get()


class Graph:
	table = {}

	def addVertex(self, value):
		if value not in self.table:
			self.table[value] = []
		else:
			print "Vertex already exists."
			print self.table

	def addEdge(self, value1, value2):
		if value1 in self.table:
			if value2 in self.table:
				if value1 in self.table[value2] and value2 in self.table[value1]:
					print "Edge already exists"
				else:
					self.table[value1].append(value2)
					self.table[value2].append(value1)
			if value2 not in self.table:
				print "One or more vertices not found."
		if value1 not in self.table:
			print "One or more vertices not found."

	def findVertex(self, value):
		if value in self.table:
			print self.table[value]
		if value not in self.table:
			print "Vertex not found."



class Stack:
	stack = []

	def push(self, integer):
		self.stack.append(integer)
	def pop(self):
		print self.stack.pop()
	def checkSize(self):
		len(self.stack)



class Node:
	right = None
	left = None
	def __init__(self, key, left, right, parent):
		self.key = key
		self.left = left
		self.right = right
		self.parent = parent

class BTree:
	root = None
	def __init__(self, key):
		self.root =  Node(key, None, None, None)

	def add(self, value, parentValue):
		def recurseAdd(self, value, parentValue, startNode):
			if startNode is None:
				return False
			if startNode.key is parentValue:
				if startNode.left is None:
					startNode.left = Node(value, None, None, startNode.left)
					return True
				elif startNode.right is None:
					startNode.right = Node(value, None, None, startNode.right)
					return True
				else:
					print "Parent has two children, node not added"
					return False
			elif recurseAdd(self, value, parentValue, startNode.left):
				return True
			elif recurseAdd(self, value, parentValue, startNode.right):
				return True
			else:
				"Parent not found"
				return False
		recurseAdd(self, value, parentValue, self.root)
	def delete(self, value):
		if (self.root.key is value):
			if (self.root.left is None) and (self.root.right is None):
				self.root = None
			else:
				print "Node not deleted, has children"
		else:
			print "Node not found."
	def printTree(self):
		def recursePrintTree(self, node):
			if node is None:
				print "Node is None"
				return
			else:
				print node.key
			print "Left Node"
			recursePrintTree(self, node.left)
			print "Right Node"
			recursePrintTree(self, node.right)
		recursePrintTree(self, self.root)



def testGraph():
	print "Initialize Graph"
	myGinneaPig = Graph()
	print"Add vertex %d to graph" % (0)
	myGinneaPig.addVertex(0)
	print"Add vertex %d to graph" % (1)
	myGinneaPig.addVertex(1)
	print"Add vertex %d to graph" % (2)
	myGinneaPig.addVertex(2)
	print"Add vertex %d to graph" % (3)
	myGinneaPig.addVertex(3)
	print"Add vertex %d to graph" % (4)
	myGinneaPig.addVertex(4)
	print"Add vertex %d to graph" % (5)
	myGinneaPig.addVertex(5)
	print"Add vertex %d to graph" % (6)
	myGinneaPig.addVertex(6)
	print"Add vertex %d to graph" % (7)
	myGinneaPig.addVertex(7)
	print"Add vertex %d to graph" % (8)
	myGinneaPig.addVertex(8)
	print"Add vertex %d to graph" % (9)
	myGinneaPig.addVertex(9)
	print"Add vertex %d to graph" % (10)
	myGinneaPig.addVertex(10)
	print"Try to add vertex %d to graph again" % (4)
	myGinneaPig.addVertex(4)

	print "Add edge from %d to %d" % (0,1)
	myGinneaPig.addEdge(0,1)
	print "Add edge from %d to %d" % (0,3)
	myGinneaPig.addEdge(0,3)
	print "Add edge from %d to %d" % (0,5)
	myGinneaPig.addEdge(0,5)
	print "Add edge from %d to %d" % (0,7)
	myGinneaPig.addEdge(0,7)
	print "Add edge from %d to %d" % (0,9)
	myGinneaPig.addEdge(0,9)
	print "Add edge from %d to %d" % (1,2)
	myGinneaPig.addEdge(1,2)
	print "Add edge from %d to %d" % (1,4)
	myGinneaPig.addEdge(1,4)
	print "Add edge from %d to %d" % (1,8)
	myGinneaPig.addEdge(1,8)
	print "Add edge from %d to %d" % (2,4)
	myGinneaPig.addEdge(2,4)
	print "Add edge from %d to %d" % (2,6)
	myGinneaPig.addEdge(2,6)
	print "Add edge from %d to %d" % (2,10)
	myGinneaPig.addEdge(2,10)
	print "Add edge from %d to %d" % (5,10)
	myGinneaPig.addEdge(5,10)
	print "Add edge from %d to %d" % (7,4)
	myGinneaPig.addEdge(7,4)
	print "Add edge from %d to %d" % (7,1)
	myGinneaPig.addEdge(7,1)
	print "Add edge from %d to %d" % (8,5)
	myGinneaPig.addEdge(8,5)
	print "Add edge from %d to %d" % (8,3)
	myGinneaPig.addEdge(8,3)
	print "Add edge from %d to %d" % (10,1)
	myGinneaPig.addEdge(10,1)
	print "Add edge from %d to %d" % (10,3)
	myGinneaPig.addEdge(10,3)
	print "Add edge from %d to %d" % (10,7)
	myGinneaPig.addEdge(10,7)
	print "Add edge from %d to %d" % (10,9)
	myGinneaPig.addEdge(10,9)
	print "Try to add edge from %d to %d again" % (0,1)
	myGinneaPig.addEdge(0,1)
	print "Try adding false edge from %d to %d" % (0,15)
	myGinneaPig.addEdge(0,15)
	print "Try adding false edge from %d to %d" % (12,15)
	myGinneaPig.addEdge(12,15)

	print "Find %d in graph" % (0)
	myGinneaPig.findVertex(0)
	print "Find %d in graph" % (1)
	myGinneaPig.findVertex(1)
	print "Find %d in graph" % (2)
	myGinneaPig.findVertex(2)
	print "Find %d in graph" % (3)
	myGinneaPig.findVertex(3)
	print "Find %d in graph" % (4)
	myGinneaPig.findVertex(4)
	print "Find %d in graph" % (100)
	myGinneaPig.findVertex(100)
	

def testStack():
	print "Initialize stack"
	myStackPig = Stack()
	for x in range(10):
		print "Add %d to stack" % (x+10)
		myStackPig.push(x+10)
	for x in range(10):
		print "Popping value from stack"
		myStackPig.pop()

def testQueue():
	"Initialize Queue"
	myQueuePig = AIQueue()
	for x in range(10):
		print "Add %d to Queue" % (x+10)
		myQueuePig.put(x+10)
	print "Try to add a non-integer type"
	myQueuePig.put("STRING")
	for x in range(10):
		print "Removing integer from the queue"
		myQueuePig.get()

def testBTree():
	print "Initialize BTree with 1"
	myBTreepig = BTree(1)
	print "Add 2 to node with value 1"
	myBTreepig.add(2, 1)
	print "Add 3 to node with value 1"
	myBTreepig.add(3,1)
	print "Add 4 to node with value 2"
	myBTreepig.add(4, 2)
	print "Add 5 to node with value 2"
	myBTreepig.add(5, 2)
	print "Add 6 to node with value 3"
	myBTreepig.add(6, 3)
	print "Add 7 to node with value 3"
	myBTreepig.add(7, 3)
	print "Add 8 to node with value 4"
	myBTreepig.add(8, 4)
	print "Add 9 to node with value 4"
	myBTreepig.add(9, 4)
	print "Add 10 to node with value 5"
	myBTreepig.add(10, 5)

	print "Delete 10 from tree"
	myBTreepig.delete(10)
	print "Delete 5 from tree"
	myBTreepig.delete(5)

	print "Printing tree"
	myBTreepig.printTree()


testBTree()
#testQueue()
#testStack()
#testGraph()