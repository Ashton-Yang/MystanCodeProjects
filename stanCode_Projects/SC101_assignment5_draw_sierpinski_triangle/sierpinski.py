"""
File: sierpinski.py
Name: Ashton Yang
---------------------------
This file recursively prints the Sierpinski triangle on GWindow.
The Sierpinski triangle is a fractal described in 1915 by Waclaw Sierpinski.
It is a self similar structure that occurs at different levels of iterations.
"""

from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GLine
from campy.gui.events.timer import pause

# Constants
ORDER = 6                  # Controls the order of Sierpinski Triangle
LENGTH = 600               # The length of order 1 Sierpinski Triangle
UPPER_LEFT_X = 150		   # The upper left x coordinate of order 1 Sierpinski Triangle
UPPER_LEFT_Y = 100         # The upper left y coordinate of order 1 Sierpinski Triangle
WINDOW_WIDTH = 950         # The width of the GWindow
WINDOW_HEIGHT = 700        # The height of the GWindow
DELAY = 30

# Global Variable
window = GWindow(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)  # The canvas to draw Sierpinski Triangle


def main():
	draw_first_triangle(ORDER, LENGTH, UPPER_LEFT_X, UPPER_LEFT_Y)
	sierpinski_triangle(ORDER, LENGTH, UPPER_LEFT_X, UPPER_LEFT_Y)


def draw_first_triangle(order, length, upper_left_x, upper_left_y):
	line_1 = GLine(upper_left_x, upper_left_y, upper_left_x + length, upper_left_y)
	line_2 = GLine(upper_left_x, upper_left_y, upper_left_x + length * 0.5, upper_left_y + length * 0.866)
	line_3 = GLine(upper_left_x + length, upper_left_y, upper_left_x + length * 0.5, upper_left_y + length * 0.866)
	pause(DELAY)
	window.add(line_1)
	window.add(line_2)
	window.add(line_3)
	order -= 1


def sierpinski_triangle(order, length, upper_left_x, upper_left_y):
	if order > 0:
		# mid_1 = (upper_left_x + length*0.5, upper_left_y)
		# mid_2 = (upper_left_x + length*0.25, upper_left_y + length*0.433)
		# mid_3 = (upper_left_x + length*0.75 , upper_left_y + length*0.433)

		line_2_1 = GLine(upper_left_x + length*0.25, upper_left_y + length*0.433,upper_left_x + length*0.5, upper_left_y)
		line_1_3 = GLine(upper_left_x + length*0.5, upper_left_y, upper_left_x + length*0.75, upper_left_y + length*0.433)
		line_2_3 = GLine(upper_left_x + length*0.25, upper_left_y + length*0.433, upper_left_x + length*0.75, upper_left_y + length * 0.433)
		pause(DELAY)
		window.add(line_2_3)
		window.add(line_1_3)
		window.add(line_2_1)
		order -= 1
		sierpinski_triangle(order, length*0.5, upper_left_x, upper_left_y)
		sierpinski_triangle(order, length*0.5, upper_left_x + 0.5 * length, upper_left_y)
		sierpinski_triangle(order, length*0.5, upper_left_x + length*0.25, upper_left_y + length*0.433)


if __name__ == '__main__':
	main()