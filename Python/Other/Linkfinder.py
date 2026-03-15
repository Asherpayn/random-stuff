# Script to get the current mirror links for https://annasarchive.org
# You can find these in the Wikipedia page: https://en.wikipedia.org/wiki/Anna's_Archive
# This script solves the problem of poking around on the internet just to visit one site

import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Anna's_Archive"
# using my normal user agent for Zen Browser (Firefox based) to get around error 403: forbidden
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:148.0) Gecko/20100101 Firefox/148.0'}

def parse(content):
	print(content)


def main():
	response = requests.get(url, headers=headers)

	if response.status_code == 200:
		print(f"Success: {response.status_code} OK")
	elif response.status_code == 404:
		print(f"Error: {response.status_code} Not Found")
	elif response.status_code == 403:
		print(f"Error: {response.status_code} Forbidden")
	else:
		print(f"Unknown error: {response.status_code}")
	content = response.content.decode("utf-8")
	parse(content)


if __name__ == "__main__":
	main()