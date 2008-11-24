#!/usr/bin/python
# filename: test_bucket.py
# author: latrokles
#
# description: test functions for bucket

from pyglet import window
from pyglet.gl import *
import bucket

def test_player():
	main_window = window.Window(caption='Test Player')
	x,y = main_window.get_size()
	bounds = {'LEFT':0, 'RIGHT':x, 'TOP':y, 'BOTTOM':0}
	player = bucket.Player(x/2, 40, bounds)

	while not main_window.has_exit:
		main_window.dispatch_events()
		glClear(GL_COLOR_BUFFER_BIT)
		glLoadIdentity()
		player.update_position()
		player.draw()

		main_window.flip()

if __name__=='__main__':
	test_player()
		
