import os
def transcriptParser(fileName):
	transcript = open(fileName, 'r')
	
	wordsToParse = transcript.read()
	
	delete = ['[',']','{','}','.','?','!','"',',', ':', '\\', ' -', '(', ')']
	wordsToParse = wordsToParse.replace('\\n', ' ')
	for s in delete:
		wordsToParse = wordsToParse.replace(s, '')
	wordsToParse = wordsToParse.replace('-', ' ')
	wordsToParse = wordsToParse.lower()

	
	#print(wordsToParse)
	
	transcript.close()
	path = ".\\new_transcription"
	if not os.path.exists(path):
		os.makedirs(path)
	os.chdir(path)
	output = open('new_' + fileName, 'w')
	
	output.write(wordsToParse)
	output.close()
	os.chdir("..")
	
for i in range(1, 1750):
	if os.path.isfile(str(i) + '_transcript.txt'):
		transcriptParser(str(i) + '_transcript.txt')