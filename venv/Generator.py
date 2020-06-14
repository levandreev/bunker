# -*- coding: UTF-8 -*-
import os, time
import Person as Pers

class Generator(object):
	Character = None
	ActionCards = None
	Bunker = None
	Catastrophe = None
	def __init__(self):
		super(Generator, self).__init__()

	def FileApp(self):
		self.Character = open("Character.txt", "r", encoding='utf-8')
		self.ActionCards = open("ActionCards.txt", "r", encoding='utf-8')
		self.Bunker = open("Bunker.txt", "r", encoding='utf-8')
		self.Catastrophe = open("Catastrophe.txt", "r", encoding='utf-8')
	def GenerateCharacter(self,	Num):
		for NewCharacter in range(Num):
			NewPerson = Pers.Person(self.Character)
			#NewPerson.OutputFile = open(str(Num)+".txt", "w", encoding='utf-8')
			NewPerson.Generate()

def main():
	GeneratorInst = Generator()
	GeneratorInst.FileApp()
	GeneratorInst.GenerateCharacter(1)

if __name__ == '__main__':
	main()
