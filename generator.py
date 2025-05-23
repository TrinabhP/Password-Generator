from generatorFuncs import *


def main():

	if (check_password()):
		print("Your password is strong!")

	else:
		print("Your password is weak!")

	change_password = input("\nDo you want to change your password?(y/n) ")
	if (change_password == 'y'):
		length = int(input("\nHow long do you want your password to be?\nEnter a number: "))

		# makes sure password length is greater than 13
		while (length < 14):
			print("\nA strong passcode requires more than 13 characters!")
			length = int(input("\nHow long do you want your password to be?\nEnter a number: "))

		symbols = input("\nDo you want symbols in your password?(y/n) ")
		if (symbols == 'y' or symbols == 'Y'):
			symbols = True

		else:
			symbols = False

		uppercase = input("\nDo you want uppercase letters in your password?(y/n) ")
		if (uppercase == 'y' or uppercase == 'Y'):
			uppercase = True

		else:
			uppercase = False

		digits = input("\nDo you want numbers in your password?(y/n) ")
		if (digits == 'y' or digits == 'Y'):
			digits = True

		else:
			digits = False

		password = generate(length, symbols, uppercase, digits)

		print("\n----------------------------------------\n")

		print("\nYour new password is: " + password + "\nMake sure to save it!\n")

	else:
		print("\n----------------------------------------\n")


if __name__ == '__main__':
	main()