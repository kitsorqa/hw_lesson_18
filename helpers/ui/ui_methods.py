from selene import browser, have, be


def check_quantity_of_cart_icon(quantity):
    return browser.element(".cart-qty").should(have.text(f'({quantity})'))


def check_cart(quantity):
    return browser.all(".cart-item-row").should(have.size(quantity))


def check_quantity(quantity):
    return browser.element(".cart-item-row").element(f"[value='{quantity}']").should(be.visible)


def check_product_by_name(name):
    return browser.element(".product-name").should(have.text(name))


def check_products_by_name(name):
    return browser.element(".cart-item-row").should(have.text(name))


def check_price_of_product(price):
    return str(browser.element(".product-subtotal").should(have.text(price)))
