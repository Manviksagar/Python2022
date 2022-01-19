import datetime
import os
import time
from select import select


from selenium import webdriver
from selenium.webdriver import Keys

va=3
for i in range(1,13):

    print(f"{va}*{i} = " + str(va*i))

print(datetime.datetime.today())
os.path
driver = webdriver.Chrome(executable_path="C:\\Users\\Va185060\\Downloads\\chromedriver.exe")
driver.get('https://www.google.com')
driver.find_element_by_name("q").send_keys("Sagar",Keys.ENTER)




