from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup

url = "https://www.psychologytoday.com/us/therapists/african-american/mn/minneapolis"

req = Request(url , headers={'User-Agent': 'Mozilla/5.0'})

webpage = urlopen(req).read()

page_soup = soup(webpage, "html.parser")

div = page_soup.find('div', class_= 'result-row normal-result row')

# name = div.find('span', itemprop="name")

print(div.prettify())
# print(name)

# description
# <div class="result-desc hidden-sm-down" dir="ltr" itemprop="description" lang="en">

#phone number
# <div class="result-phone hidden-xs-down">

#certification
#<span itemprop="jobTitle">

#link to full profile  
# <a class="btn btn-default btn-sm" data-event-action="ClickResultsProfileBtn" data-event-label="Result1"

# containers = page_soup.find("div", "result-row normal-result row")[0]
# print(containers)

# for container in containers:
#     print(container)