'''
    手机商品详情页：PhonePage，主要显示手机的商品详情内容，用于执行对应的操作行为
'''
from time import sleep

from selenium import webdriver

from basePage.base_page import BasePage

class PhonePage(BasePage):
    '''
        页面对象的模板
            1.url
            2.关键元素
            3.行为
    '''
    # URL
    URL= 'http://shop-xo.hctestedu.com/index.php?s=/index/goods/index/id/2.html'
    # 关键元素
    suite = ('xpath','//li[@data-value = "套餐一"]')
    color = ('xpath','//li[@data-value = "金色"]')
    memory = ('xpath','//li[@data-value = "128G"]')
    add_cart_button = ('xpath','//button[@title= "加入购物车"]')

    #添加购物车行为
    def add_cart(self):
        # 访问登录页
        self.toOpen(self.URL)
        # 选择商品属性
        self.click(self.suite)
        self.sleep(1)
        self.click(self.color)
        self.sleep(2)
        self.click(self.memory)
        self.sleep(1)
        # 点击添加购物车
        self.click(self.add_cart_button)
        self.sleep(1)
# 调试
if __name__ == '__main__':
    driver = webdriver.Chrome()
    pp = PhonePage(driver)
    pp.add_cart()