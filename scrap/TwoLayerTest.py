#from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import requests
import csv
from datetime import datetime

userInput = 'noExit'
while userInput != 'exit':
    userKeyword = input('Enter keyword to search : ')
    userAllergy = input('Enter allergy to search : ')
    headers = {'User-Agent':'Mozilla/5.0'}
    first_url = 'https://guardian.com.my/index.php/'

    a_second_url = 'pbrand/'
    a_third_url = '.html'
    a_concat_url = first_url+a_second_url+userKeyword+a_third_url
    a_my_url = a_concat_url



    my_page_1 = requests.get(a_my_url)
    page_soup = soup(my_page_1.text, "html.parser")


    containers = page_soup.findAll("div", {"class": "product-info"})
    for container in containers:

        producturl = container.h2.a["href"]

        line = producturl
        my_line = requests.get(line)
        page_soup_line = soup(my_line.text, "html.parser")

        containers = page_soup_line.findAll("div", {"class": "product-view"})
        for container in containers:
            try:
                productprice = container.findAll("span", {"class": "price-incl-tax-new-theme price-incl-tax-special"})
                brandpricelist = productprice[0].text.strip()
            except IndexError:
                productprice = container.findAll("span", {"class": "price price-incl-tax-new-theme"})
                brandpricelist = productprice[0].text.strip()

            #productname = container.find("div", attrs={"class": "product-name"})
            pname = container.h1.string

            productimg = container.img.get('src')

            print("Product : " + str(pname))
            print("URL : " + producturl)
            print("Price : " + str(brandpricelist))
            print("URL img : " + str(productimg))

            all_data = container.find_all('td', class_='data')

            findword = userAllergy


            for table1 in all_data:
                s = table1.text
                # print(s)
                x = 0

                if findword in s:
                    x = 1
                    # print("This product has " + findword)
                    break
                elif findword not in s:
                    x = 0
                    # print("This product is free from your allergy.")

            if x == 1:
                print("This product has " + findword)
            else:
                print("This product is free from your allergy.")

            print()
            print()
