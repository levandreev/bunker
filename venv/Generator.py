import os, time

class Generator(object):
	def __init__(self, arg):
		super(Generator, self).__init__()
		self.arg = arg

	def FileApp(self):
		Character = open("Character.txt", "w")
		ActionCards = open("ActionCards.txt", "w")
		Bunker = open("Bunker.txt", "w")
		Catastrophe = open("Catastrophe.txt", "w")

def main():
	Generator = Generator()
	Generator.FileApp()
