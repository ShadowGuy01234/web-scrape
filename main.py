from notice_scrape import notice_scrape
from fastapi import FastAPI

app = FastAPI()

@app.get("/download")
def download_notice():
    try:
        data = notice_scrape()
        links = data["links_list"]
        titles = data["link_titles"]
        
        links_dict = {}
        for i in range(len(titles)):
            links_dict[titles[i]] = links[i]
            
        return {"status": "success",
                "links": links_dict
                }
    except:
        return {"status": "failed"}