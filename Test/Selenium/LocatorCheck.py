import time

import webdriver_manager
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://google.com")
driver.maximize_window()
t=driver.find_element(By.NAME,"btnK").get_attribute("value")
time.sleep(2)
print(t)
print(s)
driver.find_element(By.NAME,"q").send_keys("Sagar",Keys.ENTER)
time.sleep(2)
print(driver.current_url)


