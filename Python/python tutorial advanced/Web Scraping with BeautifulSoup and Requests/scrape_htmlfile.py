from bs4 import BeautifulSoup
import requests

with open('simple.html') as html_file:
    soup = BeautifulSoup(html_file,'lxml')

# print(soup.prettify())   ###to indent tags

# match = soup.title.text       ##.title brings the first match with title .use .text to get rid of html tags
# print(match)

# match = soup.find('div',class_='footer')       ###find first match
# print(match)

# article = soup.find('div',class_='article')
# headline = article.h2.a.text
# print(headline)
# summary = article.p.text
# print(summary)

for article in soup.find_all('div',class_='article') :      ####find_all to find all matches
    headline = article.h2.a.text
    summary = article.p.text
    print(headline,summary,sep='\n')
    print()

