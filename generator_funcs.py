import random
import string

def check_password():
	user_pass = input("What is your current passcode? ")

	if (len(user_pass) < 14):
		return False

	return True


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
		password.append(characters[random.randint(0, len(characters))])

	return "".join(password)





