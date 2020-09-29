__author__ = 'rmostafin'
from model.user_contacts import UserContacts
from model.goods import Goods


def test_order_goods(app):
    app.goods.add_first_item_in_cart(Goods(number='5'))
    app.goods.order_in(UserContacts(phone='99999999999', address='New York. Komsomolsckay Street 16'))
