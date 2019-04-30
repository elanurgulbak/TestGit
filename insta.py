from selenium import webdriver
import time


browser = webdriver.Firefox(executable_path="C:/Users/elanurgulbak/Desktop/geckodriver.exe")
browser.get("https://www.instagram.com")
time.sleep(10)
giris_yap = browser.find_element_by_xpath("/html/body/span/section/main/"
                                        "article/div[2]/div[2]/p/a")
giris_yap.click()
time.sleep(2)
username=browser.find_element_by_name("username")
password=browser.find_element_by_name("password")
username.send_keys("xxxxx")
password.send_keys("xxxxx")
time.sleep(5)
giris_yap2 = browser.find_element_by_xpath("/html/body/span/section/main/div/article/"
                                         "div/div[1]/div/form/div[3]")
giris_yap2.click()
time.sleep(10)
browser.close()
