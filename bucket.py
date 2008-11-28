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

	## Game Window ##
	main_window = window.Window(width=600, height=500, caption='Bucket V0.2')


	## Game Loop ##
	while not main_window.has_exit:
		main_window.dispatch_events()
		glLoadIdentity()
		glClear(GL_COLOR_BUFFER_BIT)
		
		## Create Water Drops ##

		# Randomly Create Water Drops
		# Need to keep track of their positions somehow...

		## Update Water Drops ##
		
		# Update their position 

		## Update player ##
		window_width, window_height = main_window.get_size()
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

		## Score ##

		# Check for collision
		# Update Score or not

		main_window.flip()


if __name__=='__main__':
	main()
