# init

ram_constant = 999

def square(x):
	return (x ** 2)

class Array:

	def __init__(self,data):
		self.data = data
		
	def sum(self):
		return sum(self.data)