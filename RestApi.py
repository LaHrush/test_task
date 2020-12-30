import requests
import dataclasses

from names.CallNames import CallNames


class RestApi:

    @staticmethod
    def post(resource, payload):
        url = CallNames.URL + resource
        # Converts the dataclass instance to a dict
        if dataclasses.is_dataclass(payload):
            payload = dataclasses.asdict(payload)
        try:
            rsp = requests.post(url, json=payload, headers=CallNames.HEADERS)
        except requests.exceptions.ConnectionError as errc:
            print("Error Connecting:", errc)
        return rsp

    @staticmethod
    def put(resource, payload):
        # Converts the dataclass instance to a dict
        if dataclasses.is_dataclass(payload):
            payload = dataclasses.asdict(payload)
        try:
            url = CallNames.URL + resource
            rsp = requests.put(url, json=payload, headers=CallNames.HEADERS)
        except requests.exceptions.ConnectionError as errc:
            print("Error Connecting:", errc)

        return rsp

    @staticmethod
    def delete(resource):
        try:
            url = CallNames.URL + resource
            rsp = requests.delete(url, headers=CallNames.HEADERS)
        except requests.exceptions.ConnectionError as errc:
            print("Error Connecting:", errc)

        return rsp

    @staticmethod
    def get(resource):
        try:
            url = CallNames.URL + resource
            rsp = requests.get(url)
        except requests.exceptions.ConnectionError as errc:
            print("Error Connecting:", errc)

        return rsp


