import sys


# For each word, check if in {form: lemma}
# If not, note it.

def get_lemma_corpus():
	corpus = {}   # {form: lemma}
	lemmas = []
	for line in open("corpus/NGSL+1.01+by+band.csv").readlines():
		lemma = line.split(',')[0]
		freq = line.split(',')[1]
		for form in line.split(',')[2:]:
			if not form:
				break
			corpus[form] = lemma
		lemmas += [lemma]
	return lemmas, corpus


if __name__ == '__main__':
	f = open(sys.argv[1])
	lemmas, corpus = get_lemma_corpus()
	freq = {}  # {lemma: freq}
	for potential_segment in f.read().split('\n\n'):
		content = " ".join(potential_segment.split('\n')[2:]).strip().lower()
		for punctuation in ["!", "?", ".", ",", "-"]:
			content = content.replace(punctuation, "")
		content = content.replace("'", " ")
		for word in content.split():
			if word.isalpha():
				if word in corpus:  # Means it's a non-dictionary form.
					freq[corpus[word]] = freq.get(corpus[word], 0) + 1
				elif word in lemmas: # Means it's dictionary form.
					freq[word] = freq.get(word, 0) + 1
				else:   # Means it's a word we don't have lemma data on.
					print(word, content)
	# Show all lemmas appear in the movie, in order of general frequency, listed with their frequency in the movie.
	for lemma in lemmas:
		if lemma in freq:
			print(freq[lemma], "\t", lemma)
	import pdb; pdb.set_trace()
