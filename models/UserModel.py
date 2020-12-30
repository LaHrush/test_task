from dataclasses import dataclass

from Helper import random_string


@dataclass
class UserModel:
    name: str = f"test_{random_string()}"
    gender: str = 'Male'
    email: str = f"test_{random_string()}@gmail.com"
    status: str = "Active"


