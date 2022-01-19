import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.execute_script("window.open('http://google.com','_self')")

time.sleep(3)

