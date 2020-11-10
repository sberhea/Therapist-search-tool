from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup

url = "https://www.psychologytoday.com/us/therapists/african-american/mn/minneapolis"

req = Request(url , headers={'User-Agent': 'Mozilla/5.0'})

webpage = urlopen(req).read()

page_soup = soup(webpage, "html.parser")

"""Get name"""
div = page_soup.find('div', class_= 'result-row normal-result row')

name = div.find('span', itemprop="name")

name.get_text()

"""Get description
# <div class="result-desc hidden-sm-down" dir="ltr" itemprop="description" lang="en">"""

description = page_soup.find('div', class_ = 'result-desc hidden-sm-down')
description.get_text()

"""Get phone number
        <div class="result-phone hidden-xs-down">"""

phone_num = page_soup.find('a', class_= 'btn btn-info btn-sm btn-block tr-result-phone')
# print(description.prettify)

phone_num.get_text()

"""Get title
        Located in <span itemprop="jobTitle"""

title = page_soup.find('span', itemprop='jobTitle')
print(title)

"""Get link to full profile  
    Located in <a class="btn btn-default btn-sm"""

full_profile = page_soup.find('a', class_ = 'btn btn-default btn-sm')
full_profile.get('href')

"""Get picture"""

picture = page_soup.find('img', class_= 'result-photo')
picture.get('src')

# containers = page_soup.find("div", "result-row normal-result row")[0]
# print(containers)

# for container in containers:
#     print(container)