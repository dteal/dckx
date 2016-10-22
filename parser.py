def transcriptParser(fileName):
	transcript = open(fileName, "r+") 

	wordsToParse = transcript.read()
	wordsToParse = wordsToParse.replace('.', '')
	wordsToParse = wordsToParse.replace('\n', ' ')
	wordsToParse = wordsToParse.replace('"', '')
	wordsToParse = wordsToParse.replace(',', '')
	wordsToParse = wordsToParse.lower()
	
	transcript.seek(0)
	transcript.truncate(0)
	
	transcript.write(wordsToParse)
	transcript.close()

from sys import argv

script, filename = argv

transcriptParser(filename)