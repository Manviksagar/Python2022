from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="C:\\Users\\Va185060\\Downloads\\chromedriver.exe")
driver.get("https://www.google.com/")
driver.fullscreen_window()


driver.find_element(By.NAME,"q").send_keys("Sagar")
time.sleep(10)

driver.quit()