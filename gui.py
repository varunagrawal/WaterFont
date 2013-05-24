# GUI Module

from Tkinter import *

import tkFileDialog
import Image, ImageTk

class GUI(Frame):

	def __init__(self, root):

		Frame.__init__(self, root)

		self.root = root
		
		self.initUI()

	def initUI(self):

		self.root.title = "WaterFont"
		
		#Set up Tkinter Canvas with scrollbars
		frame = Frame(self.root, bd=2, relief=SUNKEN)
		frame.grid_rowconfigure(0, weight=1)
		frame.grid_columnconfigure(0, weight=1)
		
		#Get the scroll bars
		xscroll, yscroll = self.scroll_bars()

		canvas = Canvas(self, bd=0, xscrollcommand=xscroll.set, yscrollcommand=yscroll.set)
		canvas.grid(row=0, column=0, sticky=N+S+E+W)
	
	
		xscroll.config(command=canvas.xview)
		yscroll.config(command=canvas.yview)

		self.File, self.img = self.load_image(self.root)
		self.watermark_img = None
	
		canvas.create_image(0, 0, image=self.img)
		canvas.config(scrollregion=canvas.bbox(ALL))
	
		self.pack(fill=BOTH,expand=1)
		
		
		#Scale Label
		scale_label = Label(self.root, text="Opacity:")
		scale_label.grid(column=0, sticky=W)
		scale_label.pack()
		
		#Scale widget to select opacity
		opacity_scale = Scale(self.root, from_=0, to=100, orient=HORIZONTAL, length=300)
		opacity_scale.grid(column=1, sticky=W)
		opacity_scale.pack()
		
		#Label for coords
		v = StringVar()
		v.set("Coordinates = x : None, y : None")
		coord_label = Label(self.root, textvariable=v, borderwidth=20)
		#coord_label.grid(sticky=E)
		coord_label.pack()
		
		
		#mouseclick event
		canvas.bind("<Button 1>", lambda event: self.getcoords(event, v))
		
		#Scroll using Mouse
		#canvas.bind("<MouseWheel>", self.mouse_wheel) # For Windows. Test!!
		canvas.bind("<Button 4>", lambda event : canvas.yview("scroll", -1, "units"))
		canvas.bind("<Button 5>", lambda event : canvas.yview('scroll', 1, "units"))

		

	def load_image(self, root):
		#adding the image

		File = tkFileDialog.askopenfilename(parent=root, initialdir="/home/varun/Pictures", title='Choose an image')
		img = ImageTk.PhotoImage(Image.open(File))
		
		return File, img


	#function to be called when mouse is clicked
	x, y = None, None
	def getcoords(self, event, v):
		
		self.x, self.y = event.x, event.y

		v.set("Coordinates = x : " + str(self.x) + ", y : " + str(self.y))
	
		#outputting x and y coords to console
		print (event.x,event.y)
		
		
		
	#function to be called when mouse is used to scroll
	def mouse_wheel(self, event):
		global count
		if event.num == 4:
			canvas.xview('scroll', -1, 'units')
		elif event.num == 5:
			canvas.xview('scroll', 1, 'units')
			
		
	def scroll_bars(self):
		xscroll = Scrollbar(self, orient=HORIZONTAL)
		xscroll.grid(row=1, column=0, sticky=E+W)
		yscroll = Scrollbar(self)
		yscroll.grid(row=0, column=1, sticky=N+S)
		
		return xscroll, yscroll


if __name__ == "__main__":
	root = Tk()
	app = GUI(root)
	
	root.mainloop()
