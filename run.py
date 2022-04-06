slowo = 'test test'
new = ''

for x in slowo:
	if x == " ":
		new += "  "
	else:
		new += "_ "

print(new)