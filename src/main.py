import pygame

from World import World
from RigidBody import RigidBody
from Vector import Vector

from render import *
from coordinates import set_zoom
from coordinates import get_zoom

def weight(body):
	return Vector(0, -9.81*body.mass)

# Initialize the game engine
pygame.init()

size = [400, 300]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Moteur physique")


world = World()

obj1 = RigidBody(10, 0, Vector(0, 0))
obj1.pos = Vector(0.2, 0)
obj1.add_force(weight, Vector(0, 0))

world.add_object(obj1)

quit = False
clock = pygame.time.Clock()
set_zoom(100)

world.time_factor = 1
world.start()

while not quit :

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			quit = True

		# Handle pause event
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				world.set_paused(not world.pause)

	world.update()

	render(screen, world)

	clock.tick(60)

pygame.quit()
