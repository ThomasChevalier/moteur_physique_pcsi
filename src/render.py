import pygame

from coordinates import *

white = (255, 255, 255)

def render(screen, world):
	"""
	Permet d'effectuer le rendu sur l'écran des objets du monde.
	screen : où dessiner les objets
	world : le monde à dessiner
	"""

	# Clear the screen
	screen.fill(white)

	# Foreach object in the world draw it
	for obj in world.bodies:
		size = 0.1 # m
		pos = world_to_scene(obj.pos)
		size *= get_zoom()
		pygame.draw.circle(screen, (0, 255, 0), [int(pos.x), int(pos.y)], int(size))

	# Finalize the drawing
	pygame.display.flip()
