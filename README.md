# 📢 MMUT Notice Scraper API

A fast and simple API built using **FastAPI** that scrapes the latest 10 notices from the official [MMMUT](https://mmmut.ac.in) website. It returns direct PDF download links in structured JSON format.

🌐 **Live URL**:
👉 [https://web-scrape-api.vercel.app/download](https://web-scrape-api.vercel.app/download)

---

## 🚀 Features

* 🔍 Real-time scraping of MMUT's Examination Schedule page
* 📄 Returns the **10 latest notice PDFs** with direct download links
* ⚡ Deployed using **Vercel** for instant and global access

---

## 📡 API Endpoint

### `GET /download`

Returns a JSON object containing filenames and their corresponding download URLs.

#### ✅ Sample Response:

```json
{
  "status": "success",
  "links": {
    "300420257689.pdf": "https://mmmut.ac.in/Download/300420257689.pdf",
    "280420259994.pdf": "https://mmmut.ac.in/Download/280420259994.pdf",
    ...
  }
}
```

If something goes wrong:

```json
{
  "status": "failed"
}
```

---

## 🧪 Example Usage

### Curl

```bash
curl https://web-scrape-api.vercel.app/download
```

### Python

```python
import requests

res = requests.get("https://web-scrape-api.vercel.app/download")
data = res.json()
print(data["links"])
```

---

## 🛠️ Tech Stack

* **FastAPI** – Lightning-fast web framework for APIs
* **BeautifulSoup4** – For parsing HTML content
* **Requests** – For fetching web pages
* **Vercel** – For deployment and serverless hosting

---

## 📁 Folder Structure

```
├── main.py             # FastAPI app with /download route
├── notice_scrape.py    # Scraping logic using requests + BeautifulSoup
├── requirements.txt    # Python dependencies
```

---

## 📄 `requirements.txt`

```txt
fastapi
beautifulsoup4
requests
```

---

## ⚠️ Disclaimer

This project is **not affiliated with MMMUT**. It simply scrapes publicly available data. If the MMUT website structure changes, the scraper may need updates.

---

## 🤝 Contributing

Have an idea or improvement? You're welcome to:

* Fork the repo
* Open an issue or PR
* Suggest features or enhancements

---