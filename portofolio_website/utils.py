import numpy as np

import nltk
# nltk.download("punkt")
from nltk.stem.porter import PorterStemmer

stemmer = PorterStemmer()

# Tokenizer = split sentence into array of words/tokens a token can be a word or punctuation character, or number
def tokenize(sentence):
    return nltk.word_tokenize(sentence)


# Stemming = find the root form of the word (["organize", "organizes", "organizing"]) -> ["organ", "organ", "organ"]
def stem(word):
    return stemmer.stem(word.lower())


# Bag of words = 1 for each known word that exists in the sentence, 0 otherwise
def bag_of_words(pattern_sentence, all_words):
    # Stem each word
    sentence_words = [stem(word) for word in pattern_sentence]
    # Initialize bag with 0 for each word
    bag = np.zeros(len(all_words), dtype=np.float32)
    for idx, w in enumerate(all_words):
        if w in sentence_words: 
            bag[idx] = 1

    return bag