from bs4 import BeautifulSoup
import requests # to request information from website
# request.get('link').text  --> nak text dia je
html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
print(html_text)

soup = BeautifulSoup(html_text,'lxml') # parse html into python object
print(soup)

# pattern utk setiap job = tags:li class
jobs = soup.find('li',class_="clearfix job-bx wht-shd-bx")
print(jobs)
#print(jobs) #---> print utk semua job dekat page tu (find_all)
# iterate utk semua jobs dalam page tu
for job in jobs:
    
   # job = soup.find('li',class_="clearfix job-bx wht-shd-bx") -->besarkan scope jadi find_all
    #print(job)  # --> bagi first match je

    # nak cari company name -- tags: h3
    # nak tag h3 yg dalam specific job tu je  
    company_name = job.find('h3',class_="joblist-comp-name").text
   # print(company_name) # kita nak text je

    # skill requirement
    skills = job.find('span',class_="srp-skills").text.replace(' ','')   # buang space
    #print(skills)   

    # days posted
    days_posted = job.find('span',class_="sim-posted").text
    #print(days_posted)

    # print
    print(f'''
          Company Name: {company_name}    
          Required Skills: {skills}    
          ''')   
          
    print('') #print empty line
        
      
      
      
      
      
    
    
                    
 