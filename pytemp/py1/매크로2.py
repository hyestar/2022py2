
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
chrome_path = 'C:\py_test2\chromedriver.exe' # 크롬드라이버 경로
url = 'https://movie.naver.com/movie/running/current.naver'
browser = webdriver.Chrome(chrome_path)
browser.get(url)
browser.find_element_by_css_selector('#content > div.article > div:nth-child(1) > div.lst_wrap > ul > li:nth-child(1) > dl > dt > a').text