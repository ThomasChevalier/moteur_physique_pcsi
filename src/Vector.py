class Vector:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __add__(self, other):
		"""
		Ajoute deux vecteurs entre eux
		"""
		x = self.x + other.x
		y = self.y + other.y
		return Vector(x, y)

	def __sub__(self, other):
		"""
		Soustrait deux vecteurs entre eux
		"""
		x = self.x - other.x
		y = self.y - other.y
		return Vector(x, y)

	def __mul__(self, alpha):
		"""
		Multiplie un vecteur par un scalaire.
		"""
		x = self.x * alpha
		y = self.y * alpha
		return Vector(x, y)

	def __truediv__(self, alpha):
		"""
		Divise un vecteur par un scalaire.
		"""
		x = self.x / alpha
		y = self.y / alpha
		return Vector(x, y)

