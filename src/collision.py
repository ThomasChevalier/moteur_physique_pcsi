
def check_collision(objects):
	"""
	Teste les collisions entre tous les objets de la liste objets.
	Renvoie une liste dont les éléments sont les objets qui rentrent
	en collision
	"""

	for i in range(len(objects)):
			for j in range(i+1, len(objects)):
				res = objects[i].geometry.intersect(objects[j].geometry)
				if res:
					resolve_collision(objects[i], objects[j], res[1])

					
def resolve_collision(objectA, objectB, nVec):
	"""
	S'occupe de résoudre la collision en se basant
	sur les deux objets et leur vecteur normal de collision.
	Ne prend pas en compte les rotations
	"""

	e = 0.95 # coefficient de restitution
	vAB = objectA.vel - objectB.vel # vitesse relative

	# Les objets s'éloignent
	if -1e-5 < vAB.dot(nVec) < 1e-5:
		print(nVec)
		print("contact")
		return

	# Impulsion j :
	j = -(1+e)*vAB.dot(nVec) / (nVec.dot(nVec)*(1/objectA.mass + 1/objectB.mass))

	objectA.vel = objectA.vel + nVec * j/objectA.mass
	objectB.vel = objectB.vel - nVec * j/objectB.mass
