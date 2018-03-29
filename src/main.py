from sfml import sf

import tkinter
import numpy as np
import matplotlib.pyplot as plt

import time

from World import World
from Environment import Environment
from RigidBody import RigidBody
from Vector import Vector

from Geometry import GeometryType

from render import *
from coordinates import set_zoom
from coordinates import get_zoom
from forces import *


if __name__ == "__main__":

	# Initialise sfml
	window = sf.RenderWindow(sf.VideoMode(640, 480), "Moteur physique")
	window.vertical_synchronization = True

	world = World()

	apple = RigidBody(world, "apple")
	apple.mass = 1e8/10
	apple.geometry.type = GeometryType.Circle
	apple.geometry.radius = 0.1
	apple.geometry.pos = Vector(3, -2)
	apple.log = True
	apple.geometry.calc_bounding_box()
	apple.geometry.color = (0, 255, 0)

	# earth = RigidBody(world, "earth")
	# earth.mass = 5.9736e24
	# earth.geometry.type = GeometryType.Circle
	# earth.geometry.radius = 6378137
	# earth.geometry.pos = Vector(0, -6378137-10)
	# earth.geometry.calc_bounding_box()
	# earth.geometry.color = (0, 0, 255)

	space = Environment(world, "space")
	space.geographyFunc = lambda obj : True
	space.add_global_force(gravity)

	world.time_factor = 1
	world.start()

	set_zoom(100)

	fps = 0
	fps_timer = time.time()
	render_time = 0
	update_time = 0
	event_time = 0

	zooming = False

	while window.is_open:
		for event in window.events:
			# Ferme la fenêtre
			if type(event) is sf.CloseEvent:
				window.close()
			# Met en pause
			if type(event) is sf.KeyEvent and event.pressed:
				if event.code == sf.Keyboard.SPACE :
					world.set_paused(not world.pause)

				# Navigation
				if event.code == sf.Keyboard.LEFT:
					view = window.view
					view.move(-view.size.x/25, 0)
				if event.code == sf.Keyboard.RIGHT:
					view = window.view
					view.move(view.size.x/25, 0)
				if event.code == sf.Keyboard.UP:
					view = window.view
					view.move(0, -view.size.y/25)
				if event.code == sf.Keyboard.DOWN:
					view = window.view
					view.move(0, view.size.y/25)
				if event.code == sf.Keyboard.I:
					set_zoom(get_zoom()*1.5)
					print("Zoom : ", get_zoom())
				if event.code == sf.Keyboard.O:
					set_zoom(get_zoom()/1.5)
					print("Zoom : ", get_zoom())

				if event.code == sf.Keyboard.A :
					accY = [a.y for a in apple.accList]
					velY = [v.y for v in apple.velList]
					posY = [p.y for p in apple.posList]
					#plt.plot(apple.timeList, acc)
					plt.plot(apple.timeList, accY, color="red")
					plt.plot(apple.timeList, velY, color="green")
					plt.plot(apple.timeList, posY, color="blue")
					p = world.pause
					world.set_paused(True)
					plt.show()
					quit()

			# Rempli d'objet
			if type(event) is sf.MouseButtonEvent and event.pressed and event.button == 0:
				pos = event.position

				for i in range(0, 1):
					for j in range(0, 1):
						w = scene_to_world(Vector(pos[0], pos[1])+Vector(i*30,j*30))
						obj = RigidBody(world, str(i)+str(j))
						obj.mass = 1e8
						obj.geometry.type = GeometryType.Circle
						obj.geometry.radius = 0.1
						obj.geometry.pos = w
						obj.geometry.calc_bounding_box()
						obj.geometry.color = (i*35+70, j*35+70, (i+j)/2*35+70)

			if type(event) is sf.MouseButtonEvent and event.button == 1:
				if event.pressed:
					if not zooming:
						zooming = True
						zoomPos = window.map_pixel_to_coords(event.position)
					lastPos = window.map_pixel_to_coords(event.position)
					lastPos.y = (lastPos.x - zoomPos.x)/ window.size.x * window.size.y
				if not event.pressed and zooming:
					zooming = False
					lastPos = window.map_pixel_to_coords(event.position)
					rect = sf.Rectangle()
					rect.left = zoomPos.x
					rect.top  = zoomPos.y
					rect.width = lastPos.x - zoomPos.x
					rect.height = rect.width / window.size.x * window.size.y
					window.view = sf.View(rect)
			if type(event) is sf.MouseMoveEvent:
				if zooming:
					lastPos = window.map_pixel_to_coords(event.position)

		# For end

		a = time.time()
		world.update()
		update_time += time.time() - a

		a = time.time()


		window.clear(sf.Color.WHITE)
		render(window, world)
		if zooming:
			zoomRect = sf.RectangleShape()
			zoomRect.size = (lastPos.x - zoomPos.x, lastPos.y - zoomPos.y)
			zoomRect.outline_thickness = 1
			zoomRect.outline_color = sf.Color.RED
			zoomRect.fill_color = sf.Color.TRANSPARENT
			zoomRect.position = (zoomPos.x, zoomPos.y)
			window.draw(zoomRect)

		window.display()
		render_time += time.time() - a

		# Affiche le nombre d'image par seconde
		fps += 1
		a = time.time()
		if a - fps_timer >= 1:
			print("fps : %4d | render : %.2f%% | update : %.2f%% | objects : " % (fps, render_time / (a - fps_timer) * 100, update_time / (a - fps_timer) * 100), len(world.bodies))
			update_time = 0
			render_time = 0 
			fps = 0
			fps_timer = time.time()
