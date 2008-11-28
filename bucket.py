#!/usr/bin/python
# filename: bucket.py
# author: latrokles
#
# description: A Game in which you have to use a bucket to catch as much water
# as you can. Since it uses the sudden motion sensor on the mac, you do this 
# by tilting your laptop side to side and back and forth.
#

import applesms
import pyglet
import random
from pyglet.gl import *
from pyglet import window

def is_there_a_collision(player, object):
	raise NotImplementedError


def create_drops(some_number):
	raise NotImplementedError


def main():
	"""Game Loop"""
	#Initialize player and game
	player_img = pyglet.image.load('./assets/at.png')
	player = pyglet.sprite.Sprite(player_img)
	score = 0

	## Keep Track of water drops
	water_drops_tracker = []
	water_drops_batch = pyglet.graphics.Batch()
	water_drop_img = pyglet.image.load('./assets/star.png')

	## Game Window ##
	main_window = window.Window(width=600, height=500, caption='Bucket V0.2')
	window_width, window_height = main_window.get_size()


	## Game Loop ##
	while not main_window.has_exit:
		main_window.dispatch_events()
		glLoadIdentity()
		glClear(GL_COLOR_BUFFER_BIT)
		
		## Create Water Drops ##
		# Random Position for a created drop of water
		drop_x = random.randint(0, window_width)
		drop_y = random.randint(window_height/2, window_height)
		
		water_drops_tracker.append(pyglet.sprite.Sprite(water_drop_img, x=drop_x, y=drop_y, batch=water_drops_batch))


		## Update Water Drops ##
		
		# Update their position 

		## Update player ##
		x, y, z = applesms.coords()
		player_x, player_y = player.position

		if x > 20 and player_x > 0:
			player_x -= 5

		if x < 20 and (player_x + player.width) < window_width :
			player_x += 5
	
		if y > 20 and player_y > 0:
			player_y -= 5
	
		if y < 20 and player_y < (window_height/2):
			player_y += 5

		player.set_position(player_x, player_y)

		## Draw the player ##
		player.draw()

		## Draw Water Drops ##
		water_drops_batch.draw()

		## Score ##

		# Check for collision
		# Update Score or not

		main_window.flip()


if __name__=='__main__':
	main()
