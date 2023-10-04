import csv

from requests_html import HTML,HTMLSession

with open('simple_html.html') as html_file:
    source = html_file.read()
    html = HTML(html=source)

match = html.find('html')
print(match[0].html)

