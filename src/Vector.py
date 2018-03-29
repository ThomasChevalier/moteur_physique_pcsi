from math import *

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

	def __str__(self):
		"""
		Convertir un vecteur en chaîne de caractères
		"""
		return "(" + str(self.x) + "; " + str(self.y) + ")"

	def __eq__(self,other):
		"""
		Compare deux vecteurs (égalité)
		"""
		return (abs(self.x - other.x) < 1e-3 and abs(self.y - other.y) < 1e-3)

	def __ne__(self,other):
		"""
		Compare deux vecteurs (différent)
		"""
		return not(self.__eq__(other))

	def dot(self, other):
		"""
		Calcul le produit scalaire entre deux vecteurs.
		Cela suppose que le repère est orthonormé
		"""
		return self.x * other.x + self.y * other.y

	def det(self, other):
		"""
		Retourne Vraie si les deux vecteurs sont colinéaire, Faux sinon
		"""
		return self.x * other.y - self.y * other.x

	def norm(self):
		"""
		Retourne la norme du vecteur
		"""
		return (self.x * self.x + self.y * self.y)**0.5

	def norm2(self):
		"""
		Retourne la norme au carré du vecteur
		"""
		return self.x * self.x + self.y * self.y

	def rotate(self, teta):
		"""
		Retourne un vecteur ayant subit une rotation de teta (en radian).
		"""
		return Vector(self.x*cos(teta) - self.y*sin(teta), self.x*sin(teta)+self.y*cos(teta))