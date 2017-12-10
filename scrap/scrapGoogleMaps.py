#from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import requests
import csv
from datetime import datetime

userInput = 'noExit'
while userInput != 'exit':
   # userKeyword = input('URL to search : ')
    headers = {'User-Agent':'Mozilla/5.0'}
    #first_url = 'https://guardian.com.my/index.php/'

    #a_second_url = 'pbrand/'
    #a_third_url = '.html'
    #a_concat_url = first_url+a_second_url+userKeyword+a_third_url
    a_my_url = "https://www.google.com/maps/place/Jalan+Belangkas,+Kampung+Pandan,+55100+Kuala+Lumpur,+Wilayah+Persekutuan+Kuala+Lumpur/@3.1432609,101.7315242,17z/data=!3m1!4b1!4m5!3m4!1s0x31cc36491fdeffe7:0xd38acceb7463bc9a!8m2!3d3.1432609!4d101.7337129"


    my_page_1 = requests.get(a_my_url)

    page_soup = soup(my_page_1.text, "html.parser")


    #for tag in cont:
        #print(tag.get('src'))

    containers = page_soup.findAll("div", {"class": "section-hero-header-title"})
    for container in containers:
        #productname = container.h2.a["title"]
        #try:
            #productprice = container.findAll("span", {"class": "price-incl-tax-new-theme price-incl-tax-special"})
            #brandpricelist = productprice[0].text.strip()
        #except IndexError:
            #productprice = container.findAll("span", {"class": "price price-incl-tax-new-theme"})
            #brandpricelist = productprice[0].text.strip()
            # brandpricelist = 'Price not available'
        address = container.h1

        #print("Product : " + productname)
        #print("Price : " + str(brandpricelist))
        print("Address : " + address)

