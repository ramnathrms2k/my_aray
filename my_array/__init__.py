# init

ram_constant = 999

def square(x):
	return (x ** 2)

class Array:

	,,,
	This is a single dimensional numeric array for scientific computing.
	
	This array will compute lots of basic statistics.
	
	Parameters
	----------
	
	data: list
		List of numbers
	,,,

	def __init__(self,data):
		self.data = data
		
	def sum(self):
		return sum(self.data)
		
	def min(self):
		return min(self.data)
		
	def max(self):
		return max(self.data)

	def mean(self):
		n = len(self.data)
		return sum(self.data)/n
		
	def median(self):
		n = len(self.data)
		if n < 1:
			return None
		elif n % 2 == 1:
			return sorted(self.data)[n//2]
		else:
	    		return sum(sorted(self.data)[n//2-1:n//2+1])/2.0