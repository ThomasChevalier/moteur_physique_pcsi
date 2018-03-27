from Vector import Vector

class RigidBody:
	def __init__(self, mass, moment_inertia, center_grav):
		"""
		Constructeur d'un solide indéformable
		mass : la masse du solide en kg
		moment_inertia : le moment d'inertie de l'objet
		center_grav : un vecteur décrivant le centre de gravité du solide, par rapport à son origine (en haut à droite par défaut)
		"""

		self.pos = Vector(0, 0)
		self.vel = Vector(0, 0)

		self.rot = Vector(0, 0)
		self.v_rot = Vector(0, 0)

		self.mass = mass
		self.J = moment_inertia
		self.G = center_grav

		self.forces = []

	def add_force(self, force, application_point):
		"""
		Ajoute une force locale sur l'objet.
		force : une fonction prenant un objet en argument et retournant un vecteur
		application_point : le point d'application dans le référentiel de l'objet
		"""
		self.forces.append((force, application_point))

	def update(self, dt):
		"""
		Met à jour la vitesse et la position de l'objet,
		en tenant compte des forces qui s'exercent sur l'objet.
		"""
		
		sum_force = Vector(0, 0)
		for force_struct in self.forces:
			sum_force += force_struct[0](self)

		fVec = sum_force / self.mass

		self.vel += fVec * dt
		self.pos += self.vel * dt
