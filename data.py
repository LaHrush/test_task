from Helper import random_string
from models.UserModel import UserModel

testdata_with_empty_fields = [
    UserModel('', 'Male', f"{random_string()}@gmail.com", 'Active'),
    UserModel(f"{random_string()}", '', f"{random_string()}@gmail.com", 'Active'),
    UserModel(f"{random_string()}", 'Male', '', 'Active'),
    UserModel(f"{random_string()}", 'Male', f"{random_string()}@gmail.com", '')
]

testdata_with_all_fields = [
    UserModel(f"{random_string()}", 'Male', f"{random_string()}@gmail.com", 'Active'),
    UserModel(f"{random_string()}", 'Male', f"{random_string()}@gmail.com", 'Active')
]

