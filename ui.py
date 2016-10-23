import sys
from PIL import Image

#word = input('Please enter a word: ')
#TESTING print('The work is: ',word)
#number = input('How many panels do you want to see: ')
#output = functname(word, number)


#output = "1749_1"
#png = ".png"
#TESTING print(output)

#photo = output + png

#Takes in an image and outputs to another png file
#with open(photo, 'rb') as inf:
#	pngdata = inf.read()
	
#with open('1749_out.txt', 'wb') as inf:
#	inf.write(pngdata)
	

#Adds pictures together
#images = map(Image.open, ['Test1.png', 'Test2.png'])
#widths, heights = zip(*(i.size for i in images))

#total_width = sum(widths)
#max_height = max(heights)

#new_im = Image.new('RGB', (total_width, max_height))

#x_offset = 0
#for im in images:
#	new_im.paste(im, (x_offset,0))
#	x_offset += im.size[0]

#new_im.save('Test.png')


#WORKING
#list_im = ['Test1.png','Test2.png']
#new_im = Image.new('RGB', (444,95)) #creates a new empty image, RGB mode, and size 444 by 95

#for elem in list_im:
#    for i in range(0,444,95):
#        im=Image.open(elem)
#        new_im.paste(im, (i,0))
#new_im.save('Test.png')

#Testing
list_im = ['Test1.png','Test2.png']
new_im = Image.new('RGB', (740,305)) #creates a new empty image, RGB mode, and size 444 by 95


continuex = True
index = 0

while(continuex == True):
	word = input('Please enter a word: ')
	number = input('How many panels do you want to see: ')
	#output = functname(word, number)
	
	im=Image.open(word)
	new_im.paste(im, (index,0))
	index += 500
	
	next = input('Continue?(1 for yes, 0 for no): ')
	if(next == '0'):
		continuex = False
	
new_im.save('Test.png')


#WORKING
#opens an image:
#im = Image.open("Test1.png")
#creates a new empty image, RGB mode, and size 400 by 400.
#new_im = Image.new('RGB', (400,400))

#Here I resize my opened image, so it is no bigger than 100,100
#im.thumbnail((100,100))
#Iterate through a 4 by 4 grid with 100 spacing, to place my image
#for i in range(0,500,100):
#    for j in range(0,500,100):
#        #I change brightness of the images, just to emphasise they are unique copies.
#        im=Image.eval(im,lambda x: x+(i+j)/30)
#        #paste the image at location i,j:
#        new_im.paste(im, (i,j))

#new_im.show()



	

