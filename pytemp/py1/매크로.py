from selenium import webdriver
import time
chrome_path = 'C:\py_test2\chromedriver.exe' # 크롬드라이버 경로
url = 'https://codepen.io/'   # 들어가고 싶은 url
id = '0109jhs@naver.com'
pw = 'koreait11'
browser = webdriver.Chrome(chrome_path)
browser.get(url)
time.sleep(3)
browser.find_element_by_xpath('//*[@id="react-page"]/div[1]/a[2]').click()
time.sleep(2)
browser.find_element_by_xpath('//*[@id="login-email-field"]').send_keys(id)
time.sleep(2)
browser.find_element_by_css_selector('#login-password-field').send_keys(pw)
time.sleep(2)
browser.find_element_by_xpath('//*[@id="log-in-button"]').click()