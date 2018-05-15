from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

def getText(url):
	req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
	page = urlopen(req).read()
	soup = BeautifulSoup(page,"html.parser")
	text = ' '.join(map(lambda p: p.text, soup.find_all('p')))
	print(text)
	return [soup.title.text, text]

if __name__=='__main__':
	getTtext('https://en.wikipedia.org/wiki/Iron_Man_(2008_film)')