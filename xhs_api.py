from fastapi import FastAPI, Query
from DrissionPage import ChromiumPage
import time

app = FastAPI()
page = ChromiumPage()

@app.get("/extract")
def extract(url: str = Query(..., description="小红书笔记URL")):
    try:
        page.get(url)
        time.sleep(5)
        title_element = page.ele('xpath://div[@id="detail-title"]')
        if not title_element:
            return {"error": "未找到标题"}
        title = title_element.text
        content_element = page.ele('xpath://span[@class="note-text"]')
        content = content_element.text if content_element else 'None'
        return {"title": title, "content": content}
    except Exception as e:
        return {"error": str(e)}