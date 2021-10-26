import img2pdf
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from PIL import Image
from fpdf import FPDF
import os


s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
driver.maximize_window()

username = ""
password = ""

url =""
driver = webdriver.Chrome("C:/Users/user/Downloads/chromedriver.exe")


driver.get(url)


driver.find_element_by_id("username").send_keys(username)
driver.find_element_by_id("password").send_keys(password)

driver.find_element_by_id("loginbtn").click()
i = 0
driver.get_screenshot_as_file('D:/sdo/' + str(i) + '.png')

while(driver.find_element_by_xpath("//*[@id=\"content\"]/div/div[3]/div[3]/button").is_enabled()):
    driver.find_element_by_xpath("//*[@id=\"content\"]/div/div[3]/div[3]/button").click()
    i+=1
    sleep(0.5)
    driver.get_screenshot_as_file('D:/sdo/' + str(i) + '.png')

i+=1
driver.get_screenshot_as_file('D:/sdo/' + str(i) + '.png')
sleep(0.5)

print("loggin succesfully")
