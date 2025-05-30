import random
import string

def check_password():
	user_pass = input("What is your current passcode? ")

	if (len(user_pass) < 14):
		return False

	symbol = False
	digits = False
	letters = False

	for c in user_pass:
		if (c in string.digits):
			digits = True
		elif (c in string.punctuation):
			symbol = True
		else:
			letters = True

	if (symbol and digits and letters):
		return True

	else:
		return False

def generate(length, symbols=False, uppercase=False, digits=False):
	password = []
	characters = []
	characters.append(string.ascii_lowercase)

	if (uppercase):
		characters.append(string.ascii_uppercase)
	if digits:
		characters.append(string.digits)
	if symbols:
		characters.append(string.punctuation)

	for i in range(length):
		characters = "".join(characters)
		password.append(characters[random.randint(0, len(characters) - 1)])

	return "".join(password)





