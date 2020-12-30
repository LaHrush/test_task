import string
import random

def get_status_code(responce):
    return responce.json()['code']


def get_user_id(responce):
    return responce.json()['data']['id']


def get_user_name(responce):
    return responce.json()['data']['name']


def get_user_email(responce):
    return responce.json()['data']['email']


def get_user_gender(responce):
    return responce.json()['data']['gender']


def get_message(responce):
    return responce.json()['data'][0]['message']

def random_string():
    chars = string.ascii_lowercase
    return ''.join((random.choice(chars) for i in range(8)))


