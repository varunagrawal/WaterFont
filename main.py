#!/usr/bin/python

# Create GUI. Use TKinter for cross-platform support

#The image does not load when I use the wrapper class. Check that out.
#Should be able to load fonts
#Should have a slider for opacity
#Should show the watermark
#Option for multiple images


import font
import Tkinter
import tkFileDialog
import Image, ImageTk

def load_image(root):
	#adding the image

	File = tkFileDialog.askopenfilename(parent=root, initialdir="/home/varun/Pictures", title='Choose an image')
	img = ImageTk.PhotoImage(Image.open(File))

	return img


#function to be called when mouse is clicked
def printcoords(event):
	#outputting x and y coords to console
	print (event.x,event.y)


#function to be called when mouse is used to scroll
def mouse_wheel(event):
	global count
	if event.num == 4:
		canvas.xview('scroll', -1, 'units')
	elif event.num == 5:
		canvas.xview('scroll', 1, 'units')


		
class App:

	def __init__(self, root):

		#Set up Tkinter Canvas with scrollbars
		frame = Tkinter.Frame(root, bd=2, relief=Tkinter.SUNKEN)
		frame.grid_rowconfigure(0, weight=1)
		frame.grid_columnconfigure(0, weight=1)
		
		#xscroll = Tkinter.Scrollbar(frame, orient=Tkinter.HORIZONTAL)
		#xscroll.grid(row=1, column=0, sticky=Tkinter.E+Tkinter.W)
		#yscroll = Tkinter.Scrollbar(frame)
		#yscroll.grid(row=0, column=1, sticky=Tkinter.N+Tkinter.S)

		canvas = Tkinter.Canvas(frame, bd=0)
		#canvas = Tkinter.Canvas(frame, bd=0, xscrollcommand=xscroll.set, yscrollcommand=yscroll.set)
		canvas.grid(row=0, column=0, sticky=Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W)
		
		
		#xscroll.config(command=canvas.xview)
		#yscroll.config(command=canvas.yview)
		
		frame.pack(fill=Tkinter.BOTH, expand=1)
		
		
		img = load_image(root)
		
		canvas.create_image(0, 0, image=img)
		canvas.config(scrollregion=canvas.bbox(Tkinter.ALL))
		
		#mouseclick event
		canvas.bind("<Button 1>", printcoords)
		
		#Scroll using Mouse
		#canvas.bind("<MouseWheel>", mouse_wheel) # For Windows. Test!!
		canvas.bind("<Button 4>", lambda event : canvas.yview("scroll", -1, "units"))
		canvas.bind("<Button 5>", lambda event : canvas.yview('scroll', 1, "units"))


		

def main():
	root = Tkinter.Tk()
	root.title("WaterFont")
	
	
	#Set up Tkinter Canvas with scrollbars
	frame = Tkinter.Frame(root, bd=2, relief=Tkinter.SUNKEN)
	frame.grid_rowconfigure(0, weight=1)
	frame.grid_columnconfigure(0, weight=1)
	
	xscroll = Tkinter.Scrollbar(frame, orient=Tkinter.HORIZONTAL)
	xscroll.grid(row=1, column=0, sticky=Tkinter.E+Tkinter.W)
	yscroll = Tkinter.Scrollbar(frame)
	yscroll.grid(row=0, column=1, sticky=Tkinter.N+Tkinter.S)

	#canvas = Tkinter.Canvas(frame, bd=0)
	canvas = Tkinter.Canvas(frame, bd=0, xscrollcommand=xscroll.set, yscrollcommand=yscroll.set)
	canvas.grid(row=0, column=0, sticky=Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W)
	
	
	xscroll.config(command=canvas.xview)
	yscroll.config(command=canvas.yview)

	img = load_image(root)

	"""
	#Doesn't seem to work well
	w, h = root.winfo_screenwidth(), root.winfo_screenheight()
	root.overrideredirect(1)
	root.geometry("%dx%d+0+0" % (w, h))
	root.focus_set()
	"""

	canvas.create_image(0, 0, image=img)
	canvas.config(scrollregion=canvas.bbox(Tkinter.ALL))
	
	frame.pack(fill=Tkinter.BOTH,expand=1)

	opacity_scale = Tkinter.Scale(root, from_=0, to=100, orient=Tkinter.HORIZONTAL, length=300)
	opacity_scale.pack()
	
	
	#mouseclick event
	canvas.bind("<Button 1>", printcoords)
	
	#Scroll using Mouse
	#canvas.bind("<MouseWheel>", mouse_wheel) # For Windows. Test!!
	canvas.bind("<Button 4>", lambda event : canvas.yview("scroll", -1, "units"))
	canvas.bind("<Button 5>", lambda event : canvas.yview('scroll', 1, "units"))
	

	#app = App(root)
	
	
	root.mainloop()


def test():
	opacity = opacity_scale.get()
	font_file = "/usr/share/fonts/truetype/ttf-dejavu/DejaVuSans-Bold.ttf"
	
	
if __name__ == "__main__":

	main()
