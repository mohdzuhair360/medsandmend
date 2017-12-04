from bs4 import BeautifulSoup as soup
import requests
from django.shortcuts import render,get_object_or_404
from homepage import models
import csv
from datetime import datetime

class guardianDesc:

    def describe (self, producturl,page):

        test = get_object_or_404(models.PageSource, page_id = page.page_id)
        print(test)
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

            productname = container.find("div", attrs={"class": "product-name"})
            pname = container.h1.string

            productimg = container.img.get('src')

            print("Product : " + str(pname))
            print("Price : " + str(brandpricelist))
            print("URL img : " + str(productimg))
            try:
                item_instance = models.SearchItem.objects.create(page = test,
                                                             item_name=productname,
                                                             item_price=brandpricelist,
                                                             item_image=productimg)
            except Exception as e:
                print("ERROR " + str(e))


           # all_data = container.find_all('td', class_='data')

            #findword = 'eczema'
            # findword = 'sensitive'

            #for table1 in all_data:
             #   s = table1.text
                # print(s)
              #  x = 0

#                if findword in s:
 #                   x = 1
                    # print("This product has " + findword)
  #                  break
   #             elif findword not in s:
      #              x = 0
                    # print("This product is free from your allergy.")

    #        if x == 1:
     #           print("This product has " + findword)
      #      else:
       #         print("This product is free from your allergy.")

        return "some"