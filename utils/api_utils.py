import requests
import allure
import curlify
import logging
from allure_commons.types import AttachmentType

from tests.conftest import BASE_URL


def send_post_request(url, **kwargs):
    url = BASE_URL + url
    with allure.step(f"POST {url}"):
        response = requests.post(url, **kwargs)
        curl = curlify.to_curl(response.request)
        allure.attach(
            body=curl, name="curl", attachment_type=AttachmentType.TEXT, extension="txt")
        logging.info(curlify.to_curl(response.request))
        return response
