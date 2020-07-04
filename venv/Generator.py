# -*- coding: UTF-8 -*-
import os, sys, time
import Person as Pers
import Catastrophe as Catas
from PyQt5 import QtWidgets
import gui

class GeneratorGUI(QtWidgets.QMainWindow, gui.Ui_MainWindow):
	Generator = None
	custom = False
	custom_catastrophe = False
	custom_bragging = False
	def __init__(self, arg):
		super (GeneratorGUI, self).__init__()
		self.setupUi(self)
		self.checkBox.stateChanged.connect(self.ch_bragging)
		self.checkBox_2.stateChanged.connect(self.ch_catastrophe)
		self.pushButton.clicked.connect(self.generate)
		self.Generator = arg
	def ch_catastrophe(self):
		if self.checkBox_2.isChecked():
			self.custom_catastrophe = True
		else:
			self.custom_catastrophe = False
	def ch_bragging(self):
		if self.checkBox.isChecked():
			self.custom_bragging = True
		else:
			self.custom_bragging = False
	def generate(self):
		self.Generator.FileApp()
		self.Generator.GenerateCharacter(self.spinBox.value(), self.custom_bragging)
		self.Generator.GenerateCatastrophe(self.custom_catastrophe)

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
	def GenerateCharacter(self,	Num, custom_bragging):
		for NewCharacterNum in range(1, Num+1):
			NewCharacter = Pers.Character()
			NewCharacter.OutputFile = open(str(NewCharacterNum)+".txt", "w+", encoding='utf-8')
			NewCharacter.Generate(custom_bragging)
	def GenerateCatastrophe(self, custom_catastrophe):
		Cat = Catas.Catastrophe()
		Cat.Generate(custom_catastrophe)

def main():
	GeneratorInst = Generator()
	app = QtWidgets.QApplication(sys.argv)
	window = GeneratorGUI(GeneratorInst)
	window.show()
	app.exec()

if __name__ == '__main__':
	main()
