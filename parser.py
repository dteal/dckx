def transcriptParser(fileName):
	transcript = open(fileName, 'r')
	
	delete = ['[',']','{','}','.','?','!','\n','"',',', ':']
	wordsToParse = transcript.read()
	for s in delete:
		wordsToParse = wordsToParse.replace(s, '')
	wordsToParse = wordsToParse.lower()
	
	print(wordsToParse)
	
	transcript.close()
	output = open('new_' + fileName, 'w')
	
	output.write(wordsToParse)
	output.close()