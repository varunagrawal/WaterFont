#!/usr/bin/python

"""
 Author: Varun Agrawal (Eulerion)

 File: Main program file. Defines the starting point
"""


# Add doc strings to all functions


import font
import Tkinter
import tkFileDialog
import Image, ImageTk

import gui


def main():

	root = Tkinter.Tk()
	app = gui.GUI(root)

	
	#Test suite
	#test(app)

	root.mainloop()


def test(app):

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
