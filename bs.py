

import requests
from bs4 import BeautifulSoup

url = "https://codewithharry.com"

# Step 1: Get the HTML
r = requests.get(url)
htmlContent = r.content
# print(htmlContent)

# Step 2: Parse the HTML
soup = BeautifulSoup(htmlContent, 'html.parser')
print(soup)



# Get the title of the HTML page
title = soup.title

# Get all the paragraphs from the page
paras = soup.find_all('p')
print(paras)






 #Get the text from the tags/soup



# Get all the anchor tags from the page
anchors = soup.find_all('a')
all_links = set()
# Get all the links on the page:
for link in anchors:
    if (link.get('href') != '#'):
        linkText = "https://codewithharry.com" + link.get('href')
        all_links.add(link)


navbarSupportedContent = soup.find(id='navbarSupportedContent')

 #.contents - A tag's children are available as a list




ul = soup.find("ul")
print(ul.contents)
anchors = soup.find_all('a')
print(anchors)

paras = soup.find_all('p')
print(paras)

ul = soup.find("ul")
print(ul.contents)


ul = soup.find("ul")
for i in ul.children:
	print(i)

ul = soup.find("ul")
print(ul.parent)

ul = soup.find(id="li")

ul = soup.find(id="li")

f = open("file.csv", "w")
f.write("Every,word,will,go,in,separate,column\n")
f.write("This,will,go,in,next,row")
f.close()


