from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
chrome_path = 'C:\py_test2\chromedriver.exe' # 크롬드라이버 경로
url = 'https://www.naver.com/'
browser = webdriver.Chrome(chrome_path)
browser.get(url)
seachbox = browser.find_element_by_xpath('//*[@id="query"]')
seachbox.send_keys("코리아it학원")
seachbox.send_keys(Keys.ENTER)
browser.find_element_by_xpath('//*[@id="web_1"]/div/div[2]/div[2]/a').click()