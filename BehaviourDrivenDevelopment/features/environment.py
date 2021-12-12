from selenium import webdriver


def before_all(context):
    context.browser = webdriver.Chrome("D:/AUTOMATION TESTING COURSE/PythonTesting-main/PageObjectModel/Resources/chromedriver.exe")

def after_all(context):
    context.browser.quit()
