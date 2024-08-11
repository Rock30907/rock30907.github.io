import requests
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome()

driver.get('https://epic7x.com/characters/')

html= driver.page_source

soup = BeautifulSoup(html,'html.parser')
a_tag = soup.select('a.no-decoration.white.f-14>div.pure-u-1.text-center>span')

print(a_tag)
# for div in (a_tag,'class'=='pure-u-1 text-center'):
#     {
#     print('span')
#     }