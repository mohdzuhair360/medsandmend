from bs4 import BeautifulSoup as soup
import requests
from django.shortcuts import render,get_object_or_404
from homepage import models
import csv
from datetime import datetime

class guardianScrapEngine:

    def scrapIt(self, a_my_url):

        my_url = a_my_url
        headers = {'User-Agent':'Mozilla/5.0'}
        my_page = requests.get(my_url)
        page_soup = soup(my_page.text, "html.parser")



        page = get_object_or_404(models.PageSource, pk=1)
        cont = page_soup.findAll("li", {"class": "item"})
        for con in cont:
            productimg = con.a.img["src"]
            print("Image : " + productimg)
            containers = page_soup.findAll("div", {"class": "product-info"})
            for container in containers:
                productname = container.h2.a["title"]
                try:
                    productprice = container.findAll("span", {"class": "price-incl-tax-new-theme price-incl-tax-special"})
                    brandpricelist = productprice[0].text.strip()
                except IndexError:
                    productprice = container.findAll("span", {"class": "price price-incl-tax-new-theme"})
                    brandpricelist = productprice[0].text.strip()
                producturl = container.h2.a["href"]

                item_instance = models.SearchItem.objects.create(page=page,
                                                                 item_name= productname,
                                                                 item_price=brandpricelist,
                                                                item_link = producturl,
                                                                 item_image = productimg)

                print("Product : " + productname)
                print("Price : " + str(brandpricelist))
                print("Url : " + producturl)


            return

