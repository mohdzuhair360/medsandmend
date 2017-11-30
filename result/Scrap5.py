from bs4 import BeautifulSoup as soup
import requests

line = "https://guardian.com.my/index.php/pbrand/cetaphil/cetaphil-restoraderm-skin-restoring-body-mosturizer-295ml.html"
my_line = requests.get(line)
page_soup_line = soup(my_line.text, "html.parser")
# print(my_line.text)


# print(page_soup_line.title)
# print(page_soup_line.title.string)

all_data = page_soup_line.find_all('td', class_='data')

findword = 'eczema'
#findword = 'sensitive'

for table1 in all_data:
    s = table1.text
    #print(s)
    x=0

    if findword in s:
        x=1
        #print("This product has " + findword)
        break
    elif findword not in s:
        x=0
        #print("This product is free from your allergy.")

if x==1:
    print("This product has " + findword)
else:
    print("This product is free from your allergy.")