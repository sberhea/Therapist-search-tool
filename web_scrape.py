from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup

url = "https://www.psychologytoday.com/us/therapists/african-american/mn/minneapolis"

req = Request(url , headers={'User-Agent': 'Mozilla/5.0'})

webpage = urlopen(req).read()

page_soup = soup(webpage, "html.parser")

title = page_soup.find("title")

# print(title)

containers = page_soup.find("div", "result-row normal-result row")[0]
print(containers)

# for container in containers:
#     print(container)