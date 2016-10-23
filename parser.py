import os
def transcriptParser(fileName):
	with open(fileName, 'r') as transcript:
		wordsToParse = transcript.read()

	delete = ['[',']','{','}','.','?','!','"',',', ':', '\\', ' -', '(', ')']
	wordsToParse = wordsToParse.replace('\\n', ' ')
	for s in delete:
		wordsToParse = wordsToParse.replace(s, '')
	wordsToParse = wordsToParse.replace('-', ' ')
	wordsToParse = wordsToParse.lower()

	with open('processed' + fileName[8:-15] + '.txt', 'w') as output:
		output.write(wordsToParse)

for i in range(1, 1750):
	filename = 'original/' + str(i) + '_transcript.txt'
	if os.path.isfile(filename):
		transcriptParser(filename)

