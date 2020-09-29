__author__ = 'rmostafin'
from selenium.webdriver.chrome.webdriver import WebDriver
from fixture.session import SessionHelper
from fixture.goods import GoodsHelper


class Application:

    def __init__(self):
        self.wd = WebDriver('../chromedriver')
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)
        self.goods = GoodsHelper(self)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        self.wd.get('http://shop.bugred.ru/')

    def open_login_page(self):
        wd = self.wd
        wd.find_element_by_id('navbarSupportedContent') \
            .find_elements_by_css_selector('li[class="nav-item "]')[2].find_element_by_css_selector('a').click()

    def open_cart(self):
        wd = self.wd
        wd.find_element_by_css_selector('[class="nav-link "]').click()

    def open_goods(self):
        wd = self.wd
        wd.find_elements_by_css_selector('[class="col-md-4"]')[1].find_element_by_css_selector('a').click()

    def destroy(self):
        self.wd.quit()
