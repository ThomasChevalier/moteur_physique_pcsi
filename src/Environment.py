class Environment:
	"""
	Classe décrivant un environnement.
	Un environnement est une région de l'espace dans laquelle tous les objets
	s'y trouvant subissent une force globale s'exerçant sur leur centre de 
	gravité. Par exemple l'espace est un environnement où s'exercent la gravité.
	Un océan est également un environnement où s'exerce la poussé d'Archimède.
	"""

	def __init__(self, world, name):
		self.geographyFunc = lambda obj : False
		self.forces = []
		self.name = name
		self.world = world
		self.world.add_environment(self)

	def add_global_force(self, force):
		"""
		Ajoute une force  l'environnement.
		force(object) -> Vector
		"""
		self.forces.append(force)

	def __contains__(self, object):
		return self.geographyFunc(object)