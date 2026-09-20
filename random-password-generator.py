import sys


if sys.path and sys.path[0].lower() == __file__.rsplit("\\", 1)[0].lower():
	sys.path.pop(0)

import secrets
import string


def generate_password(length, use_uppercase=True, use_digits=True, use_symbols=True):
	"""Generate a cryptographically secure random password."""
	character_sets = [string.ascii_lowercase]

	if use_uppercase:
		character_sets.append(string.ascii_uppercase)
	if use_digits:
		character_sets.append(string.digits)
	if use_symbols:
		character_sets.append(string.punctuation)

	if length < len(character_sets):
		raise ValueError(
			f"Password length must be at least {len(character_sets)} characters."
		)

	password_characters = [secrets.choice(characters) for characters in character_sets]
	all_characters = "".join(character_sets)
	password_characters.extend(
		secrets.choice(all_characters) for _ in range(length - len(password_characters))
	)
	secrets.SystemRandom().shuffle(password_characters)
	return "".join(password_characters)


def main():
	print("Random Password Generator")

	try:
		length = int(input("Password length (minimum 4): "))
		if length < 4:
			raise ValueError
	except ValueError:
		print("Please enter a whole number of at least 4.")
		return

	password = generate_password(length)
	print(f"Generated password: {password}")


if __name__ == "__main__":
	main()
