from bs4 import BeautifulSoup
import requests

index_filename = 'original/index.txt'
with open(index_filename, 'w') as index_file:

	for comic_index in range(972):

		index_file.write(str(comic_index+1)+'\n')

		# get html file
		url = 'https://www.xkcd.com/' + str(comic_index+1)
		r = requests.get(url)
		html = r.text

		'''
		<div id="comic">
		<img src="//imgs.xkcd.com/comics/alternative_literature.png" title="I just noticed CVS has started stocking homeopathic pills on the same shelves with--and labeled similarly to--their actual medicine. Telling someone who trusts you that you&#39;re giving them medicine, when you know you’re not, because you want their money, isn’t just lying--it’s like an example you’d make up if you had to illustrate for a child why lying is wrong." alt="Alternative Literature" />
		</div>

		<div id="transcript" style="display: none">[[Person 1 and 2 stand in front of Person 2&#39;s bookcase.  Person 1 flips through a number of them]]
		Person 1: All your books are full of blank pages.
		Person 2: Not true. That one has some ink on page 78.
		[[Person 1 looks at page 78]]
		Person 1: A smudge.
		Person 2: So?

		Person 1: There are no words. You&#39;re not reading. There&#39;s no *story* there.
		Person 2: Maybe not for you. When I look at those books, I think about all *kinds* of stories.

		Person 2: Reading is about more than what&#39;s on the page. Holding a book prompts my mind to enrich itself.  Frankly, I suspect the book isn&#39;t even necessary.

		Person 2: The whole industry is evil. Greedy publishers and rich authors try to convince us our brains *need* their words. But I refuse to be a sucker.
		Person 1: Who sold you all these blank books?

		{{Title text: I just noticed CVS has started stocking homeopathic pills on the same shelves with--and labeled similarly to--their actual medicine. Telling someone who trusts you that you&#39;re giving them medicine, when you know youâre not, because you want their money, isnât just lying--itâs like an example youâd make up if you had to illustrate for a child why lying is wrong.}}</div>
		</div>
		'''

		# beautify html
		soup = BeautifulSoup(html, 'lxml')

		# find image url
		comic_url = soup.find('div', {'id':'comic'}).img.get('src')
		comic_url = 'https:' + comic_url
#		print(comic_url)

		transcript = soup.find('div', {'id':'transcript'}).contents
#		print(transcript)

		filename = 'original/' + str(comic_index) + '.png'
		with open(filename, 'wb') as f:
			f.write(requests.get(comic_url).content)

		filename = 'original/' + str(comic_index) + '_transcript.txt'
		with open(filename, 'w') as f:
			for line in transcript:
				f.write(line)

