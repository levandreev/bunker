import random
def Parse(mod, filename):
	file = open(filename, "r", encoding="utf-8")
	file.seek(0)
	result = list()
	FirstEntry = False
	for lineNum, Line in enumerate(file, 1):
		if str(mod) in Line and FirstEntry == False:
			FirstEntry = True
			continue
		elif str(mod) in Line and FirstEntry == True:
			break
		if FirstEntry == True:
			result.append(Line.strip())
	file.close()
	return result
