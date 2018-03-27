from Vector import Vector
from math import *

def equation(A, B):
	"""
	Retourne l'équation cartésienne de la droite (AB)
	"""
	# Ici ce ne sont plus des points mais un vecteur, directeur de (AB)
	vecDir = A - B

	# Equation de la droite ax+by+c = 0 
	# vecDir == (-b; a)
	a = vecDir.y
	b = -vecDir.x
	c = -a*A.x - b*A.y

	return (a, b, c)

class Polygon:
	def __init__(self):
		self.points = []

	def add_point(self, point):
		self.points.append(point)

	def check(self):
		"""
		A continuer...
		Pas forcément utile...
		"""
		
		if len(self.points) == 1:
			return

		edges = []

		# Calcul tous les côtés
		for i in range(len(self.points)-1):
			p1 = self.points[i];
			p2 = self.points[i+1];
			edges.append((p1, p2)) # les vecteurs sont ici traités comme des points

		# Vérifie que les côtés ne s'intersectent pas
		for i in range(len(edges)-1):
			A = edges[i][0]
			B = edges[i][1]
			vec1 = A - B

			a, b, c = equation(A, B)

			for j in range(i+1, len(edges)):
				print("Teste ", i , " et ", j)
				C = edges[j][0]
				D = edges[j][1]
				vec2 = C - D
				d, e, f = equation(C, D)
				# s'ils ne sont pas colinéaire, chercher l'intersection
				if abs(vec1.det(vec2)) > 1e-3:
					yi = (a*e-c*d)/(b*d-f*a)
					xi = (f-b)*yi/(a-d)
					I = Vector(xi, yi)
					print("Intersection du côté ", i, " et du ", j , " en ", I)
					print("A = ", A)
					print("B = ", B)
					print("C = ", C)
					print("D = ", D)
					# Maintenant si le point d'intersection n'est pas un des points générateur des droites (les sommets)
					# alors il y a un problème
					if I != A and I != B and I != C and I != D:
						return False
		return True


	def serialize():
		pass