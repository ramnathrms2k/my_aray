from array import array
from . import _utils

# init

ram_constant = 999

def square(x):
	return (x ** 2)

options_max_value = 20

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
		# Allow a user to pass only an array or a list to the constructor
		if isinstance(data, array):
			# TODO - check for cases where typecode is not 'b', 'q' or 'd'
			self.data = data
		elif isinstance(data, list):
			dtype = _utils.get_dtype_of_list(data)
			
			try:
				self.data = array(dtype, data)
			except TypeError:
				self.data = array('d',data)
		else:
			raise TypeError('Array constructor only accepts lists or arrays')
		# b - boolean (1 byte integer)
		# q - integer (4 bytes)
		# d - float (8 bytes)
		self.dtype = self.data.typecode


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
		n = len(self)
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

	def __repr__(self):
		final_str = ''
		half_max = options_max_value // 2
		if len(self) <= options_max_value:
			for val in self.data:
				final_str += f'{val:5}\n'
		else:
			for val in self.data[:half_max]:
				final_str += f'{val:5}\n'
			final_str += f'...\n'
			for val in self.data[-half_max:]:
				final_str += f'{val:5}\n'
		return final_str

	def __len__(self):
		return len(self.data)

	def sort(self, reverse=False):
		data = sorted(self.data, reverse=reverse)
		return Array(data)

	def __iter__(self):
		return iter(self.data)
