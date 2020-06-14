import random
class Person(object):
	OutputFile = None
	PersonFile = None
	profList = list()
	hobbyList = list()
	traitList = list()



	def __init__(self, PersonF):
		super(Person, self).__init__()
		self.PersonFile = PersonF
		self.getProf()
		self.getHobby()
		self.getTrait()

	def getProf(self):
		self.profList = self.Parse("=ПРОФЕССИИ=")
		print(self.profList)
	def getHobby(self):
		self.hobbyList = self.Parse("=ХОББИ=")
		print(self.hobbyList)
	def getTrait(self):
		self.traitList = self.Parse("=ЧЕРТЫ=")
		print(self.traitList)
	def Parse(self, mod):
		self.PersonFile.seek(0)
		result = list()
		FirstEntry = False
		for lineNum, Line in enumerate(self.PersonFile, 1):
			if str(mod) in Line and FirstEntry == False:
				FirstEntry = True
				continue
			elif str(mod) in Line and FirstEntry == True:
				break
			if FirstEntry == True:
				result.append(Line.strip())
		return result

	def Generate(self):
		# Пол, возраст, ориентация
		# Профессия
		#
		Sex = random.randint(1, 100)
		if Sex < 60:
			Sex = "мужчина"
		else:
			Sex = "женщина"
		Age = random.randint(16, 100)
		Orientation = random.randint(1, 100)
		if Orientation < 60:
			Orientation = "гетеро"
		else:
			Orientation = "гомо"
		self.OutputFile.writelines("Пол: {}, возраст: {}, ориентация: {}\n".format(Sex, str(Age), Orientation))
		self.OutputFile.writelines("Профессия: {}".format(self.profList.pop(random.randint(0,len(self.profList)))))
		self.OutputFile.close()
