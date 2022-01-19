import allure
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def before_scenario(context,scenario):
    print("befor Scenario")
    #context.driver=webdriver.Chrome(ChromeDriverManager().install())
    context.driver=webdriver.Chrome(executable_path="C:\\Users\\Va185060\\Downloads\\chromedriver_win32 (96)\\chromedriver.exe")

def after_scenario(context,scenario):
    print("quitting after scenario")


def after_step(context, step):
    print()
    if(step.status=='failed'):
        allure.attach(context.driver.get_screenshot_as_png(),name="screenshot",attachment_type=allure.attachment_type.PNG)
