import requests
from allure_commons._allure import step
from selene import browser
from helpers.ui import ui_methods
from utils.attach import log_to_allure

MAIN_URL = 'https://demowebshop.tricentis.com'
LOGIN = 'biba_boba@example.com'
PASSWORD = 'qwerty12345'


def test_add_to_cart_one_product():
    with step("Add product to cart from API"):
        response = requests.post(
            url=MAIN_URL + '/addproducttocart/catalog/31/1/1',
            data={"Email": LOGIN, "Password": PASSWORD, "RememberMe": False},
            allow_redirects=False)
        log_to_allure(response)

    with step("Get cookie from API"):
        cookie_cart = response.cookies.get("Nop.customer")

    with step("Set Cookie through UI"):
        browser.open("https://demowebshop.tricentis.com/")
        browser.driver.add_cookie({"name": "Nop.customer", "value": cookie_cart})
        browser.open("https://demowebshop.tricentis.com/")

    with step("Check through UI count of a products in a cart title at header"):
        browser.open("https://demowebshop.tricentis.com/books")
        ui_methods.check_quantity_of_cart_icon(1)

    with step("Open a cart"):
        browser.open(MAIN_URL + "/cart")

    with step("Check products in a cart"):
        ui_methods.check_quantity_of_cart_icon(1)
        ui_methods.check_cart(1)

    with step("Check product name and price UI"):
        ui_methods.check_product_by_name('14.1-inch Laptop')
        ui_methods.check_price_of_product('1590.00')


def test_add_to_cart_few_products():
    pass