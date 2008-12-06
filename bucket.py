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
from pyglet import font

def main():
	"""Game Loop"""
	#Initialize player and game variables
	player_img = pyglet.image.load('./assets/bucket_md.png')
	player = pyglet.sprite.Sprite(player_img)
	ft = font.load('Arial', 20)
	score = 0		#player score

	## Keep Track of water drops
	water_drops_tracker = []
	water_drops_batch = pyglet.graphics.Batch()
	water_drop_img = pyglet.image.load('./assets/drop_sm.png')

	missed_drops = 0	#water not caught
	#water_flood_img = pyglet.image.load('./assets/flood.png')
	#flood_x = 0
	#flood = pyglet.sprite.Sprite(water_flood_img, x=flood_x)

	## Game Window ##
	main_window = window.Window(width=600, height=500, caption='Bucket V0.2')
	back_img = pyglet.image.load('./assets/background.png')
	window_width, window_height = main_window.get_size()

	## Game Loop ##
	while not main_window.has_exit:
		main_window.dispatch_events()
		glLoadIdentity()
		glClear(GL_COLOR_BUFFER_BIT)
		back_img.blit(0, 0)

		## Create Water Drops ##
		# Random Position for a created drop of water
		if len(water_drops_tracker) < 20 and (random.randint(0,100)%3) == 0:
			drop_x = random.randint(0, window_width)
			drop_y = random.randint(window_height, window_height+200)
			water_drops_tracker.append(pyglet.sprite.Sprite(water_drop_img, x=drop_x, y=drop_y, batch=water_drops_batch))
		
		## Update player ##
		x, y, z = applesms.coords()
		player_x, player_y = player.position

		if x > 20 and player_x > 0:
			player_x -= 5

		if x < 20 and (player_x + player.width) < window_width :
			player_x += 5
	
		player.set_position(player_x, player_y)

		## Update Water Drops ##
		# Update their position 
		for each_drop in water_drops_tracker:
			drop_x, drop_y = each_drop.position
			each_drop.set_position(drop_x, drop_y-5)
			
			# Check for collision
			if (drop_x > player_x and drop_x < (player_x + player.width)) and (drop_y > player_y and drop_y < player_y + player.height):
				water_drops_tracker.remove(each_drop)
				each_drop.delete()
				score += 1
			# or if drops hits floor
			elif drop_y < 0:
				water_drops_tracker.remove(each_drop)
				each_drop.delete()
				missed_drops += 1

		## Update and Draw the water accumulated ##
		#if missed_drops%2 == 0:
		#	flood_x += 5
		#flood.draw()

		## Draw the player ##
		player.draw()
		## Draw Water Drops ##
		water_drops_batch.draw()

		## Draw Score ##
		score_str = font.Text(ft, "Score: " + str(score), 0, window_height - 20)
		score_str.draw()

		main_window.flip()


if __name__=='__main__':
	main()
