import feedparser
import pandas as pd

url = "https://www.dailysecu.com/rss/allArticle.xml"

feed = feedparser.parse(url)

#print(feed.entries) #<item>태그 안의 정보들만 가져오기

titles = []
links = []
descriptions = []
authors = []
pubDates = []

for entry in feed.entries:
    titles.append(entry.title)
    links.append(entry.link)
    descriptions.append(entry.description)
    authors.append(entry.author)
    pubDates.append(entry.published)

data = {'Title': titles, 'Link': links, 'Description': descriptions, 'Author': authors, 'Published': pubDates}
df = pd.DataFrame(data)

df.to_excel('dailysecu.xlsx', index=False)