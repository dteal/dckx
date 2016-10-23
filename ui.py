
import os
import sys
from PIL import Image
import search

input_code = ['dog', 'computer', 'flower'] #[input('Please enter a word: ')]
print('The work is: ', input_code)
number = input('How many panels do you want to see: ')

filename = ''
image_names = []
for word in input_code:
	filename = filename + word + '_'
	#print('Filename: ', filename)
	possibilities = search.search(word, 1)
	#print('Possibilities: ', possibilities)
	image_names.append('original/' + possibilities[0] + '.png')
	#print('Image selected: ', possibilities[0]+'.png')
filename = filename[:-1] + '.png'
#print('Output filename: ', filename)

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
new_im = Image.new('RGB', (total_width, max_height))
index = 0
for i in range(len(widths)):
	temp_width = int(widths[i] * max_height / heights[i])
	#print("Temp width: ", temp_width)
	temp_im=Image.open(image_names[i])
	temp_im = temp_im.resize((temp_width, max_height), Image.ANTIALIAS)
	#temp_im=temp_im.transform((temp_width, max_height), Image.AFFINE, (widths[0], heights[0], temp_width, max_height))
	new_im.paste(temp_im, (index,0))
	index += temp_width

new_im.save(filename)
os.system(filename)

