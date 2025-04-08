import requests

from utils.attach import log_to_allure


def add_book_to_cart(product):
    response = requests.post(
        url=f'https://demowebshop.tricentis.com/addproducttocart/catalog/{product}/1/1',
    )
    log_to_allure(response)
    return response
