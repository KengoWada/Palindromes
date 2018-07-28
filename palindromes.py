import re # Import regular expressions

# win = input('Enter text:')


def palindrome(word):

	word1 = word + ' \n'

	data = open('data.txt', 'a') # Opens data.txt for writing
	data.write(word1) # Writes to the text file 
	data.close() # Then closes the file

	word = re.sub(r'[^a-z\d ]','',str.lower(word)) # Removes all characters that are not in the alphabet and makes the input lowercase
	word = word.replace(' ', '')
	word_rev = reversed(word)

	if list(word) == list(word_rev):
		return 'True, is palindrome.'
	else:
		return 'False, isn\'t palindrome.'



# print(palindrome(win))