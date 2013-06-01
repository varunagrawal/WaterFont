"""
    Author:    Varun Agrawal (Eulerion)

    About:     Module which does all the image processing

"""

from PIL import Image, ImageFont, ImageDraw


def select_font( font_path, size ):

	"""
	Returns an instance of the ImageFont with the specified font and font size.
	"""
	
	wfont = ImageFont.truetype( font_path, size )

	return wfont



def watermark(img_file, text, wfont, text_pos, trans):

	"""
	Watermarks the specified image with the text in the specified font and on the specified point.
	"""

	
	#Open the image file
	img = Image.open(img_file)
	
	#The Text to be written will be white with trans as the alpha value
	t_color = (0, 0, 0, trans)

	
	#Specify alpha as 0 to get transparent image on which to write
	watermark = Image.new("RGBA", img.size, (255, 255, 255, 0))


	waterdraw = ImageDraw.Draw(watermark, "RGBA")
	waterdraw.text(text_pos, text, fill=t_color, font=wfont)

	
	#watermark.save("watermark.jpg")
	
	img.paste(watermark, None, watermark)

	return img



	
def main():

	"""
	Test suite for this module
	"""
	
	font_file = "/usr/share/fonts/truetype/ttf-dejavu/DejaVuSans-Bold.ttf"
	wfont = select_font(font_file, 20)

	text = "Varun Agrawal"

	#Transparency of Text
	trans = 120

	img_file = "orig.jpg"
	img = Image.open(img_file)
	text_pos = (img.size[0]-170, img.size[1]-25)

	img = watermark(img_file, text, wfont, text_pos, trans)

	img.save("temp-wm.jpg")


	
if __name__ == "__main__":
	main()
