class Person(object):
	OutputFile = None
	PersonFile = None
	profList = list()



	def __init__(self, PersonF):
		super(Person, self).__init__()
		self.PersonFile = PersonF
	def getProf(self):
		self.Parse("=ПРОФЕССИИ=")
	def Parse(self, mod):
		FirstEntry = False
		for lineNum, Line in enumerate(self.PersonFile, 1):
			if str(mod) in Line and FirstEntry == False:
				FirstEntry = True
			elif str(mod) in Line and FirstEntry == True:
				break
			if FirstEntry == True:
				self.profList.append(Line)
		print(self.profList)

	def Generate(self):
		self.getProf()
