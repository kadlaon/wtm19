import re
import math

# sentence start and end
sentence_start = "<s>"
sentence_end = "</s>"
unigram_frequencies = dict()
word_probabilities = dict()

def read_sentences_from_file(file_path):
    with open(file_path, "r") as f:
        return [re.split("\s+", line.rstrip('\n')) for line in f]

def Unigram(sentences):
	corpus_length = 0
	for sentence in sentences:
		for word in sentence:
			unigram_frequencies[word] = unigram_frequencies.get(word,0) + 1
			if word != sentence_start and word != sentence_end:
				corpus_length += 1
	unique_words = len(unigram_frequencies) - 2

	return unigram_frequencies, unique_words, corpus_length, word_probabilities

def compute_unigram_probabilities(word, corpus_len):
	word_probability_numerator = unigram_frequencies.get(word,0)
	word_probability_denominator = corpus_len 
	return float(word_probability_numerator) / float(word_probability_denominator)

def main():
	data = read_sentences_from_file("./data.txt")
	test_data = read_sentences_from_file("./test_data.txt")

	print(toy_dataset)
	print(toy_dataset_test)
	print("==============Unigram===============================")
	a,b,c,d = Unigram(toy_dataset_test)
	print("Unigram Frequencies:",a)
	print("Unique Words:",b)
	print("corpus_length:",c)
	for sentence in toy_dataset_test:
		for word in sentence:
			if word != sentence_start and word != sentence_end:
				uni_prob = compute_unigram_probabilities(word,c)
				word_probabilities[word] = word_probabilities.get(word, uni_prob)

	print(word_probabilities)		

main()   
