import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag


ex = 'European authorities fined Google a record $5.1 \
	billion on Wednesday for abusing its power in the mobile \
phone market and ordered the company to alter its practices'

def preprocess(sentence):
	sentence = nltk.word_tokenize(sentence)
	sentence = nltk.pos_tag(sentence)
	return sentence


sentence = preprocess(ex)



#chunking of named phrases using a regex
#Named phrase : 0/1:(a/an) + any:adjectives + Noun
pattern = 'NP:{<DT>?<JJ>*<NN>}'


chunkparser = nltk.RegexpParser(pattern)
chunks = chunkparser.parse(sentence)
print(chunks)
