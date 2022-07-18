import string
import random
import requests
import json
from json import JSONDecodeError
from kuda.error import ClientError, ServerError

class Kuda():
    from kuda.api import bank_list
    from kuda.api import name_enquiry
    from kuda.api import create_virtual_account
    from kuda.api import get_virtual_single_account
    from kuda.api import single_fund_transfer
    from kuda.api import virtual_fund_transfer
    from kuda.api import txn_status_query
    from kuda.api import get_main_account_balance
    from kuda.api import get_virtual_account_balance
    from kuda.api import txn_logs
    from kuda.api import main_txn_logs
    from kuda.api import filter_main_txn_logs
    from kuda.api import virtual_txn_logs
    from kuda.api import filter_virtual_txn_logs
    from kuda.api import fund_virtual_account
    from kuda.api import withdraw_virtual_account

    def __init__(self, 
                email, 
                apiKey, 
                sandbox=False, 
                show_request=False,
                show_header=False,
                base_url = "",**kwargs):

        if sandbox and base_url == "":
            self.url = "https://kuda-openapi-uat.kudabank.com/v2".replace("\u200b", "")
        elif not sandbox and base_url == "":
            self.url = "​https://kuda-openapi.kuda.com/v2".replace("\u200b", "")
        else:
            self.url = base_url.replace("\u200b", "")
        
        if show_request: 
            self.show_request = True    
        else:
            self.show_request = True

        if show_header: 
            self.show_header = True
        else: 
            self.show_header = False
        
        self.token = self.getToken(email, apiKey)

    def getToken(self, email, apiKey):
        token = requests.post(f"{self.url}/Account/GetToken",
                            json={"email" : email, "apiKey":apiKey})
        self._handle_exception(token)
        return token.text

    def get_ref(self, length: int) -> int:
        """Generate a unique reference per request (requestRef)

        Args:
            length (int): length of reference

        Returns:
            int: random requestRef
        """
        digits = string.digits
        result_int = ''.join(random.choice(digits) for i in range(length))
        return int(result_int)

    def koboToNGN(self, kobo):
        return kobo/100

    def ngntoKobo(self, naira):
        return naira*100
 
    def sign_request(self, url_path: str, payload={}):

        request = {
            "header": {
                "Authorization": f"Bearer {self.token}",
            },
            "body" : {
                "data": {
                    "serviceType": url_path,
                    "requestRef" : str(self.get_ref(7)),
                    "data" : payload
                }
            }
        }

        request['body']['data'] = str(request['body']['data'])
        if self.show_request:
            print(json.dumps(request['body'], indent=4))
        return self.send_request(request)

    def send_request(self, request):
        # Make request to Kuda API
        resp = requests.post(self.url, headers=request['header'], json=request['body'])
    
        # Handle exceptions in response
        self._handle_exception(resp)

        try:
            data = resp.json()
        except ValueError:
            data = resp.text
        
        result = {}
        
        # Display header for debugging purpose
        if self.show_header:
            result['headers'] = resp.request.headers
            result['body'] = data
            return result
        
        result['data'] = json.loads(data['data'])
        return result

    def _handle_exception(self, response):
        # http status code
        code = response.status_code
        if code < 400:
            return
        if 400 <= code <= 500:
            try:
                err = json.loads(response.text)
            except JSONDecodeError:
                raise ClientError(code, response.text, response.headers)
            raise ClientError(code, err, f"Response Headers: {response.headers}")
        raise ServerError(code, response.text)