# Problem       : Add two numbers
# Description   : You are given two non-empty linked lists representing two non-negative
#                 integers. The digits are stored in reverse order and each of their nodes
#                 contain a single digit. Add the two numbers and return it as a linked list.
#                 You may assume the two numbers do not contain any leading zero, except
#                 the number 0 itself.
# Input         : (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output        : 7 -> 0 -> 8
# Python Version: 2.7
# Author        : Robert Tang
# Created       : 4/6/2017

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    # Time complexity: N
    # Hope can make it more concise
    def addTwoNumbers(self, l1, l2):
        residue = []
        node = ListNode(0)
        root = node

        while l1 or l2:
          lnum = l1.val if l1 else 0
          rnum = l2.val if l2 else 0
          sum = lnum + rnum if len(residue) < 1 else lnum + rnum + residue.pop()

          if sum < 10:
            digit = sum
          else:
            digit = sum%10
            residue.append(1) # Because of the sum of two maximum single digits is 18

          node.next = ListNode(digit)
          node = node.next

          if l1:
            l1 = l1.next

          if l2:
            l2 = l2.next

        if len(residue):
          node.next = ListNode(residue.pop())
          node = node.next

        return root.next

# Test case 1:
# Input : (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8

l1 = ListNode(2);
l1.next = ListNode(4);
l1.next.next = ListNode(3);

l2 = ListNode(5);
l2.next = ListNode(6);
l2.next.next = ListNode(4);

s = Solution();
r = s.addTwoNumbers(l1, l2)
print r.val, r.next.val, r.next.next.val


# Test case 2:
# Input : (2 -> 4 -> 3) + (5 -> 6)
# Output: 7 -> 0 -> 4
l1 = ListNode(2);
l1.next = ListNode(4);
l1.next.next = ListNode(3);

l2 = ListNode(5);
l2.next = ListNode(6);

r = s.addTwoNumbers(l1, l2)
print r.val, r.next.val, r.next.next.val

# Test case 3:
# Input : (2 -> 4) + (5 -> 6)
# Output: 7 -> 0 -> 1
l1 = ListNode(2);
l1.next = ListNode(4);

l2 = ListNode(5);
l2.next = ListNode(6);

r = s.addTwoNumbers(l1, l2)
print r.val, r.next.val, r.next.next.val
