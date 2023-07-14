
class Node():
	def __init__(self, data=None):
		self.data = data
		self.next = None

def detect_cycle(head):
	fast = head
	slow = head
	cycleDetected = 0
	while ((fast.next is not None) & (slow.next is not None)):
		fast = fast.next.next
		slow = slow.next
		print('Slow, fast data : ', fast.data, slow.data)
		if (fast == slow):
			cycleDetected = 1
			break
	if (cycleDetected == 1):
		print()
		print('Cycle detected in linked list')
		print()
	else:
		print()
		print('Cycle not detected in linked list')
		print()

if __name__ == '__main__':
	node = Node(1)
	node.next = Node(2)
	node.next.next = Node(3)
	node.next.next.next = Node(4)
	node.next.next.next.next = Node(5)
	node.next.next.next.next.next = Node(6)
	node.next.next.next.next.next.next = Node(7)

	#node.next.next.next.next.next.next.next = node.next.next
	

	detect_cycle(node)
