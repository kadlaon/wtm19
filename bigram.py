import re
import math
from unigram import unigram_frequencies

# sentence start and end
SENTENCE_START = "<s>"
SENTENCE_END = "</s>"
bigram_frequencies = dict()
bigram_word_probabilities = dict()

def read_sentences_from_file(file_path):
    with open(file_path, "r") as f:
        return [re.split("\s+", line.rstrip('\n')) for line in f]

def Bigram(sentences):
	
	unique_bigrams = set()
	for sentence in sentences:
		previous_word = None
		for word in sentence:
			if previous_word != None:
				bigram_frequencies[(previous_word, word)] = bigram_frequencies.get((previous_word, word),0) + 1
			if previous_word != SENTENCE_START and word != SENTENCE_END:
				unique_bigrams.add((previous_word, word))
			previous_word = word
	#unique__bigram_words = len(unigram_frequencies)
	return unique_bigrams, unique__bigram_words, bigram_frequencies, unigram_frequencies

def compute_bigram_probabilities(previous_word, word):
	bigram_word_probability_numerator = bigram_frequencies.get((previous_word, word), 0)
	bigram_word_probability_denominator = unigram_frequencies.get(previous_word, 0)

	return 0.0 if bigram_word_probability_numerator == 0 or bigram_word_probability_denominator == 0 else float(
            bigram_word_probability_numerator) / float(bigram_word_probability_denominator)

def main():
	toy_dataset = read_sentences_from_file("./sampledata.txt")
	toy_dataset_test = read_sentences_from_file("./sampletest.txt")

	print("==============Bigram===============================")
	a,b,c,d = Bigram(toy_dataset_test)
	print("Unique Bigrams;",a)
	print("Bigram Frequencies:",c)
	print(d)		
	for sentence in toy_dataset_test:
		previous_word = None
		for word in sentence:
			if previous_word != None:
				bi_prob = compute_bigram_probabilities(previous_word, word)
				bigram_word_probabilities[(previous_word, word)] = bigram_word_probabilities.get((previous_word, word),bi_prob)
			previous_word = word

	for key,val in bigram_word_probabilities.items():
		print(key,val)
	
	
main()   
