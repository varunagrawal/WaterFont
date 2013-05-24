#!/usr/bin/python

# Create GUI. Use TKinter for cross-platform support

#Should be able to load fonts
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

	return File, img


#function to be called when mouse is clicked
x, y = None, None
def getcoords(event, v):

	global x, y
	x, y = event.x, event.y

	v.set("Coordinates = x : " + str(x) + ", y : " + str(y))
	
	#outputting x and y coords to console
	print (event.x,event.y)



#function to be called when mouse is used to scroll
def mouse_wheel(event):
	global count
	if event.num == 4:
		canvas.xview('scroll', -1, 'units')
	elif event.num == 5:
		canvas.xview('scroll', 1, 'units')

def scroll_bars( frame ):
	xscroll = Tkinter.Scrollbar(frame, orient=Tkinter.HORIZONTAL)
	xscroll.grid(row=1, column=0, sticky=Tkinter.E+Tkinter.W)
	yscroll = Tkinter.Scrollbar(frame)
	yscroll.grid(row=0, column=1, sticky=Tkinter.N+Tkinter.S)

	return xscroll, yscroll


def main():
	root = Tkinter.Tk()
	root.title("WaterFont")
	
	
	#Set up Tkinter Canvas with scrollbars
	frame = Tkinter.Frame(root, bd=2, relief=Tkinter.SUNKEN)
	frame.grid_rowconfigure(0, weight=1)
	frame.grid_columnconfigure(0, weight=1)

	#Get the scroll bars
	xscroll, yscroll = scroll_bars(frame)

	#canvas = Tkinter.Canvas(frame, bd=0)
	canvas = Tkinter.Canvas(frame, bd=0, xscrollcommand=xscroll.set, yscrollcommand=yscroll.set)
	canvas.grid(row=0, column=0, sticky=Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W)
	
	
	xscroll.config(command=canvas.xview)
	yscroll.config(command=canvas.yview)

	File, img = load_image(root)
	watermark_img = None
	
	canvas.create_image(0, 0, image=img)
	canvas.config(scrollregion=canvas.bbox(Tkinter.ALL))
	
	frame.pack(fill=Tkinter.BOTH,expand=1)


	#Scale Label
	scale_label = Tkinter.Label(root, text="Opacity:")
	scale_label.grid(column=0, sticky=Tkinter.W)
	scale_label.pack()
	
	#Scale widget to select opacity
	opacity_scale = Tkinter.Scale(root, from_=0, to=100, orient=Tkinter.HORIZONTAL, length=300)
	opacity_scale.grid(column=1, sticky=Tkinter.W)
	opacity_scale.pack()

	#Label for coords
	v = Tkinter.StringVar()
	v.set("Coordinates = x : None, y : None")
	coord_label = Tkinter.Label(root, textvariable=v, borderwidth=20)
	#coord_label.grid(sticky=E)
	coord_label.pack()


	
	
	#mouseclick event
	canvas.bind("<Button 1>", lambda event: getcoords(event, v))
	
	#Scroll using Mouse
	#canvas.bind("<MouseWheel>", mouse_wheel) # For Windows. Test!!
	canvas.bind("<Button 4>", lambda event : canvas.yview("scroll", -1, "units"))
	canvas.bind("<Button 5>", lambda event : canvas.yview('scroll', 1, "units"))

	

	#Test suite
	
	opacity = opacity_scale.get()
	#print opacity
	
	text_pos = (x, y)

	if x and y:
		test(canvas, File, opacity, text_pos)

	#app = App(root)
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
