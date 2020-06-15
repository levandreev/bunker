# -*- coding: UTF-8 -*-
import os, time
import Person as Pers
import Catastrophe as Catas

class Generator(object):
	Character = None
	ActionCards = None
	Bunker = None
	Catastrophe = None
	def __init__(self):
		super(Generator, self).__init__()

	def FileApp(self):
		self.Character = open("Character.txt", "r", encoding='utf-8')
		self.Bunker = open("Bunker.txt", "r", encoding='utf-8')
		self.Catastrophe = open("Catastrophe.txt", "r", encoding='utf-8')
	def GenerateCharacter(self,	Num):
		for NewCharacterNum in range(1, Num+1):
			NewCharacter = Pers.Character()
			NewCharacter.OutputFile = open(str(NewCharacterNum)+".txt", "w", encoding='utf-8')
			NewCharacter.Generate()
	def GenerateChatastrophe(self):
		Cat = Catas.Catastrophe()
		Cat.Generate()

def main():
	GeneratorInst = Generator()
	GeneratorInst.FileApp()
	GeneratorInst.GenerateCharacter(5)
	GeneratorInst.GenerateChatastrophe()

if __name__ == '__main__':
	main()
