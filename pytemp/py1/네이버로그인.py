from tokenize import Comment
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pyperclip
chrome_path = "C:\py_test2\chromedriver.exe"
url = "https://naver.com"

browser = webdriver.Chrome(chrome_path)
browser.get(url)
time.sleep(1)
s = browser.find_element_by_xpath("/html/body/div[2]/div[3]/div[3]/div/div[2]/a")
s.click()
# id 복사 후 입력
id = browser.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[1]/form/ul/li/div/div[1]/div[1]/input")
pyperclip.copy("0109jhs") # 아이디 입력칸
id.send_keys(Keys.CONTROL,'v')
# password 복사 후 입력
password = browser.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[1]/form/ul/li/div/div[1]/div[2]/input")
pyperclip.copy("z990109") # 비밀번호 입력칸
password.send_keys(Keys.CONTROL,'v')
browser.implicitly_wait(time_to_wait=5)
# 로그인 하기
browser.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[1]/form/ul/li/div/div[7]/button").click()

# 메일 들어가기
browser.find_element_by_xpath('/html/body/div/div/div[1]/div[1]/div/div[2]/a[1]').click()
