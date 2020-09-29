__author__ = 'r mostafin'
from model.goods import Goods


def test_modify_goods(app):
    app.goods.add_first_item_in_cart(Goods(number='5'))
    app.goods.modify_number_in_order(Goods(number='9'))
