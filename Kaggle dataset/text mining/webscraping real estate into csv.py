from bs4 import BeautifulSoup
import requests
from csv import writer # nak export data ke csv file
html_text = requests.get('https://www.pararius.com/apartments/amsterdam').text
#print(html_text)

soup = BeautifulSoup(html_text,'lxml')
#print(soup)

#houses = soup.find_all('li', class_="search-list__item search-list__item--listing")
lists = soup.find_all('section', class_ ="listing-search-item")
# look through the lists and find a title for each list
with open('housing2.csv', 'w', encoding = 'utf8', newline = '') as f:
    thewriter = writer(f) # assign the writer tolong write dlm f
    header = ['title','location','price', 'living_area', 'room', 'interior','construction_period']
    thewriter.writerow(header) # tuliskan setiap row ikut header
    
    for list in lists: # for each section in all the sections
        title = list.find('a' , class_ = "listing-search-item__link listing-search-item__link--title").text.replace('\n','')
        location = list.find('div', class_="listing-search-item__location").text.replace('\n','')
        price = list.find('div', class_="listing-search-item__price").text.replace('\n','')
        living_area = list.find('li', class_="illustrated-features__item illustrated-features__item--surface-area").text
        room = list.find('li', class_ = "illustrated-features__item illustrated-features__item--number-of-rooms").text
        if list.find('li', class_="illustrated-features__item illustrated-features__item--interior") == None:
            interior = 'None'
        else:
            interior = list.find('li', class_="illustrated-features__item illustrated-features__item--interior").text
            
        if list.find('li', class_="illustrated-features__item illustrated-features__item--construction-period") == None:
            construction_period = 'None'
        else:
            construction_period = list.find('li', class_="illustrated-features__item illustrated-features__item--construction-period").text

        info = [title,location,price, living_area, room, interior,construction_period]
        print(info)
       # print(info) # nak tengok part mana naktukar jadi text
        thewriter.writerow(info)