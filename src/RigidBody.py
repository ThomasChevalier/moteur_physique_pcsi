from Vector import Vector
from Geometry import Geometry
from World import World


class RigidBody:
	def __init__(self, world, name):
		"""
		Constructeur d'un solide indéformable
		Le référentiel de l'objet à pour origine son coin en haut à gauche dans tous les cas.
		"""
		self.vel = Vector(0, 0)
		self.v_rot = Vector(0, 0)

		self.geometry = Geometry(type)
		self.geometry.rotOrigin = Vector(0,0)

		self.mass = 0
		self.J = 0
		self.G = Vector(0,0)

		self.forces = []
		self.temp_forces = []

		self.world = world

		self.name = name
		self.world.add_object(self)

		# Logging des info
		self.log = False
		self.posList = []
		self.velList = []
		self.accList = []
		self.rotList = []
		self.vRotList = []
		self.aRotList = []
		self.timeList = []

	def attach_force(self, force, application_point):
		"""
		Ajoute une force locale sur l'objet.
		force : une fonction prenant un objet en argument et retournant un vecteur
		application_point : le point d'application dans le référentiel de l'objet
		"""
		self.forces.append((force, application_point))

	def apply_force(self, force, application_point):
		"""
		Applique une force temporairement sur l'objet
		"""
		self.temp_forces.append((force, application_point))

	def reset_log(self):
		self.posList.clear()
		self.velList.clear()
		self.accList.clear()
		self.rotList.clear()
		self.vRotList.clear()
		self.aRotList.clear()

	def update(self, t, dt):
		"""
		Met à jour la vitesse et la position de l'objet,
		en tenant compte des forces qui s'exercent sur l'objet.
		"""
		
		sum_force = Vector(0, 0)
		for force_struct in self.forces:
			sum_force += force_struct[0](self)

		for force_struct in self.temp_forces:
			sum_force += force_struct[0](self)
		self.temp_forces.clear()

		acc = sum_force / self.mass
		
		self.vel += acc * dt
		self.geometry.pos += self.vel * dt

		# Si l'on doit logger les infos :
		if self.log == True:
			self.posList.append(self.geometry.pos)
			self.velList.append(self.vel)
			self.accList.append(acc)
			self.rotList.append(self.geometry.rot)
			self.vRotList.append(self.v_rot)
			self.aRotList.append(0)
			self.timeList.append(t)
