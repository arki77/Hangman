import os, json, random, time

def readJson(filename):
	with open(filename) as json_file:
		data = json.load(json_file)
	return data

def saveJson(filename, data):
	with open(filename, 'w') as f:
		json.dump(data, f)

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
	return random.choice(data[category]).upper(), category

data = readJson(r'wisielec\base.json')


usedLetter = []
info = ''
heart = 10

GameStatus, settings = False, False

while True:
	settings_file = readJson(r'wisielec\settings.json')
	os.system('cls')
	print('Hey, in hangman game! \n[1] Roll random Slogan\n[2] Settings\n[3] Exit')
	choice = input('..')
	if choice == '1':
		guessWord, category = randomSlogan(data)
		os.system('cls')
		print('Random slogan rolling...')
		time.sleep(1)
		heart = settings_file["tries"]
		GameStatus = True
	elif choice == '2':
		settings = True
		while settings:
			os.system('cls')
			print('SETTINGS MENU')
			print(f'[1] * Number of tries: [{settings_file["tries"]}]')
			print('[2] * Save & Exit')
			choiceSettings = input('..')
			if choiceSettings == '1':
				print('What number of tries do you want?')
				choiceInput = int(input('..'))
				settings_file["tries"] = choiceInput
			elif choiceSettings == '2':
				saveJson(r'wisielec\settings.json', settings_file)
				settings = False
				os.system('cls')
				print('Config Settings Saveing...')
				time.sleep(1)
			else:
				print('KeyError.. Type [1-2]')


	elif choice == '3':
		break
	else:
		print('KeyError.. Type [1-2]')
	while GameStatus:
		os.system('cls')
		design = printDesing(usedLetter, guessWord)
		info_used = f'Used letters: {usedLetter}\n'
		print(info_used)
		print(f'Category: {category}')
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
					input('')
					GameStatus = False
					usedLetter = []
					info = ''
			else:
				os.system('cls')
				print(f'Congrats You WIN!\nGuessed word is `{guessWord}`')
				input('')
				GameStatus = False
				usedLetter = []
				info = ''
		else:
			info = 'You can use one letter!'

