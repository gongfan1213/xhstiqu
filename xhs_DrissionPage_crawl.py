from DrissionPage import ChromiumPage
import time
import csv
from url_process import generate_urls
import logging
from tqdm import tqdm
import random
import os

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('crawler.log', encoding='utf-8'),
        logging.StreamHandler()
    ]
)

class XHSCrawler:
    def __init__(self):
        self.name_lst = []
        self.content_lst = []
        self.page = ChromiumPage()
        self.max_retries = 3
        self.delay_range = (3, 7)  # 随机延迟范围（秒）

    def read_file_to_list(self, filename):
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                return [line.strip() for line in file if line.strip()]
        except Exception as e:
            logging.error(f"读取文件 {filename} 失败: {str(e)}")
            return []

    def random_delay(self):
        delay = random.uniform(*self.delay_range)
        time.sleep(delay)

    def get_data(self, url, retry_count=0):
        try:
            self.page.get(url)
            self.random_delay()
            
            # 获取标题
            title_element = self.page.ele('xpath://div[@id="detail-title"]')
            if not title_element:
                if retry_count < self.max_retries:
                    logging.warning(f"未找到标题元素，第 {retry_count + 1} 次重试: {url}")
                    return self.get_data(url, retry_count + 1)
                logging.error(f"多次尝试后仍未找到标题元素: {url}")
                return False
                
            title = title_element.text.strip()
            
            # 获取正文
            content_element = self.page.ele('xpath://span[@class="note-text"]')
            content = content_element.text.strip() if content_element else 'None'
            
            self.name_lst.append(title)
            self.content_lst.append(content)
            
            logging.info(f"成功抓取笔记: {title}")
            return True
            
        except Exception as e:
            if retry_count < self.max_retries:
                logging.warning(f"处理URL出错，第 {retry_count + 1} 次重试: {url}")
                return self.get_data(url, retry_count + 1)
            logging.error(f"处理URL失败 {url}: {str(e)}")
            return False

    def save_to_csv(self, filename='xhs_data.csv'):
        try:
            with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(['标题', '内容'])
                
                for i in range(len(self.name_lst)):
                    writer.writerow([self.name_lst[i], self.content_lst[i]])
                    
            logging.info(f'数据已成功写入 {filename}')
            return True
        except Exception as e:
            logging.error(f"保存CSV文件失败: {str(e)}")
            return False

    def run(self):
        try:
            # 确保输入文件存在
            if not os.path.exists('input.txt'):
                logging.error("input.txt 文件不存在")
                return False

            # 生成URL文件
            generate_urls('input.txt', 'xhs_urls.txt')
            
            # 读取URL列表
            urls = self.read_file_to_list('xhs_urls.txt')
            if not urls:
                logging.error("没有找到有效的URL")
                return False

            # 使用tqdm显示进度
            for i, url in enumerate(tqdm(urls, desc="爬取进度")):
                logging.info(f'正在爬取第 {i+1}/{len(urls)} 个URL: {url}')
                self.get_data(url)
                
            # 保存数据
            return self.save_to_csv()
            
        except Exception as e:
            logging.error(f"程序执行出错: {str(e)}")
            return False
        finally:
            self.page.quit()

def main():
    crawler = XHSCrawler()
    success = crawler.run()
    if success:
        logging.info("爬虫任务完成")
    else:
        logging.error("爬虫任务失败")

if __name__ == '__main__':
    main()