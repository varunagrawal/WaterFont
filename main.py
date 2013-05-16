#!/usr/bin/python

# Create GUI. Use TKinter for cross-platform support

#Should display the image
#Should be able to load fonts
#Should have a slider for opacity
#Should show the watermark
#Option for multiple images


import font
import Tkinter
import tkFileDialog
import Image, ImageTk


def main():
	root = Tkinter.Tk()

	#Set up Tkinter Canvas with scrollbars
	frame = Tkinter.Frame(root, bd=2, relief=Tkinter.SUNKEN)
	frame.grid_rowconfigure(0, weight=1)
	frame.grid_columnconfigure(0, weight=1)
	#xscroll = Tkinter.Scrollbar(frame, orient=Tkinter.HORIZONTAL)
	#xscroll.grid(row=1, column=0, sticky=Tkinter.E+Tkinter.W)
	#yscroll = Tkinter.Scrollbar(frame)
	#yscroll.grid(row=0, column=1, sticky=Tkinter.N+Tkinter.S)

	canvas = Tkinter.Canvas(frame, bd=0)#, xscrollcommand=xscroll.set, yscrollcommand=yscroll.set)
	canvas.grid(row=0, column=0, sticky=Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W)

	
	#xscroll.config(command=canvas.xview)
	#yscroll.config(command=canvas.yview)

	frame.pack(fill=Tkinter.BOTH,expand=1)
		

	#adding the image
	File = tkFileDialog.askopenfilename(parent=root, initialdir="/home/varun/Pictures", title='Choose an image.')
	img = ImageTk.PhotoImage(Image.open(File))

	canvas.create_image(0, 0, image=img)
	canvas.config(scrollregion=canvas.bbox(Tkinter.ALL))
	
	root.mainloop()

	
if __name__ == "__main__":

	main()

	"""
	

	
	#function to be called when mouse is clicked
	def printcoords(event):
		#outputting x and y coords to console
		print (event.x,event.y)
		#mouseclick event

	canvas.bind("<Button 1>",printcoords)
	"""
