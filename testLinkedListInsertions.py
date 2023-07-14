import numpy as np

class Node():
	def __init__(self, data=None, next=None):
		self.data = data
		self.next = next

class LinkedList():
	def __init__(self):
		self.data = None
		self.next = None

	def insert_at_beginning(self, data):
		node = Node(data, self.next)
		self.next = node

	def print(self):
		if (self.next is not None):
			itr = self.next
			llDataStr = str(itr.data) + '-->'

			while (itr.next is not None):
				itr = itr.next
				llDataStr = llDataStr + str(itr.data) + '-->'

			print('Linked list data :', llDataStr)

		else:
			print('Linked list is empty')

if __name__ == '__main__':
	ll = LinkedList()
	ll.print()
	ll.insert_at_beginning(1)
	ll.print()
	ll.insert_at_beginning(2)
	ll.print()
	ll.insert_at_beginning(3)
	ll.print()
	ll.insert_at_beginning(4)
	ll.print()
