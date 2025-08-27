def word_count(text):
	words = text.split()
	num_words = len(words)
	return num_words
def character_count(text):
	num_characters = {}
	text = text.lower()
	for letter in text:
		if letter in num_characters:
			num_characters[letter] += 1
		else:
			num_characters[letter] = 1
	return num_characters
def sort_characters(dictionary):
	list_of_characters = []
	for character in dictionary:
		list_of_characters.append({"character": character, "num": dictionary[character]})
	def get_count(list):
		return list['num']
	list_of_characters.sort(reverse=True, key=get_count)
	return list_of_characters