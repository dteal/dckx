from sys import exit
from bs4 import BeautifulSoup
import requests

# open indexing file
index_filename = 'original/index.txt'
with open(index_filename, 'w') as index_file:

	# find number of comics
	try:
		homepage = requests.get('https://www.xkcd.com/').text
		homepage_soup = BeautifulSoup(homepage, 'lxml')
		prev_comic = homepage_soup.find('a', {'rel':'prev'}).get('href')[1:-1]
		num_comics = 1 + int(prev_comic)
	except IOError:
		print('Error: could not retrieve number of comics!')

	# loop through all comics
	for comic_index in range(num_comics):

		if (comic_index + 1) % 10 == 0:
			print(comic_index + 1)

		#print('Attempting to download XKCD ' + str(comic_index + 1) + '...')

		# get html file of comic and beautify
		try:
			comic_url = 'https://www.xkcd.com/' + str(comic_index+1)
			comic_raw = requests.get(comic_url)
			comic_html = comic_raw.text
			comic_soup = BeautifulSoup(comic_html, 'lxml')
		except IOError:
			print('Error: could not load XKCD ' + str(comic_index + 1) + '!')
			continue

		# find image url
		try:
			image_url = comic_soup.find('div', {'id':'comic'}).img.get('src')
			image_url = 'https:' + image_url
		except IOError:
			print('Error: could not load XKCD ' + str(comic_index + 1) + '!')
			continue

		# find comic transcript
		try:
			transcript = comic_soup.find('div', {'id':'transcript'}).contents
		except IOError:
			print('Error: no transcript in XKCD ' + str(comic_index + 1) + '!')
			continue

		# download and write image to file
		try:
			filename = 'original/' + str(comic_index + 1) + '.png'
			with open(filename, 'wb') as f:
				f.write(requests.get(image_url).content)
		except IOError:
			print('Error: no picture in XKCD ' + str(comic_index + 1) + '!')
			continue

		# write transcript to file
		try:
			filename = 'original/' + str(comic_index + 1) + '_transcript.txt'
			with open(filename, 'w') as f:
				for line in transcript:
					f.write(str(line.encode('utf-8')))
		except IOError:
			print('Error: transcripting XKCD ' + str(comic_index + 1) + '!')
			continue

		# record comic number in index file
		index_file.write(str(comic_index + 1) + '\n')

