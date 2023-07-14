import numpy as np

class Node():
	def __init__(self, data=None, next=None):
		self.data = data
		self.next = next

class LinkedList():
	def __init__(self):
		self.data = None
		self.next = None

	def insert_at_beginning(self, value):
		node = Node(value, self.next)
		self.next = node
		return node

	def insert_at_end(self, value):
		if (self.next is not None):
			nodeObj = self.next
				
			while (nodeObj.next is not None):
				nodeObj = nodeObj.next

			nodeObj.next = Node(value, None)
		else:
			nodeObj = Node(value, self.next)
			self.next = nodeObj
		return nodeObj

	def print(self):
		if (self.next is not None):
			itr = self.next
			llDataString = str(itr.data) + '-->' 
		
			while (itr.next is not None):
				itr = itr.next
				llDataString = llDataString + str(itr.data) + '-->'
			print('Linked list data : ', llDataString)

		else:
			print('Linked list is empty')


if __name__ == '__main__':
	ll = LinkedList()
	ll.print()
	nd = ll.insert_at_beginning(1)
	ll.print()
	nd = ll.insert_at_beginning(2)
	ll.print()
	nd = ll.insert_at_beginning(3)
	ll.print()
	ndo = ll.insert_at_end(0)
	ll.print()
	ndo = ll.insert_at_end(-1)
	ll.print()
	ndo = ll.insert_at_end(-2)
	ll.print()
	ndo = ll.insert_at_beginning(4)
	ll.print()
	print()
