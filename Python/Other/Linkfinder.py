# Script to get the current mirror links for https://annasarchive.org
# You can find these in the Wikipedia page: https://en.wikipedia.org/wiki/Anna's_Archive
# This script solves the problem of poking around on the internet just to visit one site

import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Anna's_Archive"
# using my normal user agent for Zen Browser (Firefox based) to get around error 403: forbidden
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:148.0) Gecko/20100101 Firefox/148.0'}
welcome = """
This is a program that finds the links to Anna's Archive using the wikipedia article.
If you get an unknown http error refer to https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status
"""

def parse(content):
	# Pimp up the raw HTML string with beautifulsoup
	soup = BeautifulSoup(content, 'html.parser')

	if input("Would you like to see the raw HTML?\n>>> ").lower().strip() == "y":
		print(soup)
	else:
		print("Ok, Moving on\n")

	return soup

def find_links(soup):
	# Find all <span class="url"> elements
	links = soup.find_all('span', class_='url')
	result = []
	for link in links:
		a = link.find('a')
		# Only keep links that point to an Anna's Archive mirror
		if a and 'annas-archive' in a.get('href', ''):
			result.append(a.get('href'))

	# Turns into set to drop dupes then back into a list to keep it working - list of N (can change)
	result = list(set(result))
	return result

def main():
	print(welcome)
	response = requests.get(url, headers=headers)

	# Handles common HTTP status codes
	if response.status_code == 200:
		print(f"Success: {response.status_code} OK")
	elif response.status_code == 404:
		print(f"Error: {response.status_code} Not Found")
	elif response.status_code == 403:
		print(f"Error: {response.status_code} Forbidden")
	else:
		print(f"Unknown error: {response.status_code}")

	# Pop into a string then send to beautifulsoup
	content = response.content.decode("utf-8")
	soup = parse(content)

	print("The current links are:")
	for links in find_links(soup):
		print(links)


if __name__ == "__main__":
	main()