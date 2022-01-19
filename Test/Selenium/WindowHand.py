import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.hyrtutorials.com/p/window-handles-practice.html")
parent=driver.current_window_handle
print(parent)
time.sleep(3)
driver.find_element(By.ID,'newWindowBtn').click()
all=driver.window_handles
print(all)
for i in all:
    if i != parent:
        driver.switch_to.window(i)
        driver.maximize_window()
        time.sleep(4)
        driver.find_element(By.ID,'firstName').send_keys("Sagar")
        time.sleep(3)
        driver.close()
        break
driver.switch_to.window(parent)
print(driver.current_url)