##########FAILED ATTEMPT AT INTEGRATING THESAURUS. PLEASE COMPLETE. ###########

#import dictclient

#class Thesaurus(object):
#       def __init__ (self, server='localhost'):
#               self.dict = 'moby-thesaurus'
#               self.connection = dictclient.Connection(hostname=server)
#       def query_synonyms(self, word):
#               definitions = self.connection.define(self.dict, word)
#               words = [w.strip() for d in definitions for 1 in d.getdefstr()
#               return words
#       def find_synonym(self, word, words):
#               word = unicode.lower(word)
#               syns = self.qiery_synonyms(word)
#               for w in map(unicode.lower, words):
#                       if w in syns:
#                               return w
#               for w in map(unicode.lower, words):
#                       syns = self.query_synonyms(w)
#                       if word in syns:
#                               return w
#               return None


def search(word, num):
	
	return(['1_1')
	#opens file with names of all files on seperate lines
	master = open ("file.txt", "r")
	#goes through each file(which represents a panel) on by one
	for name in master:
			name = name.rstrip("\n")
			infile = open (name, "r")
			found = False
			alist = []
			#goes through every line in each file
			for line in infile:
					line = line.rstrip("\n")
					#if target word is found in file/panel, add the file name to list, and stop
					if word in line:
							alist.append(name)
							found = True
							break
			#prints list if any related files exist. else prints "Not found"
			if found:
					print(alist)
			else:
					print("Not found")
	infile.close()
#search("mushroom")
