import allure
from allure_commons._allure import step
from selene import browser
from helpers.ui import ui_methods
from helpers.api import api_methods

MAIN_URL = 'https://demowebshop.tricentis.com'
LOGIN = 'biba_boba@example.com'
PASSWORD = 'qwerty12345'


@allure.title("Покупка одного товара")
def test_add_to_cart_one_product():
    with step("Добавление товара в корзину"):
        response = api_methods.add_product_to_cart(31)

    with step("Получение кук"):
        cookie_cart = response.cookies.get("Nop.customer")

    with step("Открытие браузера и применение кук"):
        browser.open("https://demowebshop.tricentis.com/")
        browser.driver.add_cookie({"name": "Nop.customer", "value": cookie_cart})
        browser.open("https://demowebshop.tricentis.com/")

    with step("Открытие каталога книги"):
        browser.open("https://demowebshop.tricentis.com/books")

    with step("Проверка, что в хедере отображается количество товаров, что находятся в корзине"):
        ui_methods.check_quantity_of_cart_icon(1)

    with step("Открытие корзины"):
        browser.open(MAIN_URL + "/cart")

    with step("Проверка количества товаров в самой корзине и в хедере"):
        ui_methods.check_quantity_of_cart_icon(1)
        ui_methods.check_cart(1)

    with step("Проверка содержимого корзины"):
        ui_methods.check_product_by_name('14.1-inch Laptop')
        ui_methods.check_price_of_product('1590.00')


@allure.title("Покупка у одного товаров нескольких позиций")
def test_add_to_cart_few_products():
    with step("Добавление товара в корзину"):
        response = api_methods.add_product_to_cart(45, 3)

    with step("Получение кук"):
        cookie_cart = response.cookies.get("Nop.customer")

    with step("Открытие браузера и применение кук"):
        browser.open("https://demowebshop.tricentis.com/")
        browser.driver.add_cookie({"name": "Nop.customer", "value": cookie_cart})
        browser.open("https://demowebshop.tricentis.com/")

    with step("Открытие каталога книги"):
        browser.open("https://demowebshop.tricentis.com/books")

    with step("Проверка, что в хедере отображается количество товаров, что находятся в корзине"):
        ui_methods.check_quantity_of_cart_icon(3)

    with step("Открытие корзины"):
        browser.open(MAIN_URL + "/cart")

    with step("Проверка количества товаров в самой корзине и в хедере"):
        ui_methods.check_quantity_of_cart_icon(3)
        ui_methods.check_quantity(3)

    with step("Проверка содержимого корзины"):
        ui_methods.check_products_by_name('Fiction')
        ui_methods.check_price_of_product('72.00')
