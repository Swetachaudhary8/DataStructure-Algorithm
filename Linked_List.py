class Node:
	def __init__(self, data):
		self.data = data
		self.next = None


class linked_list:
	def __init__(self):
		self.head = None

#New node at the begining 
	def push(self,new_data):
		new_node = Node(new_data)
		new_node.next = self.head
		self.head = new_node

# New Node insert after given node
	def insert(self, prev_node, new_data):
		if prev_node is None:
			print "node should be in linkedlist"
			return
		new_node = Node(new_data)
		new_node.next = prev_node.next
		prev_node.next = new_node


#New Node at the last
	def append(self,new_data):
		new_node = Node(new_data)
		if self.head is None:
			self.head = New_node
			return 

		last = self.head
		while(last.next):
			last = last.next

		last.next = new_node

	def printList(self):
		temp = self.head
		while(temp):
			print temp.data,
			temp = temp.next


#codeexecution
if __name__ == '__main__':
	llist = linked_list()

	llist.push(6)
	llist.push(7)
	llist.push(3)
	llist.push(5)
	llist.append(8)
	llist.insert(llist.head.next.next,2)

	llist.printList()
