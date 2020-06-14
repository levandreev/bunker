# -*- coding: utf-8 -*-
import os, time, Person

class Generator(object):
	Character = None
	ActionCards = None
	Bunker = None
	Catastrophe = None
	def __init__(self):
		super(Generator, self).__init__()

	def FileApp(self):
		self.Character = open("Character.txt", "r")
		self.ActionCards = open("ActionCards.txt", "r")
		self.Bunker = open("Bunker.txt", "r")
		self.Catastrophe = open("Catastrophe.txt", "r")
	def GeneratePerson(Num):
		for NewPerson in range(Num):
			NewPersonFile = open(str(NewPerson), "w")
			NewPersonInst = Person()
			NewPersonInst.Generate()
			NewPersonFile.close()

def main():
	GeneratorInst = Generator()
	GeneratorInst.FileApp()

if __name__ == '__main__':
	main()
