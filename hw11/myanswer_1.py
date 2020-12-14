class treenode:
	def __init__(self,value = 0,left = None,right = None):
		self.setter(value,left,right)
		self.__rootpath = []

	def setter(self,value = {None}, left = {None}, right = {None}):
		if value != {None}: self.__value = value
		if left != {None}: self.__left = left
		if right != {None}: self.__right = right

	def getter(self):
		return self.__value, self.__left, self.__right

	def setrootpath(self,path):
		self.__rootpath = path

	def getrootpath(self):
		return self.__rootpath

class binarysearchtree:
	def __init__(self):
		self.__root = None

	def getroot(self):
		return self.__root

	def setroot(self,node):
		self.__root = node

	def search(self,value):
		def searchnode(current,value):
			if current == None:
				return None
			current_value,current_left,current_right = current.getter()
			if value < current_value:
				return searchnode(current_left,value)
			elif value == current_value:
				return current
			else:
				return searchnode(current_right,value)
		return searchnode(self.getroot(),value)

	def insert(self,value):
		def insertnode(current, value, path):
			if current == None:
				newnode = treenode(value = value)
				newnode.setrootpath(path+[value])
				return newnode
			current_value,current_left,current_right = current.getter()
			path.append(current_value)
			if value < current_value:
				current.setter(left = insertnode(current_left,value, path))
			else:
				current.setter(right = insertnode(current_right,value, path))
			return current
		self.setroot(insertnode(self.getroot(),value,[]))

	def distance(self,value1,value2):
		path1 = self.search(value1).getrootpath()
		path2 = self.search(value2).getrootpath()
		len1 = len(path1)
		len2 = len(path2)
		l = 0
		while l < len1 and l < len2 and path1[l] == path2[l]:
			l += 1
		return len1 + len2 - 2*l

n = int(input())
nodes = []
for _ in range(n):
	nodes.append(tuple(map(int,input().split(' '))))
nodes = sorted(nodes,key = lambda x: (x[1],x[0]))

BST = binarysearchtree()
for i in range(n):
	BST.insert(nodes[i][0])

p = int(input())
for _ in range(p):
	query = list(map(int,input().split(' ')))
	print(BST.distance(*query))