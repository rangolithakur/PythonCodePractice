class Node(object):
	def __init__(self, data=None, next_node=None):
		self.data=data
		self.next_node = next_node
	def get_data(self):
		return self.data
	def get_next(self):
		return self.next_node
	def set_next(self, new_next):
		self.next_node=new_next

class LinkedList(object):
	def __init__(self, head=None):
		self.head
	def insert(sel, data):
		new_node = Node(data)
		new_node.set_next(self.head)
	def size(self):
		current=self.head
		count=0
		while current:
			count+=1
			current=current.get_next()
		return count
	def search(self, data):
		current=self.head
		found=False
		while current ad found in False:
