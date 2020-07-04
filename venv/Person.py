import Parser, random
class Character(object):
	OutputFile = None
	CharacterFile = "Character.txt"
	profList = list()
	hobbyList = list()
	traitList = list()
	healthList = list()
	phobiaList = list()
	bagageList = list()
	addInfoList = list()
	actionCardsList = list()

	def __init__(self):
		super(Character, self).__init__()
		self.getProf()
		self.getHobby()
		self.getTrait()
		self.getHealth()
		self.getPhobia()
		self.getBagage()
		self.getAddInfo()
		self.getActionCards()

	def getProf(self):
		self.profList = Parser.Parse("=ПРОФЕССИИ=", self.CharacterFile)
	def getHobby(self):
		self.hobbyList = Parser.Parse("=ХОББИ=", self.CharacterFile)
	def getTrait(self):
		self.traitList = Parser.Parse("=ЧЕРТЫ=", self.CharacterFile)
	def getHealth(self):
		self.healthList = Parser.Parse("=ЗДОРОВЬЕ=", self.CharacterFile)
	def getPhobia(self):
		self.phobiaList = Parser.Parse("=ФОБИИ=", self.CharacterFile)
	def getBagage(self):
		self.bagageList = Parser.Parse("=БАГАЖ=", self.CharacterFile)
	def getAddInfo(self):
		self.addInfoList = Parser.Parse("=ДОП.ИНФО=", self.CharacterFile)
	def getActionCards(self):
		self.actionCardsList = Parser.Parse("=КАРТЫ ДЕЙСТВИЙ=", self.CharacterFile)

	def CorrectAge(self, Age):
		Q = Age % 10
		if (Q > 9) and (Age < 20) or (Age > 110) or (Q > 4) or (Q==0):
			return (str(Age) + " лет")
		else:
			if Q == 1: return (str(Age) + " год")
			else:
				return (str(Age) + " года")
	def Bragging(self, mode):
		str = ""
		if mode:
			brag = random.randint(0,100)
			if brag >= 90:
				str = "[Хвастовство]"
		return str
	def Generate(self, custom_bragging):
		# Пол, возраст, ориентация [Готово]
		# Профессия [Готово]
		# Состояние здоровья [Готово]
		# Телосложение [Не используется]
		# Человеческая черта [Готово]
		# Хобби [Готово]
		# Фобия [Готово]
		# Багаж [Готово]
		# Доп. информация [Готово]
		# Карты действия [Готово]
		Sex = {1: "Мужчина", 2:"Женщина"}
		Orientation = {1: "гетеро", 2: "би", 3: "гомо"}
		Age = random.randint(16, 100)
		self.OutputFile.writelines("{}, {}, ориентация: {} {}\n".format(Sex[random.randint(1,2)], self.CorrectAge(Age), Orientation[random.randint(1,3)], self.Bragging(custom_bragging)))
		self.OutputFile.writelines("Профессия: {}\n".format(random.choice(self.profList)))
		self.OutputFile.writelines("Состояние здоровья: {} {}\n".format(random.choice(self.healthList), self.Bragging(custom_bragging)))
		self.OutputFile.writelines("Человеческая черта: {} {}\n".format(random.choice(self.traitList), self.Bragging(custom_bragging)))
		self.OutputFile.writelines("Хобби: {} {}\n".format(random.choice(self.hobbyList), self.Bragging(custom_bragging)))
		self.OutputFile.writelines("Фобия: {} {}\n".format(random.choice(self.phobiaList), self.Bragging(custom_bragging)))
		self.OutputFile.writelines("Багаж: {} {}\n".format(random.choice(self.bagageList), self.Bragging(custom_bragging)))
		self.OutputFile.writelines("Доп. информация: {} {}\n".format(random.choice(self.addInfoList),  self.Bragging(custom_bragging)))
		self.OutputFile.writelines("Карты действий:\n1 - {}\n2 - {}\n".format(random.choice(self.actionCardsList), random.choice(self.actionCardsList)))
		self.OutputFile.close()
