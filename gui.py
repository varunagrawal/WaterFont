# GUI Module

from Tkinter import *

import os
import tkFileDialog, tkMessageBox
import Image, ImageTk

import font


# wrapper class for GUI
class GUI:

	
	def __init__(self, root):

		self.root = root
		
		self.initUI()


		
	def initUI(self):

		self.root.title("WaterFont")
		main_frame = Frame(self.root)
		
		
		img_frame, data_frame = self.create_frames(main_frame)

		
	
		
	def create_frames(self, main_frame):
			
		#Set up Tkinter Canvas with scrollbars
		img_frame = Frame(main_frame, bd=2, relief=SUNKEN)
		img_frame.grid(row=0, column=0)
		img_frame.grid_rowconfigure(0, weight=1)
		img_frame.grid_columnconfigure(0, weight=1)
		
		#Get the scroll bars
		xscroll, yscroll = self.scroll_bars(img_frame)
		
		canvas = Canvas(img_frame, bd=0, xscrollcommand=xscroll.set, yscrollcommand=yscroll.set)
		canvas.grid(row=0, column=0, sticky=N+S+E+W)
		
		
		xscroll.config(command=canvas.xview)
		yscroll.config(command=canvas.yview)
		
		self.load_image(self.root)
		self.watermark_img = None
		
		canvas.create_image(0, 0, image=self.img)
		canvas.config(scrollregion=canvas.bbox(ALL))
		
		img_frame.pack()

		main_frame.pack(fill=BOTH, expand=1)
		

		
		#Data Frame starts here
		
		data_frame = Frame(self.root, relief=RAISED)
		
		#Scale Label
		scale_label = Label(data_frame, text="Opacity:")
		scale_label.grid(row=0, column=0, sticky=W)

		
		#Scale widget to select opacity
		self.opacity_scale = Scale(data_frame, from_=0, to=100, orient=HORIZONTAL, length=300)
		self.opacity_scale.grid(row=1, column=0, sticky=W)

		
		#Label for coords
		v = StringVar()
		v.set("Coordinates = x : None, y : None")
		coord_label = Label(data_frame, textvariable=v, borderwidth=20)
		coord_label.grid(row=2)


		# Label for font
		fl = StringVar()
		fl.set("No font")
		font_label = Label(data_frame, textvariable=fl)
		font_label.grid(row=3, column=0)
		
		# Button to select font
		font_button = Button(data_frame, text="Select Font", command=lambda: self.getfont(fl))
		font_button.grid(row=3, column=1)


		# Watermark buttons
		watermark_button = Button(data_frame, text="Watermark", command=self.watermark_image)
		watermark_button.grid(row=4, column=0)
		done_button = Button(data_frame, text="Save", command=self.save_image)
		done_button.grid(row=4, column=1)
		next_button = Button(data_frame, text="Next", command=lambda: self.next_image(canvas))
		next_button.grid(row=4, column=2)
		
		data_frame.pack()

		main_frame.pack(fill=BOTH, expand=1)
		
		
		#mouseclick event
		canvas.bind("<Button 1>", lambda event: self.getcoords(event, v))
		
		#Scroll using Mouse
		#canvas.bind("<MouseWheel>", self.mouse_wheel) # For Windows. Test!!
		canvas.bind("<Button 4>", lambda event : canvas.yview("scroll", -1, "units"))
		canvas.bind("<Button 5>", lambda event : canvas.yview('scroll', 1, "units"))

		
		return img_frame, data_frame


	def watermark_image(self):
		#stuff
		abc = 1

	def save_image(self):
		#save watermarked image
		abc = 2


	#Get next image in directory
	def next_image(self, canvas):

		if self.count >= len(self.Files):
			tkMessageBox.showerror("End of images", "No more images to display")
		else:
			
			try:
				self.img = ImageTk.PhotoImage( Image.open( os.path.join(self.filedir, self.Files[self.count] ) ) )

			except IOError:
				print "Not an image file"
				
			self.count += 1
			canvas.create_image(0, 0, image=self.img)


			

	def load_image(self, root):
		#adding the image

		# This function selects muliple files
		#Files = tkFileDialog.askopenfilenames(parent=root, initialdir="/home/varun/Pictures", title='Choose an image')

		# This function selects a directory
		self.filedir = tkFileDialog.askdirectory(parent=root, initialdir="/home/varun/Pictures", title='Choose a directory', mustexist=True)
		self.Files = os.listdir(self.filedir)
				
		self.count = 0
		self.img = ImageTk.PhotoImage( Image.open( os.path.join(self.filedir, self.Files[self.count] ) ) ) 

		self.count += 1
			
		
		
		
	# Get the font from the user
	def getfont(self, fl):

		# Change the initial dir for Windows
		font_file = tkFileDialog.askopenfilename(parent=self.root, initialdir="/usr/share/fonts/truetype/ttf-dejavu", title="Choose a font")
		
		font_type = font_file.split('/')[-1]
		fl.set(font_type)

		self.textfont = font.select_font(font_file, int(self.img.height()*0.1))



	#function to be called when mouse is clicked
	def getcoords(self, event, v):
		
		self.x, self.y = event.x, event.y

		v.set("Coordinates = x : " + str(self.x) + ", y : " + str(self.y))
	
		
		
		
	#function to be called when mouse is used to scroll
	def mouse_wheel(self, event):
		global count
		if event.num == 4:
			canvas.xview('scroll', -1, 'units')
		elif event.num == 5:
			canvas.xview('scroll', 1, 'units')
			
		
	def scroll_bars(self, frame):
		xscroll = Scrollbar(frame, orient=HORIZONTAL)
		xscroll.grid(row=1, column=0, sticky=E+W)
		yscroll = Scrollbar(frame)
		yscroll.grid(row=0, column=1, sticky=N+S)
		
		return xscroll, yscroll



def run():
	root = Tk()
	app = GUI(root)
	
	root.mainloop()

	
if __name__ == "__main__":
	run()
