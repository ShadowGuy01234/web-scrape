from bs4 import BeautifulSoup
import requests

URL = "https://mmmut.ac.in/ExaminationSchedule"
urlNEW = "https://mmmut.ac.in/"
page = requests.get(URL)

soup = BeautifulSoup(page.text, 'html.parser')
res = soup.find('table',{ 'id' : "ContentPlaceHolder2_ContentPlaceHolder3_GridView1"} )
print(res.prettify)

