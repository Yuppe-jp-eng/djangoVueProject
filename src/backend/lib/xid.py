from django.conf import settings
from django.core.exceptions import PermissionDenied
from django.http.response import Http404
from django.utils.http import urlencode

from nacl.public import PrivateKey
from nacl.public import SealedBox
from nacl.encoding import Base64Encoder

import requests
import string
import random

from requests.exceptions import HTTPError


def authenticate(request):
    state = get_random_str(8)
    request.session["state"] = state
    param = {
        "client_id": settings.XID_CLIENT_ID,
        "redirect_uri": settings.XID_REDIRECT_URI,
        "scope": settings.XID_SCOPE,
        "response_type": "code",
        "response_mode": "query",
        "state": state,
        "nonce": get_random_str(8),
    }

    return f"{settings.BASE_URL_FOR_AUTH}?{urlencode(param)}"


def get_access_token(session_code):
    headers = {"Accept": "application/json", "Content-Type": "application/x-www-form-urlencoded", "Authorization": f"Basic {settings.XID_TOKEN_PASS}"}
    param = {"code": session_code, "grant_type": "authorization_code", "client_id": settings.XID_CLIENT_ID, "redirect_uri": settings.XID_REDIRECT_URI}
    base_url = settings.BASE_URL_FOR_TOKEN
    try:
        response = requests.post(base_url, headers=headers, data=param)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        raise get_error_by_code(e.response.status_code)
    return response


def get_user_info(access_token):
    """
    email,sub,xid_verifiedなどの登録情報を返します。
    """
    headers = {"Accept": "application/json", "Authorization": f"Bearer {access_token}"}
    base_url = settings.BASE_URL_FOR_USERINFO
    try:
        response = requests.get(base_url, headers=headers)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        raise get_error_by_code(e.response.status_code)
    return response


def get_user_data(access_token, userdataid):
    """
    性別、姓名、住所などの個人情報を返します。
    """
    headers = {"Accept": "application/json", "Authorization": f"Bearer {access_token}"}
    param = {"userdataid": userdataid}
    base_url = settings.BASE_URL_FOR_USERDATA
    try:
        response = requests.get(base_url, params=urlencode(param), headers=headers)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        raise get_error_by_code(e.response.status_code)
    return response


def get_my_number_code(access_token, userdataid):
    headers = {"Accept": "application/json", "Authorization": f"Bearer {access_token}"}
    param = {
        "userdataid": userdataid,
        "reason": "ワクチン予約サイトの認証です。",
        "reasonNotification": "ワクチン予約サイトの認証です。",
    }
    base_request_url = settings.BASE_URL_FOR_MY_NUMBER
    try:
        response = requests.post(base_request_url, headers=headers, data=param)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        raise get_error_by_code(e.response.status_code)

    return response


def request_my_number(access_token, request_id):
    headers = {"Accept": "application/json", "Authorization": f"Bearer {access_token}"}
    param = {
        "requestID": request_id,
    }
    base_status_url = settings.BASE_URL_FOR_MY_NUMBER
    try:
        my_number_status = requests.get(base_status_url, params=urlencode(param), headers=headers)
        my_number_status.raise_for_status()
    except requests.exceptions.RequestException as e:
        raise get_error_by_code(e.response.status_code)
    return my_number_status


def decrypt_data(encrypted_data):
    decryptor = Decryptor(settings.XID_PRIVATE_KEY)
    plain_data = decryptor.decrypt(encrypted_data)
    return plain_data


def get_random_str(num):
    dat = string.digits + string.ascii_lowercase + string.ascii_uppercase
    return "".join([random.choice(dat) for i in range(num)])


def get_error_by_code(code):
    if code == requests.codes.bad_request:
        return HTTPError("リクエストエラー")
    elif code == requests.codes.forbidden:
        return PermissionDenied
    elif code == requests.codes.not_found:
        return Http404
    else:
        return HTTPError("サーバエラー")


class Decryptor:
    def __init__(self, private_key: str):
        self.private_key = private_key

    def decrypt(self, cipher: str, decode="utf-8") -> str:
        private_byte = PrivateKey(Base64Encoder.decode(self.private_key))
        cipher_byte = Base64Encoder.decode(cipher)
        crypt_box = SealedBox(private_byte)
        return crypt_box.decrypt(cipher_byte[24:]).decode(decode)

    def decrypt_list(self, str_list):
        decrypted_str = ""
        for str in str_list:
            decrypted_str += self.decrypt(str)
        return decrypted_str
