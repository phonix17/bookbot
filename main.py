from stats import word_count, character_count, sort_characters
import sys
def get_book_text(book_path):
	with open(book_path) as f:
		book_contents = f.read()
	return book_contents
def main():
	try:
		num_words = word_count(get_book_text(sys.argv[1]))
		count_of_characters = character_count(get_book_text(sys.argv[1]))
		sorted_list = sort_characters(count_of_characters)
		sorted_characters = {}
		for item in sorted_list:
			if item['character'].isalpha():
				sorted_characters[item['character']] = item['num']
		print("============ BOOKBOT ============")
		print(f"Analyzing book found at {sys.argv[1]}...")
		print("----------- Word Count ---------")
		print(f"Found {num_words} total words")
		print("--------- Character Count -------")
		for key in sorted_characters:
			print(f"{key}: {sorted_characters[key]}")
		print("============= END ===============")
	except:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)



	
main()