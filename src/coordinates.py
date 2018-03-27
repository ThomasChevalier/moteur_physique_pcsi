from Vector import Vector

zoom = 1

def world_to_scene(world):
	"""
	Convertie un vecteur de coordonnées du monde vers un vecteur de coordonées de la scène.
	Tient compte du zoom éventuelle entre la scène et le monde.

	world : un vecteur de coordonnées du monde
	"""

	global zoom
	return Vector(world.x, -world.y) * zoom

def scene_to_world(scene):
	"""
	Convertie un vecteur de coordonnées de la scène vers un vecteur de coordonées du monde.
	Tient compte du zoom éventuelle entre la scène et le monde.
	
	scene : un vecteur de coordonnées de la scène
	"""
	global zoom
	return Vector(scene.x, -scene.y) / zoom

def set_zoom(z):
	"""
	Permet d'affecter une valeur à la variable globale zoom
	"""

	global zoom
	zoom = z

def get_zoom():
	"""
	Permet de récupérer la valeur de la variable globale zoom
	"""
	global zoom
	return zoom