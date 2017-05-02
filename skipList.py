# File name     : skipList.py
# Author        : Robert.Tang
# Created       : 5/2/2017
# Last Modified :
# Description   : Searching nodes in O(log n) in avg.
# Python Version: 2.7

import os, random

class Node():
	def __init__(self, key = None, val = None):
		self.down = None
		self.up   = None

		self.next = None
		self.prev = None

		self.key = key
		self.val = val

	def display(self, newline = False):
		if newline:
			print self.key
		else:
			print self.key,


class skipList():
	top = Node()

	def insertNode(self, key, val):

		nodePtr = self.top

		# Find bottom node
		while nodePtr.down != None:
			nodePtr = nodePtr.down

		# Find last node
		while nodePtr.next != None:
			nodePtr = nodePtr.next

		# create new node
		node = Node(key, val)
		node.prev = nodePtr
		nodePtr.next = node


		self.linkNodes(node)

	def linkNodes(self, nodePtr):
		bottomNode = nodePtr

		level 		 = 1
		coinFlip 	 = 1 # 1 = head, 0 = tail

		while coinFlip == 1 :
			level += 1
			prevNode   = nodePtr.prev

			node 				= Node(nodePtr.key, nodePtr.val)
			node.down 	= nodePtr
			nodePtr.up 	= node
			nodePtr 		= nodePtr.up # move node up

			# link prev node
			if prevNode.up != None:
				prevNode = prevNode.up
				prevNode.next = node
				node.prev = prevNode
			else:
				while prevNode.prev != None and prevNode.up == None:
					prevNode = prevNode.prev

				if prevNode.prev == None:
					# at the leftest"
					newNode = Node(prevNode.key, prevNode.val)
					newNode.down = prevNode
					prevNode.up = newNode

					newNode.next = node
					node.prev = newNode
					self.top = newNode
				else:
					prevNode = prevNode.up
					prevNode.next = node
					node.prev = prevNode

		 	# flip coin
			coinFlip = random.randint(0, 1)

		print "node", nodePtr.val, "created with", str(level) ,"levels"
		# os.system("pause")


	# @staticmethod
	def __show(self, nodePtr):
		while nodePtr != None:
			print nodePtr.val,
			nodePtr = nodePtr.next
		print


	def show(self):
		level = 0
		while self.top != None:
			print "L" + str(level) + ":",
			self.__show(self.top)

			self.top = self.top.down
			level += 1


# skip list end

# test
list = skipList()
for i in range(3):
	list.insertNode(i, i)

list.show();

# output
# None = infinity
# node 0 created with 3 levels
# node 1 created with 8 levels
# node 2 created with 4 levels
# L0: None 	 1
# L1: None 	 1
# L2: None 	 1
# L3: None 	 1
# L4: None 	 1 2
# L5: None 0 1 2
# L6: None 0 1 2
# L7: None 0 1 2




