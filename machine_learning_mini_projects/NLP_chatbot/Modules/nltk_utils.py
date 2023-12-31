
import nltk
from nltk.stem.porter import PorterStemmer
import numpy as np

#so nltk.word_tokenize() works 
# nltk.download("punkt") 

stemmer = PorterStemmer()

def tokenize(sentence):
    return nltk.word_tokenize(sentence)

def stem(word):
    return stemmer.stem(word.lower())

def bag_of_words(tokenized_sentence, all_words):
    tokenized_sentence = [stem(w) for w in tokenized_sentence]
    bag = np.zeros(len(all_words), dtype=np.float32)
    for idx,word in enumerate(all_words):
        if word in tokenized_sentence:
            bag[idx] = 1.0
            
    return bag
    
        
