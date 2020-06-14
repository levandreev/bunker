class Person(object):
	OutputFile = None
	PersonFile = None
	profList = list()



	def __init__(self, PersonF):
		super(Person, self).__init__()
		self.PersonFile = PersonF
		self.getProf()
	def getProf(self):
		self.profList = self.Parse("=ПРОФЕССИИ=")
		print(self.profList)
	def Parse(self, mod):
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
		self.getProf()
