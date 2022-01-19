from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://training.openspan.com/login")
driver.maximize_window()
check=driver.find_element(By.XPATH,"//input[@id='login_button']").is_enabled()
print(check)

