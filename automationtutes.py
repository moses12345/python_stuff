from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path=r"D:\my_projectsandall\pyhon_stuff\chromedriver.exe")
driver.get("https://www.eduonix.com/")

driver.find_elements_by_link_text("LOG IN").click()











