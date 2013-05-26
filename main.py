#!/usr/bin/python

# Create GUI. Use TKinter for cross-platform support

#Should show the watermark



import font
import Tkinter
import tkFileDialog
import Image, ImageTk

import gui


def main():

	root = Tk()
	app = gui.GUI(root)

	
	#Test suite
	
	opacity = opacity_scale.get()
	print opacity
	
	text_pos = (x, y)

	if x and y:
		test(canvas, File, opacity, text_pos)


	root.mainloop()


def test(File, trans, text_pos):
	
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
