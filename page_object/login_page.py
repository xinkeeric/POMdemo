'''
    LoginPage：登录页，只为系统的登录业务而生成的页面对象
'''
from time import sleep

from selenium import webdriver

from basePage.base_page import BasePage


# 登录页
class LoginPage(BasePage):
    '''
        页面对象的模板
            1.url
            2.关键元素
            3.行为
    '''
    # URL
    URL= 'http://shop-xo.hctestedu.com/index.php?s=/index/user/logininfo.html'
    # 关键元素
    username = ('name', 'accounts')
    password = ('name', 'pwd')
    login_button =('xpath','//button[text()="登录"]')

    #行为
    def login(self,user,pwd):
        # 访问登录页
        self.toOpen(self.URL)
        # 输入账号密码
        self.input(self.username, user)
        self.input(self.password, pwd)
        sleep(3)
        # 点击登录按钮
        self.click(self.login_button)
        sleep(5)


# 调试
if __name__ == '__main__':
    driver = webdriver.Chrome()
    user ='eric_test'
    pwd = '123456'
    lp = LoginPage(driver)
    lp.login(user,pwd)