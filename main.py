from typing import Union
from notice_scrape import notice_scrape
from fastapi import FastAPI

app = FastAPI()


@app.get("/download")
def download_notice():
    try:
        links = notice_scrape()
        return {"status": "success",
                "links" : links}
    except:
        return {"status": "failed"}