# Problem		: Divisibility
# Description   : Determining whether one whole number is divisible by another or not.
# For example   : 11 is not divisible by [2,5,7]
# 			      9  is divisible by [2,5,7]
# Author        : Robert Tang
# Email         : bayareabird@gmail.com
# Created       : 6/16/2017

class Solution():

	def isDivisible(self, factors, n):
		for x in factors:
			remainder = n % x;

			if remainder == 0:
				return True;
			elif self.DFS(factors, remainder, [x]) == True:
				return True

		return False

	def DFS(self, factors, n, visited =[]):
		for x in factors:
			if x not in visited:
				visited.append(x)
				remainder = n % x

				if remainder == 0:
					return True

				self.DFS(factors, remainder, visited)

# test
s = Solution();

factors = [2,5,7]
n   	= 9
ret 	= s.isDivisible(factors, n)

if ret == True:
	print n, 'is divisible by', factors
else:
	print n, 'is NOT divisible by', factors
