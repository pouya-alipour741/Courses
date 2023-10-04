from requests_html import HTMLSession

session = HTMLSession()
r = session.get('https://coreyms.com/')

# match = r.html.find('.entry-header a')
# match = r.html.find('.entry-title a')
# match = r.html.find('.entry-title-link')
# print(match[0].text)

articles = r.html.find('article')
for article in articles:

    try:
        headline = article.find('.entry-title-link',first=True).text
        # print(headline[0].text)

        summary = article.find('.entry-content p',first=True).text
        # print(summary[0].text)

        vid_src = article.find('.youtube-player',first=True).attrs['src']
        vid_id = vid_src.split('?')[0]
        vid_id = vid_id.split('/')[4]
        youtube_link = f'https://www.youtube.com/watch?v={vid_id}'
        print(headline,summary,youtube_link,sep='\n')
        print()

    except Exception:
        youtube_link = None


