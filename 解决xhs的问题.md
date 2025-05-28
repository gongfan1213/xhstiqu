你可以这样在 `xhs_api.py` 里配置 webshare 代理（以第一个代理为例）：

---

### 1. 代理信息整理

- 代理地址：198.23.239.134
- 端口：6540
- 用户名：nbedpcuw
- 密码：u0w2acmb90yw

代理格式为：
```
http://nbedpcuw:u0w2acmb90yw@198.23.239.134:6540
```

---

### 2. 修改 `xhs_api.py` 关键代码

找到如下位置（大约在 20 行左右）：

```python
co = ChromiumOptions()
co.set_argument('--no-sandbox')
co.set_argument('--headless=new')
co.set_argument('--disable-gpu')
co.set_argument('--disable-dev-shm-usage')
co.set_argument('--disable-web-security')
co.set_argument('--disable-features=IsolateOrigins,site-per-process')
co.set_argument('--disable-blink-features=AutomationControlled')
co.set_argument('--window-size=1920,1080')
```

**在这些参数后面加上：**

```python
# 设置webshare代理
proxy = "http://nbedpcuw:u0w2acmb90yw@198.23.239.134:6540"
co.set_argument(f'--proxy-server={proxy}')
```

---

### 3. 完整示例片段

```python
co = ChromiumOptions()
co.set_argument('--no-sandbox')
co.set_argument('--headless=new')
co.set_argument('--disable-gpu')
co.set_argument('--disable-dev-shm-usage')
co.set_argument('--disable-web-security')
co.set_argument('--disable-features=IsolateOrigins,site-per-process')
co.set_argument('--disable-blink-features=AutomationControlled')
co.set_argument('--window-size=1920,1080')

# 设置webshare代理
proxy = "http://nbedpcuw:u0w2acmb90yw@198.23.239.134:6540"
co.set_argument(f'--proxy-server={proxy}')
```

---

### 4. 保存、上传并重启服务

1. 保存文件
2. 上传到服务器
3. 重启服务

---

### 5. 代理轮换

如果需要切换代理，只需更换 `proxy` 变量的内容即可。

---

如需我帮你直接生成完整代码片段，请告知！  
如果遇到认证弹窗或代理无效，请反馈报错信息，我帮你继续排查。
