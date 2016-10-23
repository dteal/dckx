import os
import re
import sys
import search
import requests
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from bs4 import BeautifulSoup

'''
# get times headlines
times_raw = requests.get('http://www.nytimes.com/').text
times_soup = BeautifulSoup(times_raw, 'lxml')
headline = times_soup.find('h2', {'class':'story-heading'}).a.contents
headline = str(headline[0].encode('utf-8'))[2:-1]
print(headline)
'''

headline = ""

for i in range(len(sys.argv)):
	if i > 0:
		headline = headline + sys.argv[i] + " "
headline = headline[:-1]

text_height = 150 

input_code = headline.split() #[input('Please enter a word: ')]
redo = []
pattern = re.compile('[^a-zA-Z]')
for word in input_code:
	if (not (len(word)<4)) and (re.match(pattern, word) is None) and word.find('&')==-1:
		redo.append(word)
input_code = redo
print('The work is: ', input_code)

used=[]

filename = ''
image_names = []
for word in input_code:
	filename = filename + word + '_'
	#print('Filename: ', filename)
	possibilities = search.search(word, 20)
	print('Possibilities: ', possibilities)
	i = 0
	flag = True
	while (flag==True ):
		i = i + 1
		try:
			ft = open('processed/' + possibilities[i] + '_1.png', 'r')
			flag = False
			print('processed/' + possibilities[i] + '_1.png')
			
		except FileNotFoundError:
			pass
		if flag == False and (not possibilities[i] in used or i >= 19):
			break;
	if i == 19:
		disp('out of range')

	image_names.append('processed/' + possibilities[i] + '_1.png')
	used.append(possibilities[i])
	#print('Image selected: ', possibilities[0]+'.png')
filename = 'output/' + filename[:-1] + '.png'
filename = filename.lower()
print('Output filename: ', filename)

images = map(Image.open, image_names)
widths, heights = zip(*(i.size for i in images))
#print('Widths: ', widths)
#print('Heights: ', heights)

max_height = max(heights)
total_width = 0
for i in range(len(widths)):
	total_width += int(widths[i] * (max_height/heights[i]))
#print('Total width: ', total_width)
# generate new image
new_im = Image.new('RGB', (total_width, max_height+text_height))
index = 0
for i in range(len(widths)):
	temp_width = int(widths[i] * max_height / heights[i])
	#print("Temp width: ", temp_width)
	temp_im=Image.open(image_names[i])
	temp_im = temp_im.resize((temp_width, max_height), Image.ANTIALIAS)
	#temp_im=temp_im.transform((temp_width, max_height), Image.AFFINE, (widths[0], heights[0], temp_width, max_height))
	new_im.paste(temp_im, (index,text_height))
	index += temp_width

draw = ImageDraw.Draw(new_im)
w=1000000000
fontsize = 110
while(w > total_width):
	fontsize = int(.9 * fontsize)
	font = ImageFont.truetype('lsansuni.ttf', fontsize)
	w, h = draw.textsize(headline.upper(), font=font)

draw.rectangle([(0,0), (total_width, text_height)], fill=(255,255,255))
draw.text(((total_width-w)/2, max(0,(text_height-h)/2)-10), headline.upper(), (0,0,0), font=font)

new_im.save(filename)
os.chdir('output')
os.system(filename[7:])

