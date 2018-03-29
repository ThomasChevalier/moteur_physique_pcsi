import time

from collision import *

class World:
	def __init__(self):
		"""
		Constructeur du monde.
		Assigne les valeurs par défaut
		"""

		self.bodies = []
		self.envs = []

		self.last_update = 0
		self.time_origin = 0

		self.time_factor = 1 # Par combien ralentir ou accélérer le temps
		self.pause = True	# En pause ou non

	def start(self):
		"""
		Lance la simulation.
		"""

		self.pause = False
		self.last_update = time.time()
		self.time_origin = self.last_update

	def set_paused(self, pause):
		"""
		Met le monde en pause ou non.
		pause : un booléan
		"""

		if pause == self.pause:
			return

		self.pause = pause
		if self.pause == False:
			self.start()

	def add_object(self, body):
		"""
		Ajoute un objet au monde.
		"""
		print("L'objet %s a été ajouté au monde." % (body.name))
		self.bodies.append(body)

	def update(self):
		"""
		Calcule les nouvelles positions des objets.
		Gèrent les éventuelles collisions.
		"""

		# Ne pas calculer si on est en pause
		if self.pause == True:
			return

		# Calcule dt et t
		now = time.time()
		# print("now = ", now)
		dt = (now - self.last_update) * self.time_factor
		t = (now - self.time_origin) * self.time_factor
		self.last_update = now

		# Calcule les forces globales
		for body in self.bodies:
			for env in self.envs:
				if body in env:
					for force in env.forces:
						body.apply_force(force, body.G)

		# Mise à jour des vitesses / positions
		for body in self.bodies:
			body.update(t, dt)

		check_collision(self.bodies)
		# for i in range(len(self.bodies)):
		# 	for j in range(i+1, len(self.bodies)):
		# 		if self.bodies[i].geometry.intersect(self.bodies[j].geometry):
		# 			self.bodies[i].vel = self.bodies[i].vel * -0.95
		# 			self.bodies[j].vel = self.bodies[j].vel*-0.95

	def add_environment(self, env):
		for body in self.bodies:
			if body in env:
				print("body %s is in env %s" % (body.name, env.name))
		self.envs.append(env)