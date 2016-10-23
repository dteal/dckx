def transcriptParser(fileName):
	transcript = open(fileName, "r+")
	
	delete = ['[',']','{','}','.','\n','"',',']

	wordsToParse = transcript.read()
	for s in delete:
		wordsToParse = wordsToParse.replace(s, '')
	wordsToParse = wordsToParse.lower()
	
	transcript.seek(0)
	transcript.truncate(0)
	
	transcript.write(wordsToParse)
	transcript.close()