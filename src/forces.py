from Vector import Vector
from coordinates import *

def gravity(body):
	world = body.world
	sumForce = Vector(0, 0)
	for actor in world.bodies:
		if actor != body:
			# print(actor.name, " attire ", body.name, " vers ", object_to_world(actor, actor.G))
			unitVec = (object_to_world(body, body.G) - object_to_world(actor, actor.G) )
			distance = unitVec.norm();
			unitVec /= distance;
			sumForce += unitVec * (-6.674e-11 * (actor.mass * body.mass) / (distance*distance))
	return sumForce

def wind(body):
	return Vector(1, 0)

