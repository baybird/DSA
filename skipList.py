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

	def search(self, K):
		nodePtr = self.top
		print "***search***"
		print "from ", nodePtr.val

		while nodePtr.down != None:
			while nodePtr.next != None and K >= nodePtr.next.val:
				nodePtr = nodePtr.next
				print "move to ", nodePtr.val

				if nodePtr.val == K:
					print "found"
					return nodePtr

			nodePtr = nodePtr.down
			print "down to ", nodePtr.val


	# @staticmethod
	def __show(self, nodePtr):
		recent = 0

		while nodePtr != None:
			# print "recent:", recent, ",",
			if nodePtr.val != None and recent + 1 < nodePtr.val:
				self.insertSpace(nodePtr.val, recent)

			print nodePtr.val,"",

			if nodePtr.val != None:
				recent = nodePtr.val

			nodePtr = nodePtr.next
		print

	def show(self):
		level = 0
		nodePtr = self.top
		while nodePtr != None:
			print "L" + str(level) + ":",
			self.__show(nodePtr)

			nodePtr = nodePtr.down
			level += 1

	def insertSpace(self, val, recent):
		if recent == None :
			step = val
		else:
			step = val - recent

		for x in xrange(step-1):
			print "  ",
		# print "val:", val, ", blank:", step

# skip list end

# test
list = skipList()
for i in xrange(1,10):
	list.insertNode(i, i)
list.show();

# search 7
node = list.search(7)
if node:
	print "result:", node.val
else:
	print "not found"

# search not existed term
node = list.search(11)
if node:
	print "result:", node.val
else:
	print "not found"

# output
# None = infinity

# node 1 created with 2 levels
# node 2 created with 4 levels
# node 3 created with 4 levels
# node 4 created with 2 levels
# node 5 created with 3 levels
# node 6 created with 5 levels
# node 7 created with 2 levels
# node 8 created with 3 levels
# node 9 created with 4 levels
# L0: None                 6
# L1: None     2  3        6        9
# L2: None     2  3     5  6     8  9
# L3: None  1  2  3  4  5  6  7  8  9
# L4: None  1  2  3  4  5  6  7  8  9
# ***search***
# from  None
# move to  6
# down to  6
# down to  6
# down to  6
# found
# result: 7


