import csv
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formater = logging.Formatter('%(asctime)s:%(name)s:%(message)s')
filehandler = logging.FileHandler('scrape_logger.log')
filehandler.setFormatter(formater)
# filehandler.setLevel(logging.ERROR)

streamhandler = logging.StreamHandler()
streamhandler.setFormatter(formater)

logger.addHandler(filehandler)
logger.addHandler(streamhandler)

from requests_html import HTML

with open('simple_html.html',mode='r') as html_file:
    source = html_file.read()
    html = HTML(html=source)
    # html.render()   ##render dynamic data #wasn't able to download


# print(html.html)

title = html.find('title',first=True)    ##first=True equals position [0] in the list
# print(header)
# print(header[0].html)      ###can't run it with first=True
# print(header.text)

# match = html.find('#footer',first=True)
# print(match.html)

# article = html.find('div.article',first=True)
articles = html.find('div.article')
csv_file = open('scrape_file.csv',mode='w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['header','summary'])


for article in articles:
# print(article)
    header = article.find('h2',first=True).text
    # print(header)
    logger.debug(header)
    summary = article.find('p',first=True).text
    # print(summary)
    logger.debug(summary)
    # print()
    csv_writer.writerow([header,summary])

csv_file.close()




