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
    phonenum = phonenum_tag.get_text()
    print(phonenum)

    """Create list of therapists"""

    therapists = ({'name': name,
                # 'title': title,
                'pic': pic,
                'description': descr,
                'phonenum': phonenum
    })
    
    data.append(therapists)


with open("therapists.json", "w") as outfile:  
    json.dump(data, outfile) 

# fields = ['Name', 'Img Link', 'Description', 'Phone Number']
# with open('GFG.csv', 'w') as f: 
      
#     # using csv.writer method from CSV package 
    
#     write = csv.writer(f) 
#     write.writerow(fields) 

#     for i in data:  
#         write.writerows(data['name']) 

# with open('filename', 'wb') as myfile:
#     wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
#     wr.writerow(mylist)


"""Get link to full profile  
    Located in <a class="btn btn-default btn-sm"""

# full_profile = page_soup.find('a', class_ = 'btn btn-default btn-sm')
# full_profile.get('href')


# data = []
# for i in soup.find_all('div', {'class': 'row'}):
#     job_title = i.find('a', {'data-tn-element': 'jobTitle'})['title']
#     company_name = i.find('span', {'class': 'company'}).text.strip()    
#     job_summary = ''.join([j.text.strip() for j in i.find_all('span', 
#                                                               {'class': 'summary'})])
#     location = i.find('span', {'class': 'location'})
#     if location is not None:
#         location = location.text.strip()

#     salary_range = i.find('span', {'class': 'no-wrap'})
#     if salary_range is not None:
#         salary_range = salary_range.text.strip()


#     datum = {'job_title': job_title,
#              'company_name': company_name,
#              'job_summary': job_summary,
#              'location': location,
#              'salary_range': salary_range}

#     data.append(datum)

# df = pd.DataFrame(data)
# df.head()