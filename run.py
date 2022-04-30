import os, json, random

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

def randomSlogan(data):
	categories = []
	for x in data:
		categories.append(x)
	category = random.choice(categories)
	return random.choice(data[category])


data = readJson(r'wisielec\base.json')


usedLetter = []
info = ''
heart = 10
guessWord = randomSlogan(data).upper()

while True:
	os.system('cls')
	design = printDesing(usedLetter, guessWord)
	info_used = f'Used letters: {usedLetter}\n'
	print(info_used)
	print(design)
	print('')
	print(info)

	keyadd = input('Type Letter: ').upper()
	
	if len(keyadd) == 1:
		
		usedLetter.append(keyadd)
		design = printDesing(usedLetter, guessWord)
		if not design.count('_') == 0: 
			print(design.count('_'))
			if heart != 0:
				if keyadd in guessWord:
					info = f'Great! The letter `{keyadd}` is in the word!\n'
					continue
				else:
					heart -= 1
					info = f'The letter `{keyadd}` is not in the word. Numbers of attempts left: {heart} '
					print(f'Number of attempts left: {heart}')
			else:
				print(f'You lose!\nGuessed word is `{guessWord}`')
				break
		else:
			print(f'You win!\nGuessed word is `{guessWord}`')
			break
	else:
		info = 'You can use one letter!'

