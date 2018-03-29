from Vector import Vector
from math import *
from enum import Enum

class GeometryType(Enum):
	Point = 0
	Circle = 1
	Polygon = 2

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

def rotate_polygon(points, teta, origin):
	"""
	Retourne un polygône ayant subi une rotation de teta par 
	rapport a l'origine origin.
	teta en radian
	origin dans le repère du polygône
	"""
	rPoly = []
	for point in points:
		vec = point - origin
		vec = vec.rotate(teta)
		rPoly.append(origin+vec)
	return rPoly

class Geometry:
	"""
	Classe décrivant la géométrie d'un objet du monde.
	Trois types sont possibles : le point, le cercle et le polygône.
	Pour que les intersections et que l'affichage soit correct il faut
	que la géométrie soit mise à jour en même temps que l'objet (c'est 
	peut-être même elle qui devrait contenir les variables de position 
	et de rotation ...). Lorsqu'un paramètre (type de géométrie, points
	ou rayon) est modifié il faut appeler la fonction calc_bounding_box
	pour que cette dernière soit toujours à jour.
	"""

	def __init__(self, type):
		self.type = type

		# Polygone
		self.points = []

		# Cercle
		self.radius = 0

		# Un rectangle parallèle aux axes du repère
		self.bounding_box_size = Vector(0, 0)

		# Positionnement
		self.pos = Vector(0, 0)
		self.rot = 0
		self.rotOrigin = Vector(0, 0)

		self.color = (0, 0, 0)

	def calc_bounding_box(self):
		"""
		Calcule la boîte englobante de la géométrie en tenant compte
		de l'éventuelle rotation.
		Non testée.
		"""
		if self.type == GeometryType.Circle:
			self.bounding_box_size = Vector(self.radius*2, self.radius*2)

		# Doit tenir compte de la rotation
		elif self.type == GeometryType.Polygon:
			if len(self.points) == 0:
				self.bounding_box_size = Vector(0, 0)
			else:
				polyR = rotate_polygon(self.points, self.rot, self.rotOrigin)
				listX = [point.x for point in polyR]
				listY = [point.y for point in polyR]
				self.bounding_box_size = Vector(max(listX) - min(listX), max(listY) - min(listY))
		else:
			self.bounding_box_size = Vector(0, 0)

	def intersect(self, other):
		"""
		S'occupe de calculer l'intersection entre deux géométrie.
		S'il' n'y a pas d'intersection alors renvoie un tuple vide.
		Sinon renvoie un tuple contenant True et le vecteur normal de collision.
		"""

		# Premier test, vérifie que les boîtes englobantes ne s'intersectent pas
		# Test si l'autre est trop à droite,
		# trop à gauche, trop en bas et trop en haut
		if other.pos.x >= self.pos.x + self.bounding_box_size.x  or \
		   other.pos.x + other.bounding_box_size.x <= self.pos.x or \
		   other.pos.y >= self.pos.y + self.bounding_box_size.y  or \
		   other.pos.y + other.bounding_box_size.y <= self.pos.y :
		   return ()

		# Les boîtes englobantes s'intersectent

		# Pas de collisions entre un point et autre chose
		if self.type == GeometryType.Point or other.type == GeometryType.Point:
			return ()

		# Collision cercle / cercle
		if self.type == GeometryType.Circle and other.type == GeometryType.Circle:
			# Attention ici car la position de l'objet est celle de son point en haut à gauche.
			# Il faut donc ajouter le rayon sur les deux composantes pour obtenir la position du centre
			vecDist = self.pos + Vector(self.radius, -self.radius) - (other.pos + Vector(other.radius, -other.radius))
			# Calcul le carré pour des questions de performance
			if vecDist.norm2() <= (self.radius+other.radius)*(self.radius+other.radius):
				# Intersection
				d = vecDist.norm() - (self.radius+other.radius) # distance de pénétration
				return (True, vecDist / (vecDist.norm()) * d)
			else:
				return ()

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