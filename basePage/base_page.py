'''
    POM的体系下的底层代码，用于封装各类行为操作，便于页面对象类进行调用
        根本核心是关键字驱动的设计理念
'''
import time

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


# 基类
class BasePage(object):

    def __init__(self,driver):
        self.driver = driver
        self.driver.implicitly_wait(15)

    def toOpen(self,url):
        self.driver.get(url)

    def toClose(self):
        self.driver.quit()

    def locator(self,loc):
        return self.driver.find_element(*loc)

    def click(self,loc):
        self.locator(loc).click()

    def input(self,loc,txt):
        self.locator(loc).send_keys(txt)

    def sleep(self,txt):
        time.sleep(txt)

    def wait(self,loc):
        WebDriverWait(self.driver,10,0.5).until(lambda d: self.locator(loc),message='等待失败')

    def assert_text(self,loc,txt):
        try:
            reality = self.locator(loc).text
            assert txt == self.locator(loc).text,'断言失败'
            return True
        except:
            return False