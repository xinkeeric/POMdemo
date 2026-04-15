'''
    CartPage： 购物车页面，校验商品是否添加成功
'''
from basePage.base_page import BasePage


class CartPage(BasePage):
    URL = 'http://shop-xo.hctestedu.com/index.php?s=/index/cart/index.html'

    goods = ('xpath','//a[contains(text(),"iPhone")]')

    def cart_info(self):
        self.toOpen(self.URL)
        self.wait(self.goods)