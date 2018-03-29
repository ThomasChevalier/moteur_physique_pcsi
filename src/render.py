from sfml import sf

from coordinates import *
from Geometry import GeometryType

white = (255, 255, 255)

def render(window, world):
	"""
	Permet d'effectuer le rendu sur l'écran des objets du monde.
	window : où dessiner les objets
	world : le monde à dessiner
	"""

	# Foreach object in the world draw it
	for obj in world.bodies:
		pos = world_to_scene(obj.geometry.pos)
		
		if obj.geometry.type == GeometryType.Circle:
			size = obj.geometry.radius # m
			size *= get_zoom()

			circle = sf.CircleShape()
			circle.radius = size
			circle.fill_color = sf.Color(obj.geometry.color[0], obj.geometry.color[1], obj.geometry.color[2])
			circle.origin = (size / 2, size / 2)
			circle.position = (pos.x, pos.y)
			window.draw(circle)

