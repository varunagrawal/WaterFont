"""
    GUI Module

    Author:    Varun Agrawal (Eulerion)

    About:     Creates the GUI and functions that take user input and get the work done

"""


from Tkinter import *

import os
import tkFileDialog, tkMessageBox
import Image, ImageTk

import font


class GUI:

	"""
	Wrapper class for the GUI
	"""

	
	def __init__(self, root):

		self.root = root
		
		
		
		# Instance Variables init
		self.canvas = None
		self.opacity_scale = None
		
		self.filedir = None
		self.Files = None

		self.img_file = None
		self.img = None
		self.pimg = None
		self.watermark_img = None

		self.text = None
		self.textfont = None
		self.font_file = None
		self.font_size = None
		self.x, self.y = None, None

		self.count = None
		# Done initializing instance variables


		self.initUI()


		
	def initUI(self):

		"""
		Initialize the UI
		"""
		
		self.root.title("WaterFont")
		main_frame = Frame(self.root)
		
		
		img_frame, data_frame = self.create_frames(main_frame)

		
	
		
	def create_frames(self, main_frame):

		"""
		Create 2 frames. First to store the image and the second to store the controls for watermarking.
		Create and add all the widgets.
		"""

		
		#Set up Tkinter Canvas with scrollbars
		img_frame = Frame(main_frame, bd=2, relief=SUNKEN)
		img_frame.grid(row=0, column=0)
		img_frame.grid_rowconfigure(0, weight=1)
		img_frame.grid_columnconfigure(0, weight=1)
		
		# Get the scroll bars
		self.xscroll, self.yscroll = self.scroll_bars(img_frame)

		# Init the Image Canvas
		self.canvas = Canvas(img_frame, bd=0, xscrollcommand=self.xscroll.set, yscrollcommand=self.yscroll.set)
		self.canvas.grid(row=0, column=0, sticky=N+S+E+W)
		
		
		self.xscroll.config(command=self.canvas.xview)
		self.yscroll.config(command=self.canvas.yview)


		# Load the image on startup
		self.load_image(self.root)
		self.watermark_img = None


		# Image Label
		i = StringVar()
		i.set(self.Files[self.count-1])
		img_label = Label(img_frame, textvariable=i)
		img_label.grid(row=2, column=0)

		
		img_frame.pack()

		main_frame.pack(fill=BOTH, expand=1)
		

		
		# Data Frame starts here
		
		data_frame = Frame(self.root, relief=RAISED)


		# Text Label
		text_label = Label(data_frame, text="Watermark Text:")
		text_label.grid(row=0, column=0, sticky=W)

		# Text Input
		self.text = Entry(data_frame, width=30)
		self.text.grid(row=0, column=1)

		
		# Scale Label
		scale_label = Label(data_frame, text="Opacity:")
		scale_label.grid(row=1, column=0, sticky=W)

		#Scale widget to select opacity
		self.opacity_scale = Scale(data_frame, from_=0, to=100, orient=HORIZONTAL, length=300)
		self.opacity_scale.grid(row=1, column=1, sticky=W)

		
		# Coordinate Label
		coord_label = Label(data_frame, text="Co-ordinates:")
		coord_label.grid(row=2, column=0)

		#Label for coords
		v = StringVar()
		v.set("x : None, y : None")
		coordxy_label = Label(data_frame, textvariable=v, borderwidth=5)
		coordxy_label.grid(row=2, column=1)


		# Label for font
		fl = StringVar()
		fl.set("No font")
		font_label = Label(data_frame, textvariable=fl)
		font_label.grid(row=4, column=0)
		
		# Button to select font
		font_button = Button(data_frame, text="Select Font", command=lambda: self.getfont(fl))
		font_button.grid(row=4, column=1)


		# Label for font size
		font_size_label = Label(data_frame, text="Font size:")
		font_size_label.grid(row=5, column=0)
		
		# Entry for font
		self.font_size_input = Entry(data_frame, width=10)
		self.font_size_input.grid(row=5, column=1)

		# Button to set font size
		font_size_btn = Button(data_frame, text="Set Size", command=self.set_font_size)
		font_size_btn.grid(row=5, column=2)
		
		
		# Watermark buttons
		watermark_button = Button(data_frame, text="Watermark", command=self.watermark_image)
		watermark_button.grid(row=6, column=0)
		done_button = Button(data_frame, text="Save", command=self.save_image)
		done_button.grid(row=6, column=1)

		next_button = Button(data_frame, text="Next", command=lambda: self.next_image(i))
		next_button.grid(row=6, column=2)

		
		data_frame.pack()
		
		main_frame.pack(fill=BOTH, expand=1)
		
		
		# mouseclick event
		self.canvas.bind("<Button 1>", lambda event: self.get_coords(event, v))
		
		# Scroll using Mouse
		self.canvas.bind("<Button 4>", lambda event : self.canvas.yview("scroll", -1, "units"))
		self.canvas.bind("<Button 5>", lambda event : self.canvas.yview('scroll', 1, "units"))


		
		return img_frame, data_frame

	
	
	def watermark_image(self):

		"""
		Method to run when user clicks the Watermark button
		"""
		
		text_pos = (self.x, self.y)
		
		if self.img_file == None:
			tkMessageBox.showerror("No image", "No image selected")
			
		elif self.text.get() == "" or self.text.get() == None:
			tkMessageBox.showerror("Text Missing", "Please enter watermark text")

		elif self.textfont == None:
			tkMessageBox.showerror("No Font", "Please click on the image to select co-ordinates!")
			
		elif self.x == None or self.y == None:
			tkMessageBox.showerror("No Co-ords", "Please click on the image to select co-ordinates!")
			
		else:
			self.watermark_img = font.watermark(self.img_file, self.text.get(), self.textfont, text_pos, self.opacity_scale.get())

			self.pimg = ImageTk.PhotoImage( self.watermark_img )

			self.set_image()
			
			

			
	def save_image(self):

		"""
		Method to save the image with 'wm' prepended to the image name
		"""
		
		# Split file path. Check in windows
		file_name = os.path.split(self.img_file)
		wm_file = os.path.join(file_name[0], "wm-"+file_name[1])
		
		self.watermark_img.save(wm_file)

		tkMessageBox.showinfo("Image Saved", "Image successfully saved!")


		
		
	def next_image(self, i):

		"""
		Get next image in directory
		"""

		self.get_image()
		self.set_image()

		i.set(self.Files[self.count-1])


	def set_image(self):

		"""
		Set the image in the canvas
		"""
		
		self.canvas.create_image(0, 0, image=self.pimg, anchor="nw")
		self.canvas.config(scrollregion=self.canvas.bbox(ALL))

		

		
	def get_image(self):

		"""
		Obtains the next image in the specified directory.
		"""
		
		if self.count >= len(self.Files):
			tkMessageBox.showerror("End of images", "No more images to display")
			self.img = None
		 
		else:
			self.img_file = os.path.join(self.filedir, self.Files[self.count] )

			
			try:
			
				self.img = Image.open( self.img_file )
				self.pimg = ImageTk.PhotoImage( self.img )

			except IOError:
				print "Not an image file"
				tkMessageBox.showerror("Invalid Image", "Invalid Image. Please click Next")

			self.count += 1
				
			self.set_image()


		
			
	def load_image(self, root):

		"""
		Load the image directory on startup and set the 1st image in the dir to the canvas.
		"""

		# This function selects muliple files
		#Files = tkFileDialog.askopenfilenames(parent=root, initialdir="/home/varun/Pictures", title='Choose an image')

		# This function selects a directory
		self.filedir = tkFileDialog.askdirectory(parent=root, initialdir="/home/varun/Pictures", title='Choose a directory', mustexist=True)
		self.Files = os.listdir(self.filedir)
		
		self.count = 0

		self.get_image()
			
		
		
		
	def get_font(self, fl):

		"""
		Get the font from the user.
		"""
		
		
		self.font_file = tkFileDialog.askopenfilename(parent=self.root, initialdir="/usr/share/fonts/truetype/ttf-dejavu", title="Choose a font")
		
		font_type = os.path.split(self.font_file)[-1]
		fl.set(font_type)

		
		try:
			self.font_size = int(self.font_size_input.get())
			
		except ValueError:
			tkMessageBox.showerror("Input Error", "Invalid font size. Setting default")
			self.font_size = 20

			self.font_size_input.delete(0, END)
			self.font_size_input.insert(0, 20)
			
			
			
		self.textfont = font.select_font(self.font_file, self.font_size)


		
	def set_font_size(self):

		"""
		Set the font size when getting the font instance.
		"""
		
		try:
			self.font_size = int(self.font_size_input.get())
			
		except ValueError:
			tkMessageBox.showerror("Input Error", "Invalid font size. Setting default")
			self.font_size = 20

			self.font_size_input.delete(0, END)
			self.font_size_input.insert(0, 20)

		if self.font_file == None:
			tkMessageBox.showerror("Invalid Font", "Please select a font file.")
			return
		
		self.textfont = font.select_font(self.font_file, self.font_size)
		


		
	def get_coords(self, event, v):

		"""
		Method to be called when mouse is clicked. Stores the click co-ords in x, y
		"""
		
		self.x, self.y = self.canvas.canvasx(event.x), self.canvas.canvasy(event.y)		
		
		v.set("x : " + str(self.x) + ", y : " + str(self.y))
	
		
		

		
	def mouse_wheel(self, event):

		"""
		Method to be called when mouse is used to scroll.
		"""

		if event.num == 4:
			self.canvas.xview('scroll', -1, 'units')
		elif event.num == 5:
			self.canvas.xview('scroll', 1, 'units')


			
		
	def scroll_bars(self, frame):

		"""
		Defines the scrollbar objects for the canvas.
		"""
		
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
