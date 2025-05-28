from fastapi import FastAPI, Query
from DrissionPage import ChromiumPage, ChromiumOptions
import time
from fastapi.responses import JSONResponse
import logging
import sys
import traceback

# 配置日志
logging.basicConfig(
    level=logging.DEBUG,  # 改为DEBUG级别以显示更多信息
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

try:
    app = FastAPI()
    logger.info("FastAPI应用创建成功")

    # 配置Chrome选项
    logger.info("开始配置Chrome选项...")
    co = ChromiumOptions()
    co.set_argument('--no-sandbox')  # Linux系统必需
    co.set_argument('--headless=new')  # 无界面模式
    co.set_argument('--disable-gpu')  # 禁用GPU加速
    co.set_argument('--disable-dev-shm-usage')  # 禁用/dev/shm使用
    co.set_argument('--disable-web-security')  # 禁用同源策略
    co.set_argument('--disable-features=IsolateOrigins,site-per-process')  # 禁用站点隔离
    co.set_argument('--disable-blink-features=AutomationControlled')  # 禁用自动化控制检测
    co.set_argument('--window-size=1920,1080')  # 设置窗口大小

    # 设置webshare代理
    proxy = "http://nbedpcuw:u0w2acmb90yw@198.23.239.134:6540"
    co.set_argument(f'--proxy-server={proxy}')

    logger.info("Chrome选项配置完成")

    # 使用配置创建页面
    logger.info("正在初始化Chrome浏览器...")
    page = ChromiumPage(co)
    # 设置页面超时时间
    page.set.timeouts(30, 30, 30)  # 页面加载、脚本执行、元素等待超时时间都设为30秒
    logger.info("Chrome浏览器初始化完成")

    # 检查代理是否生效
    logger.info("检查代理是否生效，访问httpbin.org/ip ...")
    page.get("http://httpbin.org/ip")
    with open("proxy_check.html", "w", encoding="utf-8") as f:
        f.write(page.html)
    logger.info(f"代理检测页面内容已保存到 proxy_check.html")

    # 设置cookie
    cookie_str = "abRequestId=64c4b337-8610-5b62-ab45-5b57206a1b43; xsecappid=xhs-pc-web; a1=196f091dedf2muagwsqnzt07h3weu50k6xdbhxd0d50000223298; webId=fa2345bf32be117abf942d2b77ea2152; gid=yjKi8jydj2KiyjKi8jyfdCCffiJ670kEMAIuf8f98WxqED28d728Tx888JJqJjY8jK8y8fKi; webBuild=4.64.0; acw_tc=0ad6fbc417484229618205469e391269b311fac59b7fa39013cac8a7d26e2f; websectiga=8886be45f388a1ee7bf611a69f3e174cae48f1ea02c0f8ec3256031b8be9c7ee; sec_poison_id=e2aff3fa-ebfa-4128-8d32-1218606fd12a; web_session=040069b2fdc2f52f159e689a033a4be8a1f773; loadts=1748423208747"
    page.set.cookies(cookie_str)
    logger.info("已设置小红书cookie")

    @app.get("/")
    async def root():
        return {"message": "服务正在运行"}

    @app.get("/extract")
    async def extract(url: str = Query(..., description="小红书笔记URL")):
        try:
            logger.info(f"开始处理URL: {url}")
            # 访问目标url并保存页面源码
            logger.info(f"访问目标URL: {url}")
            page.get(url)
            with open("debug.html", "w", encoding="utf-8") as f:
                f.write(page.html)
            logger.info("已保存目标页面源码到 debug.html")
            
            # 等待页面加载
            time.sleep(3)
            
            # 尝试多个可能的选择器
            title = None
            content = None
            
            # 更新xpath选择器（如需调整请用F12重新获取）
            title_selectors = [
                'xpath://div[@id="detail-title"]',
                'xpath://h1[@class="title"]',
                'xpath://div[contains(@class, "title")]'
            ]
            
            logger.info("开始查找标题...")
            for selector in title_selectors:
                title_element = page.ele(selector)
                if title_element:
                    title = title_element.text
                    logger.info(f"找到标题: {title}")
                    break
                
            # 尝试不同的内容选择器
            content_selectors = [
                'xpath://span[@class="note-text"]',
                'xpath://div[contains(@class, "content")]',
                'xpath://div[contains(@class, "note-content")]'
            ]
            
            logger.info("开始查找内容...")
            for selector in content_selectors:
                content_element = page.ele(selector)
                if content_element:
                    content = content_element.text
                    logger.info("找到内容")
                    break
            
            if not title and not content:
                logger.error("未找到标题和内容")
                return JSONResponse(
                    status_code=404,
                    content={"error": "未找到内容，可能是页面结构变化或需要登录"}
                )
            
            return {
                "title": title or "未找到标题",
                "content": content or "未找到内容"
            }
            
        except Exception as e:
            logger.error(f"处理URL时出错: {str(e)}")
            logger.error(f"错误详情: {traceback.format_exc()}")
            return JSONResponse(
                status_code=500,
                content={"error": f"处理请求时出错: {str(e)}"}
            )

    if __name__ == "__main__":
        import uvicorn
        logger.info("正在启动服务...")
        try:
            uvicorn.run(
                app, 
                host="0.0.0.0", 
                port=3334, 
                log_level="debug",
            )
        except Exception as e:
            logger.error(f"启动服务时出错: {str(e)}")
            logger.error(f"错误详情: {traceback.format_exc()}")
            raise

except Exception as e:
    logger.error(f"程序初始化时出错: {str(e)}")
    logger.error(f"错误详情: {traceback.format_exc()}")
    raise