from Vector import Vector

def gravity(body):
	world = body.world
	sumForce = Vector(0, 0)
	for actor in world.bodies:
		if actor != body:
			unitVec = ((body.G+body.geometry.pos) - (actor.G+actor.geometry.pos))
			distance = unitVec.norm();
			unitVec /= distance;
			sumForce += unitVec * (-6.674e-11 * (actor.mass * body.mass) / (distance*distance))
	return sumForce