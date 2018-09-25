# init

import statistics

ram_constant = 999

def square(x):
	return (x ** 2)

class Array:

	def __init__(self,data):
		self.data = data
		
	def sum(self):
		return sum(self.data)
		
	def min(self):
		return min(self.data)
		
	def max(self):
		return max(self.data)
		
	def mean(self):
		return statistics.mean(self.data)
		
	def median(self):
		return statistics.median(self.data)