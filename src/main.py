#!/usr/bin/python

"""
 Author: Varun Agrawal (Eulerion)

 File: Main program file. Defines the starting point
"""


import font
import Tkinter
import tkFileDialog
import Image, ImageTk

import gui


def main():

	"""
	Starting point for the application. Initializes the GUI
	"""
	
	root = Tkinter.Tk()
	app = gui.GUI(root)

		
	root.mainloop()


def test(app):

	"""
	Test suite for application
	"""

	
	opacity = app.opacity_scale.get()
	print opacity
	
	text_pos = (app.x, app.y)


	font_file = "/usr/share/fonts/truetype/ttf-dejavu/DejaVuSans-Bold.ttf"
	Font = font.select_font(font_file)
	text = "Varun Agrawal"

	watermark_img = font.watermark(File, Font, text, text_pos, int(trans*255/100))

	print opacity
	print text_pos
	
	canvas.create_image(0, 0, image=watermark_img)
	canvas.config(scrollregion=canvas.bbox(Tkinter.ALL))

	
	
if __name__ == "__main__":

	main()
