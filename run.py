slowo = 'test test'

new = ''
for x in slowo:
	if x == " ":
		new += "  "
	else:
		new += "_ "

print(new)

usedLetter = []

def printDesing(list, words):
	text = ''
	for x in words:
		if x in list:
			text += x + ' '
		else:
			if x == ' ':
				text += '  '
			else:
				text += '_ '
	return text

while True:
	keyadd = input('Letter?\n')
	usedLetter.append(keyadd)
	design = printDesing(usedLetter, slowo)
	print(design)
