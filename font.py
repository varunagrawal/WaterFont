#!/usr/bin/python

import PIL
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

def select_font( font_path ):
	font = ImageFont.truetype( font_path, 20 )

	return font


def watermark(file, text, font, text_pos, trans):
	img = Image.open("orig.jpg")
	
	#The Text to be written will be white with trans as the alpha value
	t_color = (0, 0, 0, trans)

	
	#Specify alpha as 0 to get transparent image on which to write
	watermark = Image.new("RGBA", img.size, (255, 255, 255, 0))


	waterdraw = ImageDraw.Draw(watermark, "RGBA")
	waterdraw.text(text_pos, text, fill=t_color, font=font)

	
	#watermark.save("watermark.jpg")
	
	img.paste(watermark, None, watermark)

	return img

	
def main():
	font_file = "/usr/share/fonts/truetype/ttf-dejavu/DejaVuSans-Bold.ttf"
	font = select_font(font_file)

	text = "Varun Agrawal"

	#Transparency of Text
	trans = 120

	text_pos = (img.size[0]-170, img.size[1]-25)

	img = watermark(file, font, text, text_pos, trans)

	img.save("temp-wm.jpg")

if __name__ == "__main__":
	main()
