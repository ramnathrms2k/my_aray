from array import array

# init

ram_constant = 999

def square(x):
	return (x ** 2)

class Array:

	'''
	This is a single dimensional numeric array for scientific computing.
	
	This array will compute lots of basic statistics.
	
	Parameters
	----------
	
	data: list
		List of numbers
	'''

	def __init__(self,data):
		# b - boolean (1 byte integer)
		# q - integer (4 bytes)
		# d - float (8 bytes)
		self.data = array('d',data)
		
	def sum(self):
		'''
		Sums all the values in the array
		
		Returns
		-------
		int or float
		'''
		return sum(self.data)
		
	def min(self):
		'''
		Minimum value from the array
				
		Returns
		-------
		int or float
		'''
		return min(self.data)
		
	def max(self):
		'''
		Maximum value from the array
				
		Returns
		-------
		int or float
		'''
		return max(self.data)

	def mean(self):
		'''
		Mean value of the array
				
		Returns
		-------
		int or float
		'''
		n = len(self.data)
		return sum(self.data)/n
		
	def median(self):
		'''
		Median value of the array
				
		Returns
		-------
		int or float
		'''

		n = len(self.data)
		if n < 1:
			return None
		elif n % 2 == 1:
			return sorted(self.data)[n//2]
		else:
	    		return sum(sorted(self.data)[n//2-1:n//2+1])/2.0