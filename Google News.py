from requests_html import HTMLSession
import pandas as pd

s = HTMLSession()

data = []
url = 'https://news.google.com/topics/CAAqJQgKIh9DQkFTRVFvSUwyMHZNRE55YXpBU0JXVnVMVWRDS0FBUAE?hl=en-IN&gl=IN&ceid=IN%3Aen'

r = s.get(url)
r.html.render(sleep=3, timeout=100, keep_page=True, scrolldown=5)
cont = r.html.find('article.MQsxIb.xTewfe')
for item in cont:
	try:
		news = item.find('h3', first=True).text
		url = item.find('a', first=True).attrs['href']
		news_channel = item.find('div.SVJrMe a', first=True).text
		posted = item.find('time.WW6dff.uQIVzc', first=True).text
		data.append([news, url, news_channel, posted])
	except:
		pass

df = pd.DataFrame(data, columns=['News', 'Url', 'news_channel', 'posted'])
df.to_csv('new data.csv', index=False)