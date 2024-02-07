import os

import allure
from allure_commons._allure import step
from selene import browser, have, be

from tests.conftest import BASE_URL
from utils.utils import send_post_request

LOGIN = os.getenv('LOGIN')
PASSWORD = os.getenv('PASSWORD')


@allure.title("Проверка добавления и удаления первого товара из корзины")
def test_add_item_to_cart():
    response = send_post_request("login", data={"Email": LOGIN, "Password": PASSWORD}, allow_redirects=False)
    cookies = response.cookies.get("NOPCOMMERCE.AUTH")
    browser.driver.add_cookie({"name": "NOPCOMMERCE.AUTH", "value": cookies})
    with step("Добавляем товар в корзину"):
        response2 = send_post_request("addproducttocart/details/75/1", data={
            "product_attribute_75_5_31": 96,
            "product_attribute_75_6_32": 101,
            "product_attribute_75_3_33": 103,
            "product_attribute_75_8_35": 107,
            "product_attribute_75_8_35": 108,
            "addtocart_75.EnteredQuantity": 1}, allow_redirects=True, cookies={"NOPCOMMERCE.AUTH": cookies}, )
        assert response.status_code == 302
        browser.open(f"{BASE_URL}cart")
        browser.element(".product-name").should(be.visible)
        browser.element(".remove-from-cart").click()
        browser.element(".update-cart-button").click()


@allure.title("Проверка добавления и удаления второго товара из корзины")
def test_add_second_item_to_cart():
    with step("Проходим авторизацию"):
        response = send_post_request("login", data={"Email": LOGIN, "Password": PASSWORD}, allow_redirects=False)
        cookies = response.cookies.get("NOPCOMMERCE.AUTH")
        browser.driver.add_cookie({"name": "NOPCOMMERCE.AUTH", "value": cookies})
    with step("Добавляем второй товар в корзину"):
        response2 = send_post_request("addproducttocart/details/2/1", data={
            "giftcard_2.RecipientName": "Exam Ple", "giftcard_2.RecipientEmail": "example1200@example.com",
            "giftcard_2.SenderName": "Exam Ple", "giftcard_2.SenderEmail": "example1200@example.com",
            "giftcard_2.Message": "demo_qa_gift", "addtocart_2.EnteredQuantity": 1},
                                      allow_redirects=True, cookies={"NOPCOMMERCE.AUTH": cookies}, )
        assert response.status_code == 302
        browser.open(f"{BASE_URL}cart")
        browser.element(".product-name").should(have.exact_text("$25 Virtual Gift Card"))
        browser.element(".remove-from-cart").click()
        browser.element(".update-cart-button").click()
