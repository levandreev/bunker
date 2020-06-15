import Parser, random
from PIL import Image, ImageDraw, ImageFont
class Catastrophe(object):
	CatastropheFile = "Catastrophe.txt"
	Scenario = list()
	ScenCount = 7

	def __init__(self):
		super(Catastrophe, self).__init__()
	def Generate(self):
		mode ="["+ str(random.randint(1, self.ScenCount))+"]"
		self.Scenario = Parser.Parse(mode, self.CatastropheFile)
		self.CreateImage()

	def CreateImage(self):
		max_w, max_h = 0, 0
		text_size = 20
		img = Image.new('RGB', (100, 100))
		font = ImageFont.truetype("arial.ttf", text_size)
		draw = ImageDraw.Draw(img)
		for lines in self.Scenario:
			lines = lines.encode('utf-8')
			wd, hd = draw.textsize(lines)
			if max_w < wd: max_w = wd
			if max_h < hd: max_h = hd
		print(max_w)
		print(max_h)
		img = Image.new('RGB', (max_w+100, 150), (255,255,255))
		draw = ImageDraw.Draw(img)

		offset = 10
		print(self.Scenario)
		for line in self.Scenario:
			draw.text((10, offset), str(line), font=font, fill=(0, 0, 0, 255))
			offset += 30
		img.save('Catastrophe.png', "png")
