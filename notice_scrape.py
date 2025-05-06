from bs4 import BeautifulSoup
import requests

def notice_scrape():
    URL = "https://mmmut.ac.in/ExaminationSchedule"
    urlNEW = "https://mmmut.ac.in/"
    page = requests.get(URL)
    
    soup = BeautifulSoup(page.text, 'html.parser')
    table = soup.find('table',{ 'id' : "ContentPlaceHolder2_ContentPlaceHolder3_GridView1"} )
    # print(table.prettify)

    links_list = []
    link_title = []
    trs = table.find_all('tr')
    
    for tr in trs[:10]:
        a = tr.find('a').attrs
        link = a['href']
        completeLink = urlNEW + link
        clean_filename = link.replace("Download/", "")
        links_list.append(completeLink)
        link_title.append(clean_filename)
    
    return {
        "links_list": links_list,
        "link_titles": link_title
    }


