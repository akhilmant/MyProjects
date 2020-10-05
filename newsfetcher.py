#Times of India 
import requests
import bs4
url=requests.get("https://timesofindia.indiatimes.com/")
soup=bs4.BeautifulSoup(url.text,"lxml")
trending=soup.select(".list8")
print("TIMES OF INDIA!")
for item in trending:
    print(item.text)
    print("\n")


#NDTV
url2=requests.get("https://www.ndtv.com/")
soup1=bs4.BeautifulSoup(url2.text,"lxml")
top_stories=soup1.select("a")
xyz=top_stories[40:75]
print("NDTV")
for story in xyz:
    print(story.text)


#Fotmob
url3=requests.get("https://www.fotmob.com/")
soup2=bs4.BeautifulSoup(url3.text,"lxml")
trending_news=soup2.select(".ArticleTitle.css-te5xhv-ArticleTitleCSS.e1v32l8r0")
trending_news1=soup2.select(".ArticleTitle.css-1gyp63k-ArticleTitleCSS.e1v32l8r0")
trending_news2=soup2.select(".ArticleTitle.css-1gyp63k-ArticleTitleCSS.e1v32l8r0")
print("FOTMOB- The Pulse of Football")
for goal in trending_news:
    print(goal.text)
    print("\n")
for box in trending_news1[:2]:
    print(box.text)
    print("\n")
for player in trending_news2:
    print(player.text)
    print("\n")


#Beebom
url4=requests.get("https://beebom.com/")
soup3=bs4.BeautifulSoup(url4.text,"lxml")
latest=soup3.select(".td-block-span12")
print("BEEBOM-Tech that Matters!")
for tech in latest:
    print(tech.text)
    

#