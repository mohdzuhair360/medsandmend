from bs4 import BeautifulSoup as soup
import requests
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from homepage import models
#from HTMLParser import HTMLParser
from . import guardianDescription
import csv
from datetime import datetime

class guardianScrapEngine:

    def scrapIt(self, a_my_url, user_allergy, request):

        my_url = a_my_url
        headers = {'User-Agent': 'Mozilla/5.0'}
        #try:
        my_page_1 = requests.get(my_url)
        print("MY PAGE : " + str(my_page_1))

        #if str(my_page_1)== "<Response [404]>":
         #   print("YES")
          #  return

        #try:
        page_soup = soup(my_page_1.text, "html.parser")
        #print("page soup : " + str(page_soup))
        page = get_object_or_404(models.PageSource, pk=1)
        try:

            containers = page_soup.findAll("div", {"class": "product-info"})
            for container in containers:

                producturl = container.h2.a["href"]

                print("URL : " + producturl)

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
                    print("Price : " + str(brandpricelist))
                    print("URL img : " + str(productimg))
                    all_data = container.find_all('td', class_='data')

                   # findword = 'eczema'
                    #findword = 'muscle'
                    findword = user_allergy

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
                        allergyresult = "This product has the '" + findword + "' allergy and not suitable for you to use"
                        print("This product has " + findword)


                    else:
                        allergyresult = "This product is free from your allergy"
                        print("This product is free from your allergy.")




                    item_instance = models.SearchItem.objects.create(page=page,
                                                                 item_name=pname,
                                                                 item_price=brandpricelist,
                                                                 item_image=productimg,
                                                                 item_link=producturl,
                                                                 item_allergy=allergyresult)

        except Exception as e:
            containers = page_soup.findAll("div", {"class": "product-info"})
            print("No Product Found : " + my_url)

        return