# xhstiqu
```js
admin@DESKTOP-KNJMU3O MINGW64 /d/xhstiqu (main)
$ python xhs_api.py
2025-05-28 16:06:07,834 - INFO - FastAPI应用创建成功
2025-05-28 16:06:07,835 - INFO - 开始配置Chrome选项...
2025-05-28 16:06:07,836 - INFO - Chrome选项配置完成
2025-05-28 16:06:07,836 - INFO - 正在初始化Chrome浏览器...
2025-05-28 16:06:07,837 - DEBUG - Converted retries value: 0 -> Retry(total=0, connect=None, read=None, redirect=None, status=None)
2025-05-28 16:06:07,837 - DEBUG - Converted retries value: 0 -> Retry(total=0, connect=None, read=None, redirect=None, status=None)
2025-05-28 16:06:07,838 - DEBUG - Starting new HTTP connection (1): 127.0.0.1:9222  
2025-05-28 16:06:07,839 - DEBUG - http://127.0.0.1:9222 "GET /json HTTP/1.1" 200 2890
2025-05-28 16:06:07,840 - DEBUG - Converted retries value: 0 -> Retry(total=0, connect=None, read=None, redirect=None, status=None)
2025-05-28 16:06:07,840 - DEBUG - Converted retries value: 0 -> Retry(total=0, connect=None, read=None, redirect=None, status=None)
2025-05-28 16:06:07,840 - DEBUG - Starting new HTTP connection (1): 127.0.0.1:9222  
2025-05-28 16:06:07,842 - DEBUG - http://127.0.0.1:9222 "GET /json/version HTTP/1.1" 200 431
2025-05-28 16:06:09,017 - DEBUG - Converted retries value: 0 -> Retry(total=0, connect=None, read=None, redirect=None, status=None)
2025-05-28 16:06:09,018 - DEBUG - Converted retries value: 0 -> Retry(total=0, connect=None, read=None, redirect=None, status=None)
2025-05-28 16:06:09,019 - DEBUG - Starting new HTTP connection (1): 127.0.0.1:9222  
2025-05-28 16:06:09,527 - DEBUG - http://127.0.0.1:9222 "GET /json HTTP/1.1" 200 1428
2025-05-28 16:06:09,529 - DEBUG - Converted retries value: 0 -> Retry(total=0, connect=None, read=None, redirect=None, status=None)
2025-05-28 16:06:09,529 - DEBUG - Converted retries value: 0 -> Retry(total=0, connect=None, read=None, redirect=None, status=None)
2025-05-28 16:06:09,530 - DEBUG - Starting new HTTP connection (1): 127.0.0.1:9222
2025-05-28 16:06:09,532 - DEBUG - http://127.0.0.1:9222 "GET /json/version HTTP/1.1" 200 431
2025-05-28 16:06:09,537 - DEBUG - Converted retries value: 0 -> Retry(total=0, connect=None, read=None, redirect=None, status=None)
2025-05-28 16:06:09,537 - DEBUG - Converted retries value: 0 -> Retry(total=0, connect=None, read=None, redirect=None, status=None)
2025-05-28 16:06:09,538 - DEBUG - Starting new HTTP connection (1): 127.0.0.1:9222
2025-05-28 16:06:09,540 - DEBUG - http://127.0.0.1:9222 "GET /json HTTP/1.1" 200 1428
2025-05-28 16:06:09,707 - INFO - 正在启动服务...
2025-05-28 16:06:09,717 - DEBUG - Using proactor: IocpProactor
INFO:     Started server process [39368]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:3334 (Press CTRL+C to quit)
INFO:     127.0.0.1:58142 - "GET / HTTP/1.1" 200 OK
INFO:     127.0.0.1:58142 - "GET /favicon.ico HTTP/1.1" 404 Not Found
INFO:     127.0.0.1:58143 - "GET /docs HTTP/1.1" 200 OK
INFO:     127.0.0.1:58143 - "GET /openapi.json HTTP/1.1" 200 OK
INFO:     127.0.0.1:58178 - "GET /docs HTTP/1.1" 200 OK
INFO:     127.0.0.1:58178 - "GET /openapi.json HTTP/1.1" 200 OK
2025-05-28 16:07:10,288 - INFO - 开始处理URL: https://www.xiaohongshu.com/explore/67e211df000000001e000463?note_flow_source=wechat&xsec_token=ABQy-L4K2mu_uBO-5f-B4MWveae211df000000001e000463?nr1fDKGp1J6RTi-VX844=
2025-05-28 16:07:11,649 - INFO - 页面加载完成
2025-05-28 16:07:14,650 - INFO - 开始查找标题...
2025-05-28 16:07:14,672 - INFO - 找到标题: 破双非是我的案底
2025-05-28 16:07:14,672 - INFO - 开始查找内容...
2025-05-28 16:07:14,677 - INFO - 找到内容
INFO:     127.0.0.1:58280 - "GET /extract?url=https%3A%2F%2Fwww.xiaohongshu.com%2Fexplore%2F67e211df00000000plore%2F67e211df000000001e000463%3Fnote_flow_source%3Dwechat%26xsec_token%3DABQy-L4Kp1J6RTi-VX844%3D HTTP/1.2mu_uBO-5f-B4MWvear1fDKGp1J6RTi-VX844%3D HTTP/1.1" 200 OK
```

BlueFocus-小红书提取链接当中的题目和内容


提取这个url当中题目和内容

https://www.xiaohongshu.com/explore/67e211df000000001e000463?note_flow_source=wechat&xsec_token=ABQy-L4K2mu_uBO-5f-B4MWvear1fDKGp1J6RTi-VX844=


![image](https://github.com/user-attachments/assets/e496c7ee-dcc7-4ba6-809f-05b14a8fb1c8)


![image](https://github.com/user-attachments/assets/2eb55241-a2ab-444e-a704-64f0257c5797)


results

![image](https://github.com/user-attachments/assets/3a4afd3c-36cf-4ad2-a80b-0b1a4e8114dc)
