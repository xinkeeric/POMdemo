import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait

def open_broswer(type_):
    try:
        driver = getattr(webdriver, type_)()
        driver.maximize_window()
    except:
        driver = webdriver.Chrome(options=Options().conf_options())
    return driver
class WebKey:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)

    def toOpen(self,url):
        self.driver.get(url)

    def toClose(self):
        self.driver.quit()

    def locator(self,name,value):
        return self.driver.find_element(name,value)

    def click(self,name,value):
        self.locator(name,value).click()

    def input(self,name,value,txt):
        self.locator(name,value).send_keys(txt)

    def sleep(self,txt):
        time.sleep(txt)

    def wait(self,name,txt):
        WebDriverWait(self.driver,10,0.5).until(lambda d: d.find_element(name,txt),message='等待失败')

    def assert_text(self,name,value,txt):
        try:
            reality = self.locator(name,value).text
            assert txt == self.locator(name,value).text
            return True
        except:
            return False