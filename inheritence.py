#Inheritence example
class Printer:
	"""
	=== Attributes ===
	@type brand: str
		the brand of the Printer
	@type inks
		the ink amount of the printer
	"""
	def __init__(self, brand, ink_amount):
		"""
		....
		"""
		self.brand = brand
		self.inks = ink_amount

	def print_thing(self, msg):
		raise NotImplementedError()

	def test(self):
		print('haha')


class Inkjet(Printer):
	"""
	"""
	def __init__(self, brand, ink_amount, fax_number):
		Printer.__init__(self, brand, ink_amount)
		self.fax = fax_number

	def print_thing(self, msg):
		print(msg)
		self.inks -= 1

	def fax(self, msg):
		print('msg has been faxed')


class Laser(Printer):
	def __init__(self, brand, ink_amount):
		Printer.__init__(self, brand, ink_amount)

	def print_thing(self, msg):
		print(msg)
		self.inks -= 0.1

if __name__ == '__main__':
	P1 = Inkjet('HP', 5, '123456')
	P = Printer('Canon', 10)
	P2 = Laser('Epson', 5)
	P1.print_thing('hello')
	print(P1.inks)
	P2.print_thing('hello')
	print(P2.inks)