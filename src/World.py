import time

class World:
	def __init__(self):
		"""
		Constructeur du monde.
		Assigne les valeurs par défaut
		"""

		self.bodies = []
		self.last_update = 0

		self.time_factor = 1 # Par combien ralentir ou accélérer le temps
		self.pause = True	# En pause ou non

	def start(self):
		"""
		Lance la simulation.
		"""

		self.pause = False
		self.last_update = time.clock()

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

		self.bodies.append(body)

	def update(self):
		"""
		Calcule les nouvelles positions des objets.
		Gèrent les éventuelles collisions.
		"""

		# Ne pas calculer si on est en pause
		if self.pause == True:
			return

		# Calcule dt
		now = time.clock()
		dt = (now - self.last_update) * self.time_factor
		self.last_update = now

		# Mise à jour
		for body in self.bodies:
			body.update(dt)
