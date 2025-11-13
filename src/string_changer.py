def concatenate_strings_with_space(str1, str2):
	"""
	Concatenates two strings with a space in between.

	Args:
		str1 (str): The first string.
		str2 (str): The second string.

	Returns:
		str: The concatenated string with a space in between.
	"""
	return f"{str1} {str2}"

def string_has_pattern(str, pattern):
	"""
	Checks if the given string contains the specified pattern.

	Args:
		str (str): The string to check.
		pattern (str): The pattern to look for.
	Returns:
		bool: True if the pattern is found in the string, False otherwise.
	"""
	return pattern in str

def string_is_rich(str):
	"""
	Checks if a string has at least 1 space, 1 special character, 1 uppercase letter, and 1 digit.

	Args:
		str (str): The string to check.

	Returns:
		bool: True if the string meets the criteria, False otherwise.
	"""
	has_space = any(char.isspace() for char in str)
	has_special = any(not char.isalnum() for char in str)
	has_uppercase = any(char.isupper() for char in str)
	has_digit = any(char.isdigit() for char in str)

	return has_space and has_special and has_uppercase and has_digit

def insert_pattern_at_index(str, pattern, index):
	"""
	Inserts a pattern into a string at the specified index.

	Args:
		str (str): The original string.
		pattern (str): The pattern to insert.
		index (int): The index at which to insert the pattern.

	Returns:
		str: The modified string with the pattern inserted.
	"""
	return str[:index] + pattern + str[index:]