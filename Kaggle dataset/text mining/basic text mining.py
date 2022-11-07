# basic webscraping
# import beautifulsoup
from bs4 import beautifulsoup
# kena access content dalam html file --> work with file object
# open a file and read the content
# kalau directory file sama dgn pyhon then xyah specify path
with open('home.html', 'r') as html_file # 'r' = nak read je
    content = html_file.read() # dah setkan content file ni as variable html_file
    print(content) # nak scrape information dari content pakai tags
    soup = beautifulsoup(content,'lxml') # (content, parse method)
 # get some information on the header tags
 # find (tags in html) --> carikan yg first h5 tag dia jumpa
     tags = soup.find('h5') # dapat satu je
     courses_html_tags = soup.find_all('h5') # carikan semua
     for course in courses_html_tags:
         print(course.text) # nak print text tu je
         
--------------------Program 2------------------------------
# nak cari price of the course--> point dekat price then inspect
# cari tag yg bagi price tu
# kita nak listkan semua course dgn price

with open('home.html', 'r') as html_file # 'r' = nak read je
    content = html_file.read() # dah setkan content file ni as variable html_file
    print(content) # nak scrape information dari content pakai tags
    soup = beautifulsoup(content,'lxml') # (content, parse method)
    course_card = soup.find_all('div', class_ = 'card' ) # name dgn price ada tag ni
# find_all(tgk common tags utk semua card, class ada built-in function lain so letak underscoreutk bezakan)
    for courses in course_card:
        course_name = course.h5.text # dekat tag tu kita nak text dia je
        course_price = course.a.text
        print(course_name) # 'python for beginner'
        print(course_price) # 'start for 60$'
# kita nak buat ayat 'python for beginner cost 60$',
# so kena buang ayat 'start for' --> split string tu
        course_price = course.a.text.split()[-1]  # nak yg belakang je             
        print(f'{course_name} costs {course_price}') # f string