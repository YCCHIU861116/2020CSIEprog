class treenode:
	def __init__(self,value = 0,left = None,right = None):
		self.setter(value,left,right)

	def setter(self,value = {None}, left = {None}, right = {None}):
		if value != {None}: self.__value = value
		if left != {None}: self.__left = left
		if right != {None}: self.__right = right

	def getter(self):
		return self.__value, self.__left, self.__right

class binarysearchtree:
	def __init__(self):
		self.__root = None

	def getroot(self):
		return self.__root

	def setroot(self,node):
		self.__root = node

	def insert(self,value):
		def insertnode(current, value):
			if current == None:
				return treenode(value = value)
			current_value,current_left,current_right = current.getter()
			if value < current_value:
				current.setter(left = insertnode(current_left,value))
			else:
				current.setter(right = insertnode(current_right,value))
			return current
		self.setroot(insertnode(self.getroot(),value))

	def print_all_paths(self):
		#TODO
		def print_paths(current,path):
			if current == None:
				return
			current_value,current_left,current_right = current.getter()
			if current_left == None and current_right == None:
				print(*(path+[current_value]))
				return
			path.append(current_value)
			print_paths(current_left,path)
			print_paths(current_right,path)
			path.pop()
		print_paths(self.getroot(),[])

BST = binarysearchtree()
for v in input().split(' '):
	BST.insert(int(v))
BST.print_all_paths()