#from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import requests
import csv
from datetime import datetime

userInput = 'noExit'
while userInput != 'exit':
    userKeyword = input('Enter keyword to search : ')
    headers = {'User-Agent':'Mozilla/5.0'}
    first_url = 'https://guardian.com.my/index.php/'

    a_second_url = 'pbrand/'
    a_third_url = '.html'
    a_concat_url = first_url+a_second_url+userKeyword+a_third_url
    a_my_url = a_concat_url

    #b_second_url = 'catalogsearch/result/?q='
    #b_concat_url = first_url+b_second_url+userKeyword
    #b_my_url = b_concat_url

    #c_second_url = 'default-menu/over-the-counter/'
    #c_third_url = '-colds-flu.html'
    #c_concat_url = first_url+c_second_url+userKeyword+c_third_url
    #c_my_url = c_concat_url

    #d_second_url = 'coughs-'
    #d_third_url = '-flu.html'
    #d_concat_url = first_url+c_second_url+d_second_url+userKeyword+d_third_url
    #d_my_url = d_concat_url

    #e_second_url = 'coughs-colds-'
    #e_third_url = '.html'
    #e_concat_url = first_url+c_second_url+e_second_url+userKeyword+e_third_url
    #e_my_url = e_concat_url

    my_page_1 = requests.get(a_my_url)
    #my_page_2 = requests.get(b_my_url)
    #my_page_3 = requests.get(c_my_url)
    #my_page_4 = requests.get(d_my_url)
    #my_page_5 = requests.get(e_my_url)
#page_html = my_page.read()
#my_page.close()

#html parsing
    page_soup = soup(my_page_1.text, "html.parser")
    #page_soup = soup(my_page_2.text, "html.parser")
    #page_soup = soup(my_page_3.text, "html.parser")
    #page_soup = soup(my_page_4.text, "html.parser")
    #page_soup = soup(my_page_5.text, "html.parser")
#tisu = page_soup.findAll("h2",{"class":"product-name"})
#tisu = page_soup.findAll("a",{"title":""})
#tisu = page_soup.findAll("div",{"style":"height:40px"})

    #filename = "guard3.csv"
    #f = open(filename,"w")
    #headers = "Brand, Price\n"
    #f.write(headers)
    cont = page_soup.findAll("li", {"class": "item"})
    for con in cont:
        #productimg = con.a.img
        #print("URL img : " + productimg)
        containers = page_soup.findAll("div", {"class":"product-info"})
        for container in containers:
            productimg = con.a.img["src"]
            productname = container.h2.a["title"]
            try:
                productprice = container.findAll("span", {"class" : "price-incl-tax-new-theme price-incl-tax-special"})
                brandpricelist = productprice[0].text.strip()
            except IndexError:
                productprice  = container.findAll("span", {"class" : "price price-incl-tax-new-theme"})
                brandpricelist = productprice[0].text.strip()
                #brandpricelist = 'Price not available'
            producturl = container.h2.a["href"]


            print("Product : " + productname)
            print("Price : " + str(brandpricelist))
            print("URL : " + producturl)
            print("URL img : " + str(productimg))

        #f.write(productname + "," + str(brandpricelist) + "," + "\n")

    #f.close()
#print(product)
#product = page_soup.a
#containers = page_soup.findAll("div",{"class":"f-fix"})
#for container in containers:
#for link in product:
    #print(link.get("a"))
    #price = page_soup.findAll("span", {"class": "price-incl-tax-new-theme price-incl-tax-special"})
    #price = page_soup.find_all("span", {"class": "price-incl-tax-new-theme price-incl-tax-special"})
    #pricelist = price[0].text.strip()
    #print("Price : " +pricelist)
#for link in product:
    #for links in price:
        #print(link.get("title"))
        #print(price)
#print(tisu)
    #price = page_soup.findAll("span", {"class": "price-incl-tax-new-theme price-incl-tax-special"})
    #pricelist = price[0].text.strip()
    #print("Price : " + pricelist)
#price = page_soup.findAll("span",{"class":"price-incl-tax-new-theme price-incl-tax-special"})
#for links in price:
    #print(links.get("span",{"class":"price-incl-tax-new-theme price-incl-tax-special"}))
#print(price)

# open a csv file with append, so old data will not be erased
#with open('guard.csv', 'a') as csv_file:
    #writer = csv.writer(csv_file)
    #writer.writerow([product, datetime.now()])