from bs4 import BeautifulSoup

import requests

url = "https://www.gov.br/ans/pt-br/assuntos/prestadores/padrao-para-troca-de-informacao-de-saude-suplementar-2013-tiss"

def getHTMLSoup(url):
	html = requests.get(url)
	html.raise_for_status()
	return BeautifulSoup(html.content, 'html.parser')

def main():
	soup = getHTMLSoup(url)
	link_url = soup.find("a",class_="alert-link internal-link")["href"]
	 
	soup = getHTMLSoup(link_url)
	link_pdf = soup.find("tbody").find("a")["href"]

	pdf = requests.get(link_pdf).content


	with open('./componente_organizacional.pdf','wb') as f:
		f.write(pdf)


if __name__ == '__main__':
	main()

 