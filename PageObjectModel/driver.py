from selenium import webdriver


class Driver:
    def __init__(self, browser = "Chrome", path = "D:/AUTOMATION TESTING COURSE/PythonTesting-main/PageObjectModel/Resources/chromedriver.exe"):
        self._browser = browser
        self._path = path

    def get_driver(self):
        if self._browser == "Chrome":
            return webdriver.Chrome(self._path)

    def open_url(self, url):
        self.get_driver().get(url)   #metoda pachetului selenium acesibila prin webdriver

    def quit_test(self):
        self.get_driver().quit()

    #close(), spre deosebire de quit() (inchide tot browserul), inchide doar fereastra activa(curenta)