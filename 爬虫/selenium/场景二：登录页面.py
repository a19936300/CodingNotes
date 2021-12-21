# 本场景知识点
# 1.获取节点信息
# 2.节点交互
# 3.浏览器前进后退
from selenium import webdriver

# chromeDriver地址
chrome_driver_path = r"G:\OtherApp\anaconda\envs\py36\chromedriver.exe"
#获取浏览器对象
browser = webdriver.Chrome(executable_path=chrome_driver_path)
try:
    # 请求内容
    browser.get("http://localhost:9980/foodie-shop/login.html")
    # 获取
    userInput = browser.find_element_by_id("user")
    userInput.send_keys("sa")
    passInput = browser.find_element_by_id("password")
    passInput.send_keys("123123")
    # 节点交互
    submit = browser.find_element_by_class_name("am-btn")
    submit.click()
    # 获取cookie
    current_browser = browser.window_handles
    browser.switch_to_window(current_browser[0])
    cookies = browser.get_cookies()
    cookie = browser.get_cookie("user")
    print(cookies)
    print(cookie)
finally:
    #browser.close()
    print("1111111111")