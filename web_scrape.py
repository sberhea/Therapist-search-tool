from urllib.request import Request, urlopen
from bs4 import SoupStrainer, BeautifulSoup as soup
import re
import pandas as pd
import json

url = "https://www.psychologytoday.com/us/therapists/african-american/mn/minneapolis"

req = Request(url , headers={'User-Agent': 'Mozilla/5.0'})

webpage = urlopen(req).read()

page_soup = soup(webpage, "html.parser")

data = []
# result-row normal-result row


for i in page_soup.find_all('div', {'class': 'result-row normal-result row'}):
    print('******************************************')
    #Get name
    name_tag = i.find('span', {'itemprop': 'name'}) 
    name = name_tag.get_text()
    print(name)
    #Get title
    # print(i)
    # title_tag= i.find('span', {'itemprop': 'jobTitle'})
    # # import pdb; pdb.set_trace()
    # if title_tag is None:
    #     continue
    # title = title_tag.get_text() 
    # print(title)
    #Get img link
    pic_tag = i.find('img', {'class': 'result-photo'})
    pic = pic_tag.get('src')
    print(pic)
    #Get description
    descr_tag = i.find('div', {'class': 'result-desc hidden-sm-down'})
    descr = descr_tag.get_text()
    print(descr)
    #Get phone number
    phonenum_tag = i.find('a', {'itemprop': 'telephone'})
    phonenum = phonenum_tag.get_text().strip()
    print(phonenum)
    #Full profile
    fp_tag = i.find('a', {'class':'btn btn-default btn-sm'})
    fp = fp_tag.get('href')
    
    """Create list of therapists"""
     
    therapists = ({'name': name,
                    #'title': title,
                    'pic': pic,
                    'description': descr,
                    'phonenum': phonenum,
                    'fp': fp,
                    'latitude': 'x',
                    'longitude': 'x', 
                    'sliding_scale': 'x' ,
        })

    data.append(therapists)

with open("therapists2.json", "w") as outfile:  
    json.dump(data, outfile) 

