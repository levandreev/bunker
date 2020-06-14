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
	def GenerateCharacter(Num):
		for NewCharacter in range(Num):
			NewPerson = Person(Character)
			NewPerson.Output = open(str(Num)+".txt", "w")
			NewPerson.Generate()

def main():
	GeneratorInst = Generator()
	GeneratorInst.FileApp()
	GenratorInst.GenerateCharacter(2)

if __name__ == '__main__':
	main()
