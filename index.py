import requests
import time
import os
import sys
from bs4 import BeautifulSoup

main_cats = ["", "News", "Hype", "Life", "Automotive", "Tech", "Science", "Business", "Men", "Fiction"]
other_cats = ["", "Sport", "Health", "Opinion", "Travel", "Food", "Index"]

def cls():
	os.system('cls')

def exit():
	sys.exit()

def get_article(link):
	global cat
	cls()
	ttl("Loading...")
	request = requests.get('https://www.idntimes.com/news/indonesia/gregorius-pranandito/anggaran-rehabilitasi-rumah-dinas-anies-capai-rp24-miliar')
	soup = BeautifulSoup(request.content, 'html.parser')

	title = soup.find('h1', class_="title-text").getText()
	excerpt = soup.find('div', class_="excerpt").getText().strip()
	author = soup.find('div', class_="author-name").find('a').getText()
	content = soup.find('article', class_="content-post-description").find_all('p')
	cls()

	print("------------------------")
	print(title)
	print(excerpt)
	print("By : "+author)
	print("------------------------")
	for p in range(0,len(content)):
		print(content[p].getText().replace('<strong>', '').replace('</strong>', ''))
		print("\n")
	print("99. Main Menu")
	menu = input()
	try:
		menu = int(menu)
		if(menu == 99):
			first_cats()
		else:
			not_valid()
	except ValueError:
		not_valid()
def ttl(title):
	print('======================================')
	print(title)
	print('======================================')

def first_cats():
	global cat
	cls()
	ttl('Please choose one of categories below')
	print("1. News")
	print("2. Hype")
	print("3. Life")
	print("4. Automotive")
	print("5. Tech")
	print("6. Science")
	print("7. Business")
	print("8. Men")
	print("9. Fiction")
	print("0. More")
	cat = input()
	try:
		cat = int(cat)
		if(cat > 0 and cat < 10):
			get_by_cat(main_cats[cat])
		elif(cat == 0):
			more_cats()
		else:
			not_valid()
	except ValueError:
		not_valid()

def more_cats():
	global cat
	cls()
	ttl('More Categories')
	print("1. Sport")
	print("2. Health")
	print("3. Opinion")
	print("4. Automotive")
	print("5. Travel")
	print("6. Food")
	print("7. Index")
	print("0. Back")
	cat = input()
	try:
		cat = int(cat)
		if(cat > 0 and cat < 8):
			get_by_cat(other_cats[cat])
		elif(cat == 0):
			first_cats()
		else:
			not_valid()
	except ValueError:
		not_valid()

def get_by_cat(cat):
	cls()
	ttl("Loading...")
	request = requests.get("https://idntimes.com/"+cat.lower())
	soup = BeautifulSoup(request.content, 'html.parser')
	description = soup.find_all("div", class_="description-latest")
	links = []
	cls()
	ttl(cat.upper()+" Category")
	for i in range (0,len(description)):
		print(str(i+1)+". "+description[i].find('h2', 'title-text').getText())
		links.append(description[i].find_all('a')[1]['href'])

	print("0. Back")
	selected_news = input()
	try:
		selected_news = int(selected_news)
		if(selected_news > 0 and selected_news <= len(description)):
			get_article(links[selected_news-1])
		elif(selected_news == 0):
			first_cats()
		else:
			not_valid()
	except ValueError:
		not_valid()

def not_valid():
	cls()
	ttl("Input Tidak Valid")
	exit()
cls()
ttl('Welcome To IDN Times (Command Version)')
time.sleep(1)
first_cats()