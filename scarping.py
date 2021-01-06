from bs4 import BeautifulSoup
import requests

src = requests.get('https://www.newegg.com/todays-deals')
source = src.content

soup = BeautifulSoup(source, 'lxml')

price = soup.find_all('strong')
prices = []
for a in price:
    prices.append('$' + a.text)
prices.pop()
prices.pop()
# print(prices)

title = soup.find_all('a', class_='item-title')
titles = []
for result in title:
    titles.append(result.text)
    #print(result.text)

# print(titles)

total_information = {}

for header in titles and prices:
    total_information[header] = [header]



print(total_information)

