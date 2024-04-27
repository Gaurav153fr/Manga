import re
import requests as rq
from bs4 import BeautifulSoup as bs

def scrapeImg(URL):

    
    data =rq.get(URL).text

    soup =bs(data,'html.parser')
    filteredData = soup.find_all("div", class_="page-break no-gaps")
    
    images= []
    
    for data in filteredData:
        mainImg = data.find('img')
        v= mainImg['src']
        images.append(v)
        

    return images


def getepi(epi):
    URL = 'https://www.mangaread.org/manga/'+epi.replace(" ", "-")+'/'
    data =rq.get(URL).text
    

    soup =bs(data,'html.parser')
    try:
     desc = soup.find("div",class_="summary__content show-more").find_all("p")
    except:
        desc= soup.find("div",class_="summary__content show-more")
    print(desc)
    filteredData = soup.find_all("li", class_="wp-manga-chapter")
    epi =[]
    for data in filteredData:
       
       a= data.find('a')['href']
       epi.append(a)
       
    return epi

def search(searchTerm):
    URL = 'https://www.mangaread.org/?s='+searchTerm+'&post_type=wp-manga'
    data =rq.get(URL).text

    soup =bs(data,'html.parser')
    searchRes = []
    filteredData = soup.find_all("div", class_="row c-tabs-item__content")
    for data in filteredData:
        v= data.find('h3')
        img = data.find('img')['src']
        alttitle = data.find("div",class_="summary-content").text
        score = data.find("span",class_="score font-meta total_votes").text
        lat = data.find("span",class_="font-meta chapter").text
        url=v.find('a')['href']
        slug=re.search(r'/manga/([^/]+)/?$', url).group(1)
        print(slug)

        if v != None:
         da ={"title" : v.text,
              "img" : img,
              "alt":alttitle,
              "score":score,
              "latest":lat,
              "slug":slug

              
              }
         searchRes.append(da)
    return searchRes


