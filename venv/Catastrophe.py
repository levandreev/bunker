import Parser, random
from PIL import Image, ImageDraw, ImageFont
class Catastrophe(object):
	CatastropheFile = "Catastrophe.txt"
	Scenario = ""
	ScenCount = 7

	def __init__(self):
		super(Catastrophe, self).__init__()
	def Generate(self):
		mode ="["+ str(random.randint(1, self.ScenCount))+"]"
		self.Scenario = str(Parser.Parse(mode, self.CatastropheFile)[0])
		self.CreateImage()
	def CreateImage(self):
		img = Image.new('RGB', (1000,500))
		draw = ImageDraw.Draw(img)
		font = ImageFont.truetype("arial.ttf", 25, encoding='utf-8')
		draw.text((10, 10), str(self.Scenario), font=font)
		img.save('Catastrophe.png', "png")
