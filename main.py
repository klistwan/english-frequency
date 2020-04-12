import sys

if __name__ == '__main__':
	f = open(sys.argv[1])
	for potential_segment in f.read().split('\n\n'):
		content = " ".join(potential_segment.split('\n')[2:]).strip().lower()
		for punctuation in ["!", "?", ".", ",", "-"]:
			content = content.replace(punctuation, "")
		for word in content.split():
			if word.isalpha():
				print(word)