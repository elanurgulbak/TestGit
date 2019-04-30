from selenium import webdriver
import time


browser = webdriver.Firefox(executable_path="C:/Users/elanurgulbak/Desktop/geckodriver.exe")
browser.get("https://www.instagram.com")
time.sleep(10)
giris_yap = browser.find_element_by_xpath("/html/body/span/section/main/"
                                        "article/div[2]/div[2]/p/a")
giris_yap.click()

time.sleep(10)
browser.close()
