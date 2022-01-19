import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.driver import ChromeDriver

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.hyrtutorials.com/p/html-dropdown-elements-practice.html")
se=driver.find_element(By.ID,"course")
d=Select(se)
d.select_by_index(1)
v=driver.find_element(By.ID,"course").get_attribute("value")
print(v)
time.sleep(3)
