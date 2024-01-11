from bs4 import BeautifulSoup
import requests
response=requests.get("https://news.ycombinator.com")
web_page=response.text
soup=BeautifulSoup(web_page,"html.parser")
#print(soup.title)
#anchor_tags=soup.find_all(name='a')
#print(anchor_tags)
f=soup.find_all(class_="titleline")
article_texts=[]
article_links=[]
#print(f.get_text())
for tags in f:
    text=tags.get_text()
    article_texts.append(text)
    link=tags.find(name="a").get("href")
    article_links.append(link)
#    print(tags.find(name="a").get("href"))
#for tag in anchor_tags:
#    print(tag.get("href"))
#scores=soup.find_all(class_="score")
#for i in scores:
#    print(i.get_text())
article_upv=[score.get_text().split()[0] for score in soup.find_all(class_="score")]
#print(article_texts)
#print(article_links)
print(article_upv)
maximum=max(article_upv)
idx=article_upv.index(maximum)
print(idx)
print(article_texts[idx])
print(article_links[idx])



