import requests
from bs4 import BeautifulSoup as Soup

r = requests.get("https://www.gastronom.ru/recipe/5038/uzbekskij-plov")

soup = Soup(r.text, "html.parser")

list = soup.find_all(class_= "_root_ofawm_2 _title_ucjtl_46")
list2 = soup.find_all(class_= "_head_8ms0x_12")
list3 = soup.find_all(class_= "_step_8ms0x_19")

for x in list:
    print(x.text)

for x in list2:
    print(x.text)

for x in list3:
    print(x.text)


