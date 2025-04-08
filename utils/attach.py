import json
import allure
from allure_commons.types import AttachmentType


def log_to_allure(response):
    allure.attach(
        body=f"URL: {response.request.url}\nMethod: {response.request.method}\nCode: {response.status_code}\n"
             f"Body: {response.request.body}",
        name="Request",
        attachment_type=AttachmentType.TEXT,
        extension="txt",
    )

    response_json = response.json()
    allure.attach(
        body=json.dumps(response_json, indent=4, ensure_ascii=False),
        name="Response",
        attachment_type=AttachmentType.JSON,
        extension="json",
    )

    cookies = {cookie.name: cookie.value for cookie in response.cookies}
    allure.attach(
        body=json.dumps(cookies, indent=4, ensure_ascii=False),
        name='Cookies',
        attachment_type=AttachmentType.TEXT,
        extension='json'
    )


def add_screenshot(browser):
    png = browser.driver.get_screenshot_as_png()
    allure.attach(body=png, name='screenshot', attachment_type=AttachmentType.PNG, extension='.png')
