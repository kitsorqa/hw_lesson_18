import requests

from utils.attach import log_to_allure


def add_product_to_cart(product, quantity=1):
    response = requests.post(
        url=f'https://demowebshop.tricentis.com/addproducttocart/catalog/{product}/1/{quantity}',
        data={f'addtocart_{product}.EnteredQuantity': {quantity}}
    )
    log_to_allure(response)
    return response


def get_cookies(cookies, cookie_name):
    return cookies.get(cookie_name)
