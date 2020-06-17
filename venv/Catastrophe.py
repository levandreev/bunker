import Parser, random
from PIL import Image, ImageDraw, ImageFont
class Catastrophe(object):
	CatastropheFile = "Catastrophe.txt"
	BunkerFile = "Bunker.txt"
	Scenario = list()
	Bunker = {"ТОПОГРАФИЯ": "", "ОБОРУДОВАНИЕ": "", "УСТРОЙСТВО": "", "РАЗМЕР": "", "ЗАПАС": ""}
	ScenCount = 7

	def __init__(self):
		super(Catastrophe, self).__init__()
	def Generate(self):
		mode ="["+ str(random.randint(1, self.ScenCount))+"]"
		self.Scenario = Parser.Parse(mode, self.CatastropheFile)
		self.GenerateBunker()
		self.CreateImage()

	def GenerateBunker(self):
		self.Bunker["ТОПОГРАФИЯ"] =  "{}.".format(random.choice(Parser.Parse("=ТОПОГРАФИЯ=", self.BunkerFile)))
		self.Bunker["ОБОРУДОВАНИЕ"] = "В бункере есть: {}.".format(random.choice(Parser.Parse("=ОБОРУДОВАНИЕ=", self.BunkerFile)))
		self.Bunker["УСТРОЙСТВО"] = "Особенности бункера: {}.".format(random.choice(Parser.Parse("=УСТРОЙСТВО=", self.BunkerFile)))
		self.Bunker["РАЗМЕР"] = "Размер бункера: {} кв. м. ".format(random.randint(150, 600))
		self.Bunker["ЗАПАС"] = "Запасов хватит на: {} месяцев.".format(random.randint(4, 60))
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
		img = Image.new('RGB', (max_w+100, 350), (255,255,255))
		draw = ImageDraw.Draw(img)
		offset = 10
		for line in self.Scenario:
			draw.text((10, offset), str(line), font=font, fill=(0, 0, 0, 255))
			offset += 30
		for line in self.Bunker:
			draw.text((10, offset), str(self.Bunker[line]), font=font, fill=(0, 0, 0, 255))
			offset += 30
		img.save('Catastrophe.png', "png")
