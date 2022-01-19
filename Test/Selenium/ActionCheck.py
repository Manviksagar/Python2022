import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.hyrtutorials.com/p/window-handles-practice.html")
driver.maximize_window()
time.sleep(3)
wb=driver.find_element(By.ID,'newWindowBtn')
action=ActionChains(driver)
time.sleep(3)
action.move_to_element(wb).context_click().perform()

time.sleep(4)
driver.close()