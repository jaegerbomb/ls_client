import requests


def send_request(_type, url, data={}):
    try:
        if _type == 'get':
            response = requests.get(url=url)
        elif _type == 'post':
            response = requests.post(url=url, data=data)
        response.raise_for_status()
        if response.status_code == 200:
            return response.text
    except requests.exceptions.HTTPError as ex:
        return f'invalid: {ex}'
    except requests.exceptions.ConnectionError as ex:
        return f'bad: {ex}'


class LoanStreet:
    def __init__(self, url):
        self._api_url = url

    # for troubleshooting server
    def check_health(self):
        url = f'{self._api_url}/health'
        return f'Server health: {send_request("get", url)}'

    def is_server_up(self):
        url = f'{self._api_url}/health'
        if send_request("get", url) == "up":
            return True
        return False

    def add_loan(self, amount, rate, length, payment):
        if self.is_server_up():
            url = f'{self._api_url}/create'
            payload = {
                "amount": amount,
                "rate": rate,
                "length": length,
                "payment": payment
            }
            return send_request("post", url, payload)
        else:
            return self.check_health()

    def update_loan(self, options):
        if options:
            if self.is_server_up():
                url = f'{self._api_url}/create'
                return send_request("post", url, options)
            else:
                return self.check_health()
        else:
            return 'No loan options specified for this loan'
