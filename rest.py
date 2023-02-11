from typing import List, Dict
import requests


class Restful:
    """Basic restful requests."""

    def __init__(self, base_url: str, api_key: str = "", ssl_verify: bool = True):
        self.base_url = base_url
        self.api_key = api_key
        self.ssl_verify = ssl_verify


    def call(self, method: str, endpoint: str, params: Dict = None, data = None):

        url = self.base_url + endpoint
        headers = {
            'x-api-key': self.api_key
        }
        response = requests.request(method=method, url=url, verify=self.ssl_verify, headers=headers, params=params, data=data)
        if response.status_code == 200:
            response_data = response.json()
            return response_data
        else:
            raise Exception('GET request not OK', f'Code: {response.status_code}, Response: {response}')


    def get(self, endpoint: str, params: Dict = None):
        """Makes a GET request"""
        return self.call(method='GET', endpoint=endpoint, params=params)
        

    def post(self, endpoint: str, data: Dict = None, params: Dict = None):
        """Makes a POST request"""
        return self.call(method='POST', endpoint=endpoint, params=params, data=data)



        





