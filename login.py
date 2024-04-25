import re
import json
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import logging
logger = logging.getLogger(__name__)

def deal_cookies(raw):
    cookies = ""
    for i in raw:
        cookies += i["name"] + "=" + i["value"] + "; "
    return cookies

def get_login(headless=False):
    if not os.path.exists("user_data.json"):
        t =  open("user_data.json","w")
        t.write("{}")
        t.close()
        logger.info("初始化成功!")
        os.system("pause")
        exit()
    with open("./user_data.json") as r:
        config = json.load(r)
    if headless:
        logger.info("请扫码登录")
        import requests
        import requests.utils
        import qrcode
        import time
        headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 13; M2102K1AC Build/TKQ1.220829.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 XWEB/5317 MMWEBSDK/20230805 MMWEBID/5924 MicroMessenger/8.0.42.2460(0x28002A58) WeChat/arm64 Weixin NetType/5G Language/zh_CN ABI/arm64 MiniProgramEnv/android"
        }
        session = requests.session()
        session.get("https://www.bilibili.com/", headers=headers)
        generate = session.get("https://passport.bilibili.com/x/passport-login/web/qrcode/generate", headers=headers)
        generate = generate.json()
        if generate['code'] == 0:
            url = generate['data']['url']
        else:
            logger.error("服务器不知道送来啥东西")
            logger.error(json.dumps(generate,indent=4))
            exit()
        qr = qrcode.QRCode()
        qr.add_data(url)
        qr.print_ascii(invert=True)
        while True:
            time.sleep(1)
            url = "https://passport.bilibili.com/x/passport-login/web/qrcode/poll?source=main-fe-header&qrcode_key="+generate['data']['qrcode_key']
            req = session.get(url, headers=headers)
            # read as utf-8
            check = req.json()["data"]
            if check['code'] == 0:
                logger.info("登录成功")
                cookies_dict = requests.utils.dict_from_cookiejar(session.cookies)
                cookies=""
                for k,v in cookies_dict.items():
                    cookies += k + "=" + v + "; "
                user = session.get("https://api.bilibili.com/x/web-interface/nav", headers=headers)
                if user.status_code == 412:
                    logger.warning("被412风控，过一会再试试看吧")
                user = user.json()
                if (user["data"]["isLogin"]):
                    username=user["data"]["uname"]
                    uid=user["data"]["mid"]
                    config[uid] = [username, cookies]
                    logger.info("cookie已保存\n运行结束\n")
                    with open("./user_data.json", "w") as f:
                        json.dump(config, f, indent=2)
                        f.flush()
                        return config
                else:
                    logger.error("登录失败")
                    exit()
                break
            elif check['code'] == 86101:
                logger.info("代码86101")
            elif check['code'] == 86090:
                logger.info(check["message"])
            elif check['code'] == 86083:
                logger.info(check["message"])
                exit()
            elif check['code'] == 86038:
                logger.info(check["message"])
                exit()
            else:
                logger.info("不知道什么状态码，保险起见，退出")
                logger.error(check["message"])
                exit()
    logger.info("请在网页端登录b站\n")
    options = webdriver.EdgeOptions()
    options.add_argument("--log-level=3")
    WebDriver = webdriver.Edge(options=options)
    WebDriver.get("https://show.bilibili.com/")
    WebDriver.find_element(By.CLASS_NAME, "nav-header-register").click()
    while True:
        sleep(0.1)
        if WebDriver.page_source==None or "登录" not in WebDriver.page_source:
            break
    logger.info("登录成功\n")
    cookies = WebDriver.get_cookies()
    
    WebDriver.get("https://account.bilibili.com/account/home")
    username = WebDriver.find_element(By.CLASS_NAME, "home-top-msg-name").text
    userid = re.search(r"/\d{1,30}/",WebDriver.find_element(By.CLASS_NAME, "home-to-space").get_attribute("href")).group()[1:-1]
    config[userid] = [username,deal_cookies(cookies)]

    WebDriver.quit()
    logger.info("cookie已保存\n运行结束\n")
    with open("./user_data.json", "w") as f:
        json.dump(config, f, indent=2)
        f.flush()
    return config
    # os.system("pause")

if __name__ == '__main__':
    get_login()