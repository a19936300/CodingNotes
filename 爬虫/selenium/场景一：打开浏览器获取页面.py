# 本场景知识点
# 1.获取浏览器对象
# 2.获取页面源代码
# 引入包
from selenium import webdriver

# chromeDriver地址
chrome_driver_path = r"G:\OtherApp\anaconda\envs\py36\chromedriver.exe"
#获取浏览器对象
browser = webdriver.Chrome(executable_path=chrome_driver_path)
try:
    browser.get("http://localhost:9980/foodie-shop/index.html?_ijt=snbp6r9s9t88gpvssd0471i4ou")
    print(browser.page_source)
finally:
    browser.close()