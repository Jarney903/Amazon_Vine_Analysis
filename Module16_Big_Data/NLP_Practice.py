import nltk
from nltk import word_tokenize
# When researching or practicing NLP, 
# you'll often hear of part-of-speech tagging (PoS), 
# which can be helpful for a variety of different models in NLP. 
# PoS tagging is the concept of finding each word's part of speech in a given document,
# as the example below illustrates

# Word	    PoS and Tags
# I	        Personal pronoun (PRP)
# enjoy	    Verb, non-third person (VBP)
# biking	Verb, gerund, present participle (VBG)
# on	    Preposition or subordinating conjunction (IN)
# the	    Determiner (DT)
# trails	Noun, plural (NNS)

text = word_tokenize("I enjoy biking on the trails")
output = nltk.pos_tag(text)
print(output)