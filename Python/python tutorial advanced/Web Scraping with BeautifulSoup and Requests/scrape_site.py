from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('https://coreyms.com/').text

soup = BeautifulSoup(source,'lxml')

article = soup.find('article')

headline = article.header.h2.text

# summary = article.div.p.text   ##same result as below

summary = article.find('div',class_='entry-content').p.text


vid_source = article.find('iframe',class_='youtube-player')['src']
print(vid_source)
vid_id = vid_source.split('/')

for i in range(3):
    print(vid_id[i])

vid_id = vid_source.split('/')[4]

vid_id = vid_id.split('?')[0]

youtube_link = f'https://www.youtube.com/watch?v={vid_id}'



csv_file = open('scarpe_net.csv', 'w')
csv_writer = csv.writer(csv_file,delimiter='\t')

csv_writer.writerow(['headline', 'summary', 'youtube_link'])
########now we have one article we can loop through all articles with information above
for article in soup.find_all('article'):
    headline = article.header.h2.text

    # summary = article.div.p.text   ##same result as below

    summary = article.find('div', class_='entry-content').p.text
    try:
        vid_source = article.find('iframe', class_='youtube-player')['src']


        vid_id = vid_source.split('/')[4]
        vid_id = vid_id.split('?')[0]


        youtube_link = f'https://www.youtube.com/watch?v={vid_id}'
    except Exception:
        youtube_link = None

    ####write to csv
    csv_writer.writerow([headline, summary, youtube_link])

csv_file.close()

    # print(headline)
    # print(summary)
    # print(youtube_link)
    # print()

