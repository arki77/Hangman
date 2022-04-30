import os, json

slowo = 'test test'


usedLetter = []
info = ''
heart = 10

def readJson(filename):
	with open(filename) as json_file:
		data = json.load(json_file)
	return data

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
	data = readJson(r'wisielec\base.json')
	print(data)
	# os.system('cls')
	design = printDesing(usedLetter, slowo)
	info_used = f'Used letters: {usedLetter}\n'
	print(info_used)
	print(design)
	print('')
	print(info)


	keyadd = input('Type Letter: ')
	usedLetter.append(keyadd)
	design = printDesing(usedLetter, slowo)
	if not design.count('_') == 0: 
		print(design.count('_'))
		if heart != 0:
			if keyadd in slowo:
				info = f'Great! The letter `{keyadd}` is in the word!\n'
				continue
			else:
				heart -= 1
				info = f'The letter `{keyadd}` is not in the word. Numbers of attempts left: {heart} '
				print(f'Number of attempts left: {heart}')
		else:
			print(f'You lose!\nGuessed word is `{slowo}`')
			break
	else:
		print(f'You win!\nGuessed word is `{slowo}`')
		break

