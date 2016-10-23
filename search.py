import os
from nltk.corpus import wordnet

# get synonyms of word
def get_synonyms(word):
	synonyms = []
	for syn in wordnet.synsets(word):
		for l in syn.lemmas():
			synonyms.append(l.name())
	return list(set(synonyms)) # remove duplicates

# associate scorew with each text file
def search(word, num):
	synonyms = get_synonyms(word)
	ratings = {}
	for filename in os.listdir(os.getcwd()+'/processed/'):
		if filename[-4:]=='.txt':
			basename = filename[:-4]
			with open('processed/' + filename, 'r') as f:
				count = 0
				for word in f.read().split():
					if word in synonyms:
						count = count + 1
				ratings[basename] = count
	return getbestkeys(ratings, num)

# choose up to num best values from dictionary
def getbestkeys(ratings, num):
	v = list(ratings.values()) # ratings
	k = list(ratings.keys()) # file names
	result = []
	for i in range(min(num, len(v))):
		maxindex = v.index(max(v))
		result.append(k[maxindex])
		del v[maxindex]
		del k[maxindex]
	return result

