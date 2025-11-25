###
# https://realpython.com/python-web-scraping-practical-introduction/
###

# for open url
from urllib.request import urlopen
# for Regular expressions:
import re
# for soup
from bs4 import BeautifulSoup

def printSlash():
    print("\n-------------------------------------------------------------\n\n")

def getHTML(god):
    url = "http://olympus.realpython.org/profiles/"+god
    page = urlopen(url)
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")
    print("\tHTML: \n",html)
    return html

def saveHTML(html,god):
    #Write
    with open("html_"+god+".txt", "w") as file:
        file.write(html)

def getTitleByLen(god):
    html = getHTML(god)

    title_index = html.find("<title>")
    #14
    start_index = title_index + len("<title>")
    #21
    end_index = html.find("</title>")
    #39
    title = html[start_index:end_index]
    #'Profile: Aphrodite'
    print("\tTitle: \n",title)
    return title

def getTitleByRe(god):
    html = getHTML(god)

    pattern = "<title.*?>.*?</title.*?>"
    match_results = re.search(pattern, html, re.IGNORECASE)
    title = match_results.group()
    title = re.sub("<.*?>", "", title) # Remove HTML tags
    print("\tTitle: \n",title)
    return title

def getSoup(html):
    return BeautifulSoup(html, "html.parser")

#poseidon
#aphrodite
#dionysus

title = getTitleByLen("aphrodite")
printSlash()

title = getTitleByRe("poseidon")
printSlash()

title = getTitleByRe("dionysus")
printSlash()

# In Sell (CMD)
# $ python -m pip install beautifulsoup4
# $ py -m pip install beautifulsoup4
# no se pudo por el certificado :(

soup = getSoup(getHTML("dionysus"))
print("\tTitle with Soup: \n" + soup.title.string)
print("\tget_text:\n" + soup.get_text())
printSlash()

image1, image2 = soup.find_all("img")
image1.name
printSlash()