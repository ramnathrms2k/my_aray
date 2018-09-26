from array import array
from . import _utils
import collections
from collections import Counter

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
		#TODO - if dtype of array is 'b', then output True or False insteaf of 0 or 1
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

	def __getitem__(self, key):
		if isinstance(key, int):
			return self.data[key]
		elif isinstance(key, slice):
			return Array(self.data[key])
		elif isinstance(key, list):
			raise NotImplementedError('Not done yet. Will do soon!!')
		else:
			raise TypeError('Key must be an int, slice or a list')

	def __setitem__(self, key, value):
		if isinstance(key, int):
			#TODO change data type of array if given float va;ue
			self.data[key] = value

		#TODO can you set items with a slice or list

	#def __add__(self, value):
		#return an arry that has 'value' added to each element
	#	data = [val + value for val in self]
	#	return Array(data)

	def __add__(self, value):
		#return an arry that has 'value' added to each element
		if isinstance(value, (bool, int, float)):
			data = [val + value for val in self]
			return Array(data)
		elif isinstance(value, Array):
			if len(self) != len(value):
				raise ValueError(f'Arrays must be of same length {len(self)} != {len(value)}')
			data = [val1 + val2 for val1, val2 in zip(self, value)]
			return Array(data)
		else:
			raise TypeError('Addition can occur only with bool, int, float or of arrays containing bool, int or float')

	#TODO implement other opertators - subtration, multiplication, division, floor division, exponentiation and modulus - -, *, /, //, **, %

	def __sub__(self, value):
		#return an arry that has 'value' subtracted to each element
		data = [val - value for val in self]
		return Array(data)

	def __mul__(self, value):
		#return an arry that has 'value' multipled to each element
		data = [val * value for val in self]
		return Array(data)

	def __truediv__(self, value):
		#return an arry that has 'value' divided to each element
		data = [val / value for val in self]
		return Array(data)

	def __floordiv__(self, value):
		#return an arry that has 'value' floor divided to each element
		data = [val // value for val in self]
		return Array(data)

	def __pow__(self, value):
		#return an arry that has 'value' exponentiated to each element
		data = [val ** value for val in self]
		return Array(data)

	def __mod__(self, value):
		#return an arry that has 'value' modulus operated to each element
		data = [val % value for val in self]
		return Array(data)

	#TODO - implement the right side operators like radd, etc.,.

	def __gt__(self, value):
		#return an boolean arry that compares if a value is greater than
		if isinstance(value, (bool, int, float)):
			data = [val > value for val in self]
			return Array(data)
		elif isinstance(value, Array):
			if len(self) != len(value):
				raise ValueError(f'Arrays must be of same length {len(self)} != {len(value)}')
			data = [val1 > val2 for val1, val2 in zip(self, value)]
			return Array(data)
		else:
			raise TypeError('Comparison can occur only with bool, int, float or of arrays containing bool, int or float')

	#TODO - implement other comparison operators

	# Use collections module to find mode

	def mode(self):
		c = Counter(self.data)
		mode = c.most_common(1)
		return mode