'''
    测试用例类：所有的测试代码都在该类实现
'''


import unittest
from time import sleep

from selenium import webdriver

from page_object.cart_page import CartPage
from page_object.login_page import LoginPage
from page_object.phone_page import PhonePage

from ddt import ddt,file_data


@ddt
class Cass(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()
        cls.lp = LoginPage(cls.driver)
        cls.pp = PhonePage(cls.driver)
        cls.cp = CartPage(cls.driver)
    # def test_login(self):
    #     # driver = webdriver.Chrome()
    #     # lp = LoginPage(driver)
    #     # pp = PhonePage(driver)
    #     # cp = CartPage(driver)
    #
    #     user = 'eric_test'
    #     pwd = '123456'
    #     lp.login(user, pwd)
    #     pp.add_cart()
    #     cp.cart_info()
    #     sleep(5)

    # 登录
    @file_data('../data/user.yaml')
    def test_01_login(self,user,pwd):
        self.lp.login(user, pwd)

    def test_02_add_cart(self):
        self.pp.add_cart()

    def test_03_cart_info(self):
        self.cp.cart_info()

if __name__ == '__main__':
    unittest.main()