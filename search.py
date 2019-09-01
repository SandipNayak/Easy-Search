#shows the price of products
#same as,if we search in amazon

import requests
from bs4 import BeautifulSoup

Url="https://www.amazon.in/s?k=keyword&ref=nb_sb_noss_2"
url="https://www.amazon.in"

headers={"User-Agent": 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}

keyword=input("Enter the item you eant to search:")
keyword=keyword.strip().replace(" ","+")
Url=Url.replace("keyword",keyword)

text=requests.get(Url,headers=headers)
soup=BeautifulSoup(text.content,"html.parser")


item_href_names_container = soup.findAll('a', {"class": "a-link-normal a-text-normal"})
item_price_container = soup.findAll("span", {"class": "a-offscreen"})


n=1
for item_links in item_href_names_container:
    print("Item No: {}".format(n))
    item_name = item_links.span
    print("Item Name: {}".format(item_name.text))
    print("Price: {}".format(item_price_container[n].text))
    item_link = url+item_links.get('href')
    print("Item Link: {}".format(item_link))
    print("-------------------------------------------------------------------------------")
    n+= 1
