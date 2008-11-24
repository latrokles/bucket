#!/usr/bin/python
# filename: bucket.py
# author: latrokles
#
# description: A Game in which you have to use a bucket to catch as much water
# as you can. Since it uses the sudden motion sensor on the mac, you do this 
# by tilting your laptop side to side and back and forth.
#

import applesms


class Player:
	def __init__(self, x, y, bounds):
		"""Create a player at position x,y with boundaries defined in 
		bounds."""
		self.x = x
		self.y = y
		# bounds is a dict with boundary values for LEFT, RIGHT, 
		# TOP, and BOTTOM 
		self.bounds = bounds	

	def update_position(self):
		"""Update the position of the player using the input from
		the apple sudden motion sensor"""
		x, y, z = applesms.coords()
		if x > 20 and (self.x-10) >= self.bounds['LEFT']:
			self.x -= 5
		elif x < -20 and (self.x+10) <= self.bounds['RIGHT']:
			self.x += 5

		if y > 20 and (self.y-10) >= self.bounds['BOTTOM']:
			self.y -= 5
		elif y < -20 and (self.y+10) <= self.bounds['TOP']:
			self.y += 5

	def draw(self):
		glBegin(GL_QUADS)
		glVertex2f(self.x - 10, self.y - 10)
		glVertex2f(self.x - 10, self.y + 10)
		glVertex2f(self.x + 10, self.y + 10)
		glVertex2f(self.x + 10, self.y - 10)
		glEnd()

class Drop:
	def __init__(self, x, y, value):
		self.x     = x
		self.y     = y
		self.value = value

	def update(self):
		raise NotImplementedError

class Game:
	def __init__(self):
		self.game_window = window.Window(width=400, height=500, caption='Bucket V.0')
		x,y = self.game_window.get_size()
		bounds = ['LEFT':0, 'RIGHT':x, 'TOP':y, 'BOTTOM':0]
		self.player = Player(x, y, bounds)
	
	def update_game_state(self):
		raise NotImplementedError



