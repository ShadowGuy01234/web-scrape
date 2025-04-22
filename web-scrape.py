from bs4 import BeautifulSoup
import requests

URL = "https://mmmut.ac.in/ExaminationSchedule"
urlNEW = "https://mmmut.ac.in/"
page = requests.get(URL)

soup = BeautifulSoup(page.text, 'html.parser')
table = soup.find('table',{ 'id' : "ContentPlaceHolder2_ContentPlaceHolder3_GridView1"} )
# print(table.prettify)
trs = table.find_all('tr')
for tr in trs[:10]:
    # print(list(tr))
    a = tr.find('td').find('a').attrs
    print(a)

