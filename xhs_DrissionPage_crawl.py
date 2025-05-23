from DrissionPage import ChromiumPage
import time
import csv
from url_process import generate_urls
import logging

# 配置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

name_lst = []
content_lst = []

# 调用函数，处理文件
generate_urls('input.txt', 'xhs_urls.txt')

def read_file_to_list(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        content_list = [line.strip() for line in file]
    return content_list

urls = read_file_to_list('xhs_urls.txt')
page = ChromiumPage()

def get_data(url):
    try:
        page.get(url)
        time.sleep(5)  # 等待页面加载
        
        # 获取标题
        title_element = page.ele('xpath://div[@id="detail-title"]')
        if not title_element:
            logging.warning(f"未找到标题元素: {url}")
            return
            
        title = title_element.text
        name_lst.append(title)
        
        # 获取正文
        content_element = page.ele('xpath://span[@class="note-text"]')
        content = content_element.text if content_element else 'None'
        content_lst.append(content)
        
        logging.info(f"成功抓取笔记: {title}")
        
    except Exception as e:
        logging.error(f"处理URL时出错 {url}: {str(e)}")

def __main__():
    try:
        for i, url in enumerate(urls):
            logging.info(f'正在爬取第 {i+1}/{len(urls)} 个URL: {url}')
            get_data(url)
            
        # 保存数据到CSV
        filename = 'xhs_data.csv'
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Name', 'content'])
            
            for i in range(len(name_lst)):
                writer.writerow([name_lst[i], content_lst[i]])
                
        logging.info(f'数据已成功写入 {filename}')
        
    except Exception as e:
        logging.error(f"程序执行出错: {str(e)}")

if __name__ == '__main__':
    __main__()