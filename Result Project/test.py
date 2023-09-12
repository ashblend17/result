import requests
from bs4 import BeautifulSoup

URL = 'https://erp.iiitkottayam.ac.in/php/2022/1/2022BCS0014.html'

page = requests.get(URL)

page_soup = BeautifulSoup(page.content, 'html.parser')

tables = page_soup.find_all('table')
t1_rows=tables[1].find_all('tr')
name = t1_rows[1].find('td',style="text-align:left").text
roll = t1_rows[1].find('td',style="text-align:right").text
# name=row1_td.text
# roll=row1_td[1].text
rows3=tables[2].find_all('tr')
rows3_td=rows3[7].find_all('td')
sgpa=rows3_td[1].text
# print(name)
# print(roll)
# print(sgpa)