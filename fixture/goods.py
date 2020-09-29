__author__ = 'rmostafin'


class GoodsHelper:

    def __init__(self, app):
        self.app = app

    def order_in(self, user_contacts):
        wd = self.app.wd
        self.app.open_cart()
        self.fill_user_contacts_form(user_contacts)
        wd.find_elements_by_name('_csrf')[1].click()

    def fill_user_contacts_form(self, user_contacts):
        wd = self.app.wd
        if user_contacts.phone is not None:
            wd.find_element_by_id('InputPhone').send_keys(user_contacts.phone)
        if user_contacts.address is not None:
            wd.find_element_by_id('InputAddr').send_keys(user_contacts.address)

    def add_first_item_in_cart(self, goods):
        wd = self.app.wd
        self.app.open_goods()
        wd.find_element_by_id('exampleCount').send_keys(goods.number)
        wd.find_element_by_css_selector('[class="btn btn-primary"]').click()

    def modify_number_in_order(self, new_goods_data):
        wd = self.app.wd
        self.app.open_cart()
        wd.find_element_by_css_selector('[name*="item_"]').clear()
        wd.find_element_by_css_selector('[name*="item_"]').send_keys(new_goods_data.number)

