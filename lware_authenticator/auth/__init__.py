import logging

import requests


class Authenticator:

    def __init__(self, user, password, auth_service_url):
        self.user = user
        self.password = password
        self.auth_service_url = auth_service_url
        _login = self.login()
        if _login:
            self.auth_token = _login["Authorization"]
        else:
            self.auth_token = None

    def login(self):
        payload = {
            "email": self.user,
            "password": self.password
        }
        response = requests.post(url=f'{self.auth_service_url}/login', json=payload)
        if response.status_code == 200:
            return response.json()
        else:
            logging.warning({"status": "fail", "error": "could not login", "response": response.json()})
            return None
